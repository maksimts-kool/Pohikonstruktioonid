# Variant 4
import random
import time

# Ül 1
n = random.randint(1,9)

for i in range(n):
    print("  ^---^")
    print(" ( o o )")
    print("  ! = !/)")
    print("\n")
print(f"Sa näed {n} konna")

# Ül 2
while True:
    try:
        n = int(input("Arv: "))
        ast = int(input("Astme:"))
        break
    except:
        print("Ainult täisnumbrid")
limit = n*100
esimene = 1

while True:
    step = esimene ** ast
    if step > limit:
        break
    print(f"{esimene}^{ast} = {step}")
    esimene += 1

# Ül 3
opilased = random.randint(10,30)
minhin = 5
maxhin = 2
print(f"{opilased} opilased")

for i in range(opilased):
    hinne = random.randint(2,5)
    if hinne < minhin:
        minhin = hinne
    if hinne > maxhin:
        maxhin = hinne
    print(f"{i+1} opilasel on hinne {hinne}")
print(f"Min hinne: {minhin}")
print(f"Max hinne: {maxhin}")

# Ül 4
abema = 1

for i in range(3, 25, 3):
    kor = i // 3
    cel = abema * (2 ** kor)
    print(f"{i} tunni jooksul on {cel} rakke")

# Ül 5
k = random.randint(6,30)
kotlettperpann = 6
lahenemine = k // kotlettperpann
jaak = k % kotlettperpann
if jaak>0: lahenemine += 1
print(f"Kokku on {k} kotletti")

for i in range(lahenemine):
    time.sleep(.5)
    print(f"{i+1} paar")
    if jaak>0 and i == lahenemine - 1:
        print("On vaja veel 1 pann, mis ei ole täis")
        print(f"Panni peal on {jaak} kotletti.")
    else:
        print("On vaja täis pann")
        print(f"Panni peal on {kotlettperpann} kotletti.")