import pandas as pd
import streamlit as st

ramen_ratings = pd.read_csv("ramen-ratings.csv")
st.write(ramen_ratings)