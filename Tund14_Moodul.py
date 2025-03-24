import string
from random import *

def salasona(k: int):
    """
    Genereerib parooli pikkusega k.
    Parool sisaldab tähti, numbreid ja erisümboleid.
    :param int k: Parooli pikkus
    :rtype: str
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
    Registreerib uue kasutaja, kui kasutajanimi pole olemas.
    Kui parool on antud, genereeritakse see automaatselt.
    :param list loginid: Kasutajate nimede lisamine
    :param list paroolid: Kasutajate paroolide lisamine
    :param str kasutajanimi: Uue kasutajanimi lisamine
    :param str parool: Valitud parool
    :rtype: str
    """
    if kasutajanimi in loginid:
        return "Kasutajanimi on juba olemas!"
    if parool is None:
        parool = salasona(12)
    if kasutajanimi == "": return "Tühi kasutajanimi"
    loginid.append(kasutajanimi) # lisamine kasutaja
    paroolid.append(parool) # lisamine parool
    return f"Kasutaja {kasutajanimi} registreeritud! Parool: {parool}"

def autoriseerimine(loginid: list, paroolid: list, kasutajanimi: str, parool: str):
    """
    Autoriseerib kasutaja, kui kasutajanimi ja parool on õiged.
    :param list loginid: Kui kasutajate nime on järjendis
    :param list paroolid: Kui kasutajate parool on järjendis
    :param str kasutajanimi: Valitud kasutajanimi
    :param str parool: Valitud parool
    :rtype: str
    """
    if kasutajanimi in loginid:
        i = loginid.index(kasutajanimi) # Esimene nimi jäjendis
        if paroolid[i] == parool:
            return f"Tere tulemast {kasutajanimi}!"
    return "Vale kasutajanimi või parool!"

def muuda_nimi(loginid: list, vana_nimi: str, uus_nimi: str):
    """
    Muudab kasutaja nime, kui vana nimi on olemas.
    :param list loginid: Kui kasutajate nime on järjendis
    :param str vana_nimi: Vana kasutajanimi
    :param str uus_nimi: Uus kasutajanimi
    :rtype: str
    """
    if vana_nimi in loginid:
        i = loginid.index(vana_nimi)
        loginid[i] = uus_nimi
        return f"Nimi muudetud: {vana_nimi} -> {uus_nimi}"
    return "Kasutajanimi ei leitud!"

def muuda_parool(loginid: list, paroolid: list, kasutajanimi: str, vana_parool: str, uus_parool: str):
    """
    Muudab kasutaja parooli, kui vana parool on õige.
    :param list loginid: Kui kasutajate nime on järjendis
    :param list paroolid: Kui kasutajate parool on järjendis
    :param str kasutajanimi: Valitud kasutajanimi
    :param str vana_parool: Vana parool
    :param str uus_parool: Uus parool
    :rtype: str
    """
    if kasutajanimi in loginid:
        i = loginid.index(kasutajanimi)
        if paroolid[i] == vana_parool:
            paroolid[i] = uus_parool
            return "Parool muudetud!"
    return "Vale kasutajanimi või parool!"

def taasta_parool(loginid: list, paroolid: list, kasutajanimi: str):
    """
    Taastab kasutaja parooli, genereerides uue.
    :param list loginid: Kui kasutajate nime on järjendis
    :param list paroolid: Kui kasutajate parool on järjendis
    :param str kasutajanimi: Valitud kasutajanimi
    :rtype: str
    """
    if kasutajanimi in loginid:
        i = loginid.index(kasutajanimi)
        uus_parool = salasona(12)
        paroolid[i] = uus_parool
        return f"Uus parool: {uus_parool}"
    return "Kasutajanimi ei leitud!"