from time import sleep

# Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.
for o in range(20):
    print(f"Sooritab eksamit {o+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

# Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.
while True:
    try:
        P = int(input("P arvud: "))
        break
    except:
        print("Ainult numbrid")

vastus = 0
for a in range(P):
    while True:
        try:
            arv = float(input("Sisesta arv: "))
            break
        except:
            print("Ainult numbrid")
    if arv<0:
        vastus += arv
print(f"Negatiivse arvude summa: {vastus}")

# Koostage plokkskeem kotlette praadiva roboti jaoks
kokku = 100
kotlettperpann = 6
aeg = .2
lahenemine = kokku // kotlettperpann
jaak = kokku % kotlettperpann

if jaak>0: lahenemine += 1

for l in range(lahenemine):
    if jaak>0 and l == lahenemine - 1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {kotlettperpann} kotlet.")
    print(f"{l+1} esimene")
    sleep(aeg)
    print(f"{l+1} teine")
    sleep(aeg)
print("Kõik on tehtud")

# Määrake H aasta jooksul pangas kogunenud rahasumma, kui Vlad'i esialgne sissemakse oli Y dollarit ja sissemakse tehti tingimustel Z% aastas.
Y = float(input("Esialne sissemakse: "))
Z = float(input("Intress: "))
H = int(input("Aastate arv: "))
interest = Y * (Z / 100)

for a in range(1,H+1):
    Y += interest
    print(f"Aasta {a} lõpus on kogunenud summa: {round(Y,2)}$")
# küsitlege O kasutajaid. Selgitage välja nende kaal ja pikkus ning vanus. Leidke kehamassiindeks ja teatage kasutajale selle indeksi iseloomustus.
O = int(input("Mitu kasutajat soovite küsitleda? "))

for i in range(O):
    print(f"\nKasutaja {i+1}:")
    kaal = float(input("Sisestage oma kaal kg: "))
    pikkus = float(input("Sisestage oma pikkus m: "))
    vanus = int(input("Sisestage oma vanus: "))
    kmi = kaal / (pikkus ** 2)

    if kmi < 18.5:
        iseloom = "Alakaal"
    elif 18.5 <= kmi < 24.9:
        iseloom = "Normaalkaal"
    elif 25 <= kmi < 29.9:
        iseloom = "Ülekaal"
    else:
        iseloom = "Rasvumine"
        
    print(f"Kasutaja {i+1} KMI on {round(kmi,2)}, mis tähendab: {iseloom}")