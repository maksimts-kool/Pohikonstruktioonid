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
mundi_labi_cm = 25.75 # 2-eurose läbimõõt cm
pi = math.pi
maara_umbermoot_km = 2 * pi * maara_raadius_km
print(f"Maa ümbermõõt ekvaatori kohal on: {round(maara_umbermoot_km,2)} km")
mundi_labi_km = mundi_labi_cm * 0.00001 # 1 cm = 0.00001 km
print(f"2-eurose mündi läbimõõt kilomeetrites on: {round(mundi_labi_km,5)} km")
mundide_arv = maara_umbermoot_km / mundi_labi_km
print(f"Kokku on vaja {round(mundide_arv)} 2-eurost münti")

# Ül 5
word1_cap = "kill-koll".capitalize()
word2_cap = "killadi-koll".capitalize()
print(f"{word1_cap} {word1_cap} {word2_cap} {word1_cap} {word1_cap} {word2_cap} {word1_cap} {word1_cap} {word1_cap}\n{word1_cap}")

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
pikkus = float(input("Sisesta ristküliku pikkus: "))
laius = float(input("Sisesta ristküliku laius: "))
umbermoot = 2 * (pikkus + laius)
pindala = pikkus * laius
print(f"Ristküliku ümbermõõt on: {umbermoot}")
print(f"Ristküliku pindala on: {pindala}")

# Ül 8
kutuse = float(input("Sisesta tarbitud kütuse kogus: "))
labitud_km = float(input("Sisesta läbitud kilomeetrite arv: "))
kutusekulu = (kutuse / labitud_km) * 100
print(f"Kütusekulu 100 km kohta on: {round(kutusekulu,2)} liitrit")