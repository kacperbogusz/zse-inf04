# Analiza funkcjonalnosci - aplikacje desktopowe

> [!NOTE]
> Ten plik zbiera tylko **funkcjonalnosci**, ktore pojawialy sie w zadaniach desktopowych z Czesci II. Bez dokumentacji, bez rozpisywania pod konkretny jezyk. Poniewaz chcesz robic desktop w **.NET MAUI**, traktuj to jako liste rzeczy, ktore trzeba umiec odwzorowac w oknie/stronie desktopowej MAUI.

---

## Zakres

W arkuszach z lat 2021-2026 pojawilo sie **6 zadan desktopowych**:

1. `2023 - Styczen 1` - dodawanie pracownika i generator hasla
2. `2023 - Czerwiec 1` - nadawanie przesylki
3. `2024 - Styczen 1` - dane paszportowe
4. `2024 - Czerwiec 2` - `MojeDzwieki`, przegladarka albumow
5. `2025 - Czerwiec 1` - wzornik kolorow RGB
6. `2025 - Czerwiec 2` - szyfr Cezara z zapisem do pliku

---

## Co wraca najczesciej

### 1. Formularze z kilkoma typami kontrolek

Najczesciej trzeba bylo polaczyc kilka rodzajow wejsc:

- pola tekstowe
- przyciski
- radio buttony
- checkboxy
- liste rozwijana
- suwaki
- etykiety z wynikiem

To nie sa duze aplikacje, ale prawie zawsze jest kilka kontrolek naraz i trzeba je ze soba spiac logika.

### 2. Jeden lub dwa glowne przyciski akcji

Desktopowe zadania prawie zawsze maja wyrazny przycisk, ktory uruchamia cala logike:

- `Generuj haslo`
- `Sprawdz cene`
- `OK`
- `Pobierz`
- `Zaszyfruj`
- `Zapisz szyfr w pliku`

W praktyce trzeba umiec dobrze obslugiwac `Click` i po nim:

- odczytac dane z kontrolek
- przeliczyc wynik
- zaktualizowac UI
- czasem pokazac komunikat

### 3. Aktualizacja widoku po zmianie stanu

To bardzo charakterystyczne dla desktopu:

- zmiana napisu ceny
- zmiana obrazka
- zmiana danych aktualnego albumu
- zmiana koloru prostokata
- zmiana zapisanej wartosci RGB
- pokazanie zaszyfrowanego tekstu

Czyli nie tylko formularz, ale tez dynamiczna odpowiedz interfejsu.

### 4. Czeste uzycie obrazow i zasobow

W zadaniach desktopowych przewijaly sie:

- obrazy rodzaju przesylki
- zdjecie i odcisk palca
- grafiki przyciskow i plyty winylowej
- prostokaty i podglad koloru

Trzeba umiec:

- zaladowac obraz z zasobow lub pliku
- zmienic obraz w runtime
- dobrac poprawna nazwe pliku na podstawie danych wpisanych przez uzytkownika

### 5. Rosnaca integracja z logika z Czesci I

Od nowszych arkuszy coraz czesciej GUI jest tylko warstwa nad logika z konsoli:

- `2024 - Czerwiec 2` - dane albumow
- `2025 - Czerwiec 2` - szyfr Cezara

To znaczy, ze warto miec osobno:

- model danych / logike
- obsluge UI

W MAUI to sie naturalnie uklada w `Page` + kod logiki / serwis / klasy pomocnicze.

---

## Funkcjonalnosci per arkusz

### 2023 - Styczen 1 - pracownik i haslo

Trzeba bylo zrobic:

- formularz z imieniem, nazwiskiem i stanowiskiem
- pole z dlugoscia hasla
- checkboxy okreslajace sklad hasla
- generowanie hasla na podstawie ustawien
- pokazanie wygenerowanego hasla
- zatwierdzenie calego formularza komunikatem

Umiejetnosci funkcjonalne:

- pobieranie danych z pol
- obsluga `CheckBox`
- generowanie losowego tekstu
- trzymanie wygenerowanego hasla w stanie

### 2023 - Czerwiec 1 - przesylka

Trzeba bylo zrobic:

- wybor jednego z trzech typow przesylki
- dynamiczna zmiane obrazka i ceny
- walidacje kodu pocztowego
- rozroznienie bledow: zla dlugosc vs niedozwolone znaki

Umiejetnosci funkcjonalne:

- grupa `RadioButton`
- warunki `if/switch`
- walidacja tekstu
- komunikaty dla uzytkownika

### 2024 - Styczen 1 - paszport

Trzeba bylo zrobic:

- formularz z numerem, imieniem, nazwiskiem i kolorem oczu
- dynamiczne ladowanie zdjec po opuszczeniu pola `Numer`
- budowanie nazw plikow z wpisanego numeru
- wyswietlenie komunikatu po kliknieciu `OK`

Umiejetnosci funkcjonalne:

- zdarzenie po opuszczeniu pola
- ladowanie plikow warunkowo
- obsluga braku obrazka
- walidacja pustych danych

### 2024 - Czerwiec 2 - MojeDzwieki

Trzeba bylo zrobic:

- wczytanie danych albumow z pliku `Dane.txt`
- pokazanie jednego aktualnego albumu
- przechodzenie do poprzedniego i nastepnego albumu
- zawijanie indeksu na poczatku i koncu listy
- zwiekszanie liczby pobran aktualnego albumu

Umiejetnosci funkcjonalne:

- odczyt pliku
- lista obiektow
- indeks aktualnego rekordu
- aktualizacja calego widoku po zmianie indeksu

### 2025 - Czerwiec 1 - RGB

Trzeba bylo zrobic:

- trzy suwaki `R`, `G`, `B`
- pokazywanie biezacych wartosci przy suwakach
- dynamiczny podglad biezacego koloru
- zapisanie aktualnego koloru do osobnego pola po kliknieciu `Pobierz`
- rozdzielenie stanu "biezacy kolor" i "zapisany kolor"

Umiejetnosci funkcjonalne:

- obsluga `ValueChanged`
- konwersja trzech liczb na kolor
- dwa niezalezne stany podgladu

### 2025 - Czerwiec 2 - szyfr Cezara

Trzeba bylo zrobic:

- pole na klucz
- pole wielowierszowe na tekst
- wyswietlenie zaszyfrowanego tekstu
- fallback do klucza `0`, gdy wpis nie jest liczba
- otwarcie systemowego okna zapisu
- zapis szyfru do pliku

Umiejetnosci funkcjonalne:

- parsowanie liczby
- praca na duzym tekscie
- wykorzystanie istniejacej logiki szyfrowania
- zapis do pliku przez dialog systemowy

---

## Najwazniejsze mechaniki desktopowe

### Formularze i walidacja

Powtarza sie:

- sprawdzanie, czy pole jest wypelnione
- sprawdzanie, czy tekst ma odpowiednia dlugosc
- sprawdzanie, czy tekst sklada sie tylko z cyfr
- sprawdzanie, czy liczba jest poprawna
- fallback do wartosci domyslnej

### Stan aplikacji

Najczesciej trzeba przechowywac:

- wygenerowane haslo
- zaznaczony rodzaj przesylki
- aktualny album
- liczbe pobran
- biezacy kolor RGB
- zapisany kolor RGB
- zaszyfrowany tekst

### Obrazy

Trzeba umiec:

- podmieniac `Source`
- reagowac na brak pliku
- budowac sciezke lub nazwe pliku na podstawie danych
- laczyc grafike z aktualnym stanem

### Pliki

Desktop jako jedyny wyraznie wraca do pracy z plikami:

- odczyt danych z `Dane.txt`
- zapis szyfru do wybranego pliku

To jest wazny wzorzec, bo dobrze pasuje do aplikacji okienkowych.

---

## Jak to przeklada sie na MAUI Desktop

Jesli robisz to w MAUI, warto umiec wygodnie zbudowac:

- formularz na `Grid` albo `VerticalStackLayout`
- obsluge `Clicked`
- obsluge `CheckedChanged`
- obsluge `ValueChanged`
- obsluge `Unfocused` dla pola tekstowego
- zmiane `Label.Text`
- zmiane `Image.Source`
- zmiane `BackgroundColor`
- prace na lokalnej liscie obiektow
- prosty odczyt i zapis pliku

Najlepszy mentalny model dla desktopu:

1. kontrolki zbieraja dane
2. zdarzenie uruchamia logike
3. logika zmienia stan
4. stan odswieza widok

---

## Co warto umiec przed egzaminem

Najbardziej oplaca sie przepracowac:

1. formularz z `Entry`, `Picker`, `CheckBox`, `Button`
2. walidacje tekstu i liczb
3. dynamiczna zmiane obrazka i etykiety
4. odczyt listy obiektow z pliku
5. nawigacje po elementach listy `poprzedni/nastepny`
6. suwaki RGB i zmiane koloru w czasie rzeczywistym
7. zapis tekstu do pliku

> [!IMPORTANT]
> Desktopowe zadania sa mniej o "rozbudowanej architekturze", a bardziej o sprawnym spinaniu kontrolek, stanu i prostych operacji lokalnych. Jesli w MAUI dobrze ogarniesz formularze, obrazy, listy obiektow, pliki i zdarzenia, to pokryjesz prawie caly ten typ zadan.
