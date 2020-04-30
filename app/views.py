from flask import render_template
from app import app

@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html', title=title, popular = popular_movies, upcoming = upcoming_movies, now_showing =now_showing_movie_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id=movie_id)