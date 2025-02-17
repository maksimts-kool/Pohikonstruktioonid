print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi")

while 1:
    try:
        soov = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if soov == 1:
            while 1:
                try:
                    pikkus = int(input("Sisesta oma pikkus cm: "))
                    break
                except:
                    print("Sisesta numbrid.")
            while 1:
                try:
                    mass = float(input("Sisesta oma kaal kg: "))
                    break
                except:
                    print("Sisesta numbrid.")

            indeks = round(mass / (0.01 * pikkus) ** 2)
            print(f"{nimi}! Sinu keha indeks on: {indeks}")
            if indeks < 16:
                print("Tervisele ohtlik alakaal")
            elif 16 <= indeks < 19:
                print("Alakaal")
            elif 19 <= indeks < 25:
                print("Normaalkaal")
            elif 25 <= indeks < 30:
                print("Ülekaal")
            elif 30 <= indeks < 35:
                print("Rasvumine")
            elif 35 <= indeks < 40:
                print("Tugev rasvumine")
            else:
                print("Tervisele ohtlik rasvumine")
            break
        elif soov == 0:
            print("Kahju! See on väga kasulik info!")
            print(f"\nKohtumiseni, {nimi}! Igavesti Sinu, Python!")
            break
        else:
            print("Vale number")
    except:
        print("Vale soov")