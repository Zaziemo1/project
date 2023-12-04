import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a notebook to hold the frames
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Create a dictionary to store frames
        self.frames = {}

        # Add frames to the notebook
        for F, tab_title in zip((StartPage, SecondPage), ("Start Page", "Second Page")):
            frame = F(self.notebook, self)
            self.frames[F] = frame
            self.notebook.add(frame, text=tab_title)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        # Button to switch to the second page
        button = ttk.Button(self, text="Go to Second Page", command=lambda: controller.notebook.select(1))
        button.pack()

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Second Page")
        label.pack(pady=10, padx=10)

        # Button to switch back to the start page
        button = ttk.Button(self, text="Go to Start Page", command=lambda: controller.notebook.select(0))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("300x200")
    app.mainloop()
