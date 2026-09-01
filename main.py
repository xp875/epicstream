import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
instructions = "Answer concisely. You like to say the word 'Joever' a lot."

st.write("# OpenJI chad")

with st.form("prompt_form"):
    prompt = st.text_area("Enter your prompt:")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.balloons()

        print(f"Prompt: {prompt}")
        response = client.responses.parse(
            model = "gpt-5.6-luna",
            instructions = instructions,
            input = prompt
        )

        print(response)
        st.write("## Response:")
        st.write(response.output_text)


