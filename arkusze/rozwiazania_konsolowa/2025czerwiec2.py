def szyfr_cezara(tekst_jawny, klucz):
    tekst_zaszyfrowany = ''
    for znak in tekst_jawny:
        if znak != ' ':
            numer = ord(znak) - ord('a')
            nowy_numer = (numer + klucz) % 26
            tekst_zaszyfrowany += chr(nowy_numer + ord('a'))
        else:
            tekst_zaszyfrowany += ' '
    print(tekst_zaszyfrowany)
szyfr_cezara("abc xyz", 3)