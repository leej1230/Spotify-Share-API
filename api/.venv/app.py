from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)

token = 'BQB1eU42YJ2l_h9LWKy_oYaPCcSeZKzuLPB6dHm-OlAFiHi2bl6_S9YO_A1QVZGoXSibEla_v3QxBt4viMpmFZsfJboMp9zk1Oikl4AWkQ_bcGcEREVh7wDFnA1JjEdlKWZ1zQNv91rRt0jo4S7UmSA0EsLS-YszddG-MY3ExSse89hWfNUoLw'

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