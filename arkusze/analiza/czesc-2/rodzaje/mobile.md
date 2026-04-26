# Analiza funkcjonalnosci - aplikacje mobilne

> [!NOTE]
> Ten plik zbiera tylko **funkcjonalnosci**, ktore pojawialy sie w zadaniach mobilnych z Czesci II. Bez dokumentacji, bez rozbijania na jezyki. Poniewaz chcesz robic mobile w **.NET MAUI**, potraktuj to jako liste mechanik, ktore trzeba umiec zrobic w MAUI na telefonie.

---

## Zakres

W arkuszach z lat 2021-2026 pojawilo sie **9 zadan mobilnych**:

1. `2021 - Czerwiec 1` - rejestracja konta
2. `2022 - Styczen 1` - rejestracja konta
3. `2022 - Czerwiec 1` - oferta turystyczna i licznik polubien
4. `2023 - Styczen 2` - notatki
5. `2023 - Czerwiec 2` - ustawienia czcionki
6. `2024 - Styczen 2` - wizyta u weterynarza
7. `2024 - Czerwiec 1` - gra w kosci, wynik rzutu i wynik gry
8. `2025 - Styczen 2` - urzadzenia domowe
9. `2026 - Styczen 1` - gra w kosci, blokowanie kosci

---

## Co wraca najczesciej

### 1. Prosty uklad, ale spiety logika

Mobilne zadania zwykle wygladaja niepozornie:

- kilka etykiet
- jedno lub kilka pol
- przycisk
- obraz albo lista

Ale punktowane jest to, co dzieje sie po interakcji:

- zmiana tekstu
- zmiana obrazu
- zmiana licznika
- zmiana stanu przycisku
- aktualizacja kolekcji

### 2. Jeden ekran, jeden glowny przeplyw

W prawie wszystkich zadaniach jest jeden glowny ekran i jeden glowny scenariusz:

- wypelnij formularz i zatwierdz
- kliknij i zwieksz licznik
- dodaj element do listy
- przesun suwak i zobacz efekt
- nacisnij `RZUC` i zaktualizuj gre

To oznacza, ze trzeba dobrze umiec modelowac stan strony.

### 3. Bardzo czeste operacje na etykietach i obrazach

Powtarza sie:

- wpisanie komunikatu po walidacji
- aktualizacja napisu z licznikiem
- aktualizacja wieku przy suwaku
- zmiana podpisu przycisku
- zmiana obrazow kosci
- zmiana przezroczystosci obrazow

Czyli MAUI `Label`, `Image` i `Button` musza byc opanowane bardzo dobrze.

### 4. Stan aplikacji jest kluczowy

W mobilnych zadaniach bardzo czesto trzeba przechowywac:

- aktualny komunikat
- licznik polubien
- kolekcje notatek
- indeks aktualnego cytatu
- wiek zwierzecia
- wynik biezacego rzutu
- wynik gry
- stan odkurzacza
- dostepnosc konkretnej kosci

### 5. Od 2024 rosnie rola logiki z Czesci I

To szczegolnie wazne dla MAUI:

- `2024 - Czerwiec 1` - gra w kosci korzysta z logiki wyniku
- `2025 - Styczen 2` - zadanie naturalnie nawiazuje do klas urzadzen
- `2026 - Styczen 1` - mozna wykorzystac klase `Kosc`

Wniosek: warto oddzielac logike od widoku, a nie pisac wszystkiego w handlerze przycisku.

---

## Funkcjonalnosci per arkusz

### 2021 - Czerwiec 1 i 2022 - Styczen 1 - rejestracja

Trzeba bylo zrobic:

- pole e-mail
- dwa pola hasla z ukrywaniem znakow
- przycisk `ZATWIERDZ`
- obszar komunikatu
- startowy tekst `Autor ...`
- walidacje znaku `@`
- walidacje zgodnosci hasel

Umiejetnosci funkcjonalne:

- pobranie tekstu z `Entry`
- porownanie napisow
- warunki `if/else`
- ustawienie komunikatu zalezne od wyniku

### 2022 - Czerwiec 1 - oferta i polubienia

Trzeba bylo zrobic:

- wyswietlenie obrazu oferty
- trzy przyciski
- licznik polubien
- inkrementacje i dekrementacje licznika
- blokade zejscia ponizej zera

Umiejetnosci funkcjonalne:

- stan liczbowy
- kilka zdarzen `Clicked`
- aktualizacja jednego napisu przez kilka akcji

### 2023 - Styczen 2 - notatki

Trzeba bylo zrobic:

- pole do wpisania nowego elementu
- przycisk `DODAJ`
- liste notatek
- startowe dane z `dane.txt`
- dopisywanie nowego elementu na koniec

Umiejetnosci funkcjonalne:

- kolekcja tekstow
- podpiecie kolekcji pod widok listy
- dodawanie elementu do kolekcji
- automatyczne odswiezanie widoku

### 2023 - Czerwiec 2 - czcionka

Trzeba bylo zrobic:

- suwak rozmiaru
- napis pokazujacy wartosc
- napis cytatu
- przycisk przechodzacy po kolejnych tekstach

Umiejetnosci funkcjonalne:

- `Slider.ValueChanged`
- rzutowanie wartosci na liczbe calkowita
- zmiana `FontSize`
- cykliczne przechodzenie po tablicy napisow

### 2024 - Styczen 2 - weterynarz

Trzeba bylo zrobic:

- formularz z wlascicielem, gatunkiem, wiekiem, celem wizyty i czasem
- liste wyboru gatunku
- suwak wieku
- zmiane maksimum suwaka po wybraniu gatunku
- zmiane widocznej wartosci wieku
- pokazanie podsumowania danych po kliknieciu `OK`

Umiejetnosci funkcjonalne:

- reakcja na zmiane wybranego elementu listy
- dynamiczna zmiana limitu kontrolki
- skladanie tekstu z kilku pol

### 2024 - Czerwiec 1 - kosci, wynik rzutu, wynik gry

Trzeba bylo zrobic:

- piec obrazow kosci
- przycisk `RZUC KOSCMI`
- przycisk `RESETUJ WYNIK`
- wynik jednego rzutu
- wynik calej gry
- losowanie pieciu wartosci 1..6
- zmapowanie wyniku na konkretne obrazki
- wyzerowanie wszystkiego po resecie

Umiejetnosci funkcjonalne:

- lista obrazow
- lista wylosowanych wartosci
- obliczanie wyniku
- stan narastajacy

### 2025 - Styczen 2 - urzadzenia domowe

Trzeba bylo zrobic:

- sekcje pralki i odkurzacza
- pole liczbowe dla programu prania
- przycisk `Zatwierdz`
- przejscie napisu `Numer prania: nie podano` -> `Numer prania: X`
- przycisk `Wlacz/Wylacz`
- zmiane opisu stanu odkurzacza

Umiejetnosci funkcjonalne:

- walidacja zakresu liczby
- prosty bool jako stan urzadzenia
- aktualizacja przycisku i napisu z tego samego stanu

### 2026 - Styczen 1 - kosci z blokowaniem

Trzeba bylo zrobic:

- piec obrazow kosci
- przycisk `RZUT`
- pole z suma oczek
- losowanie tylko dla dostepnych kosci
- klikniecie na obraz kosci
- blokowanie/odblokowanie kosci
- zmiane przezroczystosci obrazu

Umiejetnosci funkcjonalne:

- lista obiektow `Kosc`
- stan `dostepna/niedostepna`
- osobna obsluga klikniecia obrazka
- pomijanie zablokowanych elementow przy kolejnym rzucie

---

## Najwazniejsze mechaniki mobilne

### Formularze

Powtarza sie:

- pobieranie tekstu z pol
- podstawowa walidacja
- pokazywanie komunikatu po przycisku
- skladanie jednego podsumowania z kilku wartosci

### Liczniki i stan

Powtarza sie:

- licznik polubien
- wynik rzutu
- wynik gry
- aktualny indeks cytatu
- aktualna liczba notatek
- stan przycisku `Wlacz/Wylacz`

### Listy i kolekcje

Powtarza sie:

- lista notatek
- lista gatunkow
- lista/zbior kosci
- tablica napisow dla cytatow

### Obrazy

Powtarza sie:

- wyswietlenie obrazka z assets
- podmiana obrazka na podstawie stanu
- wiele obrazow obok siebie
- klikany obraz jako kontrolka interakcyjna

### Dynamiczne UI

Powtarza sie:

- zmiana tekstu po kliknieciu
- zmiana rozmiaru czcionki po suwaku
- zmiana maksimum suwaka po wyborze gatunku
- zmiana podpisu przycisku
- zmiana przezroczystosci obrazu

---

## Jak to przeklada sie na MAUI Mobile

W MAUI warto miec opanowane:

- `VerticalStackLayout`, `HorizontalStackLayout`, `Grid`
- `Entry`
- `Button`
- `Label`
- `Image`
- `Slider`
- `CollectionView` lub `ListView`
- `Picker`
- `TimePicker`
- `TapGestureRecognizer` dla obrazow

Najczestsze rzeczy do zrobienia w kodzie:

- odczytac wartosc z kontrolki
- zaktualizowac tekst etykiety
- zmienic `Image.Source`
- zmienic `Opacity`
- zmienic `Maximum` suwaka
- dodac element do kolekcji
- przeliczyc wynik i zapisac go w stanie

---

## Co warto umiec przed egzaminem

Najbardziej oplaca sie przepracowac:

1. formularz z walidacja i komunikatem
2. licznik z przyciskami `+/-`
3. `CollectionView` z dodawaniem elementow
4. `Slider` zmieniajacy wartosc i wyglad
5. ekran z obrazami zmienianymi w runtime
6. prosty panel urzadzenia ze stanem `on/off`
7. gre z lista obiektow i logika ruchu / rzutu

> [!IMPORTANT]
> Mobilne zadania w MAUI sa mocno "event-driven": jedna akcja uzytkownika zmienia od razu kilka rzeczy na ekranie. Jesli dobrze ogarniesz stan strony, obrazy, listy i dynamiczna aktualizacje etykiet, to pokryjesz wiekszosc zadan mobilnych.
