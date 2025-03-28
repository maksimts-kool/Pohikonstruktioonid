print("Hello world","2")
# separator, end

# andmetüübid 
# täisarv - int, ujukomaarv - float, sõne - str, tõeväärtused - bool
# astendamine **
a = 5
aste = 2
tulemus = a ** aste
print(a,"**",aste,"=",tulemus)
# Korrutamine *
arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Teine korrutaja: "))
tulemus = arv1 * arv2
print(arv1,"*",arv2,"=",tulemus)
# Jagamine / 
arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Jagaja: "))
tulemus = arv1 / arv2
print(arv1,"/",arv2,"=",tulemus)
# Liitmine +
arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Teine korrutaja: "))
tulemus = arv1 + arv2
print(arv1,"+",arv2,"=",tulemus)
# Lahutamine -
arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Teine korrutaja: "))
tulemus = arv1 - arv2
print(arv1,"-",arv2,"=",tulemus)
# jagamise täisarvulise osa leidmine //
arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Teine korrutaja: "))
tulemus = arv1 // arv2
print(arv1,"//",arv2,"=",tulemus)

# upper() - all UPPERCASE
# lower() - all lowercase
# capitalize() - first is Uppercase
# date.today() - current date
# date(y,m,d) - current date

# strftime() - format date
# # 27/12/2022
# tana = tanao.strftime("%d/%m/%Y")
# # December 27, 2022
# tana = tanao.strftime("%B %d, %Y")
# # 12/27/22
# tana = tanao.strftime("%m/%d/%y")
# # Dec-27-2022
# tana = tanao.strftime("%b-%d-%Y")

# day, month, year
# monthrange(a, b)[b] - kuu päevade arv
# round(arv, punktid) - ümardamine

# isalnum()
# isalpha()
# isascii()
# isdecimal()
# isdigit()
# isidentifier()
# islower()
# isnumeric()
# isprintable()
# isspace()
# istitle()
# isupper()