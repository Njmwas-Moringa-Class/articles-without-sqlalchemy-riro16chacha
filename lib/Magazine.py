class Magazine:
    magazines = []  # to store all instances of Magazine

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def all():
        return Magazine.magazines

    def contributors(self):
        return list(set(article.author() for article in self._articles))

    def find_by_name(cls, name):
        return next((magazine for magazine in Magazine.magazines if magazine.name() == name), None)

    def article_titles(cls):
        return [article.title() for article in cls._articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author()
            authors_count[author] = authors_count.get(author, 0) + 1

        return [author for author, count in authors_count.items() if count > 2]

