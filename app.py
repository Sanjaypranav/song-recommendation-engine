'''webserver gateway run 2 methods Get() Post() are main methods for flask '''
from optparse import Values
import numpy as np
from flask import Flask, request, jsonify, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__)



def get_cosim_artist_df(track_name, data, n):
    print('data =',data.head())
    artist_array = np.array(data.T[track_name]).reshape(1, -1)
    dataset_array = data.drop(index=track_name).values
    print('dataset_array',dataset_array.shape)
    cosim_scores = cosine_similarity(artist_array, dataset_array).flatten()
    track_names_array = data.drop(index=track_name).index.values

    df_result = pd.DataFrame(
        data={
            'Song name': track_names_array,
            'cosim_' + track_name: cosim_scores,
        }
    )

    df_result = df_result.sort_values(
        by='cosim_' + track_name, ascending=False).head(n)
    return df_result.reset_index(drop=True)



@app.route('/', methods=['GET', 'POST'])
def index():
    sp = authorize_spotify()
    result = sp.current_user_recently_played(limit = 1)
    # print(result['items'][0]['track']['name'])
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        uri = []
        sp = authorize_spotify()
        data = pd.read_csv('src/data/scaled_spotify_tamil.csv')
        data.index = data['track_name']
        data.drop_duplicates(subset = "track_name", keep="first", inplace=True)
        data.drop('track_name',1,inplace=True)
        song = request.form['track_name']
        recommended_songs = get_cosim_artist_df(song, data, 15)
        for song in recommended_songs['Song name'].values:
            result = sp.search(q=song, type='track')
            uri.append(result['tracks']['items'][0]['uri'])
    return render_template('index.html',prediction=recommended_songs['Song name'].values,uris = uri,num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])


def authorize_spotify():
    client_id = "2a32ba42c2f346138baa11f711d69366"
    client_secret = "e191f2f7a99f45fba77d6f193ca4c845"

    scope = 'user-read-private user-read-email user-library-read user-library-modify playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative'

    authentication = SpotifyOAuth(
            client_id=client_id, 
            client_secret=client_secret, 
            redirect_uri='http://localhost:8888/callback',
            scope=scope)

    sp = spotipy.Spotify(auth_manager=authentication)
    return sp


if __name__ == '__main__':
    app.run(debug=True)