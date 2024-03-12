class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type str")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be of type str")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category