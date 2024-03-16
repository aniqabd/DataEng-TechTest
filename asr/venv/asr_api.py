from flask import Flask, request, jsonify
import librosa
import torch
from pydub import AudioSegment
import numpy as np
import io
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

app = Flask(__name__)

# Load pre-trained model and processor
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")

# Converts an MP3 file to WAV format using pydub. Returns the audio data as a numpy array.
def convert_mp3_to_wav(audio_file):
    # Load the MP3 audio file with pydub
    sound = AudioSegment.from_mp3(audio_file)
    # Convert to WAV format
    buffer = io.BytesIO()
    sound.export(buffer, format="wav")
    # Use librosa to load the buffer
    buffer.seek(0)
    y, sr = librosa.load(buffer, sr=16000)
    return y, sr

# Route for a ping API, returns "pong" if the service is working
@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

# Route for Automatic Speech Recognition (ASR) API
@app.route('/asr', methods=['POST'])

# This method gets uploaded audio file from request, convert it from MP3 to wav to get audio data and sample rate,
# process the audio from Wav2Vec2 nodel for transcription, and returns a JSON response with transcription and duration
def asr():
    # Check if 'file' field is present in the request, return error response if 'file' is missing
    if 'file' not in request.files:
        return jsonify({"error": "file is required"}), 400
    
    audio_file = request.files['file'] 
    audio_input, sample_rate = convert_mp3_to_wav(audio_file)
    input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    duration = librosa.get_duration(y=audio_input, sr=sample_rate)

    response = {
        'transcription': transcription[0],
        'duration': str(duration)
    }
    return jsonify(response)

# Run the flask application on port 8001 in debug mode
if __name__ == '__main__':
    app.run(debug=True,port=8001)




