import datetime
import calendar
import math

# Ül 1
tanao = datetime.date.today()
print(f"Täna on {tanao}")
# 27/12/2022
tana = tanao.strftime("%d/%m/%Y")
print(f"Täna on {tana}")
# December 27, 2022
tana = tanao.strftime("%B %d, %Y")
print(f"Täna on {tana}")
# 12/27/22
tana = tanao.strftime("%m/%d/%y")
print(f"Täna on {tana}")
# Dec-27-2022
tana = tanao.strftime("%b-%d-%Y")
print(f"Täna on {tana}")

aasta = tanao.year
kuu = tanao.month
paev = tanao.day
kuupaevad = calendar.monthrange(aasta, kuu)[1]
print(f"{tanao.strftime('%B')} kuus on {kuupaevad} päeva")
jaanud = kuupaevad - paev
print(f"Kuu lõpuni on jäänud {jaanud} päeva")
aastalopuni = 365 - calendar.monthrange(aasta,kuu)[1] + jaanud
print(f"Aasta lõpuni on jäänud {aastalopuni} päeva")

# Ül 2
tulemus = 3 + 8 / (4 - 2) * 4
print(tulemus)
# Ilma sulgudeta
tulemus = 3 + 8 / 4 - 2 * 4
print(tulemus)
# liitmine ja lahutamine on sulgudes
tulemus = (3 + 8) / (4 - 2) * 4
print(tulemus)
# korrutamine on esimesena
tulemus = 3 + (8 / (4 - 2) * 4)
print(tulemus)

# Ül 3
try:
    R = float(input("Sisesta ringi raadius: "))
    ruudu_pindala = (2 * R) ** 2
    ruudu_umbermoot = 8 * R
    ringi_pindala = math.pi * R ** 2
    ringi_umbermoot = 2 * math.pi * R
    print(f"Ruudu pindala: {round(ruudu_pindala,2)} ruutühikut")
    print(f"Ruudu ümbermõõt: {round(ruudu_umbermoot,2)} ühikut")
    print(f"Ringi pindala: {round(ringi_pindala,2)} ruutühikut")
    print(f"Ringi ümbermõõt: {round(ringi_umbermoot,2)} ühikut")
except:
    print("Siseta ujukomaarvud")

# Ül 4
maara_raadius_km = 6378
mundi_labi_cm = 2.575 # 2-eurose läbimõõt cm
pi = math.pi
maara_raadius_cm = maara_raadius_km * 100000 # 1 km = 100000 cm
umbermoot = 2 * pi * maara_raadius_cm
mundide_arv = umbermoot / mundi_labi_cm
print(f"Kokku on vaja {round(mundide_arv):,d} münti")
print(f"Kokku on vaja {round(mundide_arv*2):,d} Euro")

# Ül 5
word1_cap = "kill-koll ".capitalize()
word2_cap = "killadi-koll ".capitalize()
print(word1_cap*2,word2_cap,word1_cap*2,word2_cap,word1_cap*4)

# Ül 6
laul1 = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?"""
laul2 = """Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""
print(laul1.upper())
print()
print(laul2.upper())

# Ül 7
try:
    pikkus = float(input("Sisesta ristküliku pikkus: "))
    laius = float(input("Sisesta ristküliku laius: "))
    if pikkus > 0 and laius > 0:
        umbermoot = 2 * (pikkus + laius)
        pindala = pikkus * laius
        print(f"Ümbermõõt on: {umbermoot}")
        print(f"Pindala on: {pindala}")
    else:
        print("Sisesta positiivsed arvud")
except:
    print("Vale andmed!")

# Ül 8
try:
    kutuse = float(input("Sisesta tarbitud kütuse kogus: "))
    labitud_km = float(input("Sisesta läbitud kilomeetrite arv: "))
    if kutuse > 0 and labitud_km > 0:
        kutusekulu = (kutuse / labitud_km) * 100
        print(f"Kütusekulu 100 km kohta on: {round(kutusekulu,2)} liitrit")
    else:
        print("Sisesta positiivsed arvud")
except:
    print("Vale andmed!")

# Ül 9
try:
    minutid = int(input("Sisesta aeg minutites: "))
    if minutid > 0:
        keskmine = 29.9
        aeg_tundides = minutid / 60
        kaugus_km = keskmine * aeg_tundides
        print(f"Rulluisutaja jõuab {minutid} minutiga {round(kaugus_km,2)} km kaugusele.")
    else:
        print("Sisesta positiivsed arvud")
except:
    print("Vale andmed!")

# Ül 10
try:
    minutid2 = int(input("Sisesta aeg minutites: "))
    if minutid2 > 0:
        tunnid = minutid2 // 60
        jaakmin = minutid2 % 60
        print(f"{tunnid}:{jaakmin:02}")
    else:
        print("Sisesta positiivsed arvud")
except:
    print("Vale andmed!")