from flask import Flask,render_template
app = Flask(__name__)
movies = [
    {   "id":1,
        "title": "Interstellar",
        "rating": 8.7,
        "power": 90,
        "genres": {
            "Sci-Fi": 95,
            "Drama": 80
        }
    },
    {   "id":2,
        "title": "Inception",
        "rating": 8.8,
        "power": 92,
        "genres": {
            "Action": 85,
            "Sci-Fi": 90
        }
    }
]
@app.route('/')
def home():
    return render_template('index.html', movies=movies)
@app.route('/movies/<int:id>')
def movie_detail(id):
    for movie in movies:
        if movie["id"]==id:
            return render_template("movie_detail.html",movie=movie)
    return "Movie Not Found"
if __name__=='__main__':
    app.run(debug=True)