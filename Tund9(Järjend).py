import random
sõne = "Programmeerimine"
print(sõne)

sõne_list = list(sõne)
print(sõne_list)

sõne_list.reverse()
print(sõne_list)

print(sõne_list.index("P"))

print(len(sõne_list)) # 16
print(len(sõne)) # 16

for i in range(sõne_list.count("m")):
    sõne_list.remove("m")
print(sõne_list)

tähed = random.randint(1,22)
for i in range(tähed):
    while True:
        try:
            t = input("Sisesta täht: ")
            if t.isalpha(): break
        except:
            print("Ainult täht")
    sõne_list.append(t)
print(sõne_list)

tähed = random.randint(1,6)
for i in range(tähed):
    while True:
        try:
            t = input("Sisesta täht: ")
            if t.isalpha(): break
        except:
            print("Ainult täht")
    while True:
        try:
            ind = input("Sisesta index: ")
            if ind.isnumeric() & int(ind) < len(sõne_list): break
        except:
            print("Ainult number")
    sõne_list.insert(int(ind),t)
print(sõne_list)

print(sõne_list.sort(reverse=True))

