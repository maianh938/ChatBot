import gradio as gr
from chatbot import get_response
from tts import text_to_speech
from avatar_utils import generate_avatar_video
import time

def chat(user_input):
    # Get chatbot response
    response = get_response(user_input)
    
    # Generate audio
    audio_path = text_to_speech(response)
    
    # Generate avatar video
    video_path = generate_avatar_video(audio_path)
    
    return response, video_path

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Avatar Chatbot")
    
    with gr.Row():
        input_text = gr.Textbox(label="Your Message")
        output_video = gr.Video(label="AI Avatar")
    
    output_text = gr.Textbox(label="Chatbot Response")
    
    input_text.submit(
        fn=chat,
        inputs=input_text,
        outputs=[output_text, output_video]
    )

if __name__ == "__main__":
    demo.launch(server_port=7860, share=True)
