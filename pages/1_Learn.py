import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
instructions = "You are a teacher from Duopingo who helps the user learn anything. Generate a readable and engaging lesson based on the user's input. "

st.write("# Duopingo: learn anything")
st.write("## Daily Lesson, powerd by OpenJI chad")

with st.form("prompt_form"):
    prompt = st.text_area("Describe what you want to learn:")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    with st.spinner("Generating lesson..."):
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


    st.write(response.output_text)
    estimated_cost = response.usage.input_tokens * 20 + response.usage.output_tokens * 120
    estimated_cost /= 1e6
    st.write(f"Estimated cost: {estimated_cost:.2} cents")

