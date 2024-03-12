from author import Author
from magazine import Magazine
from article import Article

# create authors
author1 = Author("John Doe")
author2 = Author("Jane Doe")

# create magazines
magazine1 = Magazine("Magazine A", "Category A")
magazine2 = Magazine("Magazine B", "Category B")

# create articles
article1 = Article(author1, magazine1, "Article 1")
article2 = Article(author1, magazine2, "Article 2")
article3 = Article(author2, magazine1, "Article 3")

# print the name of the first author
print(author1.name)

# print the list of articles written by the first author
print(author1.articles)

# print the list of magazines for which the first author has contributed to
print(author1.magazines)

# print the name and category of the first magazine
print(magazine1.name, magazine1.category)

# print the list of articles published by the first magazine
print(magazine1.articles)

# print the list of authors who have contributed to the first magazine
print(magazine1.contributors)