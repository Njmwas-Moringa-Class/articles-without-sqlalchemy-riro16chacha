from Article import Article

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    @classmethod
    def all(cls):
        return cls._all_magazines

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name == name:
                return magazine

    def contributors(self):
        authors = {article.author for article in Article.all() if article.magazine == self}
        return list(authors)

    def article_titles(self):
        return [article.title for article in Article.all() if article.magazine == self]

    def contributing_authors(self):
        authors = {}
        for article in Article.all():
            if article.magazine == self:
                if article.author in authors:
                    authors[article.author] += 1
                else:
                    authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2]


