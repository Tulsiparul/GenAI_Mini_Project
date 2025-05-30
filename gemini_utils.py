import os
import google.generativeai as genai

def ask_gemini(prompt, context="general"):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Context: {context}\nUser Query: {prompt}")
    return response.text
