class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if not hasattr(self, "_name"):
            self._name = name
        else:
            raise ValueError("Name cannot be changed after the author is instantiated")

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        # code to return a list of all the articles the author has written
        pass