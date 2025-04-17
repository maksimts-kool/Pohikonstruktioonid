import string
from random import *
import smtplib
from email.message import EmailMessage
import ssl

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

def send_email(to_address, subject, content):
    """
    Sends an email to the specified address with the given subject and content.
    :param str to_address: Recipient's email address
    :param str subject: Email subject
    :param str content: Email content
    """
    sender_email = "maksimtsitkool@gmail.com"
    sender_password = input("Sisesta app password: ")  # Replace with your email's app-specific password

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = to_address
    message['Subject'] = subject
    message.set_content(content)

    # Secure connection to SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        server.send_message(message)

def registreerimine(loginid: list, paroolid: list, kasutajanimi: str, email: str, parool: str = None):
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

    subject = "Kasutaja registreerimine õnnestus"
    content = f"Tere {kasutajanimi},\n\nTeie konto on registreeritud!\nTeie parool on: {parool}\n\nParimate soovidega,\nMinu sait"
    send_email(email, subject, content)

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

def muuda_nimi(loginid: list, vana_nimi: str, uus_nimi: str, email: str):
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
        subject = "Nime muutmine õnnestus"
        content = f"Tere {vana_nimi},\n\nTeie nimi on muudetud.\nTeie uus nimi on: {uus_nimi}\n\nParimate soovidega,\nMinu sait"
        send_email(email, subject, content)
        return f"Nimi muudetud: {vana_nimi} -> {uus_nimi}"
    return "Kasutajanimi ei leitud!"

def muuda_parool(loginid: list, paroolid: list, kasutajanimi: str, vana_parool: str, uus_parool: str, email: str):
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
            subject = "Parooli muutmine õnnestus"
            content = f"Tere {kasutajanimi},\n\nTeie parool on muudetud.\nTeie parool on: {uus_parool}\n\nParimate soovidega,\nMinu sait"
            send_email(email, subject, content)
            return "Parool muudetud!"
    return "Vale kasutajanimi või parool!"

def taasta_parool(loginid: list, paroolid: list, kasutajanimi: str, email: str):
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
        subject = "Paaroli taastmine õnnestus"
        content = f"Tere {kasutajanimi},\n\nTeie parool on taastetud.\nTeie uus parool on: {uus_parool}\n\nParimate soovidega,\nMinu sait"
        send_email(email, subject, content)
        return f"Uus parool: {uus_parool}"
    return "Kasutajanimi ei leitud!"