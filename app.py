from flask import Flask,render_template,request
import requests 

app = Flask(__name__)

def fetch_movies():
    url = "https://api.themoviedb.org/3/trending/movie/week"
    params={
        "api_key":"5e4680fa8acf126d39b554e2d1733db0"
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data["results"]

@app.route('/',methods=['GET','POST'])
def home():
    movies = fetch_movies()
    filtered_movies=movies
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
    return render_template('404.html')


if __name__=='__main__':
    app.run(debug=True,port=3000)