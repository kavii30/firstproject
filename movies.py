import pickle
import pandas as pd
from difflib import get_close_matches

# Load data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower()
    movie_titles = movies['title'].str.lower().tolist()

    # Fuzzy match the input to known titles
    close_match = get_close_matches(movie, movie_titles, n=1, cutoff=0.4)

    if not close_match:
        return ["❌ Movie not found. Try another title."]

    # Get the index of the matched title
    matched_title = close_match[0]
    index = movies[movies['title'].str.lower() == matched_title].index[0]

    # Get similarity scores
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # Get top 5 recommendations (excluding the input movie)
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
