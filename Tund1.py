import random
import math

# Ül 1
print("Tere, maailm!")

sõne = input("Kasutaja nimi: ").capitalize()
print(f"Tere, maailm! Tervitan sind {sõne}")

vanus = int(input("Sinu vanus: "))
print(f"Tere, maailm! Tervitan sind {sõne} Sa oled {vanus} aastat vana.")
# Ül 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True  #  Või False

print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)}")

# Ül 3
kommid = random.randint(10, 100)
print(f"Laual on {kommid} komme.")
kustuta = int(input("Mitu komme soovid laualt ära võtta?\n"))
kommid -= kustuta
print(f"Nüüd on laual {kommid} komme.")

# Ül 4
ymbermoot = float(input("Sisesta puu ümbermõõt meetrites: "))
labimoot = ymbermoot / math.pi
print(f"Puu läbimõõt on: {round(labimoot, 2)} meetrit")

# Ül 5
pikk = float(input("Sisesta maatüki pikkus meetrites: "))
laius = float(input("Sisesta maatüki laius meetrites: "))
diagonaal = math.sqrt(pikk**2 + laius**2)
print(f"Maatüki diagonaal on: {round(diagonaal, 2)} meetrit")

# Ül 6
aeg = float(input("Mitu tundi kulus sõiduks?"))
teepikkus = float(input("Mitu kilomeetrit sõitsid?"))
kiirus = teepikkus / aeg        # Parandatud valem: kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# Ül 7
arv1 = int(input("Sisesta esimene täisarv: "))
arv2 = int(input("Sisesta teine täisarv: "))
arv3 = int(input("Sisesta kolmas täisarv: "))
arv4 = int(input("Sisesta neljas täisarv: "))
arv5 = int(input("Sisesta viies täisarv: "))

summa = arv1 + arv2 + arv3 + arv4 + arv5
keskmine = summa / 5
print(f"Viie sisestatud täisarvu keskmine on: {keskmine}")

# Ül 8
print("  @..@")
print(" (----)")
print("( \\__/ )")
print("^^ \"\" ^^")

# Ül 9
a = int(input("Sisesta külg a: "))
b = int(input("Sisesta külg b: "))
c = int(input("Sisesta külg c: "))
p = a + b + c
print(f"Kolmnurga ümbermõõt on: {p}")

# Ül 10
soprad = int(input("Mitu sõpra on kaasas?\n"))
hind = 12.90
jootraha = hind * 0.10
kogusumma = hind + jootraha
inimesed = soprad + 1
summa_per_inimene = kogusumma / inimesed
print(f"Igaühe makstav osa on: {round(summa_per_inimene,2)} eurot")