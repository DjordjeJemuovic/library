from datetime import datetime
import random
from faker import Faker
faker = Faker()


genres = ["Fantasy", "Horror", "Science Fiction", "Thriller", "Comedy"]
adjectives = ["Mysterious", "Forgotten", "Dark", "Cheerful", "Dangerous"]
nouns = ["Forest", "Tower", "Traveler", "Dragon", "Secret"]

def radnom_ganre():
    ganre = random.choice(adjectives)
    return ganre

def author_name():
    author = faker.name()
    return author

def generata_dob():
    age = faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(2000, 1, 1))
    return age


def book_title(ganre,author):
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)

    book_name = f"{adjective} {noun}: A {ganre} story by {author}"

    return book_name



def instert_books(con,name,category,author):
    cursor = con.cursor()

    query = "INSERT INTO books(name, category, author) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, category, author))
    con.commit()
    cursor.close()

def get_all_books(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM books")
    con.commit()
    cursor.close()
    results = cursor.fetchall()
    return results

def get_book_by_id(con,book_id):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s",book_id)
    con.commit()
    cursor.close()
    results = cursor.fetchone()
    return results

def deleete_book(con,book_id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s",book_id)
    con.commit()
    cursor.close()