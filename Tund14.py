from Tund14_Moodul import *

loginid = []
paroolid = []

while True:
    print("\nVali tegevus:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Muuda parooli")
    print("4. Taasta parool")
    valik = int(input("Sisesta valik (1-5): "))

    if valik == 1:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        if kasutajanimi in loginid:
            print("Kasutajanimi on juba olemas!")
            continue
        parool_valik = input("Kas soovid genereerida parooli? (jah/ei): ").lower()
        if parool_valik == "ei":
            parool = input("Sisesta parool: ")

            digit = False
            lower = False
            upper = False
            punctuation = False

            for p in parool:
                if p.isdigit(): # 1,2,3...
                    digit = True
                elif p.islower(): # a,b,c...
                    lower = True
                elif p.isupper(): # A,B,C...
                    upper = True
                elif p in string.punctuation: # !,.,?...
                    punctuation = True

            if digit and lower and upper and punctuation:
                vastus = registreerimine(loginid, paroolid, kasutajanimi, parool)
                print(vastus)
            else:
                print("Parool peab sisaldama numbreid, väikseid ja suuri tähti ning erisümboli!")
        else:
            print(registreerimine(loginid, paroolid, kasutajanimi))

    elif valik == 2:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        parool = input("Sisesta parool: ")
        print(autoriseerimine(loginid, paroolid, kasutajanimi, parool))

    else:
        print("Vale valik, proovi uuesti!")
    '''
    elif valik == 3:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        vana_parool = input("Sisesta vana parool: ")
        uus_parool = input("Sisesta uus parool: ")
        print(muuda_parool(loginid, paroolid, kasutajanimi, vana_parool, uus_parool))

    elif valik == 4:
        kasutajanimi = input("Sisesta kasutajanimi: ")
        print(taasta_parool(loginid, paroolid, kasutajanimi))
    '''
