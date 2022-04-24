class Repository:
    def __init__(self, name='', languages=None):
        if languages is None:
            languages = {}
        self.repository_name = name
        self.repository_languages = languages

    def print_attr(self):
        print(f'Repository name: {self.repository_name}\nRepository languages: {self.repository_languages}\n', end='')
