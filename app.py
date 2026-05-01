from flask import Flask,render_template,request
app = Flask(__name__)
movies = {
   1: {   "id":1,
        "title": "Interstellar",
        "rating": 8.7,
        "power": 90,
        "genres": {
            "Sci-Fi": 95,
            "Drama": 80
        }
    },
   2: {   "id":2,
        "title": "Inception",
        "rating": 8.8,
        "power": 92,
        "genres": {
            "Action": 85,
            "Sci-Fi": 90
        }
    }
}
@app.route('/',methods=['GET','POST'])
def home():
    filtered_movies=list(movies.values())
    if request.method=='POST':
        search=request.form.get('search')
        filtered_movies=[]
        for movie in movies.values():
             if search.lower() in movie["title"].lower():
                 filtered_movies.append(movie)
    return render_template('index.html', movies=filtered_movies)
@app.route('/movies/<int:id>')
def movie_detail(id):
    movie=movies.get(id)
    if movie:
        return render_template('movie_detail.html',movie=movie)
    return "Movie Not Found"
if __name__=='__main__':
    app.run(debug=True,port=3000)