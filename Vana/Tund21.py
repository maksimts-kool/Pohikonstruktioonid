from tkinter import *

k = 0

def vajutatud():
    global k
    k += 1
    pealkiri.config(text=f"Tere tulemast Tundi 21! {k} kord(a)", bg="lightblue")
    nupp.config(text="Vajuta veel kord!", bg="orange")
def vajutatudR(event):
    global k
    k -= 1
    pealkiri.config(text=f"Tere tulemast Tundi 21! {k} kord(a)", bg="lightpink")
    nupp.config(text="Vajuta veel kord!", bg="purple")
def tuhista(event):
    sisse.delete(0, END)
    sisse.config(bg="white", fg="black")

aken = Tk()
aken.title("Tund 21")
aken.geometry("600x400")
aken.configure(bg="lightgreen")
aken.resizable(width=False, height=False)
aken.iconbitmap("tund21img.ico")

pealkiri = Label(aken, text="Tund 21", font=("Arial", 20), bg="white", fg="green")
pealkiri.pack(pady=10)

sisse = Entry(aken, font=("Arial", 15), bg="lightyellow", fg="black")
sisse.insert(0, "Sisesta oma nimi")
sisse.bind("<FocusIn>", tuhista)
sisse.pack(pady=10)

nupp = Button(aken, text="Vajuta mind!", font=("Arial", 15), bg="blue", fg="white", relief="raised", command=vajutatud)
nupp.pack(pady=20)
nupp.bind("<Button-3>",vajutatudR)  # Right-click event

aken.mainloop()