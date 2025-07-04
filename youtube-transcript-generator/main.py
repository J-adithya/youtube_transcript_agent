# main.py
# Used to test the tools that are created, the application will work normally even without this code

from my_mcp_server.tools.navigate_to_url import open_youtube
from my_mcp_server.tools.extract_transcript import extract_youtube_transcript
from my_mcp_server.tools.summarize_text import summarize_text

def test_tools():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    print("📺 Opening YouTube video...")
    open_youtube(url)

    print("📝 Extracting transcript...")
    transcript = extract_youtube_transcript(url)
    print("📄 Transcript:", transcript[:300], "...")  # Show first 300 chars

    print("🧠 Summarizing...")
    summary = summarize_text(transcript)
    print("✅ Summary:", summary)

if __name__ == "__main__":
    test_tools()
