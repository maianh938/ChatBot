# app.py - Streamlit app
import streamlit as st
from chatbot import get_chatbot_response
from tts import text_to_speech
import os

st.title("Free Prototype Chatbot with Speaking Avatar")

user_input = st.text_input("Ask me anything:")

if user_input:
    # Get chatbot response
    response = get_chatbot_response(user_input)
    st.write("Chatbot:", response)

    # Convert response to speech
    audio_path = text_to_speech(response)
    st.audio(audio_path)

    # Here you would call SadTalker to generate avatar video
    # For prototype, just show a placeholder
    st.video("avatar_speaking.mp4")
