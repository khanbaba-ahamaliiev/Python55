from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


def load_films(filename='films.json'):
    with open(filename) as f:
        return json.load(f)

def save_films(films_data, filename='films.json'):
    with open(filename, 'w') as f:
        json.dump(films_data, f, indent=4)

class Film(BaseModel):
    title: str
    director: str
    year: int

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    films = load_films()

    for film in films:
        for id, info in film.items():
            if id == str(movie_id):
                print(info)
                return {"message": f"{info['title']} found successfully!, Director: {info['director']}, Year: {info['year']}, id: {id}"}

@app.post("/movies")
def add_movie(film: Film):
    films = load_films()

    for movie in films:
        for id, info in movie.items():
            if info['title'] == film.title:
                return {"error": "Movie with this name already exists"}

    new_film = {str(len(films) + 1):film.model_dump()}

    films.append(new_film)

    save_films(films)

    return{"message":f"{film.title} added successfully!"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    films = load_films()

    for film in films:
        for id, info in film.items():
            if id == str(movie_id):
                films.remove(film)
                save_films(films)
                return {"message": f"{info['title']} deleted successfully!"}
