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
H = int(input("Kogunenud rahasumma: "))
Y = float(input("Esialne sissemaks: "))
Z = float(input("% aastas: "))
interest = Y * (Z/100)

for i in range(H):
    print(f"{i} aasta intress on {round(Y,2)}%")
    Y += interest

print(Y)
# küsitlege O kasutajaid. Selgitage välja nende kaal ja pikkus ning vanus. Leidke kehamassiindeks ja teatage kasutajale selle indeksi iseloomustus.
