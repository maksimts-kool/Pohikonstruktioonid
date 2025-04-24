from Tund19_2_module import *

print("\nTere tulemast küsimustikku!\n")

kysimuste_arv = 5
osalejate_arv = 3
kutsutud_nimed = loe_kutsutud_nimed()

while True:
    print("\nMenüü:")
    print("1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")
    valik = int(input("Vali tegevus (1-3): "))
    if valik == 1:
        for i in range(osalejate_arv):
            while True:
                nimi = input(f"Palun sisesta {i+1}. osaleja nimi: ").strip()
                email = input(f"Palun sisesta {i+1}. osaleja email: ").strip()
                if nimi not in kutsutud_nimed:
                    break
                else:
                    print(f"{nimi} on juba testi teinud.")
            
            print(f"\n{nimi}, sa vastad {kysimuste_arv}  küsimusele.\n")
            skoor, kokku = viktoriin(nimi, kysimuste_arv)

            if skoor > kokku / 2:
                print(f"Sa lähed läbi, {nimi}! Sinu skoor on {skoor}/{kokku}.\n")
            else:
                print(f"Kahjuks, Sa ei lähed läbi, {nimi}. Sinu skoor on {skoor}/{kokku}.\n")
            salvesta_tulemused(nimi, skoor, kokku, email)
            saada_osalejale(nimi, email, skoor, kokku)
        kuva_edukad()
        saada_kokkuvote()
        print("Kõik osalejad on nüüd küsimustiku läbi teinud!")
    elif valik == 2:
        kysimus = input("Sisesta uus küsimus: ")
        vastus = input("Sisesta õige vastus: ")
        with open("Tund19_2_oiged.json", "r", encoding="utf-8") as fail:
            kysimused = json.load(fail)
        kysimused.append({
            "kusimus": kysimus,
            "vastus": vastus
        })
        with open("Tund19_2_oiged.json", "w", encoding="utf-8") as fail:
            json.dump(kysimused, fail, indent=2, ensure_ascii=False)
        
        print("Küsimus lisatud!")
    elif valik == 3:
        break

# {
#     "kõik": [],
#     "õiged": [],
#     "valed": []
# }