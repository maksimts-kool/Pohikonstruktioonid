import random

def lae_sonad_failist():
    sonad = []
    try:
        with open("Tund16_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                est, rus, eng = line.strip().split('-')
                sonad.append({'est': est, 'rus': rus, 'eng': eng})
            file.close()
    except:
        print("Faili ei leitud")
    return sonad

def salvesta_sonad_faili(sonad):
    with open("Tund16_list.txt", "w", encoding="utf-8") as file:
        for kirje in sonad:
            file.write(f"{kirje['est']}-{kirje['rus']}-{kirje['eng']}\n")
        file.close()

def otsi_sona(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():  # Check if in list
            return kirje[siht]
    return "Sõna ei leitud!"

def lisa_sona(sonad):
    uus_est = input("Sisesta sõna (est): ").lower()
    uus_rus = input("Sisesta sõna (rus): ").lower()
    uus_eng = input("Sisesta sõna (eng): ").lower()

    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})  # Add new row
    salvesta_sonad_faili(sonad)
    print("Uus sõna on lisatud!")

def kontrolli_keel(prompt):
    lubatud_keeled = ['est', 'rus', 'eng']
    while True:
        keel = input(prompt).lower()
        if keel in lubatud_keeled:
            return keel
        print(f"Viga: '{keel}' ei ole lubatud keel!")

def paranda_sona(sonad):
    allikas = kontrolli_keel("Sisesta keel, millest sõna parandada: ")
    vana_sona = input(f"Sisesta eelmine sõna ({allikas}): ").lower()
    for kirje in sonad:
        if kirje[allikas] == vana_sona:  # Check if word is in list
            uus_sona = input(f"Sisesta uus sõna ({allikas}): ").lower()
            kirje[allikas] = uus_sona  # Change old word to new
            salvesta_sonad_faili(sonad)
            return "Sõna on parandatud!"
    print("Sõna ei leitud!")

def kuva_sonad(sonad):
    print("Praegune sõnastik:")
    for kirje in sonad:
        print(f"Eesti: {kirje['est']}, Vene: {kirje['rus']}, Inglise: {kirje['eng']}")
    print("\n")

def vali_keelte_suund():
    allikas = kontrolli_keel("Vali lähtekeel: ")
    siht = kontrolli_keel("Vali sihtkeel: ")
    return allikas, siht

def testi_teadmisi(sonad):
    skoor = 0
    total = 5
    allikas, siht = vali_keelte_suund()
    print(f"Testi suund: {allikas} -> {siht}")
    for i in range(total):
        kirje = random.choice(sonad)  # Chooses random word
        print(f"Tõlgi sõna ({allikas}): {kirje[allikas]}")
        vastus = input("Sisesta tõlge: ").lower()
        if vastus == kirje[siht]:  # Check if the answer is correct
            skoor += 1
            print(f"Õige! Teie skoor: {skoor}")
        else:
            print(f"Vale! Õige vastus oli: {kirje[siht]}")
    
    return print(f"Testi tulemus: {skoor}/{total} õiget vastust!")

def kysi_kasutajalt_sisestus(prompt):
    sisestus = input(prompt)
    if not sisestus:
        print("Sisestus on tühi!")
        return kysi_kasutajalt_sisestus(prompt)
    return sisestus

def kuva_menuu():
    print(
"""Menüü:
1. Otsi sõna
2. Lisa uus sõna
3. Paranda sõna
4. Kuva sõnastik
5. Testi teadmisi
6. Kustuta sõna
7. Välju
    """)

def valjasta_tervitus():
    print("Tere tulemast sõnastikku!")

def kustuta_sona(sonad):
    allikas = kontrolli_keel("Sisesta keel, millest kustutada sõna: ")
    del_sona = input(f"Sisesta sõna ({allikas}), mida soovid kustutada: ").lower()
    
    for kirje in sonad:
        if kirje[allikas] == del_sona:
            sonad.remove(kirje)
            salvesta_sonad_faili(sonad)
            print("Sõna on kustutatud!")
            return
    print("Sõna ei leitud!")