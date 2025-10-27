class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"



# Given a Book class with the __init__ method, define the following special methods:
# (1) __str__ method - feel free to suggest a suitable string representation
# (2) __repr__ method - what do you think should be the format?
