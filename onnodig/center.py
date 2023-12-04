import tkinter as tk


root = tk.Tk()
frame2 = tk.Frame()
root.resizable(width=False,height=False)
root.geometry("400x300")
root.title('MP4 & MP3 Downloader')

def center_button(window):
    button = tk.Button(window, text="Centered Button")
    button.pack(pady=10)  # Add padding if needed
    window.update_idletasks()  # Force update to calculate button size

    # Calculate the center of the window
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    button_width = button.winfo_reqwidth()
    button_height = button.winfo_reqheight()

    x_position = (window_width - button_width) // 2
    y_position = (window_height - button_height) // 2

    # Set the button's position
    button.place(x=x_position, y=y_position)

# Center the button
center_button(root)

# Start the Tkinter event loop
root.mainloop()
