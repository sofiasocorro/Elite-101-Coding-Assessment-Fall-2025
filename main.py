from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

available_books = "available"

try:
    for books in library_books:
        if isinstance(books,dict) and books.get(available_books) is True:
            print(f'Book Available: {books.get('id')}, Title: {books.get('title')}, Author: {books.get('author')}\n')

except Exception as e:
    print(f'No books available: {e}')

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

#print(user_data[0]['name'])

#try:
    #for books in library_books:

book_genre = "genre"
book_author = "author"

'''for search in library_books:
    search_books = input("Please type author's name or book genre: ").upper

    if search_books and search.get(book_genre) == "Fantasy" :
        print(f'Title: {(library_books[0]['title'])} by {(library_books[0]['author'])}, Available: {library_books[0]['available']}')
        print(f'Title: {(library_books[5]['title'])} by {(library_books[5]['author'])}, Available: {library_books[5]['available']}')
                
    if search_books and search.get(book_genre) == "Historical" :
        print('runs')
        
    else:
        print('not working')'''

while True:      
    search_books = input("Please type author's name or book genre: ").strip().lower()
    found = False


    for book in library_books:
        if (search_books == book[book_genre].lower() or search_books == book[book_author].lower()):
            print(f'Title: {book['title']} by {book['author']}, Available: {book['available']}')
            found = True

    if not found:
        print("Please only type the author's name or book genre")



#except Exception as e:
    #print(f'No books available: {e}')



    


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



'''
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
]
'''