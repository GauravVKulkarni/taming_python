from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Movie(BaseModel):
    id: int
    name: str
    releaseDate: int
    rating: float

movies: List[Movie]=[]

@app.get("/")
def read_root():
    return {"message" : "Welcome to the Cinemaa!"}

@app.get("/movies")
def read_movies():
    return movies

@app.post("/movies")
def add_movie(movie : Movie):
    movies.append(movie)
    return movies

@app.put("/movies/{movie_id}")
def update_movie(movie_id : int, updated_movie : Movie):
    for index, movie in enumerate(movies):
        if movies.id == movie_id:
            movies[index] = updated_movie
            return movies
    return {"error" : "Movie not found"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id : int):
    for index, movie in enumerate(movies):
        if movie.id == movie_id:
            movies.pop(index)
            return movies
    return {"error" : "Movie not found"}
