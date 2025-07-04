# patch_google_genai.py
import os
from google.generativeai import configure

def patch_genai():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment!")
    configure(api_key=api_key)
