# Synthesizer Agent – Final Answer

import google.generativeai as genai

class SynthesizerAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def synthesize(self, query, context, tool_output=None):
        prompt = f"""
You are an AI assistant.
Answer using ONLY the context below.
If not present, say "I don't know".

Context:
{context}

Tool Output:
{tool_output}

Question:
{query}
"""
        return self.model.generate_content(prompt).text
