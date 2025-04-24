# chatbot.py
from transformers import pipeline

chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def get_chatbot_response(text):
    result = chatbot(text)
    return result['generated_text']
