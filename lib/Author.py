from Article import Article
class Author:
    authors = []  # to store all instances of Author

    def __init__(self, name):
        self._name = name
        self._articles = []
        Author.authors.append(self)

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine() for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines()))


