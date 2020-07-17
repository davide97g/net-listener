import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(
    client_credentials_manager=SpotifyOAuth(
        client_id="0d4a4b76120c4393afae588375cd0a35",
        client_secret="4efe0ef9a6134ddeacf2af30937aaf89",
        redirect_uri="http://localhost:5500",
        username="ghiotto.davidenko",
        scope=scope,
    )
)

for device in sp.devices().get("devices"):
    if device.get("is_active") == True:
        print(device.get("name"), "active")

next_to_play = None

resume = False

playlists = sp.user_playlists(user="ghiotto.davidenko")

for playlist in playlists.get("items"):
    # here choose the playlist you want to play
    if playlist.get("name") == "Deep focus":
        # next_to_play = playlist
        tracks = sp.playlist_tracks(playlist_id=playlist.get("id")).get("items")
        for t in tracks:
            track = t.get("track")
            if track.get("name") == "The Avengers":
                next_to_play = track.get("uri")

def pause():
    sp.pause_playback()

def play():    
    if sp.current_playback().get("item").get("uri") == next_to_play:
        sp.start_playback()
    else:
        sp.start_playback(uris=[next_to_play])

