import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError
from exceptions import SpotifyAlbumNotFound, SpotifyTrackNotFound, SpotifyPlaylistNotFound, ConfigVideoMaxLength, ConfigVideoLowViewCount, YoutubeItemNotFound
from apis.spotify import Spotify
def download_audio():
    url = url_entry2.get()
    messagebox.showinfo('Download Complete', f'Download complete {url.title}')
        


def download_video():
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
download_button = tk.Button(tab1, text='Download Video', command=download_video)
download_button.pack(pady=20)

# Download Spotify
download_button2 = tk.Button(tab2, text='Download Audio',command=download_audio)
download_button2.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
