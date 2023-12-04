import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_song(track_uri):
    try:
        track_info = sp.track(track_uri)
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']

        # Get the YouTube video URL from the track name and artist
        query = f"{artist_name} {track_name} audio"
        youtube_url = get_youtube_url(query)

        if youtube_url:
            # Download the audio from YouTube
            download_audio(youtube_url, artist_name, track_name)

            messagebox.showinfo("Download Complete", "Song downloaded and converted to MP3 successfully.")
        else:
            raise ValueError("Unable to find a suitable YouTube video for the track.")
    except Exception as e:
        print(f"Error downloading song: {e}")
        messagebox.showerror("Error", "Unable to download song.")

def get_youtube_url(query):
    try:
        # Use pytube to search for the YouTube video
        search_results = YouTube(query).streams.filter(only_audio=True).all()
        if search_results:
            return search_results[0].url
        else:
            return None
    except Exception as e:
        print(f"Error getting YouTube URL: {e}")
        return None

def download_audio(url, artist_name, track_name):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio file
        download_path = os.path.expanduser('~') + '/Downloads/'
        mp3_filename = f"{artist_name} - {track_name}.mp3"
        mp3_path = os.path.join(download_path, mp3_filename)
        audio_stream.download(output_path=download_path, filename=mp3_filename)

        # Convert to AudioSegment
        audio_segment = AudioSegment.from_file(mp3_path, format="mp3")

        # Save the audio segment to an MP3 file
        audio_segment.export(mp3_path, format="mp3")

    except Exception as e:
        print(f"Error downloading audio: {e}")

# Spotify API credentials
client_id = "4cc048fb419440f5951860cf0a9f9db0"
client_secret = "763a491995ce4b1cad73ecccd6bb9ade"

# Spotify API authentication
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create the main window
window = tk.Tk()
window.title("Song Downloader")

# Create and place widgets
url_label = tk.Label(window, text="Enter Spotify Track URI:")
url_label.pack(pady=10)

url_entry = tk.Entry(window, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(window, text="Download", command=lambda: download_song(url_entry.get()))
download_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
