import pickle
from click import command
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=825bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommended(movie):
    index = movies[movies['title'] == movie].index[0]
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True ,key=lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distance[1:6]:
       movie_id = movies.iloc[i[0]]['movie_id']
       recommended_movies_poster.append(fetch_poster(movie_id))
       recommended_movies_name.append(movies.iloc[i[0]].title)
       return recommended_movies_name, recommended_movies_poster


st.header("Movies Recommendation Systrm")
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb' ))


movies = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movies
)

if st.button('Show recommendation'):
  def recommend(movie):
    # your logic here
    return recommended_movies_name, recommended_movies_poster
  recommended_movies_name, recommended_movies_poster = recommend(selected_movie)


def recommend(movie):
    ...
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])       

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])   

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])   