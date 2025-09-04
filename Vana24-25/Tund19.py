import json
import requests

andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

# with open("Tund19.json", "w") as f:
#     json.dump(andmed, f, indent=2)

with open("Tund19.json", "r") as f:
    andmed_failist = json.load(f)
print(andmed_failist)

klass = {
    "opetaja": "Tamm",
    "opilased": 
    [
        {"nimi": "Mari", "hinne": 5},
        {"nimi": "Jüri", "hinne": 4}
    ] 
}
with open("Tund19_klass.json", "w", encoding="utf-8-sig") as f:
    json.dump(klass, f, indent=2)

linn = input("Sisesta linna nimi: ")
api_voti = ""  # asenda oma API võtmega
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    
    print(f"\nIlm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}°C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud. Palun kontrolli nime õigekirja.")
with open("Tund19_ilm.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)

nimi = input("Sisesta oma nimi: ")
if andmed_failist.get("nimi") == nimi:
    print(f"Tere, {nimi}!")
    for auto in andmed_failist.get("autod", []):
        print(f"Auto mudel: {auto['mark']}, värv: {auto['varv']}, jõud: {auto['joud']}, number: {auto['number']}")
else:
    print("Selle nimega andmeid ei leitud.")

