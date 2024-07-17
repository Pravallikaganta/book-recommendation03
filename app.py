import pickle
import streamlit as st
from utils import recommend_books
import os

st.header("Books Recommendation System")

# Define the new directory to save the artifacts
artifacts_dir = r"C:\Users\prava\model_Deployment_claiments\book-recommendation03\artifacts"

# Define the paths for the pickle files
model_path = os.path.join(artifacts_dir, 'model.pkl')
books_name_path = os.path.join(artifacts_dir, 'books_name.pkl')
final_rating_path = os.path.join(artifacts_dir, 'final_rating.pkl')
book_pivot_path = os.path.join(artifacts_dir, 'book_pivot.pkl')

# Load the pickle files
model = pickle.load(open(model_path, 'rb'))
books_name = pickle.load(open(books_name_path, 'rb'))
final_rating = pickle.load(open(final_rating_path, 'rb'))
book_pivot = pickle.load(open(book_pivot_path, 'rb'))

selected_book = st.selectbox("Type or select a book",books_name)

if st.button("Show Recommendation"):
    recommendation_books , poster_url = recommend_books(selected_book,model,books_name,final_rating,book_pivot)

    col1, col2 , col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

    with col1:
        st.caption(recommendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.caption(recommendation_books[2])
        st.image(poster_url[2])

    with col3:
        st.caption(recommendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.caption(recommendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.caption(recommendation_books[5])
        st.image(poster_url[5])

    with col6:
        st.caption(recommendation_books[6])
        st.image(poster_url[6])

    with col7:
        st.caption(recommendation_books[7])
        st.image(poster_url[7])

    with col8:
        st.caption(recommendation_books[8])
        st.image(poster_url[8])
