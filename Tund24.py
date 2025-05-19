from tkinter.messagebox import showinfo
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

def salvesta_nagu():
    failinimi = simpledialog.askstring("Salvesta", "Sisesta failinimi (ilma laiendita):")
    if not failinimi:
        return
    
    lopp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))

    for nimi in ["nägu", "juuksed", "silmad", "nina", "suu"]:
        if olemas.get(nimi):
            failitee = {
                "nägu": "nagu.png",
                "juuksed": "juuksed.png",
                "silmad": "silmad.png",
                "nina": "nohu.png",
                "suu": "suu.png"
            }.get(nimi)
            if failitee:
                osa = Image.open(failitee).convert("RGBA").resize((400, 400))
                lopp_pilt.alpha_composite(osa)

    lopp_pilt.save(f"{failinimi}.png")
    showinfo("Salvestatud", f"Fail {failinimi}.png on salvestatud.")

def mangi_muusika():
    pass

def peata_muusika():
    pass

# pygame.mixer.init()
# pygame.mixer.music.load("Tund24_Elevator.mp3")

app = ctk.CTk()
app.geometry("800x500")
app.title("Tund24")

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nagu", "nagu.png", 200, 200)
olemas["nagu"] = True

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
ctk.CTkButton(frame, text="Juuksed", command=lambda: toggle_osa("juuksed", "juuksed.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "silmad.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "nohu.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu.png", 200, 200), **nupu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Loo nägu", command=lambda: salvesta_nagu(), **nupu_seaded).pack(pady=10)

frame_music = ctk.CTkFrame(app)
frame_music.pack(side="bottom", padx=10, pady=10)
ctk.CTkButton(frame_music, text="Mängi muusikat", command=lambda: mangi_muusika(), **nupu_seaded).pack(side="left", pady=10)
ctk.CTkButton(frame_music, text="Peata muusikat", command=lambda: peata_muusika(), **nupu_seaded).pack(side="left", pady=10)

app.mainloop()
