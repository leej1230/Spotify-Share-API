from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)

# Your token
token = ''

def ms_conversion(millis,min):
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    if min:
        return minutes
    return seconds

@app.route('/')
def index():
    head = {'Authorization': 'Bearer '+ token}
    responce = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=head)
    status = {'is_playing': responce.json()['is_playing']}
    if(responce.json()['is_playing']):
        status['artist_name'] = responce.json()['item']['artists'][0]['name']
        status['song_name'] = responce.json()['item']['name']
        status['image_url'] = responce.json()['item']['album']['images'][0]['url']
        status['current_time_min'] = ms_conversion(responce.json()['progress_ms'], True)
        status['current_time_sec'] = ms_conversion(responce.json()['progress_ms'], False)
        status['total_time_min'] = ms_conversion(responce.json()['item']['duration_ms'], True)
        status['total_time_sec'] = ms_conversion(responce.json()['item']['duration_ms'], False)
        status['song_url'] = responce.json()['item']['album']['external_urls']['spotify']
        return status
    return status