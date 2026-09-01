import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
instructions = "Answer concisely. You like to say the words 'joever', 'joevering', 'joevered; at random places a lot."

st.write("# OpenJI chad")

with st.form("prompt_form"):
    prompt = st.text_input  ("Enter your prompt:")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.write("Thinking...")
        print(f"Prompt: {prompt}")
        response = client.responses.parse(
            model = "gpt-5.6-luna",
            instructions = instructions,
            reasoning={
                "effort": "low"  # Choose from "low", "medium", or "high"
            },
            # Ensure "tools" either omits {"type": "web_search"} or is completely empty
            tools=[], 
            input = prompt
        )

        st.balloons()

        print(response)
        st.write("## Response:")
        st.write(response.output_text)


