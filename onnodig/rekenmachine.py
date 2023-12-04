import tkinter as tk
app = tk.Tk()

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
    
veld = tk.Entry(master=app, background="green", textvariable=invoer)
veld.grid(row=0, column=0, columnspan=3)

knop1 = tk.Button(master=app, text="1", width=5, height=2, command=lambda:som(1))
knop1.grid(row=2, column=0)

knop2 = tk.Button(master=app, text="2", width=5, height=2, command=lambda:som(2))
knop2.grid(row=2, column=1)

knop3 = tk.Button(master=app, text="3", width=5, height=2, command=lambda:som(3))
knop3.grid(row=2, column=2)

knop4 = tk.Button(master=app, text="4", width=5, height=2, command=lambda: som(4))
knop4.grid(row=3, column=0)

knop5 = tk.Button(master=app, text="5", width=5, height=2, command=lambda: som(5))
knop5.grid(row=3, column=1)

knop6 = tk.Button(master=app, text="6", width=5, height=2, command=lambda: som(6))
knop6.grid(row=3, column=2)

knop7 = tk.Button(master=app, text="7", width=5, height=2, command=lambda: som(7))
knop7.grid(row=4, column=0)

knop8 = tk.Button(master=app, text="8", width=5, height=2, command=lambda: som(8))
knop8.grid(row=4, column=1)

knop9 = tk.Button(master=app, text="9", width=5, height=2, command=lambda: som(9))
knop9.grid(row=4, column=2)

knop0 = tk.Button(master=app, text="0", width=5, height=2, command=lambda: som(0))
knop0.grid(row=5, column=0)

knopplus = tk.Button(master=app, text="+", width=5, height=2, command=lambda: voeg_operator_toe("+"))
knopplus.grid(row=5, column=1)

knopmin = tk.Button(master=app, text="-", width=5, height=2, command=lambda: voeg_operator_toe("-"))
knopmin.grid(row=5, column=2)

knopgelijk = tk.Button(master=app, text="=", width=5, height=2, command=bereken)
knopgelijk.grid(row=6, column=0)

knopgelijk = tk.Button(master=app, text="CLR", width=12, height=2, command=wis_invoer)
knopgelijk.grid(row=6, column=1, columnspan=2)

app.mainloop()