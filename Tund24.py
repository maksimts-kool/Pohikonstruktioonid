import customtkinter as ctk
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import pygame

olemas = {}
objectid = {}
pildid = {}

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objectid[nimi])
        olemas[nimi] = False
    else:
        pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objectid[nimi] = canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True

pygame.mixer.init()
pygame.mixer.music.load("Tund24.mp3")

app = ctk.CTk()
app.geometry("800x500")
app.title("Tund24")

# Now Canvas is in your namespace
canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("Tund24", "Tund24.png", 200, 200)
olemas["Tund24"] = True

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)

nupu_seaded = {
    "width": 150, "height": 40,
    "font": ("Arial", 32),
    "fg_color": "green",
    "text_color": "white",
    "corner_radius": 20
}

ctk.CTkButton(frame, text="Vali näoosad", **nupu_seaded).pack(pady=5)
ctk.CTkButton(frame, text="Otsmik", command=lambda: toggle_osa("otsmik", "otsmik1.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "silmad1.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "nina1.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu1.png", 200, 200), **nupu_seaded).pack(pady=3)

frame_music = ctk.CTkFrame(app)
frame_music.pack(side="bottom", padx=10, pady=10)

app.mainloop()
