from math import *

def arithmetic(arv1:float, arv2:float, tehe:str)->any:
    """Lihtne kalkulaator
    + Liitimine
    - Lahutamine
    * Korrutamine
    / Jagamine
    :param float arv1: Sisend kasutajalt
    :param float arv2: Sisend kasutajalt
    :param str tehe: Aritmeetiline tehe, mis valib kasutaja
    :rtype: Määrata tüüp (float või str)"""

    if tehe in ['+','-','*','/']:
        if arv2 == 0 and tehe == '/':
            vastus = "DIV/0"
        else:
            vastus = eval(str(arv1) + tehe + str(arv2))
    else:
        vastus = "Tundmatu tehe"
    return vastus

def is_year_leap(year:int)->bool:
    """Kontrollib, kas aasta on liigaasta
    :param int year: Aasta number
    :rtype: bool
    """
    if year % 4 == 0:
        return True
    else:
        return False

def square(külg:float)->list:
    """Arvutab ruudu ümbermõõdu, pindala ja diagonaali
    :param float külg: Ruudu külje pikkus
    :rtype: list
    """
    P = 4 * külg
    S = külg ** 2
    C = külg * sqrt(2)
    return [P, S, round(C,2)]

def season(kuu:int)->str:
    """Tagastab aastaaja vastavalt kuu numbrile
    :param int kuu: Kuu number (1-12)
    :rtype: str
    """
    if kuu in [12,1,2]:
        return "Talv"
    elif kuu in [3,4,5]:
        return "Kevad"
    elif kuu in [6,7,8]:
        return "Suvi"
    elif kuu in [9,10,11]:
        return "Sügis"
    else:
        return "Tundmatu kuu"

def bank(aeur:float, years:int)->float:
    """Arvutab hoiuse summa pärast antud aastate arvu
    :param float aeur: Algne summa
    :param int years: Aastate arv
    :rtype: float
    """
    for i in range(years):
        aeur = aeur * 1.10
    return round(aeur,2)

def is_prime(n:int)->bool:
    """Kontrollib, kas arv on algarv
    :param int n: Arv, mida kontrollitakse
    :rtype: bool
    """
    if n < 0 or n > 1000:
        pass
    else:
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def date(day:int, month:int, year:int):
    """Kontrollib, kas kuupäev on korrektne
    :param int day: Päev
    :param int month: Kuu
    :param int year: Aasta
    :rtype: bool
    """
    if month in [1,3,5,7,8,10,12]:
        if day > 31:
            return False
    elif month in [4,6,9,11]:
        if day > 30:
            return False
    elif month == 2:
        if is_year_leap(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    else:
        return False
    return True

# def XOR_cipher(text:str, key:str)->str: