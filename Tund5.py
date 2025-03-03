import random

print("Vali raskusaste:")
print("1 - Tase 1 (lihtne)")
print("2 - Tase 2 (keskmine)")
print("3 - Tase 3 (raske)")
while True:
    try:
        level = int(input("Sisesta raskusaste: "))
        if level in [1, 2, 3]: # level == 1 or level == 2 or level == 3
            break
        else:
            print("Palun sisesta AINULT 1, 2 või 3.")
    except:
        print("Palun sisesta number.")

while True:
    try:
        num_questions = int(input("Mitu küsimust soovid lahendada? "))
        if 0 < num_questions <= 50: 
            break
        else:
            print("Liiga palju või negatiivne")
    except:
        print("Palun sisesta number.")

correct_answers = 0

for _ in range(num_questions):
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
    elif level == 2:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*', '/'])
    elif level == 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*', '/', '**'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = round(num1 / num2, 2)
    elif operation == '**':
        answer = num1 ** num2

    print(f"{num1} {operation} {num2} = ?")

    while True:
        try:
            user_answer = float(input("Sinu vastus: "))
            if user_answer == answer:
                print("Õige!")
                correct_answers += 1
            else:
                print(f"Vale! Õige vastus on {answer}.")
            break
        except:
            print("Palun sisesta number.")

percentage = round((correct_answers / num_questions) * 100)
print(f"Sinu tulemus: {correct_answers} õiget vastust {num_questions} küsimusest ({percentage}%).")

if percentage < 60:
    print("Hinne 2")
elif 60 <= percentage < 75:
    print("Hinne 3")
elif 75 <= percentage < 90:
    print("Hinne 4")
else:
    print("Hinne 5")