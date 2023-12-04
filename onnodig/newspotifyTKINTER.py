import os
import tkinter as tk
from tkinter import filedialog
import pygame

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

# Create the main window
root = tk.Tk()
root.title("Music Player")

# StringVar to track the file path
file_var = tk.StringVar()

# Entry to display the selected file path
file_entry4 = tk.Entry(root, textvariable=file_var, state='disabled', width=40)
file_entry4.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Browse button to select a music file
browse_button4 = tk.Button(root, text="Browse", command=browse_file)
browse_button4.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Play button to play the selected music file
play_button4 = tk.Button(root, text="Play", command=play_music)
play_button4.grid(row=1, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
