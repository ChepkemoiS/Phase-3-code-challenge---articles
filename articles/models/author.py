class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.articles))
