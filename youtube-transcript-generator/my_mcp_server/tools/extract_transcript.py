from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import tempfile
import os
import yt_dlp
import whisper

def extract_youtube_transcript(url: str) -> str:
    try:
        video_id = parse_qs(urlparse(url).query)['v'][0]
        # Try extracting subtitles
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join(entry['text'] for entry in transcript)

    except (TranscriptsDisabled, NoTranscriptFound):
        # Fall back to audio transcription using Whisper
        print("[INFO] Subtitles not found. Using Whisper to transcribe audio...")
        try:
            audio_path = download_audio(url)
            model = whisper.load_model("base")  # You can use "small", "medium", "large" for better quality
            result = model.transcribe(audio_path)
            os.remove(audio_path)
            return result["text"]
        except Exception as e:
            return f"[ERROR] Whisper transcription failed: {e}"

    except Exception as e:
        return f"[ERROR] Transcript extraction failed: {e}"

def download_audio(url: str) -> str:
    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, "yt_audio.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        return filename.replace(".webm", ".mp3").replace(".m4a", ".mp3")
