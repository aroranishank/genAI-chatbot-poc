import os
import json
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

# Initialization

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")

client = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    
MODEL = "gemini-1.5-flash"

system_message = "You are a helpful assistant"
def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

    stream = client.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

demo = gr.ChatInterface(fn=chat, type="messages")


# def greet(text: str) -> str:
#     return text


# demo = gr.Interface(
#     fn=greet,
#     inputs=gr.components.Textbox(label='Input'),
#     outputs=gr.components.Textbox(label='Output'),
#     allow_flagging='never'
# )