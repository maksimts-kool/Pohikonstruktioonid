import time

while True:
    print("\n--- Stringi funktsioonid ---")
    print("1. Otsi stringi (find)")
    print("2. Asenda string (replace)")
    print("3. Tee string ',' järgi (split)")
    print("4. Kas string koosneb ainult numbritest? (isdigit)")
    print("5. Loe teksti esinemiste arv (count)")
    print("6. Kas string lõppeb sellega stringiga? (endswith)")
    print("7. Teisenda iga sõna algus suurtäheks (title)")
    print("8. Eemalda tühikud stringi algusest ja lõpust (strip)")
    print("9. Kas string algab sellega stringiga? (startswith)")
    print("10. Ühenda list stringideks ',' (join)")
    print("0. Välju")
    
    while True:
        try:
            valik = int(input("Vali funktsiooni number: "))
            if 0 <= valik <= 10: break 
            else: print("Vale valik")
        except:
            print("Ainult nubrid")
    if valik == 0: break

    while True:
        tekst = input("Sisesta tekst: ")
        if tekst == "": print("On tühi")
        else: break
    tekstlist = list(tekst)

    if valik == 1:
        # find() otsib stringi ja tagastab selle indeksi.
        findnimi = input("Sisestage sõna, mida soovite otsida:")
        indeks = tekst.find(findnimi)
        if indeks == -1:
            print("Sõna ei leidnud")
        else:
            print(f"{findnimi}' leiti positsioonilt: {indeks}")
    elif valik == 2:
        # replace() asendab kõik stringi esinemised teise stringiga.
        tekstrepl = input("Sisesta sõne mida muuda: ")
        tekstuus = input("Sisesta uus sõne: ")
        uus_tekst = tekst.replace(tekstrepl, tekstuus)
        print(f"Algne tekst: {tekst}")
        print(f"Pärast asendamist: {uus_tekst}")
    elif valik == 3:
        # split() teeb stringi listiks stringideks, kasutades ",".
        osad = tekst.split(",")
        print(f"Algne tekst: {tekst}")
        print(f"Tehtud list: {osad}")
    elif valik == 4:
        # isdigit() kontrollib, kas string koosneb ainult numbritest.
        if tekst.isdigit():
            print(f"String '{tekst}' koosneb ainult numbritest.")
        else:
            print(f"String '{tekst}' ei sisaldab numbreid.")
    elif valik == 5:
        # count() loeb, mitu korda antud string tekstis on.
        antud = input("Sisesta sõna: ")
        arv = tekst.count(antud)
        print(f"Antud string '{antud}' näib {arv} korda.")
    elif valik == 6:
        # endswith() kontrollib, kas string lõpeb sellega stringiga.
        endwi = input("Sisesta lõpp sõna: ")
        if tekst.endswith(endwi):
            print(f"String '{tekst}' lõpeb sõnaga '{endwi}'.")
        else:
            print(f"String '{tekst}' ei lõpe sõnaga '{endwi}'.")
    elif valik == 7:
        # title() teisendab iga sõna alguse suurtäheks.
        pealkiri = tekst.title()
        print(f"Algne tekst: {tekst}")
        print(f"Pealkirjaga tekst: {pealkiri}")
    elif valik == 8:
        # strip() eemaldab tühikud stringi algusest ja lõpust.
        uustekst = tekst.strip()
        print(f"Algne tekst: {tekst}")
        print(f"Puhas tekst: {uustekst}")
    
    elif valik == 9:
        # startswith() kontrollib, kas string algab sellega stringiga.
        startwi = input("Sisesta algus sõna: ")
        if tekst.startswith(startwi):
            print(f"String '{tekst}' algab sõnaga '{startwi}'.")
        else:
            print(f"String '{tekst}' ei alga sõnaga '{startwi}'.")
    
    elif valik == 10:
        # join() ühendab listi stringideks, kasutades ",".
        ühendatud = ", ".join(tekstlist)
        print(f"List: {tekstlist}")
        print(f"Ühendatud string: {ühendatud}")

    time.sleep(1)
