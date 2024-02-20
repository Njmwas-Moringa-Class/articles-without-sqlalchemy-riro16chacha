from Article import Article

class Author:
    all_authors = []

    def _init_(self, name):
        self._name = name
        self._authored_articles = []
        self._class_.all_authors.append(self)

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