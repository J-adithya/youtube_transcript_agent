from mcp.server.fastmcp import FastMCP
from my_mcp_server.tools.navigate_to_url import open_youtube
from my_mcp_server.tools.extract_transcript import extract_youtube_transcript
from my_mcp_server.tools.summarize_text import summarize_text

app = FastMCP("YouTubeTranscriptAgent")

@app.tool()
def navigate(url: str) -> str:
    """Open a YouTube URL"""
    return open_youtube(url)

@app.tool()
def extract_transcript(url: str) -> str:
    """Extract transcript from a YouTube URL"""
    return extract_youtube_transcript(url)

@app.tool()
def summarize(transcript: str) -> str:
    """Summarize YouTube transcript"""
    return summarize_text(transcript)

if __name__ == "__main__":
    app.run(transport="stdio")
