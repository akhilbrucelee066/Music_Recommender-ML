import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pickle

st.set_page_config(page_title="Music Recommender", page_icon="🎵", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(120deg, #232526 0%, #414345 100%);
    }
    .music-title {
        font-weight: bold;
        color: #FFD369;
        margin-bottom: 4px;
    }
    .music-artist {
        color: #a3a3a3;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)


S_ID = ""
S_KEY = ""

auth_manage = SpotifyClientCredentials(client_id=S_ID, client_secret=S_KEY)
spotify = spotipy.Spotify(client_credentials_manager=auth_manage)

def fetch_album_cover(song, artist):
    query = f"track:{song} artist:{artist}"
    results = spotify.search(q=query, type="track")
    if results and results["tracks"]["items"]:
        return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    return "https://i.postimg.cc/0QNxYz4V/social.png"

def get_recommendations(song_title):
    idx = songs_df[songs_df['song'] == song_title].index[0]
    sim_scores = sorted(list(enumerate(similarity_data[idx])), reverse=True, key=lambda x: x[1])
    recommended_titles = []
    recommended_covers = []
    recommended_artists = []
    for i in sim_scores[1:6]:
        artist = songs_df.iloc[i[0]].artist
        title = songs_df.iloc[i[0]].song
        recommended_covers.append(fetch_album_cover(title, artist))
        recommended_titles.append(title)
        recommended_artists.append(artist)
    return recommended_titles, recommended_covers, recommended_artists

st.markdown(
    "<h2 style='text-align:center; color:#FFD369;'>🎵 Music Recommender</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#a3a3a3;'>Pick a song and get inspired by similar tracks 🎧</p>",
    unsafe_allow_html=True
)

songs_df = pickle.load(open('df.pkl', 'rb'))
similarity_data = pickle.load(open('similarity.pkl', 'rb'))

song_options = songs_df['song'].values
selected_song = st.selectbox(
    "Choose a song",
    song_options
)

if st.button('Show Recommendations'):
    titles, covers, artists = get_recommendations(selected_song)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(covers[i])
            st.markdown(f"<div class='music-title'>{titles[i]}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='music-artist'>by {artists[i]}</div>", unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; margin-top:2rem; color:#FFD369;'>"
    "Made by: Pranay Akhil Jeedimalla"
    "</div>",
    unsafe_allow_html=True
)
