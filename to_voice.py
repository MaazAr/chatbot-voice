import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts(text="Hello, How are you doing today?", speaker_wav="audio.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text="Have you heard about Imagine dragons?", speaker_wav="audio.wav", language="en", file_path="output.wav")