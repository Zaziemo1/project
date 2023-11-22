import qrcode
import tkinter as tk
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = tk.Tk()
    
# Define the geometry of the window
win.geometry("700x500")

frame = tk.Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter Image
def create_qr():
  img = qrcode.make(Entry.get())
  type(img)  # qrcode.image.pil.PilImage
  img = ImageTk.PhotoImage(img)
  # Create a Label Widget to display the text or Image
  label.config(image=img)
  label.image = img
  
Entry = tk.Entry(master=win,bg='green')
Entry.pack()

label = tk.Label(frame)
label.pack()

while True:
    create_qr()
    win.update()
