
from deepface import DeepFace
import google.generativeai as genai
import time

from google.auth.metrics import token_request_access_token_sa_assertion
from httplib2.auth import token
from tensorflow.dtensor.python.config import client_id

#Setup Spotify API

import base64
import requests
import datetime

client_id = 'db2a2936661b4ba096e11c96d4bdd6f0'
client_secret = 'bd2be50a6e6e472e9b678e19559cdd31'

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = 'https://accounts.spotify.com/api/token'
method = "POST"

token_data = {
    "grant_type" : "client_credentials"
}

token_headers = {
    "Authorization" : f"Basic {client_creds_b64.decode()}"
}

req = requests.post(token_url, data=token_data, headers=token_headers)
token_response_data = req.json()

token_response_data = req.json()
access_token = token_response_data['access_token']
expires_in = token_response_data['expires_in'] #seconds
token_type=token_response_data['token_type']

def token_headers(self):
    client_creds_b64= self.client_credentials()
    return{"Authorization": f"Basic {client_creds_b64.decode()}"}

def authenticate(self):
    token_url = self.token_url
    token_data = self.token_data()
    token_headers = self.token_headers()
    req= requests.post(token_url, data=token_data, headers=token_headers)
    print(req.json)

    token_response_data = req.json()
    access_token= token_response_data['access_token']
    expires_in = token_response_data['expires_in']

    self.access_token = access_token
    return token_response_data


def SpotifyAPI(client_id, client_secret):
    pass


spotify_client = SpotifyAPI(client_id, client_secret)
print(spotify_client.__init__(client_id,client_secret))

# Setup the DeepFace Library:
face_analysis = DeepFace.analyze(img_path="abc.png")
print(face_analysis[0]['dominant_emotion'])
string = str(face_analysis[0]['dominant_emotion'])

# # Setup the Gemini API:
API_KEY = "AIzaSyBxZbDPRLmch5mFIFxQS9zYKv8sR5MHXtU"
genai.configure(api_key=API_KEY)

history = "1. Bohemian Rhapsody by Queen\n2. Happier by Ed Sheeran\n3. Bad Guy by Billie Eilish\n4. Shape of You by Ed Sheeran\n5. Shallow by Lady Gaga & Bradley Cooper\n6. Dance Monkey by Tones and I\n7. Wonderwall by Oasis\n8. Believer by Imagine Dragons\n9. Thinking Out Loud by Ed Sheeran\n10. Sweet Caroline by Neil Diamond\""

model = genai.GenerativeModel("gemini-1.5-flash")
concat_string = ("My current mood is" + string +
                 "This is my listening history on Spotify" + history +
                 "You are Serenata. You are supposed to provide song recommendations for the user based on the provided current mood and my Spotify listening history for the past 50 songs. Other than outputting the name of the song, do not print anything else. If possible, also provide the Spotify link of the given song.")


response = model.generate_content(concat_string)
print(response.text)


