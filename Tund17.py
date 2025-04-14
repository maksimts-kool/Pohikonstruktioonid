def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

list_ = Loe_failist("Tund17_Tekst.txt")
for i in list_:
    print(i)

list_ = ["Ann", "Kati", "Mari"]
Kirjuta_failisse("Tund17_Tekst.txt", list_)

list_2 = Loe_failist("Tund17_Tekst.txt")
print(list_2)

with open("Tund17_Tekst.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())

# Ülesanne
import random

def failist_to_dict(f: str):
    riik_pealinn = {}  # {"Страна": "Столица"}
    pealinn_riik = {}  # {"Столица": "Страна"}
    riigid = []
    try:
        with open(f, 'r', encoding="utf-8-sig") as file:
            for line in file:
                k, v = line.strip().split('-')  # k - ключ, v - значение
                riik_pealinn[k] = v
                pealinn_riik[v] = k
                riigid.append(k)
    except:
        print("Faili ei leitud")
    return riik_pealinn, pealinn_riik, riigid

def lisamine(riik_pealinn, pealinn_riik):
    riik = input("Sisestage riigi nimi: ")
    pealinn = input("Sisestage pealinna nimi: ")
    if riik in riik_pealinn:
        print("Riik on juba sõnastikus")
    elif pealinn in pealinn_riik:
        print("Pealinn on juba sõnastikus")
    else:
        riik_pealinn[riik] = pealinn
        pealinn_riik[pealinn] = riik
        print("Lisatud!")

def muudetus(riik_pealinn, pealinn_riik):
    countrycapital = input("Sisestage parandatav riik või pealinn: ")
    if countrycapital in riik_pealinn:
        uus_pealinn = input("Sisestage pealinna uue nimi: ")
        vana_pealinn = riik_pealinn[countrycapital]
        pealinn_riik.pop(vana_pealinn)
        riik_pealinn[countrycapital] = uus_pealinn
        pealinn_riik[uus_pealinn] = countrycapital
        print("Andmed on parandatud")
    elif countrycapital in pealinn_riik:
        uus_riik = input("Sisestage riigi uue nimi: ")
        vana_riik = pealinn_riik[countrycapital]
        riik_pealinn.pop(vana_riik)
        pealinn_riik[countrycapital] = uus_riik
        riik_pealinn[uus_riik] = countrycapital
        print("Andmed on parandatud")
    else:
        print("Andmeid ei leitud")

def test(riik_pealinn):
    items = list(riik_pealinn.items())
    random.shuffle(items)
    correct = 0
    total = min(5, len(items))
    for i in range(total):
        co, ca = items[i]
        answer = input(f"Nimetage riigi pealinn {co}: ")
        if answer.lower() == ca.lower():
            print("Õige!")
            correct += 1
        else:
            print(f"Vale. Õige vastus: {ca}.")
    print(f"Te vastasite õigesti {correct}/{total} ({(correct / total) * 100:.0f}%)")

# Menüü
riik_pealinn, pealinn_riik, riigid = failist_to_dict("Tund17_riigid.txt")
if not riik_pealinn:
    exit()

while True:
    try:
        print("\nMenüü:")
        print("1. Leia pealinn riigi nime järgi")
        print("2. Leia riik pealinna nime järgi")
        print("3. Lisa kanne")
        print("4. Paranda kanne")
        print("5. Kontrollida teadmisi")
        print("6. Väljumine")
        valik = int(input("Vali number: "))
        
        if valik == 1:
            country = input("Sisestage riigi nimi: ")
            print(f"Pealinn: {riik_pealinn.get(country, 'Riiki ei leitud')}")
        elif valik == 2:
            capital = input("Введите название столицы: ")
            print(f"Riik: {pealinn_riik.get(capital, 'Pealinna ei leitud')}")
        elif valik == 3:
            lisamine(riik_pealinn, pealinn_riik)
        elif valik == 4:
            muudetus(riik_pealinn, pealinn_riik)
        elif valik == 5:
            test(riik_pealinn)
        elif valik == 6:
            break
        else:
            print("Vale valik!")
    except:
        print("Viga sisestamisel")