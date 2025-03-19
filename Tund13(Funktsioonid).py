from Tund13_Moodul import *

a1 = float(input("Sisesta arv 1: "))
a2 = float(input("Sisesta arv 2: "))
t = input("Tehe: ")
v = arithmetic(a1, a2, t)
print(v)

y = int(input("Sisesta aasta: "))
v = is_year_leap(y)
if v:
    print(f'{y} on liigaasta')
else:
    print(f'{y} ei ole liigaasta')

k = float(input("Sisesta külg: "))
v = square(k)
print(f"ruudu ümbermõõt on {v[0]}. ruudu pindala on {v[1]}. ruudu diagonaal on {v[2]}")

a = int(input("Sisesta kuu: "))
v = season(a)
print(v)

a = float(input("Sisesta summa: "))
b = int(input("Sisesta aastate arv: "))
v = bank(a, b)
print(v)

a = int(input("Sisesta arv: "))
v = is_prime(a)
print(v)

a = int(input("Sisesta päev: "))
b = int(input("Sisesta kuu: "))
c = int(input("Sisesta aasta: "))
v = date(a,b,c)
print(v)

# a = int(input("Sisesta: "))
# b = int(input("Sisesta: "))
# v = XOR_cipher(a,b)