from IseToo2_Moodul import *

sportlased = []

print("Введите имена спортсменов (для завершения нажмите Enter):")
while True:
    nimi = input("Имя спортсмена: ")
    if nimi == '':
        break
    sportlased.append(nimi)
    
tulemused = loo_tulemused(len(sportlased))
print("\nСписки успешно заполнены!")
    
while True:
    print("\nМеню:")
    print("1. Узнать n лучших результатов")
    print("2. Упорядочить список по возрастанию баллов")
    print("3. Найти результат спортсмена(ов)")
    print("4. Дисквалифицировать спортсменов с плохими результатами")
    # print("5. Показать средний результат всех спортсменов")
    print("6. Выход")
        
    valik = int(input("Выберите действие (1-6): "))

    if valik == 1:
        n = int(input("Введите количество лучших результатов: "))
        top_results = top_n(tulemused, n)
        print(f"{n} лучших результатов: {top_results}")

    elif valik == 2:
        sorteds, sortedt = sortsportlased(sportlased, tulemused)
        # zip - [1],['q'] -> [(1, 'q'), ...]
        for athlete, result in zip(sorteds, sortedt): 
            print(f"{athlete}: {result} punkti")

    elif valik == 3:
        nimi = input("Введите имена спортсменов через запятую: ").split(", ") # str to list with ', '
        sportlased_tulemused = sportlasedtulemused(sportlased, tulemused, nimi)
        for nimi, result in sportlased_tulemused:
            print(f"{nimi}: {result}")

    elif valik == 4:
        limit = int(input("Введите порог дисквалификации: "))
        sportlased, tulemused = disqualify(sportlased, tulemused, limit)
        print("Оставшиеся спортсмены и их результаты:")
        for athlete, result in zip(sportlased, tulemused):
            print(f"{athlete}: {result}")

    elif valik == 5:
        # print("Ваш вариант действий.")
        pass

    elif valik == 0:
        break

    else:
        print("Неверный выбор. Попробуйте снова.")