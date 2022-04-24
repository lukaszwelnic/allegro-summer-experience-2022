import requests
from fastapi import FastAPI, HTTPException
from user_data import UserData
from repository import Repository

app = FastAPI()


def fetching_failed_exception(status_code: int):
    return HTTPException(
        status_code=status_code,
        detail=f'Code executed with status {status_code}. Fetching failed.')


def fetch_user_data(login, token):

    if token is None or token == '':
        headers = {'Authorization': ''}
    else:
        headers = {'Authorization': 'token ' + token}

    url_user = 'https://api.github.com/users/' + login

    url_repos = 'https://api.github.com/users/' + login + '/repos'

    name = None
    bio = None

    response_user = requests.get(url=url_user, headers=headers)

    if response_user.status_code == 200:
        data = response_user.json()
        name = data['name']
        bio = data['bio']
    elif response_user.status_code == 404:
        raise HTTPException(status_code=404, detail='User Not Found')
    else:
        raise fetching_failed_exception(response_user.status_code)

    response_repos = requests.get(url=url_repos, headers=headers)

    if response_repos.status_code == 200:
        data = response_repos.json()
        repositories = []
        for repo in data:
            repo_languages = requests.get(url=repo['languages_url'], headers=headers)
            if repo_languages.status_code == 200:
                repo_languages = repo_languages.json()
            else:
                raise fetching_failed_exception(repo_languages.status_code)
            repository = Repository(repo['name'], repo_languages)
            repositories.append(repository)
        return UserData(login, name, bio, repositories)
    elif response_repos.status_code == 404:
        raise HTTPException(status_code=404, detail='Repository Not Found')
    else:
        raise fetching_failed_exception(response_repos.status_code)


@app.get('/user_info', status_code=200)
async def get_user_info(login: str = '', token: str | None = None):
    user_data = fetch_user_data(login, token)
    user_info = {
        'login': user_data.user_login,
        'name': user_data.user_name,
        'bio': user_data.user_bio,
        'languages_used': []
    }
    languages_info = user_data.get_all_language_stats()
    for lang_name, size_bytes in languages_info.items():
        user_info['languages_used'].append(
            {'language_name': lang_name,
             'size_bytes': size_bytes})
    return user_info


@app.get('/repositories_info', status_code=200)
async def get_repositories_info(login: str = '', token: str | None = None):
    user_data = fetch_user_data(login, token)
    repositories = {
        'login': login,
        'repositories': []
    }
    for repos in user_data.user_repositories:
        repo = {
            'repository_name': repos.repository_name,
            'languages': []
        }
        for lang_name, size_bytes in repos.repository_languages.items():
            lang_info = {
                'language_name': lang_name,
                'size_bytes': size_bytes
            }
            repo['languages'].append(lang_info)
        repositories['repositories'].append(repo)
    return repositories
