import os
import gradio as gr
import requests

API_URL = os.environ.get("API_URL", "http://localhost:8000/query")

def ask(query):
    response = requests.post(API_URL, json={"query": query})
    return response.json()["answer"]

gr.Interface(
    fn=ask,
    inputs="text",
    outputs="text",
    title="Cloud Multi-Agent RAG System"
).launch()
