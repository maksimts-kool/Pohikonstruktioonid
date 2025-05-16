import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

# --- Konstandid ---
SONA_PIKKUS = 5
KATSETE_ARV_MAX = 6
SONADE_FAIL = "Tund23_sonad.txt"
TULEMUSTE_FAIL = "Tund23_tulemused.txt"

# Värvid
VARV_TAUST = "#154472"
VARV_MUST = "#FFFFFF"
VARV_HALL = "#000000"
VARV_KOLLANE = "#FFA500"
VARV_ROHELINE = "#008000"
VARV_KASUTATUD_HALL = "#808080"
VARV_KASUTATUD_KOLLANE = "#B8860B"
VARV_KASUTATUD_ROHELINE = "#556B2F"

# --- Globaalsed muutujad ---
oige_sona = ""
katsete_arv = 0
koik_sonad = []
sisestus_kastid = []            # List of lists of Entry widgets
klaviatuuri_nupud = {}          # Map letter -> Label widget
klaviatuuri_seisund = {}        # Map letter -> current bg color
teade_label = None
kontrolli_nupp = None
uus_mang_nupp = None

# --- Funktsioonid ---

def loe_sonad_failist(failinimi):
    """Loeb sõnad failist, filtreerib 5-tähelised ja tagastab listina."""
    try:
        skripti_kaust = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(skripti_kaust, failinimi)
        with open(path, 'r', encoding='utf-8') as f:
            sonad = [
                line.strip().upper()
                for line in f
                if len(line.strip()) == SONA_PIKKUS
            ]
        if not sonad:
            messagebox.showerror(
                "Viga",
                f"Failist '{failinimi}' ei leitud ühtegi "
                f"{SONA_PIKKUS}-tähelist sõna."
            )
        return sonad
    except Exception:
        messagebox.showerror("Viga", f"Tekkis viga faili lugemisel '{failinimi}'")
        return []

def kontrolli_katset():
    """Kontrollib praeguse rea sisestust ja värvib tähed."""
    global katsete_arv, oige_sona

    if katsete_arv >= KATSETE_ARV_MAX:
        return

    praegune_rida = sisestus_kastid[katsete_arv]
    pakkumine = "".join(e.get() for e in praegune_rida).upper()

    if len(pakkumine) != SONA_PIKKUS or not pakkumine.isalpha():
        messagebox.showwarning(
            "Viga sisestuses",
            f"Palun sisesta {SONA_PIKKUS}-täheline sõna (ainult tähed)."
        )
        return

    # Prepare for coloring
    varvid = [VARV_HALL] * SONA_PIKKUS
    oige_list = list(oige_sona)
    pakk_list = list(pakkumine)
    uus_kl_seisund = {}

    # 1. Rohelised
    for i in range(SONA_PIKKUS):
        if pakk_list[i] == oige_list[i]:
            varvid[i] = VARV_ROHELINE
            uus_kl_seisund[pakk_list[i]] = VARV_KASUTATUD_ROHELINE
            oige_list[i] = None
            pakk_list[i] = None

    # 2. Kollased
    for i in range(SONA_PIKKUS):
        c = pakk_list[i]
        if c and c in oige_list:
            varvid[i] = VARV_KOLLANE
            prev = klaviatuuri_seisund.get(c)
            if prev != VARV_KASUTATUD_ROHELINE:
                uus_kl_seisund[c] = VARV_KASUTATUD_KOLLANE
            oige_list[oige_list.index(c)] = None

    # 3. Hallid klaviatuuril
    for i in range(SONA_PIKKUS):
        c = pakkumine[i]
        if c not in uus_kl_seisund:
            uus_kl_seisund[c] = VARV_KASUTATUD_HALL

    varvi_tahed(katsete_arv, pakkumine, varvid)
    uuenda_klaviatuuri(uus_kl_seisund)

    # Disable current row
    for e in praegune_rida:
        e.config(state="disabled")

    if pakkumine == oige_sona:
        lopeta_mang(True)
        return

    katsete_arv += 1
    if katsete_arv == KATSETE_ARV_MAX:
        lopeta_mang(False)
    else:
        # Enable next row
        nxt = sisestus_kastid[katsete_arv]
        for e in nxt:
            e.config(state="normal")
        nxt[0].focus()

def varvi_tahed(rida_i, pakk, varvid):
    """Värvib ühe rea kastid ja näitab tähed."""
    rida = sisestus_kastid[rida_i]
    for i, entry in enumerate(rida):
        bg = varvid[i]
        fg = VARV_TAUST if bg != VARV_HALL else VARV_MUST
        entry.config(
            disabledbackground=bg,
            disabledforeground=fg,
            state="normal"  # vaja enne insert
        )
        entry.delete(0, tk.END)
        entry.insert(0, pakk[i])
        entry.config(state="disabled")

def uuenda_klaviatuuri(uued):
    """Uuendab klaviatuuril iga tähe värvi."""
    global klaviatuuri_seisund
    for c, uus_bg in uued.items():
        lbl = klaviatuuri_nupud.get(c)
        prev = klaviatuuri_seisund.get(c)
        if not lbl:
            continue
        if prev == VARV_KASUTATUD_ROHELINE:
            continue
        if prev == VARV_KASUTATUD_KOLLANE and uus_bg == VARV_KASUTATUD_HALL:
            continue
        fg = VARV_TAUST if uus_bg != VARV_HALL else VARV_MUST
        lbl.config(bg=uus_bg, fg=fg)
        klaviatuuri_seisund[c] = uus_bg

def lopeta_mang(voit):
    """Näitab lõputulemust ja keelab edasise sisendi."""
    kontrolli_nupp.config(state="disabled")
    for row in sisestus_kastid:
        for e in row:
            e.config(state="disabled")
    if voit:
        teade_label.config(
            text=f"Palju õnne! Leidsid sõna '{oige_sona}'!"
        )
    else:
        teade_label.config(
            text=f"Katsed otsas! Õige sõna oli: {oige_sona}"
        )
    salvesta_tulemus(oige_sona, voit)

def salvesta_tulemus(sona, onnestus):
    """Logib tulemuse faili."""
    try:
        skr_kaust = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(skr_kaust, TULEMUSTE_FAIL)
        with open(path, 'a', encoding='utf-8') as f:
            status = "Õnnestus" if onnestus else "Ebaõnnestus"
            katsed = katsete_arv + 1 if onnestus else katsete_arv
            f.write(f"Sõna: {sona}, {status}, katseid: {katsed}\n")
    except Exception as e:
        print(f"Ei saanud tulemust salvestada: {e}")

def uus_mang():
    """Alustab uue mängu ja lähtestab lahtrid ning klaviatuuri."""
    global katsete_arv, oige_sona, klaviatuuri_seisund
    oige_sona = random.choice(koik_sonad) if koik_sonad else ""
    if not oige_sona:
        messagebox.showerror("Viga", "Ei saa uut sõna valida.")
        kontrolli_nupp.config(state="disabled")
        uus_mang_nupp.config(state="disabled")
        teade_label.config(
            text="Viga sõnade laadimisel. Kontrolli faili."
        )
        return
    
    kontrolli_nupp.config(state="normal")
    uus_mang_nupp.config(state="normal")
    
    katsete_arv = 0
    teade_label.config(text="")
    klaviatuuri_seisund = {}

    # Reset entry grid
    for r in range(KATSETE_ARV_MAX):
        for c in range(SONA_PIKKUS):
            e = sisestus_kastid[r][c]
            e.config(
                state="normal",
                bg=VARV_TAUST,
                fg=VARV_MUST,
                disabledbackground=VARV_TAUST,
                disabledforeground=VARV_MUST
            )
            e.delete(0, tk.END)
            if r == 0:
                e.config(state="normal")
            else:
                e.config(state="disabled")
    sisestus_kastid[0][0].focus()

    # Reset keyboard
    for lbl in klaviatuuri_nupud.values():
        lbl.config(bg=VARV_HALL, fg=VARV_MUST)

# --- GUI setup functions ---

def valideeri_sisend(P):
    """Validate entry: only 0 or 1 letter."""
    if len(P) == 0:
        return True
    return len(P) == 1 and P.isalpha()

def init_main_ui():
    """Ehita põhiliides: grid, nupud, klaviatuur."""
    global sisestus_kastid, klaviatuuri_nupud
    global teade_label, kontrolli_nupp, uus_mang_nupp, koik_sonad

    # Pealkiri
    lbl_title = tk.Label(
        aken, text="Wordle Mäng",
        font=("Arial", 24, "bold"),
        bg=VARV_TAUST, fg=VARV_MUST
    )
    lbl_title.pack(pady=10)

    # Grid
    frame_grid = tk.Frame(aken, bg=VARV_TAUST)
    frame_grid.pack(pady=10)
    sisestus_kastid = []
    vcmd = (aken.register(valideeri_sisend), '%P')
    for r in range(KATSETE_ARV_MAX):
        row = []
        for c in range(SONA_PIKKUS):
            e = tk.Entry(
                frame_grid, width=3, font=("Arial", 18, "bold"),
                justify="center", borderwidth=1, relief="solid",
                bg=VARV_TAUST, fg=VARV_MUST,
                disabledbackground=VARV_TAUST,
                disabledforeground=VARV_MUST,
                state="disabled",
                validate="key", validatecommand=vcmd
            )
            e.grid(row=r, column=c, padx=3, pady=3)
            row.append(e)
        sisestus_kastid.append(row)

    # Nupud
    frame_btns = tk.Frame(aken, bg=VARV_TAUST)
    frame_btns.pack(pady=10)
    kontrolli_nupp = tk.Button(
        frame_btns, text="Kontrolli", width=10,
        font=("Arial", 12), command=kontrolli_katset
    )
    kontrolli_nupp.grid(row=0, column=0, padx=5)
    uus_mang_nupp = tk.Button(
        frame_btns, text="Uus mäng", width=10,
        font=("Arial", 12), command=uus_mang
    )
    uus_mang_nupp.grid(row=0, column=1, padx=5)

    # Teade
    teade_label = tk.Label(
        aken, text="", font=("Arial", 12),
        bg=VARV_TAUST, fg=VARV_MUST
    )
    teade_label.pack(pady=10)

    # Klaviatuur
    frame_kb = tk.Frame(aken, bg=VARV_TAUST, pady=5)
    frame_kb.pack()
    klaviatuuri_nupud = {}
    tahestik = ["QWERTYUIOPÜÕ", "ASDFGHJKLÖÄ", "ZXCVBNM"]
    for row in tahestik:
        fr = tk.Frame(frame_kb, bg=VARV_TAUST)
        fr.pack()
        for c in row:
            lbl = tk.Label(
                fr, text=c, width=3, height=2,
                font=("Arial", 10, "bold"),
                borderwidth=1, relief="raised",
                bg=VARV_HALL, fg=VARV_MUST
            )
            lbl.pack(side="left", padx=2, pady=2)
            klaviatuuri_nupud[c] = lbl

    # Lae sõnad ja alusta
    koik_sonad = loe_sonad_failist(SONADE_FAIL)
    if koik_sonad:
        uus_mang()
    else:
        kontrolli_nupp.config(state="disabled")
        uus_mang_nupp.config(state="disabled")
        teade_label.config(
            text=(
                f"Viga: '{SONADE_FAIL}' puudub või pole "
                f"{SONA_PIKKUS}-tähelisi sõnu."
            )
        )

def show_intro():
    """Näita intro-ekraani koos animatsiooni ja progressbariga."""
    intro = tk.Frame(aken, bg=VARV_TAUST)
    intro.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Top: pealkiri
    lbl = tk.Label(
        intro, text="Wordle Mäng",
        font=("Arial", 30, "bold"),
        bg=VARV_TAUST, fg=VARV_MUST
    )
    lbl.pack(pady=20)

    # Lae GIF-i raamist frame'id
    raw_frames = []
    idx = 0
    while True:
        try:
            f = tk.PhotoImage(
                file="Tund23_baconhair.gif", format=f"gif -index {idx}"
            )
            raw_frames.append(f)
            idx += 1
        except tk.TclError:
            break

    # Tee GIF väiksemaks, nt poole võrra (factor=2)
    factor = 2   # 2→pool, 3→1/3, jne
    frames = [f.subsample(factor, factor) for f in raw_frames]

    gif_lbl = tk.Label(intro, bg=VARV_TAUST)
    gif_lbl.pack()

    def animate(i=0):
        # if the widget has been destroyed, stop
        if not gif_lbl.winfo_exists():
            return

        gif_lbl.config(image=frames[i])
        aken.after(100, animate, (i+1) % len(frames))


    if frames:
        animate()

    # Progressbar all
    prog = ttk.Progressbar(
        intro, orient="horizontal",
        length=300, mode="determinate", maximum=100
    )
    prog.pack(pady=30)

    def step(v=0):
        prog["value"] = v
        if v < 100:
            aken.after(30, step, v+1)
        else:
            intro.destroy()
            init_main_ui()

    step(0)

# --- Pääsukoht ---
if __name__ == "__main__":
    aken = tk.Tk()
    aken.title("Wordle Mäng")
    aken.config(bg=VARV_TAUST)
    aken.geometry("400x550")
    aken.iconbitmap("Tund23_images.ico")
    aken.resizable(False, False)

    show_intro()
    aken.mainloop()
