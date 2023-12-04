import os
import tkinter as tk
from tkinter import filedialog
import pygame

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def play_music():
    file_path = file_entry.get()
    if file_path and os.path.exists(file_path):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Entry to display the selected file path
file_entry = tk.Entry(root, state='disabled', width=40)
file_entry.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Browse button to select a music file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Play button to play the selected music file
play_button = tk.Button(root, text="Play", command=play_music)
play_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
