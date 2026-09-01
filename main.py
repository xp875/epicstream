import streamlit as st


st.write("# My Streamlit App")

with st.form("prompt_form"):
    prompt = st.text_area("Enter your prompt:")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.success(f"You entered: {prompt}")
        st.balloons()

        
