import gradio as gr
import requests

def ask(query):
    response = requests.post(
        "http://localhost:8000/query",
        json={"query": query}
    )
    return response.json()["answer"]

gr.Interface(
    fn=ask,
    inputs="text",
    outputs="text",
    title="Cloud Multi-Agent RAG System"
).launch()
