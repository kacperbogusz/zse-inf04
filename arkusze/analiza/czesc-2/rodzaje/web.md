# Analiza funkcjonalnosci - aplikacje webowe

> [!NOTE]
> Ten plik zbiera tylko **funkcjonalnosci**, ktore pojawialy sie w zadaniach webowych z Czesci II. Bez dokumentacji i bez rozpiski frameworkowej poza praktycznym odniesieniem do **Reacta**, bo tego chcesz uzywac.

---

## Zakres

W arkuszach z lat 2021-2026 pojawily sie **3 zadania webowe**:

1. `2022 - Czerwiec 2` - zapisy na kursy
2. `2023 - Czerwiec 3` - formularz filmu
3. `2025 - Styczen 1` - galeria zdjec z kategoriami

---

## Co wraca najczesciej

### 1. Jeden komponent

We wszystkich zadaniach webowych powtarza sie ten sam wzorzec:

- jedna strona
- jeden glowny komponent
- dane trzymane lokalnie
- logika bez backendu

To bardzo dobrze pasuje do prostego Reacta z jednym komponentem i `useState`.

### 2. Formularz albo widok oparty o tablice

Zadania webowe sa zbudowane wokol dwoch schematow:

- formularz + obsluga przycisku
- tablica danych + renderowanie listy / blokow

To oznacza, ze kluczowe sa:

- stan formularza
- renderowanie z `map`
- warunkowe wyswietlanie

### 3. Bootstrap jako warstwa wizualna

W kazdym webowym zadaniu wraca Bootstrap:

- stylowanie formularza
- przyciski
- pola
- checkboxy / switche

Czyli funkcjonalnie trzeba umiec oddzielic:

- stan i logike w React
- klasy wygladu w Bootstrapie

### 4. Logika bez API i bez bazy

To sa zadania czysto front-endowe:

- brak backendu
- brak fetchowania
- brak bazy danych
- brak routingu

Dane sa po prostu:

- wpisane w kodzie
- skopiowane z `dane.txt`
- trzymane w tablicy stanu

### 5. Konsola przegladarki jako wynik

W dwoch pierwszych zadaniach wynik nie trafia nawet do widoku, tylko do konsoli:

- kursy
- formularz filmu

To wazne, bo logika jest czesto prostsza niz wyglada: czasem wystarczy poprawnie odczytac stan i wypisac dane.

---

## Funkcjonalnosci per arkusz

### 2022 - Czerwiec 2 - zapisy na kursy

Trzeba bylo zrobic:

- tablice nazw kursow
- wyswietlenie liczby kursow
- automatycznie generowana liste numerowana
- formularz z imieniem i nazwiskiem
- pole z numerem kursu
- przycisk `Zapisz do kursu`
- wyswietlenie w konsoli:
  imienia i nazwiska
  oraz nazwy kursu albo komunikatu `Nieprawidlowy numer kursu`

Umiejetnosci funkcjonalne:

- lokalna tablica danych
- renderowanie listy
- odczyt dwoch pol formularza
- mapowanie numeru na element tablicy
- prosty warunek walidacyjny

### 2023 - Czerwiec 3 - formularz filmu

Trzeba bylo zrobic:

- formularz z polem `Tytul filmu`
- `select` z rodzajem filmu
- przycisk `Dodaj`
- startowo puste pola
- wypisanie danych formularza do konsoli po kliknieciu

Umiejetnosci funkcjonalne:

- kontrolowane pole tekstowe
- kontrolowany `select`
- obsluga `onSubmit` albo `onClick`
- skladanie danych do jednego wyniku

### 2025 - Styczen 1 - galeria kategorii

Trzeba bylo zrobic:

- tablice obiektow zdjec z `dane.txt`
- trzy pola `switch/checkbox`
- filtrowanie zdjec po kategorii
- wyswietlanie blokow zdjec obok siebie
- pokazanie liczby pobran
- przycisk `Pobierz` dla kazdego zdjecia
- zwiekszanie liczby pobran tylko dla kliknietego elementu

Umiejetnosci funkcjonalne:

- tablica obiektow
- renderowanie listy kart
- warunkowe filtrowanie
- aktualizacja jednego elementu w stanie
- zachowanie uniwersalne dla dowolnej liczby zdjec

---

## Najwazniejsze mechaniki webowe

### Formularze

Powtarza sie:

- `input text`
- `input number`
- `select`
- przycisk submit
- startowo puste wartosci
- obsluga zdarzenia po zatwierdzeniu

### Tablice i renderowanie

Powtarza sie:

- lista numerowana kursow
- tablica obiektow zdjec
- dynamiczne renderowanie elementow
- praca niezalezna od liczby rekordow

### Warunki

Powtarza sie:

- poprawny / niepoprawny numer kursu
- filtrowanie po checkboxach
- pokazywanie tylko tych elementow, ktore spelniaja warunek

### Aktualizacja stanu

Powtarza sie:

- wpisane wartosci formularza
- wybrany rodzaj filmu
- aktywne checkboxy kategorii
- liczba pobran dla kazdego zdjecia

To jest praktycznie czysta nauka `useState` i aktualizacji niemutowalnej.

---

## Jak to przeklada sie na React

W React najlepiej myslec o tych zadaniach tak:

### Dane stale

Trzymasz w kodzie:

- tablice kursow
- opcje selecta
- tablice obiektow zdjec

### Stan

W `useState` trzymasz:

- wartosc pola tekstowego
- wartosc pola numerycznego
- wartosc selecta
- zaznaczenie checkboxow
- aktualna tablice zdjec z licznikami pobran

### Render

W JSX robisz:

- `map` dla list i kart
- warunkowe renderowanie po checkboxach
- klasy Bootstrap dla wygladu

### Zdarzenia

Obslugujesz:

- `onChange` dla pol
- `onSubmit` dla formularza
- `onClick` dla przyciskow `Dodaj`, `Zapisz do kursu`, `Pobierz`

---

## Co warto umiec przed egzaminem

Najbardziej oplaca sie przepracowac:

1. jeden komponent formularza z `useState`
2. liste renderowana z tablicy przez `map`
3. walidacje prostego pola numerycznego
4. `select` i `checkbox`
5. filtrowanie listy po stanie
6. aktualizacje jednego elementu w tablicy obiektow
7. laczenie React + Bootstrap bez komplikowania logiki

---

## Najkrotsza synteza

Jesli masz robic web w React, to tak naprawde trzeba umiec trzy rzeczy:

1. formularz kontrolowany
2. renderowanie danych z tablicy
3. zmiane stanu po kliknieciu i odswiezenie widoku

> [!IMPORTANT]
> Webowe zadania sa najmniej o "rozbudowanej aplikacji", a najbardziej o czystym front-endzie: lokalny stan, JSX, `map`, warunki i Bootstrap. Jesli to masz ogarniete, pokrywasz praktycznie caly ten typ zadan.
