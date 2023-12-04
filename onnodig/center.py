import tkinter as tk
from PIL import Image, ImageTk

def make_rounded_button(widget):
    widget.config(relief=tk.GROOVE, bd=5, borderwidth=5, highlightthickness=0, bg='#34495e', fg='white')
    widget.update_idletasks()
    widget_height = widget.winfo_height()
    widget_width = widget.winfo_width()
    widget.config(height=widget_height, width=widget_width, borderwidth=0)
    widget.config(highlightthickness=0)

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("617x500")
root.title('MP4 & MP3 Downloader')

# Set background color to blue
root.configure(bg='#3498db')

logo = Image.open(r"afbeeldingen/Youtube_logo.png")
logo = logo.resize((64, 54))
logo = ImageTk.PhotoImage(logo)

logo1 = Image.open(r"afbeeldingen\Spotify_icon.svg.png")
logo1 = logo1.resize((64, 64))
logo1 = ImageTk.PhotoImage(logo1)

logo2 = Image.open(r"afbeeldingen\Deezer_hRGsLeP.png")
logo2 = logo2.resize((64, 34))
logo2 = ImageTk.PhotoImage(logo2)

logo3 = Image.open(r"afbeeldingen\sound_PNG22.png")
logo3 = logo3.resize((54, 54))
logo3 = ImageTk.PhotoImage(logo3)

frame1 = tk.Frame(root, bg='#3498db')  # Add a frame for the title
frame1.grid(row=0, column=0, columnspan=3, pady=10)

# Add label for the title in the center
title_label = tk.Label(frame1, text='Video/Audio Downloader', font=('Helvetica', 16), bg='#3498db', fg='white')
title_label.grid(row=0, column=0, pady=10)

button1 = tk.Button(root, text="Button 1", image=logo, width=120)
button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
make_rounded_button(button1)

button3 = tk.Button(root, text="Button 1", image=logo1, width=120)
button3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
make_rounded_button(button3)

button4 = tk.Button(root, text="Button 1", image=logo2, width=120)
button4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
make_rounded_button(button4)

button6 = tk.Button(root, text="Button 1", image=logo3, width=120)
button6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
make_rounded_button(button6)

# Configure column and row weights to center the buttons
for i in range(3):  # Number of columns
    root.grid_columnconfigure(i, weight=1)

for i in range(3):  # Number of rows
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
