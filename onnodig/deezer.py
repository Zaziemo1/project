import requests
import tkinter as tk
from tkinter import messagebox

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

# Create a simple Tkinter GUI
root = tk.Tk()
root.title("Deezer Preview Downloader")

label3 = tk.Label(root, text="Enter Deezer Track URL:")
label3.pack(pady=10)

entry3 = tk.Entry(root, width=50)
entry3.pack(pady=10)

button3 = tk.Button(root, text="Download Preview", command=download_preview_and_show_message)
button3.pack(pady=20)

root.mainloop()
