# (i)creating an instance of the class and displaying the infromation

class Book:
    def __init__(mine, title, author, pages):
        mine.title = title
        mine.author = author
        mine.pages = pages

    def display_info(mine):
        print(f"Title: {mine.title}")
        print(f"Author: {mine.author}")
        print(f"Pages: {mine.pages}")

# Creating an instance of the Book class
my_book = Book("SPORTS EDUCATION", "PEACE DIANE", 200)

# Displaying information about the book
my_book.display_info()

# (ii)creating a derived class '"EBOOK" that inherits the "BOOK''

class EBook(Book):
    def __init__(mine, title, author, pages, format):
        # Call the constructor of the base class (Book)
        super().__init__(title, author, pages)
        mine.format = format

    def display_info(mine):
        # Call the display_info method of the base class (Book)
        super().display_info()
        print(f"Format: {mine.format}")

# Creating an instance of the EBook class
my_ebook = EBook("SPORTS EDUCATION EBook", "PEACE DIANE", 200, "tk")

# Displaying information about the EBook
my_ebook.display_info()


# (iii)A function on the book returning book tittle and its author
title_and_author = my_book.get_title_and_author()
print("\nTitle and Author:", title_and_author)

# (iv) Defining the terms(a)class, (b)object
# A class is acode for creating objects.
# An object is a variable that contian data and functions that can be used to manipulate data.