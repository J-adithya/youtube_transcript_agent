from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_youtube_transcript(url: str) -> str:
    try:
        video_id = parse_qs(urlparse(url).query)['v'][0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([entry['text'] for entry in transcript])
        return text
    except Exception as e:
        return f"[ERROR] Transcript extraction failed: {e}"
