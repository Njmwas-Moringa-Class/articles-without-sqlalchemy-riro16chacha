#!/usr/bin/env python3
import ipdb
from lib.Author import Author
from lib.Magazine import Magazine
from lib.Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###

    # Create authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Create magazines
    magazine1 = Magazine("Tech Mag", "Technology")
    magazine2 = Magazine("Sci Journal", "Science")

    # Add articles
    article1 = author1.add_article(magazine1, "Python Basics")
    article2 = author2.add_article(magazine1, "Data Science Trends")
    article3 = author1.add_article(magazine2, "Quantum Computing")

    # Test relationships
    print(article1.author().name())  # Output: John Doe
    print(article1.magazine().name())  # Output: Tech Mag

    print(author1.articles())  # Output: [article1, article3]
    print(author1.magazines())  # Output: [magazine1, magazine2]

    print(magazine1.contributors())  # Output: [author1, author2]
    print(magazine2.find_by_name("Sci Journal").category())  # Output: Science
    print(magazine1.article_titles())  # Output: ['Python Basics', 'Data Science Trends']

    print(magazine1.contributing_authors())  # Output: [author1]

# DO NOT REMOVE THIS
    ipdb.set_trace()

