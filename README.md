# Music Recommender using "Content-Based-Filtering"

- The app uses a dataset of song lyrics.
- It processes the lyrics and finds songs that are textually similar.
- When you select a song, it shows you 5 recommendations, along with their album covers (fetched from Spotify).

Tech Stack:

- Python (for all the backend logic)
- Streamlit (for the web interface)
- Spotipy (to get album covers from Spotify)
- scikit-learn (for text similarity)
- NLTK (for text processing)

Run by:

- Make sure you have Python 3.8+ installed.
- Modify the spotify Key & Id.
- Install dependencies:
   ```
   pip install -r requirements.txt
   ```
- Download the dataset (i used `spotify million song dataset` - it is openly avaliable from kaggel and other sources).
- Start the app:
   ```
   streamlit run app.py
   ```
