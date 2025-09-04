def LisaIjaP(p: list, i: list):
    """
    Lisab mitu inimest ja nende palgad
    """
    while True:
        nimi = input("Sisesta nimi: ")
        if nimi == '':
            break
        if nimi.isalpha():
            try:
                palk = int(input("Sisesta palk: "))
                i.append(nimi)
                p.append(palk)
                print(f"{nimi} lisatud palgaga {palk}")
            except:
                print("Sisesta number")
        else:
            print("Sisesta tähti")

def KustutaI(p: list, i: list):
    """
    Kustutab isiku ja tema palga nime järgi
    """
    if not i:
        print("List on tühi!")
        return
    
    print("Andmed:")
    for n in i:
        print(n)
    
    knimi = input("Sisesta kustutatava nime: ")
    if knimi in i:
        index = i.index(knimi)
        i.pop(index)
        p.pop(index)
        print(f"{knimi} on kustutatud")
    else:
        print(f"{knimi} ei leitud!")

def SuurimP(palgad: list, inimesed: list):
    """
    Leiab kõrgeima palga ja inimese(d)
    """
    if not palgad:
        print("List on tühi!")
        return
    
    max_palk = max(palgad)
    max_indeksid = []
    for i, palk in enumerate(palgad): # 2500, 2500, 1200...
        if palk == max_palk:
            max_indeksid.append(i)
    
    if len(max_indeksid) > 1: # 2500,2500 -> 2
        print("Kõrgeimaid palgad:")
        for i in max_indeksid:
            print(f"{inimesed[i]} - {palgad[i]}€")
    else:
        print("Kõrgeim palk:")
        print(f"{inimesed[max_indeksid[0]]} - {palgad[max_indeksid[0]]}€")

def VaikseimP(palgad: list, inimesed: list):
    """
    Leiab väikseima palga ja inimese(d)
    """
    if not palgad:
        print("List on tühi!")
        return
    
    min_palk = min(palgad)
    min_indeksid = []

    for i, palk in enumerate(palgad):
        if palk == min_palk:
            min_indeksid.append(i)
    
    if len(min_indeksid) > 1:
        print("Kõige väiksemaid palkad:")
        for indeks in min_indeksid:
            print(f"{inimesed[indeks]} - {palgad[indeks]}€")
    else:
        print("Kõige väiksem palk:")
        print(f"{inimesed[min_indeksid[0]]} - {palgad[min_indeksid[0]]}€")

def SorteeriP(palgad: list, inimesed: list):
    """
    Järjestab palgad kasvavas ja kahanevas järjekorras
    """
    if not palgad:
        print("List on tühi!")
        return
    
    v = input("Vali: Kasvav või Kahenev\n").lower()
    andmed = sorted(zip(palgad, inimesed))

    if v == 'kasvav':
        print("\nPalgad kasvavas järjekorras:")
        for palk, nimi in andmed:
            print(f"{nimi} - {palk}€")
    elif v == 'kahenev':
        print("\nPalgad kahanevas järjekorras:")
        for palk, nimi in reversed(andmed):
            print(f"{nimi} - {palk}€")
    else:
        print('Vale valik')

def VordsedP(palgad: list, inimesed: list):
    """
    Leiab ja kuvab sama palga saavad inimesed
    """
    if not palgad:
        print("List on tühi!")
        return
    
    leitud = False
    for i in range(len(palgad)): # one palk checking others
        sama_palgaga = []
        for j in range(i+1, len(palgad)): # for 'others' 100, 200, 1200, 2500... 
            if palgad[i] == palgad[j]: # if 1200 find 'other' 1200 in search
                if not sama_palgaga: # if first person isn't added
                    sama_palgaga.append(inimesed[i])
                sama_palgaga.append(inimesed[j]) # add other person
        
        if sama_palgaga:
            leitud = True
            print(f"\nSama palga {palgad[i]}€ saavad {len(sama_palgaga)} inimest:")
            for nimi in sama_palgaga:
                print(f"{nimi}")
    
    if not leitud:
        print("Ükski inimene ei saa sama palga")

def OtsiP(palgad: list, inimesed: list):
    """
    Otsib palga isiku nime järgi
    """
    if not inimesed:
        print("List on tühi!")
        return
    
    nimi = input("Sisesta inimese nimi: ")
    leitud = False
    
    print("Tulemused:")
    for i, (palk, inimi) in enumerate(zip(palgad, inimesed)):
        if inimi.lower() == nimi.lower():
            leitud = True
            print(f"{inimi} - {palk}€")
    if not leitud:
        print(f"{nimi} ei leitud")

def FilterP(palgad: list, inimesed: list):
    """
    Kuvab inimesed, kes saavad rohkem/vähem kui määratud summa
    """
    if not palgad:
        print("List on tühi!")
        return
    
    try:
        summa = float(input("Sisesta filtri summa: "))
        valik = input("Rohkem või vähem kui sisestatud summa? ").lower()
        
        if valik not in ['rohkem', 'vähem']:
            print("Palun sisesta rohkem või vähem!")
            return
        
        leitud = False
        print("Tulemused:")
        for nimi, palk in zip(inimesed, palgad):
            if valik == 'rohkem':
                if palk > summa:
                    leitud = True
                    print(f"{nimi} - {palk}€")
            if valik == 'vähem': 
                if palk < summa:
                    leitud = True
                    print(f"{nimi} - {palk}€")
        
        if not leitud:
            print(f"Ei leidu inimesi, kes saavad rohkem/vähem kui {summa}€")
    
    except:
        print("Palun sisesta arv!")

def TopI(palgad: list, inimesed: list):
    """
    Näitab T kõige vaesemat ja rikkamat inimest
    """
    if not palgad:
        print("List on tühi!")
        return
    
    try:
        T = int(input("Mitu inimest soovid näha? "))
        if T <= 0:
            print("Arv peab olema positiivne!")
            return
        
        andmed = sorted(zip(palgad, inimesed))[:T]
        
        print(f"\n{T} kõige rikkamat inimest:")
        for palk, nimi in reversed(andmed):
            print(f"{nimi} - {palk}€")
        
        print(f"\n{T} kõige vaesemat inimest:")
        for palk, nimi in andmed:
            print(f"{nimi} - {palk}€")
            
    except:
        print("Palun sisesta täisarv!")

def KeskmineP(palgad: list, inimesed: list):
    """
    Leiab keskmise palga ja selle saajad
    """
    if not palgad:
        print("List on tühi!")
        return
    
    keskmine_palk = sum(palgad) / len(palgad)
    saajad = []
    
    for i, palk in enumerate(palgad): # 2500, 2500, 1200...
        if palk == keskmine_palk:
            saajad.append(inimesed[i])
    
    print(f"Keskmine palk on: {round(keskmine_palk,2)}€")
    if saajad:
        print("Keskmist palka saavad:")
        for nimi in saajad:
            print(nimi)
    else:
        print("Ükski inimene ei saa keskmist palka")