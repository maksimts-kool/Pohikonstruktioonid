import random
import time
import os

robotlist = ["kivi", "käärid", "paber"]
print("\nMäng 'Kivi-paber-käärid'")
print("Valige, kellega soovite mängida")
print("1. Sõbraga")
print("2. Robotiga")
while True:
    try:
        valiklevel = int(input("Sisesta arv: "))
        if valiklevel in [1,2]: break
        else: print("Ainult 1 või 2")
    except:
        print("Sisesta arv")
scores = [0, 0]
while True:
    print("\nMäng 'Kivi-paber-käärid'")
    print("kivi")
    time.sleep(.5)
    print("käärid")
    time.sleep(.5)
    print("paber")
    time.sleep(.5)
    print("kolm")
    while True:
        valik = input(f"Mängija 1, Sisesta väärtust (paber, kivi, käärid): ").lower()
        if valik not in ["paber", "kivi", "käärid"]: print("Siseta ainult paber, kivi, käärid")
        else: break
    time.sleep(.5)
    os.system('cls')
    if valiklevel == 1:
        print("Sõber valib...")
        while True:
            sõbra_valik = input(f"Mängija 2, Sisesta väärtust (paber, kivi, käärid): ").lower()
            if sõbra_valik not in ["paber", "kivi", "käärid"]: print("Siseta ainult paber, kivi, käärid")
            else: break
        time.sleep(.5)
        os.system('cls')
    else:
        random.shuffle(robotlist)
        sõbra_valik = robotlist[0]
        print("Robot valib...")
        time.sleep(1)
    print(f"Mängija 1 valis {valik}")
    time.sleep(1)
    print(f"Mängija 2 valis {sõbra_valik}")

    if valik == sõbra_valik:
        time.sleep(.5)
        print("Mõlemad valisid sama. Mängime uuesti!")
        continue
    elif (valik == "paber" and sõbra_valik == "kivi") or \
         (valik == "kivi" and sõbra_valik == "käärid") or \
         (valik == "käärid" and sõbra_valik == "paber"):
        time.sleep(.5)
        print("Mängija 1 võidab!")
        scores[0] += 1
    else:
        time.sleep(.5)
        print("Mängija 2 võidab!")
        scores[1] += 1

    print("\nTulemus:")
    print(f"Mängija 1: {scores[0]} punkti")
    print(f"Mängija 2: {scores[1]} punkti")
    time.sleep(.5)

    while True:
        val = input("Mängime veel (jah/ei)? ")
        if val == "jah" or val == "ei": break
        else: print("Sisesta ainult jah/ei")
    if val == "ei":
        break
