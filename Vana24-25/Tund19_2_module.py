import json
import random
import smtplib
from email.message import EmailMessage

def viktoriin(nimi, kysimuste_arv):
    with open("Tund19_2_oiged.json", "r") as fail:
        kysimused = json.load(fail)
    skoor = 0
    valitud = random.sample(kysimused, min(len(kysimused), kysimuste_arv)) # kõik, minimaalne arv, kui palju on vaja
    
    for i in valitud: # läbi valitud küsimuste
        kysimus = i["kusimus"]
        oige_vastus = i["vastus"]
        print(f"{nimi}, {kysimus}")
        kasutaja_vastus = input("Sinu vastus: ").strip()
        if kasutaja_vastus.lower() == oige_vastus.lower():
            print("Õige!\n")
            skoor += 1
        else:
            print(f"Vale! Õige vastus on: {oige_vastus}\n")
    
    return skoor, len(valitud)

def send_email(recipient, subject, body):
    sender = "maksimtsitkool@gmail.com"
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    msg.set_content(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender, "zbopiiftjrmmnapp")
    server.send_message(msg)

def salvesta_tulemused(nimi, õiged, kokku, email):
    with open('Tund19_2_log.json', 'r', encoding='utf-8') as f:
        andmed = json.load(f)

    andmed["kõik"].append({
        "nimi": nimi,
        "õiged": õiged,
        "kokku": kokku,
        "email": email
    })

    if õiged > kokku / 2: # kui rohkem kui pool õiged
        andmed["õiged"].append({ # õiged tulemused
            "nimi": nimi,
            "tulemus": f"{õiged}/{kokku}"
        })
    else: # kui vähem kui pool õiged
        andmed["valed"].append({ # valed tulemused
            "nimi": nimi,
            "tulemus": f"{õiged}/{kokku}"
        })
    with open('Tund19_2_log.json', 'w', encoding='utf-8') as f: # salvesta
        json.dump(andmed, f, indent=2, ensure_ascii=False) # ensure_ascii - fix eesti keele tähed

def saada_osalejale(nimi, email, õiged, kokku):
    if õiged > kokku / 2:
        subject = "Testi tulemused - edukas!"
        body = f"Tere {nimi}!\n\nSinu tulemus: {õiged}/{kokku} õigesti.\nOled testi läbi teinud!"
    else:
        subject = "Testi tulemused - pahad!"
        body = f"Tere {nimi}!\n\nSinu tulemus: {õiged}/{kokku} õigesti.\nKahjuks ei läinud test hästi."
    send_email(email, subject, body)

def saada_kokkuvote():
    with open('Tund19_2_log.json', 'r', encoding='utf-8') as f:
        andmed = json.load(f)

    employer_email = "maksimtsitkool@gmail.com"
    subject = "Päeva tulemused"
    body = "Tere!\n\nTänased testi tulemused:\n"
    
    parim = None
    for i, osaleja in enumerate(andmed["kõik"]): # count kõik data
        nimi = osaleja["nimi"]
        õiged = osaleja["õiged"]
        kokku = osaleja["kokku"]
        email = osaleja["email"]
        olek = "SOBIS" if õiged > kokku/2 else "EI SOBINUD"
        
        body += f"{i+1}. {nimi} – {õiged} õigesti – {email} – {olek}\n" # lisa iga osaleja info
        
        if not parim or õiged > parim["õiged"]:
            parim = {"nimi": nimi, "õiged": õiged}
    
    if parim:
        body += f"\nParim tulemus: {parim['nimi']} ({parim['õiged']} õigesti)"
    
    body += "\n\nLugupidamisega,\nTestisüsteem"
    send_email(employer_email, subject, body)

def kuva_edukad():
    with open('Tund19_2_log.json', 'r', encoding='utf-8') as f:
        andmed = json.load(f)

    print("\nEdukalt vastanud osalejad:")
    for osaleja in andmed["õiged"]:
        print(f"{osaleja['nimi']} – {osaleja['tulemus']}")

    print("\nTulemused saadetud e-posti aadressidele.")

def loe_kutsutud_nimed():
    with open('Tund19_2_log.json', 'r', encoding='utf-8') as f:
        andmed = json.load(f)
    return {osaleja["nimi"] for osaleja in andmed["kõik"]} # loe kõik osalejad nimi log failist kus on kõik