import whisper
import ffmpeg
import os
from pydub import AudioSegment
import time

# Replace this with the actual path to your video file
video_path = ""
audio_path = "audio.mp3"
transcript_path = "transcript.md"

# Convert video to audio (MP3)
print(f"Extracting audio from {video_path}...")
ffmpeg.input(video_path).output(audio_path, format='mp3').run(overwrite_output=True)
print(f"Audio extracted to {audio_path}.")

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper model loaded.")

# Convert MP3 to WAV for Whisper
print(f"Converting {audio_path} to WAV format...")
audio = AudioSegment.from_mp3(audio_path)
wav_path = "audio.wav"
audio.export(wav_path, format="wav")
print(f"Conversion complete. WAV file saved as {wav_path}.")

# Transcribe audio
print(f"Transcribing audio from {wav_path}...")
start_time = time.time()
result = model.transcribe(wav_path)
end_time = time.time()
print("Transcription complete.")

# Calculate and print the time taken
time_taken = end_time - start_time
print(f"Transcription took {time_taken / 60:.2f} minutes.")

# Save transcript to Markdown file
markdown_content = f"# Transcript\n\n{result['text']}"

with open(transcript_path, "w") as f:
    f.write(markdown_content)
print(f"Transcription saved to {transcript_path}.")
