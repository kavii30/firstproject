# app.py

import streamlit as st
from movies import recommend  # make sure this import works

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎥 Movie Recommender System")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name.strip():
        recommendations = recommend(movie_name)
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.warning("Please enter a valid movie name.")
