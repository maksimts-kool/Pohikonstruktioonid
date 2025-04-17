from Tund14_Moodul import *

loginid = []
paroolid = []
emails = {}

while True:
    print("\nVali tegevus:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Muuda parooli või kasutajanime")
    print("4. Taasta parool")
    print("5. Välju")
    valik = int(input("Sisesta valik (1-5): "))

    if valik == 1:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        if kasutajanimi in loginid:
            print("Kasutajanimi on juba olemas!")
            continue
        email = input("Sisesta e-mail: ")
        if not email:
            print("E-mail on kohustuslik!")
            continue

        parool_valik = input("Kas soovid genereerida parooli? (jah/ei): ").lower()
        if parool_valik == "ei":
            parool = input("Sisesta parool: ")

            digit = False
            lower = False
            upper = False
            punkt = False

            for p in parool:
                if p.isdigit(): # 1,2,3...
                    digit = True
                elif p.islower(): # a,b,c...
                    lower = True
                elif p.isupper(): # A,B,C...
                    upper = True
                elif p in string.punctuation: # !,.,?...
                    punkt = True

            if digit and lower and upper and punkt:
                vastus = registreerimine(loginid, paroolid, kasutajanimi, email, parool)
                emails[kasutajanimi] = email
                print(vastus)
            else:
                print("Parool peab sisaldama numbreid, väikseid ja suuri tähti ning erisümboli!")
        else:
            print(registreerimine(loginid, paroolid, kasutajanimi, email))
            emails[kasutajanimi] = email

    elif valik == 2:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        parool = input("Sisesta parool: ")
        print(autoriseerimine(loginid, paroolid, kasutajanimi, parool))

    elif valik == 3:
        valik2 = input("Kas soovid muuta nime või parooli (nimi/parool)? ").lower()
        if valik2 == "nimi":
            vana_nimi = input("Sisesta vana kasutajanimi: ")
            uus_nimi = input("Sisesta uus kasutajanimi: ")
            print(muuda_nimi(loginid, vana_nimi, uus_nimi, emails[vana_nimi]))
            if vana_nimi in emails:
                emails[uus_nimi] = emails.pop(vana_nimi)
        elif valik2 == "parool":
            kasutajanimi = input("Sisesta kasutajanimi: ")
            vana_parool = input("Sisesta vana parool: ")
            uus_parool = input("Sisesta uus parool: ")
            if kasutajanimi in emails:
                print(muuda_parool(loginid, paroolid, kasutajanimi, vana_parool, uus_parool, emails[kasutajanimi]))
            else:
                print("E-maili pole leitud kasutajale!")
        else:
            print("Vale valik!")

    elif valik == 4:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        print(taasta_parool(loginid, paroolid, kasutajanimi, emails[kasutajanimi]))

    elif valik == 5:
        print("Programm väljub!")
        break
    else:
        print("Vale valik, proovi uuesti!")