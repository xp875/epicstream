import streamlit as st

st.write("# Duopingo: learn anything")

st.write(
    "Here at Duopingo, we believe that anyone can learn anything. Just use our app for 5 minutes a day, "
    "and you'll become the next Einstein! Simply tell us what you want to learn, and you'll get short daily lessons and quizzes to stretch your mind."
)

st.page_link("pages/1_Learn.py", label="Learn")
st.page_link("pages/2_Quiz.py", label="Take a Quiz")