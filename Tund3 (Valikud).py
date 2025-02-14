from math import exp
import random
import datetime

# Näidis 1
arv = random.randint(0,10)
print(arv)
if arv > 5:
    print("************")
    print(f"Arv {arv} suurem kui 5")
    print("************")
elif arv == 5:
    print("************")
    print(f"Arv {arv} võrdub 5")
    print("************")
else:
    print("************")
    print(f"Arv {arv} vähem kui 5")
    print("************")

# Näidis 2
arv = random.randint(-10,10)
print(arv)
if arv < 0:
    print("Negatiivne")
else:
    print("Positiivne")

# Ülesanne 1
nimi = input("Teie nimi: ")
if nimi.isupper() and nimi.lower() == "juku":
    print("Lähme kino")
    try:
        vanus = int(input("Teie vanus: "))
        if vanus < 0 or vanus > 100:
            print("viga andmetega")
        elif vanus < 6:
            print("Tasuta")
        elif vanus <= 14:
            print("lastepilet")
        elif vanus <= 65:
            print("täispilet")
        elif vanus > 65:
            print("sooduspilet")
    except Exception as e:
        print("Tekkis viga: ",e)
else:
    print("Ma olen hõivatud")

# Ülesanne 2    
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")

arv = random.randint(0,1)

if (nimi1 == "Hussein" and nimi2 == "Nikita") or (nimi1 == "Nikita" and nimi2 == "Hussein"):
    print("Täna on minu pinginaabrid")
else:
    print("Täna ei ole minu pinginaabrid")

# Ülesanne 3
try:
    pikkus = float(input("Sisesta toa pikkus meetrites: "))
    laius = float(input("Sisesta toa laius meetrites: "))

    pindala = pikkus * laius
    print(f"Põranda pindala on {round(pindala,2)} m2.")

    soov = input("Kas soovid remonti teha?: ").lower()
    if soov == "jah":
        ruutmeetri_hind = float(input("Sisesta remondi hind eurodes: "))
        koguhind = pindala * ruutmeetri_hind
        print(f"Põranda remondi hind on {round(koguhind,2)} eurot.")
    else:
        print("Remonti ei tehta.")
except Exception as e:
    print("Tekkis viga: ",e)

# Ülesanne 4
try:
    alghind = int(input("Siseta alghind: "))
    if alghind > 700:
        soodustus_hind = alghind * (1 - 0.30)
        print(f"30% soodustusega hind: {soodustus_hind} €")
    else:
        print("Alghind peab olema suurem kui 700")
except Exception as e:
    print("Tekkis viga: ",e)

# Ülesanne 5
temperatuur = float(input("Sisesta temperatuur C: "))

if temperatuur > 18:
    print("See on hea toasoojus talvel.")
else:
    print("See on külm!")

# Ülesanne 6
pikkus = float(input("Sisesta inimese pikkus cm: "))

if pikkus < 160:
    print("Inimene on lühike.")
elif 160 <= pikkus <= 180:
    print("Inimene on keskmine.")
else:
    print("Inimene on pikk.")

# Ülesanne 7
pikkus = float(input("Sisesta inimese pikkus cm: "))
sugu = input("Sisesta sugu: ").lower()

if sugu == "mees":
    if pikkus < 175:
        print("Mees on lühike.")
    elif 175 <= pikkus <= 185:
        print("Mees on keskmine.")
    else:
        print("Mees on pikk.")
elif sugu == "naine":
    if pikkus < 160:
        print("Naine on lühike.")
    elif 160 <= pikkus <= 170:
        print("Naine on keskmine.")
    else:
        print("Naine on pikk.")
else:
    print("Sugu ei ole korrektne.")

# Ülesanne 8
try:
    piim_hind = 1.2
    sai_hind = 0.8
    leib_hind = 1.5
    valik = input("Mida soovite osta? ").lower()

    if valik == "piim":
        hind = piim_hind
    elif valik == "sai":
        hind = sai_hind
    elif valik == "leib":
        hind = leib_hind
    else:
        print("Toode pole saadaval.")

    kogus = int(input("Mitu tükki soovite osta? "))
    kogusumma = hind * kogus
    print(f"Tšekk:")
    print(f"{kogus} x {valik.capitalize()} - {round(kogusumma,2)} €")
    print(f"Kogusumma: {round(kogusumma,2)} €")
except Exception as e:
    print("Tekkis viga: ",e)

# Ülesanne 9
külg1 = float(input("Sisesta esimene külg cm: "))
külg2 = float(input("Sisesta teine külg cm: "))

if külg1 == külg2:
    print("See on ruut!")
else:
    print("See ei ole ruut.")

# Ülesanne 10
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
tehe = input("Mida soovite teha?: ")

if tehe == "+":
    tulemus = arv1 + arv2
elif tehe == "-":
    tulemus = arv1 - arv2
elif tehe == "*":
    tulemus = arv1 * arv2
elif tehe == "/":
    if arv2 != 0:
        tulemus = arv1 / arv2
    else:
        tulemus = "ERROR. Jagamine nulliga."
else:
    tulemus = "Siseta tehe"

print(f"Tulemus: {tulemus}")

# Ülesanne 11
sünnipäev = int(input("Sisesta oma sünnipäev (aasta): "))

aasta = datetime.date.today().year
vanus = aasta - sünnipäev

if vanus % 10 == 0:
    print(f"Teil on {vanus} aastat! See on juubel!")
else:
    print(f"Teil on {vanus} aastat. See pole juubel.")

# Ülesanne 12
hind = float(input("Sisesta toote hind: "))
if hind <= 10:
    soodustus = 0.10
else:
    soodustus = 0.20

lõpphind = hind * (1 - soodustus)

print(f"Hind pärast soodustust on: {round(lõpphind,2)} €")

# Ülesanne 13
sugu = input("Sisesta oma sugu: ").lower()

if sugu == "naine":
    print("Meeskond on ainult meestele.")
else:
    vanus = int(input("Sisesta oma vanus: "))
    if 16 <= vanus <= 18:
        print("Sobid meeskonnale!")
    else:
        print("Sa ei sobi meeskonda")

# Ülesanne 14

inimesed = int(input("Sisesta inimeste arv: "))
buss_suurus = int(input("Sisesta bussi kohtade arv: "))

bussid = inimesed // buss_suurus
viimane_buss = inimesed % buss_suurus

if viimane_buss > 0:
    bussid += 1

print(f"On vaja {bussid} bussi.")
print(f"Viimases bussis on {viimane_buss} inimest.")
