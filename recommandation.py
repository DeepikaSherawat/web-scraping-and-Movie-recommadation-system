# _*_ coding: utf-8 _*_
"""
created on oct 26 04:01:17 

"""




import streamlit as st
import pickle
import requests
from bs4 import BeautifulSoup
import numpy as np



def recommend(movie):
    index = df2[df2['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
   
    for i in distances[1:6]:
       
        recommended_movie_names.append(df2.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommendion System')
df2 = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = df2['title'].values
selected_movie = st.selectbox("select any movie",movie_list)


    

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        
    with col2:
        st.text(recommended_movie_names[1])
       
    with col3:
        st.text(recommended_movie_names[2])
       
    with col4:
        st.text(recommended_movie_names[3])
        
