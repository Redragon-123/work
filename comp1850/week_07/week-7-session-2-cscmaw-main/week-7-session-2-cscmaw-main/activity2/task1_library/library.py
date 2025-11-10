# Define a Library class with the following fields:
# (1) name - the name of a library, e.g., Laidlaw Library
# (2) books - a list of Book instances
# When an instance of Library is created, only the name field is required for the __init__ method.




# The Library class also has the following methods:
# (1) add_book(book) - adds a Book instance to the library, i.e., add the Book instance to the books field
# (2) __str__ - returning the library name and list of books titles in the format 
#     Library: City Library\nBooks:\n- To Kill a Mockingbird by Harper Lee (1960)\n- 1984 by George Orwell (1949)





# When complete, create 3 instances of Books for your 3 most favourite books
# Then, create an instance of Library with your most favourite library in Leeds University
# and add the 3 books to the library. Then, print the library you have created using the print method
class Library:
    def __init__(self, name,books=None):
        self.name=name
        if books is None:
            self.books=[]
        else:
            self.books=books
    def add_book(self,book):
        self.books.append(book)
    def __str__(self):
        book_list="\n".join([f"- {book.title} by {book.author} ({book.year})" for book in self.books])
        return f"Library: {self.name}\nBooks:\n{book_list}"
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
book1=Book("To Kill a Mockingbird","Harper Lee",1960)
book2=Book("1984","George Orwell",1949)
book3=Book("Pride and Prejudice","Jane Austen",1813)
library=Library("Laidlaw Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print(library)
