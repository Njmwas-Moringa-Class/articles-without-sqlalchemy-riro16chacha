class Article:
    all_articles = []

    def _init_(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._class_.all_articles.append(self)
        magazine.add_published_article(self)
        author.add_authored_article(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls.all_articles
