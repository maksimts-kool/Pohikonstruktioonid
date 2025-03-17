import random
import colorama
colorama.just_fix_windows_console()

sõnad = ['python', 'programmeerimine', 'algoritm', 'arvuti', 'klaviatuur', 'hiir', 'monitor']

randsõna = random.choice(sõnad)
randsõnacount = len(randsõna)

GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[0m'

kordus = 6
print(f"Arvake sõna {randsõnacount} tähtedest. Teil on {kordus} proovid.")

for j in range(kordus):
    while True:
        guess = input(f"Proov {j + 1}: ").lower()
        
        if len(guess) == randsõnacount:
            break
        else:
            print(f"Palun sisestage {randsõnacount} tähega sõna.")
    
    colored_guess = []
    yellowletter = []
    
    # Rohelised
    for i in range(randsõnacount):
        if guess[i] == randsõna[i]:
            colored_guess.append(f"{GREEN}{guess[i]}{WHITE}")
        else:
            colored_guess.append(None)
            yellowletter.append(randsõna[i])
    
    # Kollased ja Valged
    for i in range(randsõnacount):
        if colored_guess[i] == None:
            if guess[i] in yellowletter:
                colored_guess[i] = f"{YELLOW}{guess[i]}{WHITE}"
                yellowletter.remove(guess[i])
            else:
                colored_guess[i] = f"{WHITE}{guess[i]}{WHITE}"
    
    # List > Sõne
    print("".join(colored_guess))
    
    if guess == randsõna:
        print("Palju õnne! Sa arvasid sõna ära!")
        break
else:
    print(f"Te ei arvanud sõna ära. Õige sõna oli: {randsõna}")