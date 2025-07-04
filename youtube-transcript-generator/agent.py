import os
import asyncio
from dotenv import load_dotenv

# ✅ Load environment variables first
load_dotenv()

# ✅ Patch Gemini before using it
from patch_google_genai import patch_genai
patch_genai()

from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI

from my_mcp_server.tools.navigate_to_url import open_youtube
from my_mcp_server.tools.extract_transcript import extract_youtube_transcript
from my_mcp_server.tools.summarize_text import summarize_text
from urllib.parse import urlparse, parse_qs

# ✅ Clean the URL to avoid playlist junk
def sanitize_youtube_url(url: str) -> str:
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    video_id = query_params.get("v", [None])[0]
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

# ✅ Tool builder
def build_tools():
    return [
        Tool.from_function(
            name="OpenYouTube",
            func=open_youtube,
            description="Open a YouTube URL",
        ),
        Tool.from_function(
            name="ExtractTranscript",
            func=extract_youtube_transcript,
            description="Extract transcript from a YouTube URL",
        ),
        Tool.from_function(
            name="SummarizeTranscript",
            func=summarize_text,
            description="Summarize a long transcript text",
        ),
    ]

# ✅ Main logic
async def main():
    user_url = input("🔗 Enter a YouTube video URL: ").strip()
    clean_url = sanitize_youtube_url(user_url)
    print(f"✅ Clean URL used: {clean_url}")

    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3,
    )

    tools = build_tools()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    query = f"Summarize the transcript of this video: {clean_url}"
    result = await asyncio.to_thread(agent.run, query)
    print("\n📝 Final Summary:\n", result)

if __name__ == "__main__":
    asyncio.run(main())
