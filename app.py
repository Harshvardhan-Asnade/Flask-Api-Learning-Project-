from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    movies = [
    {
        "title": "Interstellar",
        "rating": 8.7,
        "power": 90,
        "genres": {
            "Sci-Fi": 95,
            "Drama": 80
        }
    },
    {
        "title": "Inception",
        "rating": 8.8,
        "power": 92,
        "genres": {
            "Action": 85,
            "Sci-Fi": 90
        }
    }
]
    return render_template('index.html', movies=movies)
@app.route('/movies')
def movie():
    return render_template("movies.html")
if __name__=='__main__':
    app.run(debug=True)