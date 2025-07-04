# 🎬 YouTube Transcript Summarizer with Gemini + LangChain

This project is an AI-powered agent that extracts transcripts from YouTube videos and summarizes them using Google's Gemini (via LangChain). It uses the Whisper model for audio transcription and Playwright for web automation.

---

## 🚀 Features

- Extracts transcript from any YouTube video
- Summarizes video content using Gemini AI (Generative Language API)
- Fully automated workflow with LangChain tools
- Whisper model integration for accurate transcription
- Command-line interface (CLI) for simple use

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
Copy code
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
Windows: Download here

macOS: brew install ffmpeg

Linux (Debian): sudo apt install ffmpeg
```

🧠 How It Works
You provide a YouTube URL.

The app opens the video in the browser.

It uses Whisper to extract the transcript from the audio.

LangChain agent sends the transcript to Gemini for summarization.

The final summary is shown in your terminal.

### ▶️ Run the Agent
```bash
python agent.py
You'll be prompted to enter a YouTube video URL. The system will handle the rest.
```

### 🧾 requirements.txt
```nginx
langchain
openai
google-generativeai
playwright
pytube
whisper
gradio
python-dotenv
```

To install all dependencies:

```bash

pip install -r requirements.txt
```
📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

🙌 Contributing
PRs and issues are welcome! If you have improvements or feature ideas, feel free to fork the repo and open a pull request.
