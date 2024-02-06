class Article:
    articles = []  # to store all instances of Article

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.articles.append(self)
        magazine._articles.append(self)
        author._articles.append(self)

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def all():
        return Article.articles

