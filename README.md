#  Voice-Insight-Summarizer

An AI-powered audio intelligence tool that converts speech to text and extracts actionable insights using OpenAI's Whisper and GPT-4.

###  Features
* **Local Transcription:** Uses Whisper models locally for high-speed, private speech-to-text conversion.
* **Action Item Extraction:** Automatically identifies tasks and responsibilities from meeting transcripts.
* **Audio Pre-processing:** Handles various audio formats (MP3, WAV, M4A).
* **Privacy First:** Transcription is performed on-device to minimize data exposure.

###  Tech Stack
* **Whisper:** State-of-the-art Speech-to-Text model.
* **Python / Pydub:** Audio file manipulation.
* **OpenAI API:** For advanced NLP summarization and logic extraction.

###  Quick Start
```bash
pip install openai-whisper pydub
python main.py --file meeting_recording.mp3
