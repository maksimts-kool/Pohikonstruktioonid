import string
from random import *

def salasona(k: int):
    """
    Genereerib juhusliku parooli pikkusega k.
    Parool sisaldab nii tähti kui numbreid ja kirjavahemärke.
    """
    sala = ""
    for i in range(k):
        taht = choice(string.ascii_letters)  # Aa...Zz
        num = choice(string.digits)       # 0-9
        erisymbol = choice(string.punctuation)  # !@#$%^&*()_+
        valik = [taht, num, erisymbol] # koos
        sala += choice(valik) # from koos valitakse üks!
    return sala

def registreerimine(loginid: list, paroolid: list, kasutajanimi: str, parool: str = None):
    """
    Registreerib uue kasutaja, kui kasutajanimi pole juba olemas.
    Kui parool pole ette antud, genereeritakse see automaatselt.
    """
    if kasutajanimi in loginid:
        return "Kasutajanimi on juba olemas!"
    if parool is None:
        parool = salasona(12)
    loginid.append(kasutajanimi) # lisamine kasutaja
    paroolid.append(parool) # lisamine parool
    return f"Kasutaja {kasutajanimi} registreeritud! Parool: {parool}"

def autoriseerimine(loginid: list, paroolid: list, kasutajanimi: str, parool: str):
    """
    Autoriseerib kasutaja, kui kasutajanimi ja parool on õiged.
    """
    if kasutajanimi in loginid:
        index = loginid.index(kasutajanimi)
        if paroolid[index] == parool:
            return f"Tere tulemast {kasutajanimi}!"
    return "Vale kasutajanimi või parool!"

'''
def muuda_parool(loginid: list, paroolid: list, kasutajanimi: str, vana_parool: str, uus_parool: str):
    """
    Muudab kasutaja parooli, kui vana parool on õige.
    """
    if kasutajanimi in loginid:
        index = loginid.index(kasutajanimi)
        if paroolid[index] == vana_parool:
            paroolid[index] = uus_parool
            return "Parool muudetud!"
    return "Vale kasutajanimi või parool!"

def taasta_parool(loginid: list, paroolid: list, kasutajanimi: str):
    """
    Taastab kasutaja parooli, genereerides uue.
    """
    if kasutajanimi in loginid:
        index = loginid.index(kasutajanimi)
        uus_parool = salasona(8)
        paroolid[index] = uus_parool
        return f"Uus parool: {uus_parool}"
    return "Kasutajanimi ei leitud!"

'''