def sito(pierwsze):
    pierwsze[0] = False
    pierwsze[1] = False

    n = len(pierwsze) - 1

    for p in range(2, int(n ** 0.5) + 1):
        if pierwsze[p]:
            for i in range(p * p, n + 1, p):
                pierwsze[i] = False


n = 100
pierwsze = [True] * (n + 1)

sito(pierwsze)

print("Liczby pierwsze w zakresie od 2 do 100:")

for i in range(2, n + 1):
    if pierwsze[i]:
        print(i, end=", ")