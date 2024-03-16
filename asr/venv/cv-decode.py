import pandas as pd
import requests

# Load CSV file
df = pd.read_csv("cv-valid-dev.csv")

# API endpoint where the Automatic Speech Recognition (ASR) service is hosted
url = "http://localhost:8001/asr" 

# This method iterate over each audio files in the data frame, opens the audio file in binary mode,
# create a dictionary containing the audio files, send a POST request to the ASR API endpoint with the audio file
# It will then extract the transcription from the JSON response and update the 'generated_text' column of the csv file
for index, row in df.iterrows():
    audio_file = f"cv-valid-dev/{row['filename']}"
    with open(audio_file, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files = files)
        if response.status_code == 200:
            result = response.json()
            df.at[index, 'generated_text'] = result['transcription']
        else:
            print(f"Error processing audio file: {audio_file}")  


# Save updated dataframe to a new CSV file
df.to_csv("cv-valid-dev-updated.csv", index=False)

