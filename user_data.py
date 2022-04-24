class UserData:
    def __init__(self, login='', name='', bio='', repositories=None):
        if repositories is None:
            repositories = []
        self.user_login = login
        self.user_name = name
        self.user_bio = bio
        self.user_repositories = repositories

    def get_all_language_stats(self):
        languages = {}
        for repo in self.user_repositories:
            for lang_name, size_bytes in repo.repository_languages.items():
                if lang_name in languages:
                    languages[lang_name] += size_bytes
                else:
                    languages.update({lang_name: size_bytes})
        return languages

    def print_attr(self):
        print(f'User Login: {self.user_login}\nUser Name: {self.user_name}\nUser Bio: {self.user_bio}\n'
              f'User Repositories:')
        for i in self.user_repositories:
            i.print_attr()
