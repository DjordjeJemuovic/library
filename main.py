from pymysql import cursors

from models.book import *
from models.users import add_users
from models.db import connection
from faker import Faker
faker = Faker()

books=get_all_books(connection)

for book in books:
    print(book)

choice = None

while choice is None or choice == '':
    choice = input("Enter a choice from the following options:\n"
                   "1.Create random book: \n"
                   "2.show all books: \n"
                   "3.Show book by ID:"
                   "4.Delete book:\n")

    if choice == "1":
        ganre = radnom_ganre()
        author = author_name()
        age = generata_dob()
        title = book_title(ganre,author)
        user = add_users(connection,author,age)
        instert_books(connection,title,ganre,user)
        print(f"Creatred nrew book titled:[{title}]")

    elif choice == "2":
        print(books)
    elif choice == "3":
        book_id = None
        while book_id is None or book_id == '':
            book_id = int(input("Enter a book ID:\n"))

            book = get_book_by_id(connection,book_id)
            if book:
                print(f"This book name is {book['name']}")
            else:
                print("This book does not exist")
                book_id = None

    elif choice == "4":
        book_id = None
        while book_id is None or book_id == '':
            book_id = int(input("Enter a book ID:\n"))
            book = get_book_by_id(connection,book_id)
            if book:
                deleete_book(connection,book_id)
                print(f"This book name is {book['name']} and has been deleted")
            else:
                print("This book does not exist")
    else :
        choice = None

