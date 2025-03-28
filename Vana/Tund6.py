print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage täisarv => "))) # Sulgude puudumine
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Ei ole mõtet teha midagi nulliga.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame, mitu paarilist ja mitu paaritut numbrit on numbris.")
    print()
    c=b=a # igal on üks võrdse
    paaris = 0 # üks võrdse
    paaritu = 0 # üks võrdse
    while b > 0: # Peab olema :
        if b % 2 == 0: # kaks võrdset
            paaris += 1 # Vale =+ 
        else:
            paaritu += 1 # Vale =+ 
        b = b // 10 # проверка посследнего, среднего и первого - 164. 4, 6, 1
    
    print(f"Paarilised numbrid: {paaris}") # format
    print(f"Paaritu arvud: {paaritu}") # format
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Sisestatud numbri *ümberpööramine*")
    print()
    b=0
    while a > 0: # Peab olema :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # Vale =+ 
    print("*Ümberpöördatud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse'i hüpoteesi testimine.")
    print()
    while c != 1:
        if c % 2 == 0: # kaks võrdset
            print(f"{round(c)} - paariline arv. Jagage 2ga.", end="\n") # end uus rida ja format
            c = c / 2 # üks võrdse
        else:
            print(f"{round(c)} - paaritu arv. Korrutame 3, lisame 1 ja jagame 2ga.", end="\n") # end uus rida ja format  
            c = (3*c + 1) / 2 # üks võrdse
    print("1 - Hüpotees on õige")