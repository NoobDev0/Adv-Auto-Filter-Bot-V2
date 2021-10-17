import os
import PTN
import requests
import json
import imdb

def get_details(movie):
    split = PTN.parse(movie)
    extract = split["title"]
    ia = imdb.IMDb()
    movie = ia.search_movie(extract)
    x = movie[0]
    id = x.movieID
    info = ia.get_movie(id)
    title = info["title"]
    year = info["year"]
    rating = info["rating"]
    genre = info["genres"]
    imdblink = "https://m.imdb.com/title/tt{i}".format(i=id)
    gen = ', '.join([str(elem) for elem in genre])
    return {"title":title,"year":year,"imdb":imdblink,"genre":gen,"rating":rating}

def get_poster(movie):
    split = PTN.parse(movie)
    extract = split["title"]
    ia = imdb.IMDb()
    movie = ia.search_movie(extract)
    x = movie[0]
    id = x.movieID
    info = ia.get_movie(id)
    poster=info["full-size cover url]
    return poster
    

    
           
        
