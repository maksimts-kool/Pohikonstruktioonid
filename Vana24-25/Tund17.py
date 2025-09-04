def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

list_ = Loe_failist("Tund17_Tekst.txt")
for i in list_:
    print(i)

list_ = ["Ann", "Kati", "Mari"]
Kirjuta_failisse("Tund17_Tekst.txt", list_)

list_2 = Loe_failist("Tund17_Tekst.txt")
print(list_2)

with open("Tund17_Tekst.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())