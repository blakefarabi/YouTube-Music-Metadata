"""
Spotify setup
"""
import os
import spotipy
import spotipy.util as spotipy_util
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = "4258b5c02f0e4d1ba32f0c354091590d"
SPOTIFY_CLIENT_SECRET = "3d91ca901ac143bc8527ee91e1081486"
# SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
# SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
# SPOTIFY_REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")
# SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")
# SPOTIFY_TOKEN = spotipy_util.prompt_for_user_token(
#     SPOTIFY_USERNAME, 'user-read-email', SPOTIFY_CLIENT_ID,
#     SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)
# SPOTIFY = spotipy.Spotify(auth=SPOTIFY_TOKEN)

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
SPOTIFY = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_sp(query):
    """
    Method to search for a track using Spotify API
    """
    response = SPOTIFY.search(q=query, type='track')
    return response

def track_sp(uri):
    """
    Method to search for a track using Spotify API
    """
    response = SPOTIFY.track(uri)
    return response
