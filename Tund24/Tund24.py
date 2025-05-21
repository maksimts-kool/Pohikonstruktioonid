import customtkinter as ctk
from tkinter import Canvas, StringVar
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import pygame
import os

PARTS = ["nagu", "juuksed", "silmad", "nina", "suu"]

VARIANT_NAMES = {
    "nagu": {
        "1": "Klassikaline",
        "2": "Plokk",
        "3": "Epic",
        "4": "",
        "5": "",
    },
    "juuksed": {
        "1": "Lahe",
        "2": "Bacon",
        "3": "Builders hat",
        "4": "",
        "5": "",
    },
    "silmad": {
        "1": "Must",
        "2": "Normaalne",
        "3": "Naljakas",
        "4": "Spongebob",
        "5": "",
    },
    "nina": {
        "1": "Normaalne",
        "2": "Porgandi",
        "3": "",
        "4": "",
        "5": "",
    },
    "suu": {
        "1": "Avatud suu",
        "2": "Hammastega",
        "3": "Naljakas",
        "4": "Ristkülikukujuline",
        "5": "",
    },
}

NAME_TO_ID = {
    part: {name: vid for vid, name in VARIANT_NAMES[part].items()}
    for part in PARTS
}

is_shown = {p: False for p in PARTS}
object_id = {}
tk_images = {}
selected_variant = {p: "1" for p in PARTS}


def mangi_muusika():
    pygame.mixer.music.play(-1)


def peata_muusika():
    pygame.mixer.music.stop()


def toggle_part(part):
    variant = selected_variant[part]
    fname = os.path.join(os.path.dirname(__file__), f"{part}{variant}.png")
    if is_shown[part]:
        canvas.delete(object_id[part])
        is_shown[part] = False
    else:
        img = Image.open(fname).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        tk_images[part] = tk_img
        object_id[part] = canvas.create_image(200, 200, image=tk_img)
        is_shown[part] = True


def salvesta_face():
    name = askstring("Salvesta", "Sisesta failinimi (ilma laiendita):")
    if not name:
        return
    out_img = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    for p in PARTS:
        if is_shown[p]:
            layer = (
                Image.open(f"{p}{selected_variant[p]}.png")
                .convert("RGBA")
                .resize((400, 400))
            )
            out_img.alpha_composite(layer)
    out_img.save(f"{name}.png")
    showinfo("Salvestatud", f"Fail '{name}.png' on salvestatud.")


app = ctk.CTk()
app.title("Tund24")
app.geometry("600x550")

frame_controls = ctk.CTkFrame(app)
frame_controls.pack(side="left", padx=5, pady=5, fill="y")

button_style = {
    "width": 150,
    "height": 40,
    "fg_color": "green",
    "text_color": "white",
    "corner_radius": 20,
}

for part in PARTS:
    # 3) Начальное значение — название у id=1
    var = StringVar(value=VARIANT_NAMES[part][selected_variant[part]])
    menu = ctk.CTkOptionMenu(
        frame_controls,
        variable=var,
        values=list(VARIANT_NAMES[part].values()),
        command=lambda name, p=part: selected_variant.__setitem__(
            p, NAME_TO_ID[p][name]
        ),
    )
    menu.pack(pady=5)
    ctk.CTkButton(
        frame_controls,
        text=part.capitalize(),
        command=lambda p=part: toggle_part(p),
        **button_style
    ).pack(pady=3)

ctk.CTkButton(
    frame_controls,
    text="Loo nägu",
    command=salvesta_face,
    **button_style
).pack(pady=10)

preview_frame = ctk.CTkFrame(app, width=420, height=420, corner_radius=0)
preview_frame.pack(side="top", padx=10, pady=10)

canvas = Canvas(preview_frame, width=400, height=400, bg="white")
canvas.pack(padx=5, pady=5)

frame_music = ctk.CTkFrame(app)
frame_music.pack(side="bottom", pady=5, fill="x")

ctk.CTkButton(
    frame_music,
    text="Mängi muusikat",
    command=mangi_muusika,
    **button_style
).pack(padx=5, pady=5)
ctk.CTkButton(
    frame_music,
    text="Peata muusikat",
    command=peata_muusika,
    **button_style
).pack(padx=5, pady=5)

toggle_part("nagu")

app.mainloop()
