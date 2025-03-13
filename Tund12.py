import random

sõnad = ['python', 'programmeerimine', 'algoritm', 'arvuti', 'klaviatuur', 'hiir', 'monitor']


randsõna = random.choice(sõnad)
randsõnacount = len(randsõna)


kordus = 6
print(f"Угадайте слово из {randsõnacount} букв. У вас {kordus} попыток.")

for j in range(kordus):
    guess = input(f"Попытка {j + 1}: ").lower()
    
    if len(guess) != randsõnacount:
        print(f"Пожалуйста, введите слово из {randsõnacount} букв.")
        continue
    
    result = []
    for i in range(len(guess)):
        if guess[i] == randsõna[i]:
            # if letter on right place green
        elif guess[i] in randsõna:
            # if letter on wrong place yellow
        else:
            # if no that letter white
    
    
    if guess == randsõna:
        print("Поздравляем! Вы угадали слово!")
        break
else:
    print(f"К сожалению, вы не угадали слово. Загаданное слово было: {randsõna}")