import tkinter as tk
app = tk.Tk()
from PIL import Image, ImageTk

logo = Image.open(r"afbeeldingen/Youtube_logo.png")
logo = logo.resize((64,64))
logo = ImageTk.PhotoImage(logo)

titel = tk.Label(master=app, text= "Choose your platform: ")
titel.grid(row=0, columnspan=3)

knop1 = tk.Button(master=app, text="youtube",image=logo, compound=tk.BOTTOM, width=180)
knop1.grid(row=1, column=0)

knop1 = tk.Button(master=app, text="1", width=25, height=5)
knop1.grid(row=1, column=1)

knop1 = tk.Button(master=app, text="1", width=25, height=5)
knop1.grid(row=1, column=2)

knop1 = tk.Button(master=app, text="1", width=25, height=5)
knop1.grid(row=2, column=0)

knop1 = tk.Button(master=app, text="1", width=25, height=5)
knop1.grid(row=2, column=1)

knop1 = tk.Button(master=app, text="1", width=25, height=5)
knop1.grid(row=2, column=2)

app.mainloop()