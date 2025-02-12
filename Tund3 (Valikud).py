import random

# Näidis 1
arv = random.randint(0,10)
print(arv)
if arv > 5:
    print("************")
    print(f"Arv {arv} suurem kui 5")
    print("************")
elif arv == 5:
    print("************")
    print(f"Arv {arv} võrdub 5")
    print("************")
else:
    print("************")
    print(f"Arv {arv} vähem kui 5")
    print("************")

# Näidis 2
arv = random.randint(-10,10)
print(arv)
if arv < 0:
    print("Negatiivne")
else:
    print("Positiivne")

# Ülesanne
nimi = input("Teie nimi: ")
if nimi.isupper() and nimi.lower() == "juku":
    print("Lähme kino")
    try:
        vanus = int(input("Teie vanus: "))
        if vanus < 0 or vanus > 100:
            print("viga andmetega")
        elif vanus < 6:
            print("Tasuta")
        elif vanus <= 14:
            print("lastepilet")
        elif vanus <= 65:
            print("täispilet")
        elif vanus > 65:
            print("sooduspilet")
    except Exception as e:
        print("Tekkis viga: ",e)
else:
    print("Ma olen hõivatud")

# Ülesanne 2
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")

arv = random.randint(0,1)


if (nimi1 == "Hussein" and nimi2 == "Nikita") or (nimi1 == "Nikita" and nimi2 == "Hussein"):
    print("Täna on minu pinginaabrid")
else:
    print("Täna ei ole minu pinginaabrid")


