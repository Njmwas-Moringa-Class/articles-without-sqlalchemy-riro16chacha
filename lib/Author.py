from Article import Article

class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        self._authored_articles = []
        Author.all_authors.append(self)  # Use the class name directly

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._authored_articles

    def magazines(self):
        return list(set(article.magazine for article in self._authored_articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._authored_articles.append(new_article)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._authored_articles))

    @classmethod
    def all(cls):
        return cls.all_authors
