import streamlit as st
from openai import OpenAI
from pydantic import BaseModel, Field


def generate_quiz(input: str):
    """
    Generate a quiz based on the input text and instructions.
    """
    class Question(BaseModel):
        question_statement : str 
        options: list[str]
        answer: int = Field(..., description="Index of the correct answer in the options list")


    class Quiz(BaseModel):
        introduction: str
        questions: list[Question]

    instructions = "Generate a quiz of 5 multiple-choice questions to test the user's knowledge about the topic given. Write a short introduction about the topic."

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.responses.parse(
        model = "gpt-5.6-luna",
        instructions = instructions,
        input = input,
        text_format=Quiz,
        tools=[],  # Ensure "tools" either omits {"type": "web_search"} or is completely empty
        reasoning={"effort": "low"}  # Choose from "low", "medium", or "high"
    )

    return response


st.write("# Duopingo: learn anything")

if "quiz" not in st.session_state:
    st.session_state.quiz = None


with st.form("prompt_form"):
    prompt = st.text_input  ("Describe what you want to learn:")
    submit_button = st.form_submit_button(label="Generate Quiz")

if submit_button:
    st.write("Generating quiz...")
    st.session_state.quiz = generate_quiz(prompt).output_parsed
    st.balloons()

if st.session_state.quiz is not None:
    quiz = st.session_state.quiz
    st.session_state["correct_answers"] = 0
    st.session_state["questions_answered"] = 0

    st.write(quiz.introduction)
    st.write("### Try the quiz:")
    for i, question in enumerate(quiz.questions):

        with st.container(border=True):
            answer = st.radio(
                f"{i+1}. {question.question_statement}",
                question.options, key=f"question_{i}",
                index=None
            )

            if answer is not None:
                st.session_state.questions_answered += 1
                if answer == question.options[question.answer]:
                    st.session_state.correct_answers += 1
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer is Option #{question.answer + 1}: {question.options[question.answer]}")

    if st.session_state.questions_answered == len(quiz.questions):
        if st.session_state.correct_answers == len(quiz.questions):
            st.balloons()
        st.write(f"You got {st.session_state.correct_answers} out of {len(quiz.questions)}.")
        