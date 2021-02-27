from flask import Flask, redirect, url_for, render_template, request

from tmdbv3api import Movie
from tmdbv3api import Discover
from tmdbv3api import TMDb
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')
tmdb = TMDb()
tmdb.api_key = API_KEY


app=Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    movie=Movie()
    discover = Discover()
    movie1 = discover.discover_movies({'sort_by' : 'popularity.desc'})
    movie2 = discover.discover_movies({'sort_by': 'release_date.desc'})
    temp=''
    temp2=''
    for m in movie1:
        temp+=m.title
        temp+='<hr>'
    for n in movie2:
        temp2+=n.title
        temp2+='<hr>'
    return render_template('index.html', mov=temp, mov2=temp2)

@app.route("/", methods=["POST"])
def home():
    
    movie = Movie()
    search = movie.search(request.form["movie_field"])
    s=''
    for res in search:
        name=res.title
        nm_list=name.split()
        

        s+='<p style="text-align:center;font-size:30px;">'
        s+='<a href="https://www.google.com/search?q='
        for nm in nm_list :
            s+=nm+"+"
        s=s[:-1]
        s+='+movie" target="_blank">'
        s+=(name)
        s+='</a>'
        s+='</p><hr>'
        #movie_field in the above line has the data entered in the search field on the webpage.
    
    return render_template('pass.html', movies=s)
if __name__=='__main__':
    app.run(debug=True)
