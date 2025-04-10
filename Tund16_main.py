from Tund16_sonastik import *

valjasta_tervitus()
sonad = loo_sonastik()

while True:
    kuva_menuu()
    valik = int(kysi_kasutajalt_sisestus("Vali number: "))
    
    if valik == 1:
        start, end = vali_keelte_suund()
        sona = kysi_kasutajalt_sisestus(f"Sisesta sõna ({start}): ")
        otsi = otsi_sona(sonad, start, end, sona)
        print(f"Tõlge ({end}): {otsi}")
    elif valik == 2:
        lisa_sona(sonad)
    elif valik == 3:
        paranda_sona(sonad)
    elif valik == 4:
        kuva_sonad(sonad)
    elif valik == 5:
        testi_teadmisi(sonad)
    elif valik == 6:
        kustuta_sona(sonad)
    elif valik == 7:
        break
    else:
        print("Vale valik! Proovi uuesti.")