from flask import Flask, redirect, url_for, render_template, request

from tmdbv3api import Movie
from tmdbv3api import Discover
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '0c8cda0ec2f25eaa3eaf18991dde2e6c'


app=Flask(__name__)


@app.route('/')

def index():
    movie=Movie()
    discover = Discover()
    movie1 = discover.discover_movies({'sort_by' : 'popularity.desc'})
    temp=''
    for m in movie1:
        temp+=m.title
        temp+='<br>'
    return render_template('index.html', mov=temp)

@app.route("/", methods=["POST"])
def home():
    
    movie = Movie()
    search = movie.search(request.form["movie_field"])
    s=''
    for res in search:
        s+='<p style="text-align:center;font-size:30px;">'
        s+=(res.title)
        s+='</p>'
        #movie_field in the above line has the data entered in the search field on the webpage.
    
    return render_template('pass.html', movies=s)
if __name__=='__main__':
    app.run(debug=True)
