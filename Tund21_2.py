import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def solve():
    valid = True
    for ent in (entry_a, entry_b, entry_c):
        try:
            float(ent.get())
            ent.config(bg=entry_bg)
        except:
            ent.config(bg="red")
            valid = False
    if not valid:
        return

    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    d = b**2 - 4 * a * c

    if d < 0:
        res = "Puuduvad tegelikud juured"
    elif d == 0:
        x = -b / (2 * a)
        res = f"Üks juur: {round(x,3)}"
    else:
        sqrt_d = d**0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        res = f"D = {round(d,3)}\n x1 = {round(x1,3)}\n x2 = {round(x2,3)}"
    label_result.config(text=res)

def on_graph():
    valid = True
    for ent in (entry_a, entry_b, entry_c):
        try:
            float(ent.get())
            ent.config(bg=entry_bg)
        except:
            ent.config(bg="red")
            valid = False

    if not valid:
        label_result.config(text="Puuduvad tegelikud juured")
        return

    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    vx = -b / (2 * a)
    xs = np.linspace(vx - 10, vx + 10, 200) # [0   0.25 0.5  0.75   1]
    ys = a * xs**2 + b * xs + c

    plt.figure()
    plt.plot(xs, ys, 'o-', markersize=5)

    d = b**2 - 4 * a * c
    if d >= 0:
        sqrt_d = d**0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        plt.plot([x1, x2], [0, 0], 'go', markersize=8,
                 label='Juured')

    plt.title("Parabooli graafik")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def on_focus_in(event):
    event.widget.config(bg=entry_bg)

root = tk.Tk()
root.title("Kvadraatilised võrrandid")
root.resizable(width=False, height=False)
# Header
header = tk.Label(
    root,
    text="Kvadraatilise võrrandi lahendamine",
    bg="lightblue",
    fg="green",
    font=("Arial", 20)
)
header.grid(row=0, column=0, columnspan=8, sticky="ew", padx=5, pady=5)

# Coefficient entry backgrounds
entry_bg = "lightblue"
entry_fg = "darkgreen"

# a*x^2
entry_a = tk.Entry(root, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
entry_a.grid(row=1, column=0)
tk.Label(root, text="x**2+", font=("Arial", 14), fg=entry_fg).grid(
    row=1, column=1
)

# b*x
entry_b = tk.Entry(root, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
entry_b.grid(row=1, column=2)
tk.Label(root, text="x+", font=("Arial", 14), fg=entry_fg).grid(
    row=1, column=3
)

# c
entry_c = tk.Entry(root, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
entry_c.grid(row=1, column=4)
tk.Label(root, text="=0", font=("Arial", 14), fg=entry_fg).grid(
    row=1, column=5
)

# Solve button (appearance only)
btn_solve = tk.Button(
    root,
    text="Lahenda",
    command=solve,
    bg="#008800",
    fg="white",
    font=("Arial", 14)
)
btn_solve.grid(row=1, column=6)

btn_graph = tk.Button(
    root,
    text="Graafik",
    bg="#008800",
    fg="white",
    font=("Arial", 14),
    command=on_graph
)
btn_graph.grid(row=1, column=7)

# Result display area
label_result = tk.Label(
    root,
    text="Vastus",
    bg="yellow",
    font=("Arial", 16)
)
label_result.grid(
    row=2,
    column=0,
    columnspan=8,
    sticky="nsew",
    padx=5,
    pady=(10, 5),
    ipady=20
)

for ent in (entry_a, entry_b, entry_c):
    ent.bind("<FocusIn>", on_focus_in)

root.mainloop()
