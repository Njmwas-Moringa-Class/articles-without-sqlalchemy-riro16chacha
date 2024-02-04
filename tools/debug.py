#!/usr/bin/env python3
import ipdb
from lib import Author, Magazine, Article

if __name__ == '__main__':
    # Create some authors
    author1 = Author("Riro Chacha")
    author2 = Author("Mclaurine")

    # Create some magazines
    magazine1 = Magazine("Nature", "Science")
    magazine2 = Magazine("Vogue", "Fashion")

    # Add articles to authors
    article1 = author1.add_article(magazine1, "The Science of Nature")
    article2 = author1.add_article(magazine2, "Fashion Trends")
    article3 = author2.add_article(magazine2, "The Art of Fashion")

    # Test methods
    assert author1.name == "Riro Chacha"
    assert author2.name == "Mclaurine"
    assert magazine1.name == "Nature"
    assert magazine2.category == "Fashion"
    assert article1.title == "The Science of Nature"
    assert article2.author == author1
    assert article3.magazine == magazine2

    # Test object relationships
    assert article1.author == author1
    assert article1.magazine == magazine1
    assert author1.articles == [article1, article2]
    assert author1.magazines() == [magazine1, magazine2]
    assert magazine2.contributors() == [author1, author2]

    # Test associations and aggregate methods
    author1.add_article(magazine1, "Nature Photography")
    author1.add_article(magazine1, "Ecology and Conservation")
    author2.add_article(magazine2, "Fashion Photography")
    author2.add_article(magazine2, "Designer Interviews")

    assert Magazine.find_by_name("Nature") == magazine1
    assert magazine2.article_titles() == ["Fashion Trends", "The Art of Fashion", "Fashion Photography", "Designer Interviews"]
    assert magazine2.contributing_authors() == [author2]

    # Print success message
    print("All tests passed!")

    # Start the debugger
    ipdb.set_trace()

