from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from settings import settings
import json


app = FastAPI()

class Book(BaseModel):
     id:int
     title: str
     author: str
     year:int
     pages:int


@app.get("/book")
def get_books():
    with open(settings.data_file_path) as file:
        books = json.load(file)

    if settings.max_books is not None:
        if len(books) >= settings.max_books:
            raise HTTPException(
                status_code=409,
                detail=f"Maximum number of books is {settings.max_books}"
            )

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
    with open(settings.data_file_path) as file:
        books = json.load(file)

    new_book = {
            "id": len(books) + 1,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "pages": book.pages
        }

    books.append(new_book)

    with open(settings.data_file_path, 'w') as file:
        json.dump(books, file, indent=4)

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    with open('books.json') as file:
        books = json.load(file)

    for book in books:
        if book['id'] == book_id:
            print(book)
            books.remove(book)

    with open(settings.data_file_path, 'w') as file:
        json.dump(books, file, indent=4)

@app.get("/select/author")
def get_books_by_author(author: str):
    with open(settings.data_file_path) as file:
        books = json.load(file)

    result = []

    for book in books:
        if book["author"] == author:
            result.append(book)

    return result
