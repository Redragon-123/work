class Book:
    def __init__(self, title, author, year, edition):
        self.title = title
        self.author = author
        self.year = year
        self.edition = edition
    def set_year(self, year):
        self.year = year
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.edition} edition"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, edition='{self.edition}')"


# write setter for year and update the __init__ method


# define the __repr__ method


