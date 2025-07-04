import os
from langchain_google_genai import ChatGoogleGenerativeAI

def summarize_text(transcript: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL"),
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    prompt = f"Summarize the following YouTube transcript:\n\n{transcript}"
    return llm.invoke(prompt)
