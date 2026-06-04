import random

def sortowanie_babelkowe(tablica):
    n = len(tablica)
    for i in range(n - 1):
        zamieniono = False
        for j in range(n - 1 - i):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                zamieniono = True
        if not zamieniono:
            break

def czy_posortowana(tablica):
    for i in range(len(tablica) - 1):
        if tablica[i] > tablica[i+1]:
            return False
    return True


liczby = [random.randint(1, 1000) for _ in range(100)]
print("Liczby przed sortowaniem:")
print(liczby)

sortowanie_babelkowe(liczby)
print("\nLiczby po sortowaniu:")
print(liczby)

print("\nTest:")
if czy_posortowana(liczby):
    print("Test poprawny - tablica została posortowana rosnąco")
else:
    print("Test niepoprawny - tablica nie została po")
