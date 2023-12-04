import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
frame2 = tk.Frame()
root.resizable(width=False,height=False)
root.geometry("400x300")
root.title('MP4 & MP3 Downloader')

def center_buttons(window):

    logo = Image.open(r"afbeeldingen/Youtube_logo.png")
    logo = logo.resize((64,64))
    logo = ImageTk.PhotoImage(logo)

    button1 = tk.Button(window, text="Button 1",image=logo, width=180, compound=tk.BOTTOM)
    button1.pack(pady=10)

    button2 = tk.Button(window, text="Button 2", image=logo, width=180, compound=tk.BOTTOM, height=100)
    button2.pack(pady=10)

    window.update_idletasks()

    window_width = window.winfo_width()
    window_height = window.winfo_height()

    button1_width = button1.winfo_reqwidth()
    button1_height = button1.winfo_reqheight()

    button2_width = button2.winfo_reqwidth()
    button2_height = button2.winfo_reqheight()

    x_position1 = (window_width - button1_width) // 2
    y_position1 = (window_height - button1_height - button2_height - 10) // 2

    x_position2 = (window_width - button2_width) // 2
    y_position2 = y_position1 + button1_height + 10

    button1.place(x=x_position1, y=y_position1)
    button2.place(x=x_position2, y=y_position2)

# Center the buttons
center_buttons(root)

# Start the Tkinter event loop
root.mainloop()
