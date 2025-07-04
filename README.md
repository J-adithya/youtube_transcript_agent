## 🎬 YouTube Transcript Generator & Summarizer with Gemini + LangChain

This is a powerful AI-driven command-line tool that extracts transcripts from YouTube videos and generates intelligent summaries using Google Gemini via LangChain. It utilizes the Whisper model for high-quality audio transcription and Modular Control Protocol (MCP) for structured task execution.

---

## 🚀 Features

- 🎥 Extracts audio transcript from YouTube videos using Whisper
- ✨ Summarizes content using Gemini (via LangChain)
- 🧠 LangChain agent handles multi-step logic and decision-making
- 💬 Clean terminal-based interface (no browser or GUI required)
- 🧩 Modular Control Protocol (MCP) based tool design
- 💻 Works on any platform with Python support

---

## 📁 Folder Structure

Follow the same structure as this repository

---

## ⚙️ Prerequisites

- Python 3.8 or higher
- Git
- Internet connection
- Google Cloud account with Gemini API key
- [ffmpeg](https://ffmpeg.org/download.html) installed and added to system path (for Whisper)

---

## 🧪 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/youtube-transcript-generator.git
cd youtube-transcript-generator
```
### 2️⃣ Create and Activate Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Setup Environment Variables
Create a .env file in the root directory with the following content:

```env
GOOGLE_API_KEY=your-gemini-api-key-here
GEMINI_MODEL=gemini-1.5-flash
```
You can get your Gemini API key from Google AI Studio or the Google Cloud Console.

Note: This project uses the Whisper model to transcribe YouTube audio into text. Make sure your system has ffmpeg installed, as Whisper requires it to process audio files.

Install ffmpeg:
```
# Download from https://ffmpeg.org/download.html and add to PATH

macOS: brew install ffmpeg

Linux (Debian): sudo apt install ffmpeg
```

🧠 How It Works
You provide a YouTube URL.

The app opens the video in the browser.

It uses Whisper to extract the transcript from the audio.

LangChain + Gemini AI summarizes the content intelligently.

The final summary is shown in your terminal.

### ▶️ Run the Agent
```bash
python agent.py
```
You'll be prompted to enter a YouTube video URL. The system will handle the rest.


### 🧾 requirements.txt
```
langchain
openai
google-generativeai
yt-dlp
whisper
gradio
python-dotenv
youtube-transcript-api

```

To install all dependencies:

```bash
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

## 🙌 Contributing

PRs and issues are welcome! If you have improvements or feature ideas, feel free to fork the repo and open a pull request.
