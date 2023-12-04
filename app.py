import tkinter as tk
from tkinter import messagebox,ttk,filedialog
from tkinter import ttk
from pytube import YouTube
import os
import spotipy
import pygame
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


def download_preview(track_url):
    try:
        # Extract track ID from the URL
        track_id = track_url.split("/")[-1]

        # Replace 'YOUR_API_KEY' with your actual Deezer API key
        api_key = 'fc7985f3a217be08d8f0bcfbf5e83802s'
        api_url = f'https://api.deezer.com/track/{track_id}?output=json&apikey={api_key}'

        response = requests.get(api_url)
        data = response.json()

        if 'preview' in data:
            preview_url = data['preview']
            
            # Download the preview audio file
            audio_response = requests.get(preview_url)
            with open(f"preview_{track_id}.mp3", 'wb') as audio_file:
                audio_file.write(audio_response.content)

            return f"Preview downloaded successfully as preview_{track_id}.mp3"
        else:
            return "Preview not available for this track."

    except Exception as e:
        return f"An error occurred: {e}"
    

def download_preview_and_show_message():
    track_url = entry3.get()
    message = download_preview(track_url)
    messagebox.showinfo("Download Status", message)


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        file_var.set(file_path)

def play_music():
    file_path = file_var.get()
    if file_path and os.path.exists(file_path):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error playing music: {e}")

def stop_music():
    pygame.mixer.music.stop()




# Create the main window
root = tk.Tk()
frame2 = tk.Frame()
root.resizable(width=False,height=False)
root.geometry("400x300")
root.title('MP4 & MP3 Downloader')

tabControl = ttk.Notebook(master=root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Youtuber Video Downloader')
tabControl.add(tab2, text='Spotify MP3 preview Downloader')
tabControl.add(tab3,text='Deezer MP3 preview Downloader')
tabControl.add(tab4,text='Play Music Files')

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

label3 = tk.Label(tab3, text="Enter Deezer Track URL:")
label3.pack(pady=10)

entry3 = tk.Entry(tab3, width=50)
entry3.pack(pady=10)

button3 = tk.Button(tab3, text="Download Preview", command=download_preview_and_show_message)
button3.pack(pady=20)

# StringVar to track the file path
file_var = tk.StringVar()

# Entry to display the selected file path
file_entry4 = tk.Entry(tab4, textvariable=file_var, state='disabled', width=40)
file_entry4.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Browse button to select a music file
browse_button4 = tk.Button(tab4, text="Browse", command=browse_file)
browse_button4.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Play button to play the selected music file
play_button4 = tk.Button(tab4, text="Play", command=play_music)
play_button4.grid(row=1, column=0, columnspan=2, pady=10)

stop_button = tk.Button(tab4,text="Stop",command=stop_music)
stop_button.grid(row=2,column=0,columnspan=2,pady=10)


# Run the Tkinter event loop
root.mainloop()
