import whisper
import os

class VoiceTranscriber:
    def __init__(self, model_size="base"):
        # We load the model locally - big advantage for privacy
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: str):
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        print(f"Processing audio: {audio_path}...")
        result = self.model.transcribe(audio_path)
        return result["text"]
