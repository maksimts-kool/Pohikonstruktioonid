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
    if year % 4 == 0:
        return True
    else:
        return False

def square(külg:float)->list:
    P = 4 * külg
    S = külg ** 2
    C = külg * sqrt(2)
    return [P, S, round(C,2)]