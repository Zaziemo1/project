import tkinter as tk
app = tk.Tk()
app.geometry("600x500")
app.resizable(width=False, height=False)
from PIL import Image, ImageTk

home_frame = tk.Frame(app)
home_frame.place(x=0,y=0)

logo = Image.open(r"afbeeldingen/Youtube_logo.png")
logo = logo.resize((64,64))
logo = ImageTk.PhotoImage(logo)

titel = tk.Label(master=home_frame, text= "Choose your platform: ")
titel.grid(row=0, columnspan=3)

knop1 = tk.Button(master=home_frame, text="youtube",image=logo, compound=tk.BOTTOM, width=180)
knop1.grid(row=1, column=0)

knop2 = tk.Button(master=home_frame, text="youtube",image=logo, compound=tk.BOTTOM, width=180)
knop2.grid(row=1, column=1)

app.mainloop()