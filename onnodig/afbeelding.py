from tkinter import messagebox
from PIL import Image, ImageTk

logo = Image.open(r"afbeeldingen/foto.png")
logo = logo.resize((64,64))
logo = ImageTk.PhotoImage(logo)

knop = tk.Button(app,command=exe_uitvoeren,image=logo,text=f"{naam}",compound=tk.BOTTOM,font=("Arial", 12, "underline"))
knop.grid(row=teller // col, column=teller % col, padx=10, pady=10)
knop.image = logo # Onthoud referentie naar logo (tegen garbage collection)