# Ül 1
print("Tere, maailm!")

sõne = input("Kasutaja nimi: ")
print(f"Tere, maailm! Tervitan sind {sõne}")

vanus = int(input("Sinu vanus: "))
print(f"Tere, maailm! Tervitan sind {sõne} Sa oled {vanus} aastat vana.")
# Ül 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True  #  Või False

print(vanus,type(vanus))
print(eesnimi,type(eesnimi))
print(pikkus,type(pikkus))
print(kas_käib_koolis,type(kas_käib_koolis))

if kas_käib_koolis:
    print(eesnimi,"käib koolis.")
else:
    print(eesnimi,"ei käi koolis.")
# Ül 3
kommid = 20
print(f"Laual on {kommid} komme.")
kustuta = int(input("Mitu komme soovid laualt ära võtta?\n"))
kommid -= kustuta
print(f"Nüüd on laual {kommid} komme.")