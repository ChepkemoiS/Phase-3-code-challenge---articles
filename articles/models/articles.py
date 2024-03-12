class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title must be of type str")
        if len(new_title) < 5 or len(new_title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._title = new_title