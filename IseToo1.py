from math import * # Import kõik funktsioonid math moodulist
try:
    print("Ruudu karakteristikud")
    a = float(input('Sisesta ruudu külje pikkus => ')) # peab olema number väärtus
    S=a**2
    print("Ruudu pindala", S)
    P=4*a
    print("Ruudu ümbermõõt", P) # peab olema " mitte ''
    di=a*sqrt(2) # peab olema sqrt mitte sqr, sest me importime kõik funktsioonid math moodulist ei pea kirjutama math.sqrt
    print("Ruudu diagonaal", round(di,2))
    print()
    print("Ristküliku karakteristikud") # pole vaja üks sulg
    b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # peab olema number väärtus
    c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # peab olema number väärtus
    S=b*c
    print('Ristküliku pindala', S) # ' puudub alguses
    P=2*(b+c) # puudub *
    print("Ristküliku ümbermõõt", P)
    di=sqrt(b**2+c**2) # ei pea kirjutama math.sqrt. Ja peab olema kaks **
    print("Ristküliku diagonaal", round(di,2)) # on vaja lisada üks sulg
    print()
    print("Ringi karakteristikud")
    r=float(input('Sisesta ringi raadiusi pikkus => ')) # pole vaja kaks '' ja üks sulg. peab olema number väärtus
    d=2*r # puudub *
    print("Ringi läbimõõt", d) # puudub koma keskel
    S=pi*r**2 # peab olema kaks **. Pole vaja teha pi() sulgudes
    print("Ringi pindala", round(S,2))
    C=2*pi*r # puudub *. Pole vaja teha pi() sulgudes
    print("Ringjoone pikkus", round(C,2)) # on vaja lisada üks sulg
except Exception as e:
    print("Tekkis viga: ",e)