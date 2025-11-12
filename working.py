from library_books import library_books
from datetime import datetime, timedelta

'''contacts = {
    'Sofia': 'hello',
    'Rocka': 'loves',
    'Pintura': 'most'
}
for values in contacts.values():
    if values == 'most':
        print('got it!')'''



############## VERSION 3
'''for values in library_books():
    if values == True:
        def description_book1():
            print(library_books[0]["id"])
            print(library_books[0]["title"])
            print(library_books[0]["author"])

        description_book1()'''

'''available_books = "available"

try:
    for books in library_books:
        if isinstance(books,dict) and books.get(available_books) is True:
            print(f'Book Available: {books.get('id')}, Title: {books.get('title')}, Author: {books.get('author')}')

except Exception as e:
    print(f'No books available: {e}')'''



####### VERSION 1

print(library_books["available"])



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