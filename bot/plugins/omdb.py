import os
import PTN
import requests
import json
import imdb

def get_details(movie):
    split = PTN.parse(movie)
    Key = split["title"]
    ia = imdb.IMDb()
    movie = ia.search_movie(Key)
    x = movie[0]
    id = x.movieID
    info = ia.get_movie(id)
    title = info["title"]
    year = info["year"]
    rating = info["rating"]
    genre = info["genres"]
    rated = ia.get_movie_parents_guide(id)
    rate = rated['data']['certification'][8]
    gen = ', '.join([str(elem) for elem in genre])
    url = info["full-size cover url"]
    return {"title":title,"year":year,"rated":rate,"genre":gen,"rating":rating,"image":url}
    

    
           
        
