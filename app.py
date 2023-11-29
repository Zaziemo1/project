import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydub import AudioSegment
import requests
from io import BytesIO

client_id = "4cc048fb419440f5951860cf0a9f9db0"
client_secret = "763a491995ce4b1cad73ecccd6bb9ade"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def download_Spotifysong(track_uri):
    try:
        track_info = sp.track(track_uri)
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        
        # Get the preview URL
        preview_url = track_info.get('preview_url')
        if not preview_url:
            raise ValueError("Preview URL not available for the selected track.")
        
        # Download the audio data
        audio_data = download_Spotifyaudio(preview_url)
        
        # Convert to AudioSegment
        audio_segment = AudioSegment.from_file(BytesIO(audio_data), format="mp3")
        
        # Saving the audio segment to an MP3 file
        download_path = os.path.expanduser('~') + '/Downloads/'
        mp3_filename = f"{artist_name} - {track_name}.mp3"
        mp3_path = os.path.join(download_path, mp3_filename)
        audio_segment.export(mp3_path, format="mp3")

        messagebox.showinfo("Download Complete", "Song downloaded and converted to MP3 successfully.")
    except Exception as e:
        print(f"Error downloading song: {e}")
        messagebox.showerror("Error", "Unable to download song.")

def download_Spotifyaudio(url):
    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None




        


def download_Youtubevideo():
    url = url_entry.get()

    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        messagebox.showinfo('Download Complete', f'Download complete: {yt.title}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main window
root = tk.Tk()
frame2 = tk.Frame()
root.resizable(width=False,height=False)
root.geometry("400x300")
root.title('MP4 & MP3 Downloader')

tabControl = ttk.Notebook(master=root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Youtuber Video Downloader')
tabControl.add(tab2, text='Spotify MP3 Downloader')

# tab 1 yt
url_label = tk.Label(tab1, text='Enter YouTube URL:')
url_label.pack(pady=10)
url_entry = tk.Entry(tab1, width=40)
url_entry.pack(pady=10)

# tab 2 spotify
url_label2 = tk.Label(tab2, text='Enter Spotify URL:')
url_label2.pack(pady=10)
url_entry2 = tk.Entry(tab2, width=40)
url_entry2.pack(pady=10)

# pack yt
tabControl.pack(expand=1, fill="both")


# Download yt
download_button = tk.Button(tab1, text='Download Video', command=download_Youtubevideo)
download_button.pack(pady=20)

# Download Spotify
download_button2 = tk.Button(tab2, text='Download Audio',command= lambda : download_Spotifysong(url_entry2.get()))
download_button2.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
