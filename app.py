import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_audio():
    url = url_entry.get()
    output_path = output_entry.get()

    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        messagebox.showinfo('Download Complete', f'Download complete: {yt.title}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')


root = tk.Tk()
root.title('YouTube to MP3 Downloader')

url_label = tk.Label(root, text='Enter YouTube URL:')
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

output_label = tk.Label(root, text='Enter Output Path:')
output_label.pack(pady=10)
output_entry = tk.Entry(root, width=40)
output_entry.pack(pady=10)

# Download Button
download_button = tk.Button(root, text='Download MP3', command=download_audio)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
