import os
import PTN
import requests
import json

def get_details(movie):
    split = PTN.parse(movie)
    KEY = split["title"]
    
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":KEY,"page":"1","r":"json"}
    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "c25ac23bc1mshecf589f21bf76f7p13698bjsn2b030cd03517"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    id = json.loads(response.text)
    if id.get("Response") == "True":
        ids = id.get("Search")[0]
        imdb_id = ids.get("imdbID")
    link = "https://www.omdbapi.com/?apikey=1625aff3"
    parameters = {"i":imdb_id,"r":"json"}
    details = requests.request("GET", link, params=parameters)
    gets = json.loads(details.text)
    movie = gets.get("Title")
    year = gets.get("Released")
    plot = gets.get("Plot")
    rated = gets.get("Rated")
    genre = gets.get("Genre")
    rating = gets.get("imdbRating")
    dic = {"title":movie,"released":year,"rated":rated,"genre":genre,"rating":rating,"plot":plot}
    return dic
    
           
        
