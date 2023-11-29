import tkinter as tk
from pygame import mixer

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter App with Background Music")

        # Initialize pygame mixer
        mixer.init()

        # Load the background music file
        mixer.music.load("music\CanzoniPerBimbi - A Ram Sam Sam.mp3")  # Replace with the correct path to your audio file

        # Set the volume (optional)
        mixer.music.set_volume(0.5)  # Adjust the volume as needed

        # Start playing the background music in a loop
        mixer.music.play(loops=-1)

        # Create other elements of your Tkinter app here
        # For example, add labels, buttons, etc.
        invoer = tk.StringVar()
        
        def som(cijfer):
            huidige_invoer = invoer.get()
            nieuwe_invoer = huidige_invoer + str(cijfer)
            invoer.set(nieuwe_invoer)

        def voeg_operator_toe(operator):
            huidige_invoer = invoer.get()
            nieuwe_invoer = huidige_invoer + " " + operator + " "
            invoer.set(nieuwe_invoer)

        def wis_invoer():
            invoer.set("")

        def bereken():
            try:
                resultaat = eval(invoer.get())
                invoer.set(resultaat)
            except Exception as e:
                invoer.set("Fout")

        def on_closing():
            # Stop the music when the window is closed
            mixer.music.stop()
            root.destroy()
            
        root.protocol("WM_DELETE_WINDOW", on_closing)

        veld = tk.Entry(master=root, background="green", textvariable=invoer)
        veld.grid(row=0, column=0, columnspan=3)

        knop1 = tk.Button(master=root, text="1", width=5, height=2, command=lambda: som(1))
        knop1.grid(row=2, column=0)

        knop2 = tk.Button(master=root, text="2", width=5, height=2, command=lambda: som(2))
        knop2.grid(row=2, column=1)

        knop3 = tk.Button(master=root, text="3", width=5, height=2, command=lambda: som(3))
        knop3.grid(row=2, column=2)

        knop4 = tk.Button(master=root, text="4", width=5, height=2, command=lambda: som(4))
        knop4.grid(row=3, column=0)

        knop5 = tk.Button(master=root, text="5", width=5, height=2, command=lambda: som(5))
        knop5.grid(row=3, column=1)

        knop6 = tk.Button(master=root, text="6", width=5, height=2, command=lambda: som(6))
        knop6.grid(row=3, column=2)

        knop7 = tk.Button(master=root, text="7", width=5, height=2, command=lambda: som(7))
        knop7.grid(row=4, column=0)

        knop8 = tk.Button(master=root, text="8", width=5, height=2, command=lambda: som(8))
        knop8.grid(row=4, column=1)

        knop9 = tk.Button(master=root, text="9", width=5, height=2, command=lambda: som(9))
        knop9.grid(row=4, column=2)

        knop0 = tk.Button(master=root, text="0", width=5, height=2, command=lambda: som(0))
        knop0.grid(row=5, column=0)

        knopplus = tk.Button(master=root, text="+", width=5, height=2, command=lambda: voeg_operator_toe("+"))
        knopplus.grid(row=5, column=1)

        knopmin = tk.Button(master=root, text="-", width=5, height=2, command=lambda: voeg_operator_toe("-"))
        knopmin.grid(row=5, column=2)

        knopgelijk = tk.Button(master=root, text="=", width=5, height=2, command=bereken)
        knopgelijk.grid(row=6, column=0)

        knopgelijk = tk.Button(master=root, text="CLR", width=12, height=2, command=wis_invoer)
        knopgelijk.grid(row=6, column=1, columnspan=2)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    app.run()
