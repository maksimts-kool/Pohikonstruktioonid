import tkinter as tk
from tkinter import messagebox
import random
import os # Kasutame failitee korrektseks leidmiseks

# --- Konstandid ---
SONA_PIKKUS = 5
KATSETE_ARV_MAX = 6
SONADE_FAIL = "Tund23_sonad.txt"
TULEMUSTE_FAIL = "Tund23_tulemused.txt" # Valikuline

# Värvid
VARV_TAUST = "#154472" # Valge taust
VARV_MUST = "#FFFFFF" # Must tekst/äärised
VARV_HALL = "#000000" # Hall (tähte pole)
VARV_KOLLANE = "#FFA500" # Kollane (täht vales kohas)
VARV_ROHELINE = "#008000" # Roheline (täht õiges kohas)
VARV_KASUTATUD_HALL = "#808080" # Klaviatuuri hall
VARV_KASUTATUD_KOLLANE = "#B8860B" # Klaviatuuri kollane (tumedam)
VARV_KASUTATUD_ROHELINE = "#556B2F" # Klaviatuuri roheline (tumedam)

# --- Globaalsed muutujad ---
oige_sona = ""
katsete_arv = 0
koik_sonad = []
sisestus_kastid = [] # Hoiab Entry widgeteid (list listidest)
klaviatuuri_nupud = {} # Hoiab klaviatuuri tähti (Label widgetid)
klaviatuuri_seisund = {} # Hoiab tähtede värviinfot klaviatuuril

# --- Funktsioonid ---

def loe_sonad_failist(failinimi):
    """Loeb sõnad määratud failist ja tagastab need listina."""
    try:
        # Leia skripti asukoht, et failitee oleks korrektne
        with open(SONADE_FAIL, 'r', encoding='utf-8') as f:
            # Eemalda tühikud ja konverteeri suurtähtedeks
            # Filtreeri välja ainult SONA_PIKKUS pikkused sõnad
            sonad = [
                sona.strip().upper()
                for sona in f
                if len(sona.strip()) == SONA_PIKKUS
            ]
        if not sonad:
            messagebox.showerror(
                "Viga",
                f"Failist '{failinimi}' ei leitud ühtegi {SONA_PIKKUS}-tähelist sõna.",
            )
            return []
        return sonad
    except:
        messagebox.showerror("Viga", "Tekkis viga faili lugemisel")
        return []

def kontrolli_katset():
    """Kontrollib sisestatud sõna ja värvib tähed."""
    global katsete_arv, oige_sona

    if katsete_arv >= KATSETE_ARV_MAX:
        return # Mäng juba läbi

    # Loe sõna aktiivse rea sisestuskastidest
    praegune_rida = sisestus_kastid[katsete_arv]
    pakkumine = "".join(entry.get() for entry in praegune_rida).upper()

    # Kontrolli, kas kõik tähed on sisestatud
    if len(pakkumine) != SONA_PIKKUS or not pakkumine.isalpha():
        messagebox.showwarning(
            "Viga sisestuses",
            f"Palun sisesta {SONA_PIKKUS}-täheline sõna (ainult tähed).",
        )
        return

    # --- Värvimise loogika ---
    varvid = [VARV_HALL] * SONA_PIKKUS # Algselt kõik hallid
    oige_sona_koopia = list(oige_sona)
    pakkumine_list = list(pakkumine)
    uus_klaviatuuri_seisund = {}

    # 1. Roheliste leidmine (õige täht õiges kohas)
    for i in range(SONA_PIKKUS):
        if pakkumine_list[i] == oige_sona_koopia[i]:
            varvid[i] = VARV_ROHELINE
            uus_klaviatuuri_seisund[pakkumine_list[i]] = VARV_KASUTATUD_ROHELINE
            oige_sona_koopia[i] = None # Eemalda täht, et vältida topeltkollast
            pakkumine_list[i] = None # Eemalda täht, et vältida topeltkollast

    # 2. Kollaste leidmine (õige täht vales kohas)
    for i in range(SONA_PIKKUS):
        if pakkumine_list[i] is not None and pakkumine_list[i] in oige_sona_koopia:
            varvid[i] = VARV_KOLLANE
            # Klaviatuuril uuenda ainult siis, kui pole juba roheline
            if pakkumine_list[i] not in uus_klaviatuuri_seisund or klaviatuuri_seisund.get(pakkumine_list[i]) != VARV_KASUTATUD_ROHELINE:
                 uus_klaviatuuri_seisund[pakkumine_list[i]] = VARV_KASUTATUD_KOLLANE
            # Eemalda täht õigest sõnast, et vältida mitut kollast sama tähe eest
            oige_sona_koopia[oige_sona_koopia.index(pakkumine_list[i])] = None
            # pakkumine_list[i] = None # Eemalda ka pakkumisest - pole vajalik peale kontrolli

    # 3. Hallide tähtede märkimine klaviatuuril
    for i in range(SONA_PIKKUS):
        taht = pakkumine[i] # Kasuta algset pakkumist siin
        if taht not in uus_klaviatuuri_seisund:
            uus_klaviatuuri_seisund[taht] = VARV_KASUTATUD_HALL

    # Värvi tähed ruudustikus
    varvi_tahed(katsete_arv, pakkumine, varvid)
    # Uuenda klaviatuuri värve
    uuenda_klaviatuuri(uus_klaviatuuri_seisund)

    # Keela praeguse rea sisestus
    for entry in praegune_rida:
        entry.config(state='disabled')

    # Kontrolli võitu
    if pakkumine == oige_sona:
        lopeta_mang(True)
        return

    katsete_arv += 1

    # Kontrolli kaotust
    if katsete_arv == KATSETE_ARV_MAX:
        lopeta_mang(False)
    else:
        # Luba järgmise rea sisestus
        if katsete_arv < KATSETE_ARV_MAX:
            jargmine_rida = sisestus_kastid[katsete_arv]
            for entry in jargmine_rida:
                entry.config(state='normal')
            jargmine_rida[0].focus() # Pane fookus esimesse kasti

def varvi_tahed(rea_indeks, pakkumine, varvid):
    """Värvib sisestuskastid vastavalt tulemusele."""
    rida = sisestus_kastid[rea_indeks]
    for i, entry in enumerate(rida):
        # Määra teksti värv vastavalt taustale, et see oleks loetav
        teksti_varv = VARV_TAUST if varvid[i] != VARV_HALL else VARV_MUST
        entry.config(
            disabledbackground=varvid[i], # Värv, kui kast on keelatud
            fg=teksti_varv, # Teksti värv
            state='disabled' # Muuda kohe keelatuks peale värvimist
        )
        # Veendu, et tekst jääks nähtavale (kui see oli seal)
        entry.delete(0, tk.END)
        entry.insert(0, pakkumine[i])
        entry.config(state='disabled') # Veendu, et jääb keelatuks

def uuenda_klaviatuuri(uued_seisundid):
    """Uuendab klaviatuuri tähtede värve."""
    global klaviatuuri_seisund
    for taht, uus_varv in uued_seisundid.items():
        if taht in klaviatuuri_nupud:
            praegune_varv_kood = klaviatuuri_seisund.get(taht)

            # Ära kirjuta rohelist üle kollase või halliga
            # Ära kirjuta kollast üle halliga
            if praegune_varv_kood == VARV_KASUTATUD_ROHELINE:
                continue
            if praegune_varv_kood == VARV_KASUTATUD_KOLLANE and uus_varv == VARV_KASUTATUD_HALL:
                continue

            # Määra teksti värv klaviatuuril
            teksti_varv = VARV_TAUST if uus_varv != VARV_HALL else VARV_MUST
            klaviatuuri_nupud[taht].config(bg=uus_varv, fg=teksti_varv)
            klaviatuuri_seisund[taht] = uus_varv


def lopeta_mang(voit):
    """Kuvab lõputeate ja keelab edasise mängu."""
    kontrolli_nupp.config(state='disabled')
    # Keela kõik sisestuskastid igaks juhuks
    for rida in sisestus_kastid:
        for entry in rida:
            entry.config(state='disabled')

    if voit:
        teade_label.config(text=f"Palju õnne! Leidsid sõna '{oige_sona}'!")
        salvesta_tulemus(oige_sona, True) # Valikuline
    else:
        teade_label.config(text=f"Katsed otsas! Õige sõna oli: {oige_sona}")
        salvesta_tulemus(oige_sona, False) # Valikuline

def salvesta_tulemus(sona, onnestus):
    """Salvestab mängu tulemuse faili (valikuline)."""
    try:
        skripti_kaust = os.path.dirname(os.path.abspath(__file__))
        failitee = os.path.join(skripti_kaust, TULEMUSTE_FAIL)
        with open(failitee, 'a', encoding='utf-8') as f:
            tulemus_tekst = "Õnnestus" if onnestus else "Ebaõnnestus"
            # Kasuta katsete_arv + 1 võidu korral, sest katsete_arv suureneb peale kontrolli
            katseid_kasutatud = katsete_arv + 1 if onnestus else katsete_arv
            f.write(f"Sõna: {sona}, Tulemus: {tulemus_tekst}, Katseid: {katseid_kasutatud}\n")
    except Exception as e:
        print(f"Ei saanud tulemust salvestada: {e}") # Ära kuva messageboxi siin

def uus_mang():
    """Alustab uut mängu."""
    global katsete_arv, oige_sona, klaviatuuri_seisund

    # Vali uus sõna
    oige_sona = random.choice(koik_sonad)
    if not oige_sona:
        messagebox.showerror("Viga", "Ei saanud uut sõna valida. Kontrolli sõnade faili.")
        # Ära siin quit() tee, las aken jääb lahti veateatega
        kontrolli_nupp.config(state='disabled')
        uus_mang_nupp.config(state='disabled')
        teade_label.config(text="Viga sõnade laadimisel. Kontrolli 'sonad.txt'.")
        return

    # Lähtesta muutujad
    katsete_arv = 0
    teade_label.config(text="")
    kontrolli_nupp.config(state='normal')
    klaviatuuri_seisund = {}

    # Puhasta ja lähtesta sisestuskastid
    for r in range(KATSETE_ARV_MAX):
        for k in range(SONA_PIKKUS):
            entry = sisestus_kastid[r][k]
            entry.config(
                state='normal', # Luba korraks, et saaks puhastada ja värvida
                bg=VARV_TAUST,
                disabledbackground=VARV_TAUST,
                fg=VARV_MUST
            )
            entry.delete(0, tk.END)
            # Luba ainult esimese rea sisestus alguses
            if r == 0:
                 entry.config(state='normal')
            else:
                 entry.config(state='disabled')


    # Lähtesta klaviatuuri värvid
    for taht, nupp in klaviatuuri_nupud.items():
        nupp.config(bg=VARV_HALL, fg=VARV_MUST)

    # Pane fookus esimesse kasti esimesel real
    sisestus_kastid[0][0].focus()
    # print(f"Uus mäng alustatud. Õige sõna testimiseks: {oige_sona}") # Eemalda või kommenteeri välja lõppversioonis


# --- GUI loomine ---
aken = tk.Tk()
aken.title("Wordle Mäng")
aken.config(bg=VARV_TAUST)
aken.resizable(False, False) # Ära luba akna suurust muuta
aken.iconbitmap("ff.ico") # Lisa ikoon (vajalik fail)

# Pealkiri
pealkiri_label = tk.Label(aken, text="Wordle Mäng", font=("Arial", 24, "bold"), bg=VARV_TAUST, fg=VARV_MUST)
pealkiri_label.pack(pady=10)

# Ruudustiku raam
ruudustik_raam = tk.Frame(aken, bg=VARV_TAUST)
ruudustik_raam.pack(pady=10)
# Lisa see funktsioonide plokki (enne GUI loomist)
def valideeri_sisend(P):
    """Valideerib, et sisestus oleks 0 või 1 tähemärki pikk ja täht."""
    # %P on väärtus, mis tekiks peale muudatust
    if len(P) == 0:
        return True # Luba kustutamine
    if len(P) == 1 and P.isalpha():
        return True # Luba üks täht
    return False # Keela kõik muu

vcmd = (aken.register(valideeri_sisend), '%P')
# Loo sisestuskastide ruudustik
for r in range(KATSETE_ARV_MAX):
    rida_list = []
    for k in range(SONA_PIKKUS):
        entry = tk.Entry(
            ruudustik_raam,
            width=3, # Kasti laius
            font=("Arial", 18, "bold"),
            justify='center', # Tekst keskele
            borderwidth=1,
            relief="solid", # Äärise stiil
            state='disabled', # Alguses keelatud (v.a. esimene rida peale uus_mang)
            disabledbackground=VARV_TAUST, # Keelatud taustavärv
            disabledforeground=VARV_MUST, # Keelatud teksti värv
            fg=VARV_MUST,
            bg=VARV_TAUST,
            # Lisa valideerimine
            validate='key',
            validatecommand=vcmd
        )
        entry.grid(row=r, column=k, padx=3, pady=3)
        rida_list.append(entry)
    sisestus_kastid.append(rida_list)

# Juhtnuppude raam
nupu_raam = tk.Frame(aken, bg=VARV_TAUST)
nupu_raam.pack(pady=10)

# Kontrolli nupp
kontrolli_nupp = tk.Button(
    nupu_raam,
    text="Kontrolli",
    font=("Arial", 12),
    command=kontrolli_katset,
    width=10
)
kontrolli_nupp.grid(row=0, column=0, padx=5)

# Uus mäng nupp
uus_mang_nupp = tk.Button(
    nupu_raam,
    text="Uus mäng",
    font=("Arial", 12),
    command=uus_mang,
    width=10
)
uus_mang_nupp.grid(row=0, column=1, padx=5)

# Teadete silt
teade_label = tk.Label(aken, text="", font=("Arial", 12), bg=VARV_TAUST, fg=VARV_MUST)
teade_label.pack(pady=10)

# Klaviatuuri raam
klaviatuur_raam = tk.Frame(aken, bg=VARV_TAUST, pady=5)
klaviatuur_raam.pack()

# Klaviatuuri tähed (lihtsustatud paigutus)
tahestik = [
    "QWERTYUIOPÜÕ",
    "ASDFGHJKLÖÄ",
    "ZXCVBNM"
]

for rea_nr, rida_tahed in enumerate(tahestik):
    rida_raam = tk.Frame(klaviatuur_raam, bg=VARV_TAUST)
    rida_raam.pack()
    for taht in rida_tahed:
        nupp = tk.Label(
            rida_raam,
            text=taht,
            font=("Arial", 10, "bold"),
            width=3,
            height=2,
            borderwidth=1,
            relief="raised", # Nupu välimus
            bg=VARV_HALL, # Algne värv
            fg=VARV_MUST
        )
        nupp.pack(side=tk.LEFT, padx=2, pady=2)
        klaviatuuri_nupud[taht] = nupp # Salvesta viide tähele

# --- Mängu alustamine ---
koik_sonad = loe_sonad_failist(SONADE_FAIL)
if koik_sonad: # Alusta mängu ainult siis, kui sõnad on edukalt loetud
    uus_mang()
else:
    # Kui sõnu ei leitud, keelame nupud ja näitame veateadet aknas
    kontrolli_nupp.config(state='disabled')
    uus_mang_nupp.config(state='disabled')
    teade_label.config(text=f"Viga: '{SONADE_FAIL}' ei leitud või on tühi {SONA_PIKKUS}-tähelistest sõnadest.")
    # Keela ka esimese rea kastid
    if sisestus_kastid:
        for entry in sisestus_kastid[0]:
            entry.config(state='disabled')

# --- Käivita Tkinteri põhitsükkel ---
aken.mainloop() # SEE RIDA OLI PUUDU