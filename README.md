# allegro-summer-experience-2022
My email in recruitment process: `lukaswelnic@hotmail.com`

--

## Intern - Software Engineeer

### Task number 3 (Python)

The goal was to create an API that returns:

- the list of repositories (their names) with the information about programming languages used in them (name of language, number of code bytes for specific language)
- user's data (login, name and bio) with aggregated information about programming languages used in their repositories (name of language, number of code bytes for specific language)

for any GitHub user.

The data is returned through HTTP protocol.

### Requirements

- Python 3.10 or newer
- Libraries/frameworks:

Fastapi: `pip install fastapi`

Uvicorn: `pip install uvicorn`

- REST client, e.g. Postman
- Personal access token (generated through Developer Settings on your GitHub account - to access numerous GitHub API calls)

### How to execute

In your terminal window (in the project folder) type: `uvicorn main:app`.

Send a GET request through your REST client:

**1. To get user's data:**

Copy the URL that uvicorn is running on. Add `/user_info?login=` after the URL and then the GitHub username. For example:

`http://127.0.0.1:8000/user_info?login=lukaszwelnic`

To authorize the API call you need to provide a token parameter like this:

`http://127.0.0.1:8000/user_info?login=lukaszwelnic&token=*pasteyourtokenhere*`

Sample output:

```JSON
{
    "login": "lukaszwelnic",
    "name": "Łukasz Wełnic",
    "bio": "5th year Computer Science student at Poznań University of Technology (Distributed Systems/Computing)",
    "languages_used": [
        {
            "language_name": "Java",
            "size_bytes": 38489
        },
        {
            "language_name": "Shell",
            "size_bytes": 188
        },
        {
            "language_name": "Dockerfile",
            "size_bytes": 144
        }
    ]
}
```

**2. To get repositories data:**

Copy the URL that uvicorn is running on. Add `/repositories_info?login=` after the URL and then the GitHub username. For example:

`http://127.0.0.1:8000/repositories_info?login=lukaszwelnic`

To authorize the API call you need to provide a token parameter like this:

`http://127.0.0.1:8000/repositories_info?login=lukaszwelnic&token=*pasteyourtokenhere*`

You can execute these API calls with an API rate limit.

Sample output:

```JSON
{
    "login": "lukaszwelnic",
    "repositories": [
        {
            "repository_name": "TicketReservationSystem",
            "languages": [
                {
                    "language_name": "Java",
                    "size_bytes": 38489
                },
                {
                    "language_name": "Shell",
                    "size_bytes": 188
                },
                {
                    "language_name": "Dockerfile",
                    "size_bytes": 144
                }
            ]
        }
    ]
}
```
