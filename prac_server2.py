from fastapi import FastAPI
from pydantic import BaseModel
import json



# Завдання 1
app = FastAPI()
#
# class Response(BaseModel):
#     message: str

# @app.post("/hello")
# def hello() -> Response:
#     return Response(message='HELLO')


# Завдання 2

# @app.post("/hello")
# def hello() -> Response:
#     return Response(message='HELLO from 1')
#
# app2 = FastAPI()
#
# @app2.post("/hello")
# def hello2() -> Response:
#     return Response(message='HELLO from 2')


 # Завдання 4

class Book(BaseModel):
     id:int
     title: str
     author: str
     year:int
     pages:int


@app.get("/book")
def get_books():
    with open('books.json') as file:
        return json.load(file)

@app.get("/book/{book_id}")
def get_book(book_id: int):
    with open('books.json') as file:
        books = json.load(file)

    for book in books:
        if book['id'] == book_id:
            print(book)
            return book


@app.post("/book")
def add_book(book: Book):
    with open('books.json') as file:
        books = json.load(file)

    new_book = {
            "id": len(books) + 1,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "pages": book.pages
        }

    books.append(new_book)

    with open('books.json', 'w') as file:
        json.dump(books, file)
