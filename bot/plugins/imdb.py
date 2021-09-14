import os
import PTN
import requests
import json
import imdb

def get_details(movie):
    split = PTN.parse(movie)
    KEY = split["title"]
    
    ia = imdb.IMDb()
    movie = ia.search_movie(KEY)

    x = movie[0]
    id = x.movieID
    print(id)

    info = ia.get_movie(id)
    title = info["title"]
    year = info["year"]
    rating = info["rating"]
    genre = info["genres"]
    rated = ia.get_movie_parents_guide(id)
    rate = rated['data']['certification'][8]
    gen = ', '.join([str(elem) for elem in genre])
    url = info["cover url"]
    dic = {"title":title,"year":year,"rated":rate,"genre":gen,"rating":rating,"image":url}
    return dic

    
           
        
