from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

available_books = "available"

try:
    for books in library_books:
        if isinstance(books,dict) and books.get(available_books) is True:
            print(f'Book Available: {books.get('id')}, Title: {books.get('title')}, Author: {books.get('author')}')

except Exception as e:
    print(f'No books available: {e}')

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

search_books = input("Please type author's name or book genre: ")


search_books = "book"

try:
    for books in library_books:
        if isinstance(books,dict) and books.get(search_books) is #IDK:
            print(f'Available: {books.get('id')}, Title: {books.get('title')}, Author: {books.get('author')}')

except Exception as e:
    print(f'No books available: {e}')





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
