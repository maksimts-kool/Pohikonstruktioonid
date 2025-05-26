import customtkinter as ctk
from tkinter import Canvas
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import pygame
import os


OSAD = ["nagu", "juuksed", "silmad", "nina", "suu"]

OSA_NIMED = {
    "nagu": ["Klassikaline", "Plokk", "Epic"],
    "juuksed": ["Lahe", "Bacon", "Ehitaja müts", "Lahtised"],
    "silmad": ["Must", "Normaalne", "Naljakas", "Spongebob", "Katkine"],
    "nina": ["Normaalne", "Porgandi", "Punane"],
    "suu": ["Avatud suu", "Hammastega", "Naljakas", "Ristkülik", "Katkine"]
}

valitud_osad = {}     
näidatud_osad = {}   
osa_pildid = {}      

for osa in OSAD:
    valitud_osad[osa] = 1
    näidatud_osad[osa] = False

def mängi_muusikat():
    """Alusta muusika mängimist"""
    try:
        pygame.mixer.music.play(-1) 
    except:
        showinfo("Viga", "Muusikafaili ei leitud!")

def peata_muusikat():
    """Peata muusika"""
    pygame.mixer.music.stop()

def näita_peida_osa(osa_nimi):
    """Näita või peida näo osa"""
    if näidatud_osad[osa_nimi]:
        canvas.delete(f"osa_{osa_nimi}")
        näidatud_osad[osa_nimi] = False
    else:
        variandi_number = valitud_osad[osa_nimi]
        pildi_fail = os.path.join("Tund24", f"{osa_nimi}{variandi_number}.png")
        
        if os.path.exists(pildi_fail):
            pilt = Image.open(pildi_fail).resize((400, 400))
            foto = ImageTk.PhotoImage(pilt)
            osa_pildid[osa_nimi] = foto
            canvas.create_image(200, 200, image=foto, tags=f"osa_{osa_nimi}")
            näidatud_osad[osa_nimi] = True

def muuda_varianti(osa_nimi, uus_variandi_nimi):
    variantide_nimekiri = OSA_NIMED[osa_nimi]
    variandi_number = variantide_nimekiri.index(uus_variandi_nimi) + 1
    valitud_osad[osa_nimi] = variandi_number
    
    if näidatud_osad[osa_nimi]:
        näita_peida_osa(osa_nimi)
        näita_peida_osa(osa_nimi) 

def salvesta_nägu():
    
    failinimi = askstring("Salvesta", "Sisesta faili nimi:")
    if not failinimi:
        return
    
    lõplik_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    lisatud_osad = []
    
    for osa in OSAD:
        if näidatud_osad[osa]:
            variant = valitud_osad[osa]
            osa_fail = os.path.join("Tund24", f"{osa}{variant}.png")
            
            if os.path.exists(osa_fail):
                try:
                    osa_pilt = Image.open(osa_fail).convert("RGBA").resize((400, 400))
                    lõplik_pilt.alpha_composite(osa_pilt)
                    lisatud_osad.append(f"{osa}{variant}")
                except Exception as e:
                    print(f"Viga {osa} lisamisel: {e}")
    
    väljund_fail = f"{failinimi}.png"
    lõplik_pilt.save(väljund_fail)
    
    showinfo("Valmis", "Nägu salvestatud")


# pygame.mixer.init()
try:
    pygame.mixer.music.load("Tund24_Elevator.mp3")
except:
    print("Muusikafaili ei leitud")


rakendus = ctk.CTk()
rakendus.title("Näo tegija")
rakendus.geometry("700x550")


juhtimis_paneel = ctk.CTkFrame(rakendus)
juhtimis_paneel.pack(side="left", fill="y", padx=10, pady=10)


nupu_stiil = {
    "width": 150,
    "height": 40,
    "fg_color": "green",
    "text_color": "white",
    "corner_radius": 20,
}


for osa in OSAD:

    menüü = ctk.CTkOptionMenu(
        juhtimis_paneel,
        values=OSA_NIMED[osa],
        command=lambda valik, o=osa: muuda_varianti(o, valik)
    )
    menüü.pack(pady=5)
    

    nupp = ctk.CTkButton(
        juhtimis_paneel,
        text=f"Näita {osa}",
        command=lambda o=osa: näita_peida_osa(o),
        **nupu_stiil
    )
    nupp.pack(pady=3)


salvesta_nupp = ctk.CTkButton(
    juhtimis_paneel,
    text="Salvesta nägu",
    command=salvesta_nägu,
    **nupu_stiil
)
salvesta_nupp.pack(pady=20)


lõuendi_raam = ctk.CTkFrame(rakendus, width=420, height=420, corner_radius=0)
lõuendi_raam.pack(side="top", padx=10, pady=10)

canvas = Canvas(lõuendi_raam, width=400, height=400, bg="white")
canvas.pack(padx=5, pady=5)


muusika_paneel = ctk.CTkFrame(rakendus)
muusika_paneel.pack(side="bottom", pady=5, fill="x")

mängi_nupp = ctk.CTkButton(
    muusika_paneel,
    text="Mängi muusikat",
    command=mängi_muusikat,
    **nupu_stiil
)
mängi_nupp.pack(side="left", padx=5, pady=5)

peata_nupp = ctk.CTkButton(
    muusika_paneel,
    text="Peata muusikat",
    command=peata_muusikat,
    **nupu_stiil
)
peata_nupp.pack(side="left", padx=5, pady=5)

näita_peida_osa("nagu")

rakendus.mainloop()
