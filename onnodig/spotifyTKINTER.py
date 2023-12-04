import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
from tkinter import messagebox

def download_song(track_uri):
    try:
        track_info = sp.track(track_uri)
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        download_path = os.path.expanduser('~') + '/Downloads/'
        download_path += f"{artist_name} - {track_name}.mp3"
        
        # Your code to download the song goes here
        # This example assumes that you have obtained the song file from a legal source
        
        messagebox.showinfo("Download Complete", "Song downloaded successfully.")
    except Exception as e:
        print(f"Error downloading song: {e}")
        messagebox.showerror("Error", "Unable to download song.")

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
