import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    output_path = output_entry.get()

    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        messagebox.showinfo('Download Complete', f'Download complete: {yt.title}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main window
root = tk.Tk()
root.title('YouTube Video Downloader')

tabControl = 

# URL Label and Entry
url_label = tk.Label(root, text='Enter YouTube URL:')
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

# Output Path Label and Entry
output_label = tk.Label(root, text='Enter Output Path:')
output_label.pack(pady=10)
output_entry = tk.Entry(root, width=40)
output_entry.pack(pady=10)

# Download Button
download_button = tk.Button(root, text='Download Video', command=download_video)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
