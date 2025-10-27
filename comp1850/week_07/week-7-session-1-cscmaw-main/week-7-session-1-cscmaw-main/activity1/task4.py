# Define a class Book with the following fields:
# (1) title - the book title
# (2) author - the author(s) of the book
# (3) ISBN - the International Standard Book Number, which is 10-13 digits long
# (4) availability - whether the book is available (True or False)
# When an instance of a Book is created, only the value to the first three fields are required
# for the __init__ method as the book is available when created.
class Book:
    def __init__(self, title, author, ISBN, availability=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
book1=Book("The Great Gatsby","F. Scott Fitzgerald","9780743273565")
print(f"Title: {book1.title}")
print(f"Author: {book1.author}")   
print(f"ISBN: {book1.ISBN}")
book2=Book("1984","George Orwell","9780451524935",False)
print(f"Title: {book2.title}")
print(f"Author: {book2.author}")   
print(f"ISBN: {book2.ISBN}")    
 






# Once completed, create two instances of Book with the details of two of your favourite books.
# Write code to print the details of each books
