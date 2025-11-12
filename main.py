from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def description_book1():
    print(library_books[0]["id"])
    print(library_books[0]["title"])
    print(library_books[0]["author"])

description_book1()

def description_book2():
    print(library_books[1]["id"])
    print(library_books[1]["title"])
    print(library_books[1]["author"])

description_book2()

def description_book3():
    print(library_books[2]["id"])
    print(library_books[2]["title"])
    print(library_books[2]["author"])

description_book3()

def description_book4():
    print(library_books[3]["id"])
    print(library_books[3]["title"])
    print(library_books[3]["author"])

description_book4()

def description_book5():
    print(library_books[4]["id"])
    print(library_books[4]["title"])
    print(library_books[4]["author"])

description_book5()

def description_book6():
    print(library_books[5]["id"])
    print(library_books[5]["title"])
    print(library_books[5]["author"])

description_book6()

def description_book7():
    print(library_books[6]["id"])
    print(library_books[6]["title"])
    print(library_books[6]["author"])

description_book7()

def description_book8():
    print(library_books[7]["id"])
    print(library_books[7]["title"])
    print(library_books[7]["author"])

description_book8()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
