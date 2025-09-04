import random

def loo_tulemused(pikkus:int)->list:
    tulemused = []
    for _ in range(pikkus):
        t1 = random.randint(1, 100)
        t2 = random.randint(1, 100)
        t3 = random.randint(1, 100)
        parim = max(t1, t2, t3)
        tulemused.append(parim)
    return tulemused

def top_n(results:list, n:int)->list:
    tulemused_copy = list(results)
    top_results = []
    for _ in range(n):
        max_result = max(tulemused_copy)
        top_results.append(max_result)
        tulemused_copy.remove(max_result)
    return top_results

def sortsportlased(athletes:list, results:list)->list:
    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            if results[i] > results[j]:
                results[i], results[j] = results[j], results[i]
                athletes[i], athletes[j] = athletes[j], athletes[i]
    return athletes, results

def sportlasedtulemused(athletes:list, results:list, nimi:list)->list:
    sportlased_results = []
    for ni in nimi:
        if ni in athletes:
            i = athletes.index(ni)
            sportlased_results.append((ni, results[i]))
    return sportlased_results

def disqualify(athletes:list, results:list, limit:int)->list:
    qualified_athletes = []
    qualified_results = []
    for i in range(len(athletes)):
        if results[i] >= limit:
            qualified_athletes.append(athletes[i])
            qualified_results.append(results[i])
    return qualified_athletes, qualified_results