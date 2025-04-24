from transformers import pipeline

# Load DialoGPT-medium from Hugging Face
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def get_response(text):
    response = chatbot(text)[0]['generated_text']
    return response
