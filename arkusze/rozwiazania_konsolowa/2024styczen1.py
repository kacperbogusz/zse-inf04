def sprawdz_plec(pesel):
    if int(pesel[9]) % 2 == 0:
        return 'K'
    else:
        return 'M'

def sprawdz_sume(pesel):
    sumy = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S = 0
    for i in range(10):
        iloczyn = int(pesel[i]) * sumy[i]
        S += iloczyn
        iloczyn = 0

    M = S % 10

    if M == 0:
        R = 0
    else:
        R = 10 - M

    if int(pesel[10]) == R:
        return True
    else:
        return False

pesel_uzytkownika = input("Podaj numer PESEL: ")

plec = sprawdz_plec(pesel_uzytkownika)
if plec == 'K':
    print("Kobieta")
elif plec == 'M':
    print("Mężczyzna")

suma = sprawdz_sume(pesel_uzytkownika)
if suma:
    print("Suma kontrolna jest zgodna")
elif not suma:
    print("Suma kontrolna nie jest zgodna")