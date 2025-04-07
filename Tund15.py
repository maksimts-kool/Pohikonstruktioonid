from Tund15_Moodul import *

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

while True:
    print('\nAndmed:')
    for nimi, palk in zip(inimesed, palgad):
        print(f"{nimi} - {palk}")
    print('\nVali funktioon:')
    print(
'''1 - Lisa mitu inimest ja nende palgad
2 - Isiku ja tema palga kustutada
3 - Leia kes saab kätte suurim palk
4 - Leia kes saab kätte kõige väiksem palk ja milline ta on
5 - Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega
6 - Leia inimesed, kes saavad sama palga
7 - Otsi palga järgi nime
8 - Nimekiri inimestest, kes saavad rohkem/vähem kui määratud summa
9 - Otsi T vaeseimad ja rikkamad inimesed
10 - Otsi Keskmine palk ja selle saajad
0 - Välju''')
    v = int(input('Sisesta arv: '))
    if v == 1:
        LisaIjaP(palgad, inimesed)
    elif v == 2:
        KustutaI(palgad, inimesed)
    elif v == 3:
        SuurimP(palgad, inimesed)
    elif v == 4:
        VaikseimP(palgad, inimesed)
    elif v == 5:
        SorteeriP(palgad, inimesed)
    elif v == 6:
        VordsedP(palgad, inimesed)
    elif v == 7:
        OtsiP(palgad, inimesed)
    elif v == 8:
        FilterP(palgad, inimesed)
    elif v == 9:
        TopI(palgad, inimesed)
    elif v == 10:
        KeskmineP(palgad, inimesed)
    elif v == 0:
        break