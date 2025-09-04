# Näidis
for i in range(10):
    print(i, end=", ")
for i in range(2, 12):
    print(i, end="; ")
for i in range(2, 12, 3):
    print(i, end=" ")
for i in range(12, 2, -2):
    print(i, end=" ")

# Ül 1
count = 0
for i in range(15):
    while True:
        try:
            num = float(input(f"Sisesta {i+1} arv: "))
            break
        except:
            print("Ainult numbrid")
    if num == int(num):
        count += 1
print(f"Täisarvude arv: {count}")

# Ül 2
sum_natural = 0
while True:
    try:
        A = int(input("Sisesta arv A: "))
        if A > 1:
            for i in range(1, A + 1):
                sum_natural += i
            print(f"Arvude summa vahemikus 1 kuni {A}: {sum_natural}")
            break
        else:
            print("Peab olema rohkem kui 1")
    except:
       print("Vale formaat")

# Ül 3
count = 0
for i in range(8):
    while True:
        try:
            num = int(input(f"Sisesta {i+1} arv: "))
            if num > 0:
                count += num
            break
        except:
            print("Ainult numbrid")
print(f"Positiivsete arvude korrutis: {count}")

# Ül 4
for i in range(10, 21):
    print(f"Numbri {i} ruut on {i ** 2}")

# Ül 5
negative = 0
while True:
    try:
        N = int(input("Sisesta numbrite arv: "))
        if N>1:
            for i in range(N):
                num = int(input(f"Sisesta {i+1} arv: "))
                if num < 0:
                    negative += num
            print(f"Negatiivsete arvude summa: {negative}")
            break
        else:
            print("Peab olema rohkem kui 1")
    except:
        print("Ainult numbrid")

# Ül 6
positive = 0
negative = 0
zero = 0

while True:
    try:
        N = int(input("Sisestage arv N: "))
        if N>1:
            for i in range(N):
                num = int(input(f"Sisesta {i+1} arv: "))
                if num > 0:
                    positive += 1
                elif num < 0:
                    negative += 1
                else:
                    zero += 1
            print(f"Positiivsed arvud: {positive}")
            print(f"Negatiivsed arvud: {negative}")
            print(f"Nullid: {zero}")
            break
        else:
            print("Peab olema rohkem kui 1")
    except:
        print("Ainult numbrid")

# Ül 7
while True:
    try:
        A = int(input("Sisestage intervalli algus: "))
        B = int(input("Sisestage intervalli lõpp: "))
        if A < B:
            K = int(input("Sisestage arv K: "))
            if K > 0:
                for i in range(A, B + 1):
                    if i % K == 0:
                        print(i, end=" ")
                        print()
                break
            else:
                print("K peab olema rohkem kui 0")
        else:
            print("lõpp peab olema rohkem kui algus")
    except:
        print("Ainult numbrid")

# Ül 8
print("Tollid | Sentimeetrit")
print("------------------")
for i in range(1, 21):
    cm = i * 2.5
    print(f"{i} | {cm}")

# Ül 9
while True:
    try:
        S = float(input("Sisestage esialgne hoiuse summa: "))
        N = int(input("Sisesta aastate arv: "))

        for _ in range(N):
            S *= 1.03 # 3%

        print(f"Hoiuse summa pärast {N} aastat: {round(S,2)} eurot")
        break
    except:
        print("Ainult numbrid")

# Ül 10
for _ in range(3):
    while True:
        try:
            num1 = float(input("Sisestage paari esimene number: "))
            num2 = float(input("Sisestage paari teine number: "))
            if num1 > num2:
                print(f"Suurem arv: {num1}")
            elif num2 > num1:
                print(f"Suurem arv: {num2}")
            else:
                print("Numbrid on võrdsed")
            break
        except:
            print("Ainult numbrid")

# Ül 11
import random

K = random.randint(1, 50)
print(f"Genereeritud number: {K}")

product = 1

for num in range(11, 100, 2):
    if num % K == 0:
        product *= num

if product>1:
    print(f"Kahekohaliste paaritute arvude korrutis, mis on jagatavad {K}: {product}")
else:
    print(f"Ei ole kahekohalisi paarituid numbreid, mis on jagatavad {K}.")

# Ül 12
N = int(input("Sisestage heinategijate arv: "))
m = int(input("Sisestage esimese heinaküünla tööaeg (tundid): "))

total_hours = 0
for i in range(N):
    total_hours += m + (i * 10 / 60)

print(f"Kogu meeskond töötas {round(total_hours)} tundi.")

# Ül 13
count = 0
total_sum = 0

for number in range(100, 1001):
    if number % 7 == 0:
        count += 1
        total_sum += number
print(f"jagatavate arvude arv: {count}")
print(f"jagatavate arvude summa: {total_sum}")

# Ül 14
import random
N = random.randint(1, 20)
product = 1

for i in range(1, N + 1):
    product *= i

print(f"Juhuslik number N: {N}")
print(f"Numbrite 1 kuni {N}: {product}")

# Ül 15
for i in range(10):
    for j in range(10):
        print(j,end=" ")  
    print()

# Ül 16


# Ül 17
for i in range(1, 10):
    print(f"2*{i}={2 * i}")

# Ül 18
for num in range(20, 51):
    if num % 3 == 0 and num % 5 != 0:
        print(num)

# Ül 19
for num in range(35, 88):
    if num % 7 in {1, 2, 5}:
        print(num)

# Ül 20
total = 0
for num in range(1, 51):
    if num % 5 == 0 or num % 7 == 0:
        total += num
print("Summa:", total)

# Ül 21


# Ül 22
total = 0
for num in range(100, 201):
    if num % 17 == 0:
        total += num
print("Summa:", total)

# Ül 23


# Ül 24
N = int(input("Sisestage õpilaste arv: "))
total_height = 0

for i in range(N):
    height = float(input("Sisestage õpilase pikkus: "))
    total_height += height

average_height = round(total_height / N)
print(f"Õpilaste keskmine pikkus: {average_height}")

# Ül 25
N = int(input("Sisestage arv N: "))
count = 0

for num in range(1, N + 1):
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        count += 1

print(f"Numbrite arv: {count}")

# Ül 26
for A in range(10, 100):
    for B in range(10, 100):
        num = int(f"{A}{B}")
        if num % (A * B) == 0:
            print("Arvud:", A, B)
            break

# Ül 27
for A in range(10, 100):
    for B in range(10, 100):
        num1 = int(f"{A}{B}")
        num2 = int(f"{B}{A}")
        if num1 % 99 == 0 and num2 % 49 == 0:
            print("Arvud:", A, B)
            break

# Ül 28
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Arvake ära number 1 kuni 100: "))
    attempts += 1
    if guess < number:
        print("Arvatav number on suurem.")
    elif guess > number:
        print("Arvatav number on väiksem.")
    else:
        print(f"Palju õnne! Sa arvasid ära arvu {attempts} katsetega.")
        break
    
# Ül 29


# Ül 30

# Ül 31
K = int(input("Sisestage kotlettide arv: "))
M = int(input("Asetage pannile vastav arv kotlette: "))

full_pans = K // M
remaining = K % M

print(f"Täielikud paanid: {full_pans}")
print(f"Praadimiseks on jäänud: {remaining} kotletti")