# Dokumentacja: Python

## Spis treści

- [1. Podstawy języka Python](#1-podstawy-języka-python)
  - [1.1. Typy zmiennych](#11-typy-zmiennych)
  - [1.2. Konwersja typów (rzutowanie)](#12-konwersja-typów-rzutowanie)
  - [1.3. Wyświetlanie danych — `print()`](#13-wyświetlanie-danych--print)
  - [1.4. Formatowanie napisów — f-string](#14-formatowanie-napisów--f-string)
  - [1.5. Pobieranie danych od użytkownika — `input()`](#15-pobieranie-danych-od-użytkownika--input)
  - [1.6. Komentarze](#16-komentarze)
  - [1.7. Znak nowej linii i znaki specjalne](#17-znak-nowej-linii-i-znaki-specjalne)
  - [1.8. Obsługa wyjątków — try / except / finally](#18-obsługa-wyjątków--try--except--finally)
  - [1.9. Wczytywanie wielu wartości w jednej linii](#19-wczytywanie-wielu-wartości-w-jednej-linii)
- [2. Operatory](#2-operatory)
  - [2.1. Operatory arytmetyczne](#21-operatory-arytmetyczne)
  - [2.2. Operatory porównania](#22-operatory-porównania)
  - [2.3. Operatory logiczne](#23-operatory-logiczne)
  - [2.4. Operatory przypisania](#24-operatory-przypisania)
  - [2.5. Operatory przynależności i tożsamości](#25-operatory-przynależności-i-tożsamości)
- [3. Instrukcje sterujące](#3-instrukcje-sterujące)
  - [3.1. Instrukcja warunkowa `if` / `elif` / `else`](#31-instrukcja-warunkowa-if--elif--else)
  - [3.2. Pętla `for`](#32-pętla-for)
  - [3.3. Funkcja `enumerate()` — iteracja z indeksem](#33-funkcja-enumerate--iteracja-z-indeksem)
  - [3.4. Pętla `while`](#34-pętla-while)
  - [3.5. `break`, `continue` i `else` w pętlach](#35-break-continue-i-else-w-pętlach)
  - [3.6. Pętle zagnieżdżone](#36-pętle-zagnieżdżone)
- [4. Struktury danych](#4-struktury-danych)
  - [4.1. Listy (`list`)](#41-listy-list)
  - [4.2. Krotki (`tuple`)](#42-krotki-tuple)
  - [4.3. Słowniki (`dict`)](#43-słowniki-dict)
  - [4.4. Zbiory (`set`)](#44-zbiory-set)
  - [4.5. Zagnieżdżone struktury danych](#45-zagnieżdżone-struktury-danych)
- [5. Funkcje](#5-funkcje)
  - [5.1. Definicja i wywoływanie funkcji](#51-definicja-i-wywoływanie-funkcji)
  - [5.2. Parametry domyślne](#52-parametry-domyślne)
  - [5.3. Argumenty pozycyjne i nazwane](#53-argumenty-pozycyjne-i-nazwane)
  - [5.4. Zmienna liczba argumentów — *args i **kwargs](#54-zmienna-liczba-argumentów--args-i-kwargs)
  - [5.5. Argumenty tylko pozycyjne (/) i tylko nazwane (*)](#55-argumenty-tylko-pozycyjne--i-tylko-nazwane-)
  - [5.6. Zasięg zmiennych (scope)](#56-zasięg-zmiennych-scope)
  - [5.7. Funkcja `lambda` — funkcje anonimowe](#57-funkcja-lambda--funkcje-anonimowe)
  - [5.8. Funkcje wbudowane — przegląd najważniejszych](#58-funkcje-wbudowane--przegląd-najważniejszych)
- [6. Przetwarzanie łańcuchów znaków](#6-przetwarzanie-łańcuchów-znaków)
  - [6.1. Podstawowe operacje na napisach](#61-podstawowe-operacje-na-napisach)
  - [6.2. Metody napisów — kompletny przegląd](#62-metody-napisów--kompletny-przegląd)
  - [6.3. Sprawdzanie rodzaju znaków](#63-sprawdzanie-rodzaju-znaków)
  - [6.4. Kody znaków — `ord()` i `chr()`](#64-kody-znaków--ord-i-chr)
  - [6.5. Iteracja po znakach i budowanie nowego napisu](#65-iteracja-po-znakach-i-budowanie-nowego-napisu)
  - [6.6. Obsługa polskich znaków](#66-obsługa-polskich-znaków)
  - [6.7. Przydatne wzorce przetwarzania tekstu](#67-przydatne-wzorce-przetwarzania-tekstu)
- [7. Obsługa plików](#7-obsługa-plików)
  - [7.1. Otwieranie i zamykanie plików](#71-otwieranie-i-zamykanie-plików)
  - [7.2. Odczyt pliku tekstowego](#72-odczyt-pliku-tekstowego)
  - [7.3. Zapis do pliku tekstowego](#73-zapis-do-pliku-tekstowego)
  - [7.4. Praca z plikami CSV (dane tabelaryczne)](#74-praca-z-plikami-csv-dane-tabelaryczne)
  - [7.5. Sprawdzanie istnienia pliku](#75-sprawdzanie-istnienia-pliku)
  - [7.6. Obsługa błędów przy pracy z plikami](#76-obsługa-błędów-przy-pracy-z-plikami)
  - [7.7. Operacje na ścieżkach — moduł `os.path`](#77-operacje-na-ścieżkach--moduł-ospath)
  - [7.8. Tworzenie i usuwanie plików/folderów](#78-tworzenie-i-usuwanie-plikówfolderów)
  - [7.9. Wczytywanie danych z pliku do tablicy](#79-wczytywanie-danych-z-pliku-do-tablicy)
  - [7.10. Praca z plikami JSON](#710-praca-z-plikami-json)
  - [7.11. Podsumowanie metod pracy z plikami](#711-podsumowanie-metod-pracy-z-plikami)
- [8. Operacje matematyczne](#8-operacje-matematyczne)
  - [8.1. Wbudowane funkcje matematyczne](#81-wbudowane-funkcje-matematyczne)
  - [8.2. Moduł `math`](#82-moduł-math)
  - [8.3. Dzielenie — porównanie operatorów](#83-dzielenie--porównanie-operatorów)
  - [8.4. Konwersja systemów liczbowych](#84-konwersja-systemów-liczbowych)
- [9. Moduł random — generowanie losowych danych](#9-moduł-random--generowanie-losowych-danych)
  - [9.1. Importowanie](#91-importowanie)
  - [9.2. Generowanie liczb losowych](#92-generowanie-liczb-losowych)
  - [9.3. Losowanie z kolekcji](#93-losowanie-z-kolekcji)
  - [9.4. Wypełnianie tablicy losowymi danymi](#94-wypełnianie-tablicy-losowymi-danymi)
  - [9.5. Losowanie bez powtórzeń — trzy sposoby](#95-losowanie-bez-powtórzeń--trzy-sposoby)
  - [9.6. Ustawienie ziarna (seed) — powtarzalność wyników](#96-ustawienie-ziarna-seed--powtarzalność-wyników)
- [10. Programowanie obiektowe — podstawy](#10-programowanie-obiektowe--podstawy)
  - [10.1. Definicja klasy](#101-definicja-klasy)
  - [10.2. Konstruktor `__init__` i pola instancji](#102-konstruktor-__init__-i-pola-instancji)
  - [10.3. Metody instancji](#103-metody-instancji)
  - [10.4. `self` — czym jest i dlaczego jest konieczne](#104-self--czym-jest-i-dlaczego-jest-konieczne)
  - [10.5. Metoda `__str__` — reprezentacja tekstowa obiektu](#105-metoda-__str__--reprezentacja-tekstowa-obiektu)
  - [10.6. `__repr__` vs `__str__` — dwie reprezentacje tekstowe](#106-__repr__-vs-__str__--dwie-reprezentacje-tekstowe)
- [11. Programowanie obiektowe — hermetyzacja](#11-programowanie-obiektowe--hermetyzacja)
  - [11.1. Poziomy dostępu w Pythonie](#111-poziomy-dostępu-w-pythonie)
  - [11.2. Gettery i settery — metody dostępu](#112-gettery-i-settery--metody-dostępu)
  - [11.3. Dekorator `@property` — pythoniczny getter/setter](#113-dekorator-property--pythoniczny-gettersetter)
- [12. Programowanie obiektowe — zmienne klasowe i metody statyczne](#12-programowanie-obiektowe--zmienne-klasowe-i-metody-statyczne)
  - [12.1. Zmienne klasowe (static fields)](#121-zmienne-klasowe-static-fields)
  - [12.2. Zmienne klasowe — tablice i kolekcje](#122-zmienne-klasowe--tablice-i-kolekcje)
  - [12.3. Metody statyczne — `@staticmethod`](#123-metody-statyczne--staticmethod)
  - [12.4. Metody klasowe — `@classmethod`](#124-metody-klasowe--classmethod)
- [13. Programowanie obiektowe — konstruktory zaawansowane](#13-programowanie-obiektowe--konstruktory-zaawansowane)
  - [13.1. Konstruktor z wartościami domyślnymi](#131-konstruktor-z-wartościami-domyślnymi)
  - [13.2. Wzorzec z `None` — pełny zamiennik dwóch konstruktorów](#132-wzorzec-z-none--pełny-zamiennik-dwóch-konstruktorów)
  - [13.3. Walidacja w konstruktorze](#133-walidacja-w-konstruktorze)
  - [13.4. Kopiowanie obiektów](#134-kopiowanie-obiektów)
- [14. Programowanie obiektowe — dziedziczenie, polimorfizm i klasy abstrakcyjne](#14-programowanie-obiektowe--dziedziczenie-polimorfizm-i-klasy-abstrakcyjne)
  - [14.1. Podstawy dziedziczenia](#141-podstawy-dziedziczenia)
  - [14.2. `super()` — wywoływanie metod rodzica](#142-super--wywoływanie-metod-rodzica)
  - [14.3. Hermetyzacja a dziedziczenie](#143-hermetyzacja-a-dziedziczenie)
  - [14.4. Wzorzec: logika stanów z dziedziczeniem](#144-wzorzec-logika-stanów-z-dziedziczeniem)
  - [14.5. Sprawdzanie typu i dziedziczenia](#145-sprawdzanie-typu-i-dziedziczenia)
  - [14.6. Podsumowanie — kiedy co stosować w OOP](#146-podsumowanie--kiedy-co-stosować-w-oop)
  - [14.7. Polimorfizm](#147-polimorfizm)
  - [14.8. Klasy abstrakcyjne — moduł `abc`](#148-klasy-abstrakcyjne--moduł-abc)
  - [14.9. Kompleksowa implementacja: System Quiz](#149-kompleksowa-implementacja-system-quiz)
- [15. Algorytmy w Pythonie](#15-algorytmy-w-pythonie)
  - [15.1. Sortowanie przez wybieranie (Selection Sort)](#151-sortowanie-przez-wybieranie-selection-sort)
  - [15.2. Sortowanie bąbelkowe (Bubble Sort)](#152-sortowanie-bąbelkowe-bubble-sort)
  - [15.3. Sortowanie przez wstawianie (Insertion Sort)](#153-sortowanie-przez-wstawianie-insertion-sort)
  - [15.4. Sortowanie przez scalanie (Merge Sort)](#154-sortowanie-przez-scalanie-merge-sort)
  - [15.5. Sortowanie szybkie (Quick Sort)](#155-sortowanie-szybkie-quick-sort)
  - [15.6. Wyszukiwanie liniowe](#156-wyszukiwanie-liniowe)
  - [15.7. Wyszukiwanie z wartownikiem (Sentinel Search)](#154-wyszukiwanie-z-wartownikiem-sentinel-search)
  - [15.8. Wyszukiwanie binarne (Binary Search)](#1515-wyszukiwanie-binarne-binary-search)
  - [15.9. Algorytm Euklidesa (NWD — Największy Wspólny Dzielnik)](#155-algorytm-euklidesa-nwd--największy-wspólny-dzielnik)
  - [15.10. Najmniejsza Wspólna Wielokrotność (NWW)](#1510-najmniejsza-wspólna-wielokrotność-nww)
  - [15.11. Sprawdzanie czy liczba jest pierwsza](#1513-sprawdzanie-czy-liczba-jest-pierwsza)
  - [15.12. Sito Eratostenesa](#156-sito-eratostenesa)
  - [15.13. Rozkład liczby na czynniki pierwsze](#1513-rozkład-liczby-na-czynniki-pierwsze)
  - [15.14. Konwersja systemów liczbowych (Dziesiętny <-> Binarny)](#1514-konwersja-systemów-liczbowych-dziesiętny---binarny)
  - [15.15. Szyfr Cezara](#157-szyfr-cezara)
  - [15.16. Palindromy i Anagramy](#1516-palindromy-i-anagramy)
  - [15.17. Rekurencja](#1514-rekurencja)
  - [15.18. Walidacja danych z wagami](#158-walidacja-danych-z-wagami)
  - [15.19. Usuwanie sąsiednich duplikatów](#159-usuwanie-sąsiednich-duplikatów)
  - [15.20. Zliczanie wystąpień wartości w danych](#1510-zliczanie-wystąpień-wartości-w-danych)
  - [15.21. Obliczanie średniej arytmetycznej](#1511-obliczanie-średniej-arytmetycznej)
  - [15.22. Wyodrębnianie elementów spełniających warunek](#1512-wyodrębnianie-elementów-spełniających-warunek)
- [16. Tablice dwuwymiarowe](#16-tablice-dwuwymiarowe)
  - [16.1. Tworzenie tablic 2D](#161-tworzenie-tablic-2d)
  - [16.2. Dostęp i iteracja](#162-dostęp-i-iteracja)
  - [16.3. Wypełnianie i wyświetlanie](#163-wypełnianie-i-wyświetlanie)
  - [16.4. Operacje na tablicach 2D](#164-operacje-na-tablicach-2d)
- [17. Testowanie jednostkowe — unittest i pytest](#17-testowanie-jednostkowe--unittest-i-pytest)
  - [17.1. Czym jest testowanie jednostkowe](#171-czym-jest-testowanie-jednostkowe)
  - [17.2. Moduł `unittest` — podstawy](#172-moduł-unittest--podstawy)
  - [17.3. Asercje — kompletna lista](#173-asercje--kompletna-lista)
  - [17.4. Struktura projektu z testami](#174-struktura-projektu-z-testami)
  - [17.5. Nazewnictwo testów](#175-nazewnictwo-testów)
  - [17.6. `setUp` i `tearDown` — przygotowanie i sprzątanie](#176-setup-i-teardown--przygotowanie-i-sprzątanie)
  - [17.7. Testowanie klas i obiektów](#177-testowanie-klas-i-obiektów)
  - [17.8. Testowanie wartości losowych](#178-testowanie-wartości-losowych)
  - [17.9. `pytest` — prostsza alternatywa](#179-pytest--prostsza-alternatywa)
  - [17.10. Podsumowanie — uruchamianie testów](#1710-podsumowanie--uruchamianie-testów)
- [18. Przydatne wzorce i idiomy Pythona](#18-przydatne-wzorce-i-idiomy-pythona)
  - [18.1. Zamiana wartości dwóch zmiennych](#181-zamiana-wartości-dwóch-zmiennych)
  - [18.2. `if __name__ == "__main__":`](#182-if-__name__--__main__)
  - [18.3. Rozpakowywanie z `*` (operatorem gwiazdki)](#183-rozpakowywanie-z--operatorem-gwiazdki)
  - [18.4. Dictionary comprehension](#184-dictionary-comprehension)
  - [18.5. Formatowanie wypisywania tabel w konsoli](#185-formatowanie-wypisywania-tabel-w-konsoli)
  - [18.6. Podkreślnik `_` — konwencje](#186-podkreślnik-_--konwencje)
  - [18.7. Najczęstsze pułapki i błędy w Pythonie](#187-najczęstsze-pułapki-i-błędy-w-pythonie)
  - [18.8. Wzorzec menu programu (pętla główna)](#188-wzorzec-menu-programu-pętla-główna)
  - [18.9. Sortowanie obiektów — parametr `key`](#189-sortowanie-obiektów--parametr-key)


---

> **Jak korzystać z tego poradnika:** Każdy rozdział jest samodzielny — możesz czytać je w dowolnej kolejności. Następujące po sobie rozdziały OOP (10–14) warto jednak czytać po kolei, ponieważ każdy z nich buduje na wiedzy z poprzedniego. Przykłady kodu są gotowe do uruchomienia — możesz je skopiować i przetestować w swoim edytorze.

---

## 1. Podstawy języka Python

Python jest językiem programowania wysokiego poziomu, stworzonym przez Guido van Rossuma w 1991 roku. Wyróżnia się prostą i czytelną składnią, której fundamentem jest **wcięciowanie** (indentacja) — nie używa się klamerek `{}` do oznaczania bloków kodu, lecz spacji lub tabulatorów. Standardowo stosuje się **4 spacje** na każdy poziom wcięcia.

Python jest językiem **interpretowanym** — kod nie jest kompilowany do postaci binarnej, lecz wykonywany linia po linii przez interpreter. Jest też **dynamicznie typowany**, co oznacza, że typ zmiennej jest ustalany automatycznie w momencie przypisania wartości, a nie deklarowany z góry przez programistę.

### 1.1. Typy zmiennych

W Pythonie nie trzeba deklarować typu zmiennej — interpreter sam rozpoznaje typ na podstawie przypisanej wartości. To fundamentalna różnica w porównaniu z językami takimi jak C++ czy Java, gdzie typ musi być podany jawnie (np. `int x = 5;`).

Poniższa tabela przedstawia podstawowe typy danych w Pythonie:

| Typ | Opis | Przykładowe wartości |
|---|---|---|
| `int` | Liczba całkowita (dowolnej wielkości) | `42`, `-7`, `0`, `1000000` |
| `float` | Liczba zmiennoprzecinkowa | `3.14`, `-0.5`, `2.0` |
| `str` | Łańcuch znaków (napis, tekst) | `"Witaj"`, `'Python'`, `""` |
| `bool` | Wartość logiczna (prawda/fałsz) | `True`, `False` |
| `None` | Wartość pusta (brak wartości) | `None` |
| `list` | Lista (modyfikowalna kolekcja) | `[1, 2, 3]`, `["a", "b"]` |
| `tuple` | Krotka (niemodyfikowalna kolekcja) | `(1, 2, 3)` |
| `dict` | Słownik (pary klucz-wartość) | `{"imie": "Jan"}` |
| `set` | Zbiór (unikalne elementy) | `{1, 2, 3}` |

**Przykłady deklaracji zmiennych:**

```python
# Liczby całkowite (int)
wiek = 25
liczba_elementow = 100
temperatura = -5

# Liczby zmiennoprzecinkowe (float)
temperatura = 36.6
srednia = 78.5
pi = 3.14159

# Łańcuchy znaków (str)
# Można używać zarówno cudzysłowów podwójnych, jak i pojedynczych
imie = "Jan"
komunikat = 'Witaj w programie'
pusty_napis = ""

# Wartości logiczne (bool)
# Uwaga: True i False są pisane z wielkiej litery!
jest_pelnoletni = True
czy_aktywny = False

# Wartość pusta (None)
# None oznacza "brak wartości" — używany np. jako domyślna wartość parametru
wynik = None
```

**Sprawdzanie typu zmiennej:**

Funkcja wbudowana `type()` zwraca typ obiektu. Jest przydatna podczas debugowania, gdy chcemy upewnić się, jakiego typu jest dana zmienna. Z kolei `isinstance()` pozwala sprawdzić, czy obiekt jest instancją określonego typu — ta funkcja uwzględnia również dziedziczenie.

```python
x = 42
print(type(x))        # <class 'int'>

y = "tekst"
print(type(y))        # <class 'str'>

z = 3.14
print(type(z))        # <class 'float'>

w = True
print(type(w))        # <class 'bool'>
```

Funkcja `isinstance()` jest szczególnie przydatna, gdy chcemy sprawdzić, czy zmienna należy do jednego z kilku typów jednocześnie:

```python
x = 42

if isinstance(x, int):
    print("x jest liczbą całkowitą")

# Sprawdzenie przynależności do wielu typów naraz
if isinstance(x, (int, float)):
    print("x jest liczbą (całkowitą lub zmiennoprzecinkową)")
```

### 1.2. Konwersja typów (rzutowanie)

Konwersja typów (ang. *type casting*) polega na zamianie jednego typu danych na inny. Jest to operacja niezwykle częsta — na przykład funkcja `input()` zawsze zwraca tekst `str`, więc aby wykonywać operacje arytmetyczne na danych pobranych od użytkownika, trzeba je zamienić na `int` lub `float`.

| Funkcja | Konwertuje na | Przykład | Wynik |
|---|---|---|---|
| `int()` | liczbę całkowitą | `int("42")` | `42` |
| `float()` | liczbę zmiennoprzecinkową | `float("3.14")` | `3.14` |
| `str()` | łańcuch znaków | `str(42)` | `"42"` |
| `bool()` | wartość logiczną | `bool(0)` | `False` |
| `list()` | listę | `list("abc")` | `["a", "b", "c"]` |

```python
# String → int — najczęstsza konwersja (dane z input())
tekst = "42"
liczba = int(tekst)          # 42

# String → float
tekst = "3.14"
wartosc = float(tekst)       # 3.14

# Int → string — potrzebne przy łączeniu z innymi stringami
liczba = 42
tekst = str(liczba)          # "42"

# Float → int — UWAGA: obcina część dziesiętną, nie zaokrągla!
wartosc = 3.7
calkowita = int(wartosc)     # 3 (nie 4!)
wartosc2 = 3.2
calkowita2 = int(wartosc2)   # 3
```

**Konwersja na `bool` — zasada „truthiness":**

W Pythonie każda wartość ma swoją „prawdziwość". Zrozumienie, co jest traktowane jako `True`, a co jako `False`, jest kluczowe przy pisaniu warunków:

| Wartość | `bool()` | Wyjaśnienie |
|---|---|---|
| `0` | `False` | Zero liczbowe |
| `0.0` | `False` | Zero zmiennoprzecinkowe |
| `""` | `False` | Pusty napis |
| `[]` | `False` | Pusta lista |
| `{}` | `False` | Pusty słownik |
| `None` | `False` | Brak wartości |
| `1`, `-5` | `True` | Każda niezerowa liczba |
| `"abc"` | `True` | Niepusty napis |
| `[1, 2]` | `True` | Niepusta lista |

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(-5))      # True — każda liczba ≠ 0 to True
print(bool(""))      # False — pusty napis
print(bool("abc"))   # True — niepusty napis
print(bool(None))    # False
print(bool([]))      # False — pusta lista
print(bool([0]))     # True — lista z jednym elementem (nawet zerem!)
```

### 1.3. Wyświetlanie danych — `print()`

Funkcja `print()` jest podstawowym narzędziem do wyświetlania danych w konsoli. Domyślnie dodaje znak nowej linii (`\n`) na końcu każdego wywołania, ale to zachowanie można zmienić.

**Parametry funkcji `print()`:**

| Parametr | Domyślnie | Opis |
|---|---|---|
| `*args` | — | Dowolna liczba wartości do wyświetlenia |
| `sep` | `" "` (spacja) | Separator między wartościami |
| `end` | `"\n"` (nowa linia) | Co dodać na końcu |

```python
# Podstawowe wyświetlanie
print("Witaj!")

# Wyświetlanie wielu wartości — automatycznie rozdzielone spacją
imie = "Anna"
wiek = 20
print("Imię:", imie, "Wiek:", wiek)
# Wynik: Imię: Anna Wiek: 20

# Zmiana separatora — parametr sep
print("A", "B", "C")             # A B C
print("A", "B", "C", sep=", ")   # A, B, C
print("A", "B", "C", sep=" | ")  # A | B | C
print("A", "B", "C", sep="")     # ABC (bez separatora)

# Zmiana zakończenia linii — parametr end
print("Bez nowej linii", end=" ")
print("kontynuacja")
# Wynik: Bez nowej linii kontynuacja

# Wyświetlanie pustej linii
print()
```

### 1.4. Formatowanie napisów — f-string

F-stringi (formatted string literals) to najwygodniejszy i najczęściej stosowany sposób formatowania tekstu w Pythonie 3.6+. Tworzymy je, dodając literę `f` przed cudzysłowem, a zmienne lub wyrażenia umieszczamy w klamrach `{}`.

```python
imie = "Jan"
wiek = 25
srednia = 87.4567

# Podstawowe wstawianie zmiennych
print(f"Cześć, {imie}!")                      # Cześć, Jan!
print(f"Mam {wiek} lat")                      # Mam 25 lat

# Wyrażenia wewnątrz klamr — mogą to być obliczenia, wywołania funkcji itd.
print(f"Za 5 lat będę mieć {wiek + 5} lat")   # Za 5 lat będę mieć 30 lat
print(f"Imię wielkimi: {imie.upper()}")        # Imię wielkimi: JAN
```

**Formatowanie precyzji liczb:**

Wewnątrz klamr po dwukropku `:` można podać specyfikator formatu. Jest to szczególnie ważne przy wyświetlaniu liczb zmiennoprzecinkowych i wyrównywaniu kolumn:

| Specyfikator | Opis | Przykład | Wynik |
|---|---|---|---|
| `:.2f` | 2 miejsca po przecinku | `f"{3.14159:.2f}"` | `3.14` |
| `:.4f` | 4 miejsca po przecinku | `f"{3.14159:.4f}"` | `3.1416` |
| `:05d` | 5 cyfr, uzupełnienie zerami | `f"{42:05d}"` | `00042` |
| `:>10` | Wyrównanie do prawej, szer. 10 | `f"{'abc':>10}"` | `       abc` |
| `:<10` | Wyrównanie do lewej, szer. 10 | `f"{'abc':<10}"` | `abc       ` |
| `:^10` | Wyśrodkowanie, szer. 10 | `f"{'abc':^10}"` | `   abc    ` |

```python
srednia = 87.4567

print(f"Średnia: {srednia:.2f}")          # Średnia: 87.46
print(f"Średnia: {srednia:.0f}")          # Średnia: 87
print(f"Liczba: {42:05d}")                # Liczba: 00042
print(f"{'Imię':<15}{'Wiek':>5}")         # Imię              Wiek
```

**Starsze sposoby formatowania** (na wypadek, gdyby były potrzebne):

```python
# Metoda .format()
print("Imię: {}, Wiek: {}".format(imie, wiek))

# Operator % (styl C)
print("Imię: %s, Wiek: %d" % (imie, wiek))
```

### 1.5. Pobieranie danych od użytkownika — `input()`

Funkcja `input()` wyświetla komunikat (prompt) i czeka na dane od użytkownika. Po naciśnięciu Enter zwraca wpisany tekst. **Zawsze zwraca wartość typu `str`** — nawet jeśli użytkownik wpisze liczbę, dla Pythona to nadal będzie tekst.

```python
# Pobranie tekstu — nie wymaga konwersji
imie = input("Podaj imię: ")

# Pobranie liczby całkowitej — wymaga konwersji int()
wiek = int(input("Podaj wiek: "))

# Pobranie liczby zmiennoprzecinkowej — wymaga konwersji float()
wzrost = float(input("Podaj wzrost (m): "))
```

**Obsługa błędnych danych wejściowych:**

Gdy użytkownik wpisze tekst zamiast liczby, wywołanie `int()` spowoduje błąd `ValueError`. Blok `try/except` pozwala przechwycić ten błąd i zareagować na niego w kontrolowany sposób:

```python
try:
    liczba = int(input("Podaj liczbę: "))
    print(f"Podano: {liczba}")
except ValueError:
    print("To nie jest prawidłowa liczba!")
```

Można też zbudować pętlę, która wymusi podanie poprawnej wartości:

```python
while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))
        break  # Wyjście z pętli gdy konwersja się powiodła
    except ValueError:
        print("Błąd! Podaj prawidłową liczbę.")
```

### 1.6. Komentarze

Komentarze to fragmenty kodu ignorowane przez interpreter. Służą do wyjaśniania logiki programu, dokumentowania funkcji oraz tymczasowego wyłączania fragmentów kodu. Dobry komentarz wyjaśnia **dlaczego** coś zostało zrobione, a nie **co** robi dany fragment — to drugie powinno być czytelne z samego kodu.

```python
# To jest komentarz jednoliniowy — zaczyna się od znaku #

x = 42  # Komentarz może być też na końcu linii kodu

"""
To jest komentarz wieloliniowy (technicznie to napis — string literal).
Jeśli nie jest przypisany do zmiennej, Python go po prostu ignoruje.
Często używany do opisywania dłuższych bloków logiki.
"""

'''
Alternatywna forma komentarza wieloliniowego
z użyciem apostrofów zamiast cudzysłowów.
'''
```

### 1.7. Znak nowej linii i znaki specjalne

W napisach można używać znaków specjalnych (sekwencji ucieczki), które zaczynają się od odwrotnego ukośnika `\`:

| Sekwencja | Znaczenie | Przykład |
|---|---|---|
| `\n` | Nowa linia | `"linia1\nlinia2"` |
| `\t` | Tabulacja | `"kolumna1\tkolumna2"` |
| `\\` | Dosłowny ukośnik `\` | `"C:\\folder"` |
| `\"` | Cudzysłów w napisie | `"Mówi \"cześć\""` |
| `\'` | Apostrof w napisie | `'It\'s okay'` |

```python
print("Pierwsza linia\nDruga linia")
# Pierwsza linia
# Druga linia

print("Kol1\tKol2\tKol3")
# Kol1    Kol2    Kol3

# Raw string (r"...") — ignoruje znaki specjalne
print(r"C:\nowy\folder")  # C:\nowy\folder (bez nowej linii)
```

### 1.8. Obsługa wyjątków — try / except / finally

Błędy są naturalną częścią programowania. Python oferuje mechanizm wyjątków, który pozwala na eleganckie reagowanie na błędy bez przerywania działania programu. Blok `try` zawiera kod, który może spowodować błąd. Blok `except` obsługuje konkretny typ błędu. Opcjonalny blok `finally` wykonuje się zawsze — niezależnie od tego, czy błąd wystąpił.

**Najczęstsze typy wyjątków:**

| Wyjątek | Kiedy występuje | Przykład |
|---|---|---|
| `ValueError` | Niepoprawna wartość | `int("abc")` |
| `TypeError` | Niepoprawny typ | `"tekst" + 5` |
| `IndexError` | Indeks poza zakresem | `lista[100]` gdy `len(lista) < 101` |
| `KeyError` | Brak klucza w słowniku | `slownik["brak"]` |
| `ZeroDivisionError` | Dzielenie przez zero | `10 / 0` |
| `FileNotFoundError` | Plik nie istnieje | `open("brak.txt")` |
| `AttributeError` | Brak atrybutu/metody | `"tekst".nieistniejaca()` |
| `NameError` | Niezdefiniowana zmienna | `print(zmienna)` bez deklaracji |

**Podstawowa obsługa wyjątków:**

```python
try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 100 / liczba
    print(f"Wynik: {wynik}")
except ValueError:
    print("To nie jest prawidłowa liczba!")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
```

**Łapanie wielu wyjątków naraz:**

```python
try:
    # Kod, który może rzucić różne wyjątki
    dane = [1, 2, 3]
    indeks = int(input("Podaj indeks: "))
    print(dane[indeks])
except (ValueError, IndexError) as e:
    print(f"Błąd: {e}")
```

**Blok `else` — wykonuje się tylko, gdy NIE było wyjątku:**

```python
try:
    liczba = int(input("Podaj liczbę: "))
except ValueError:
    print("Niepoprawna wartość!")
else:
    print(f"Podano poprawną liczbę: {liczba}")
```

**Blok `finally` — wykonuje się ZAWSZE:**

Blok `finally` jest gwarancją, że pewne operacje zostaną wykonane niezależnie od tego, co się wydarzy — np. zamknięcie pliku, zwolnienie zasobów:

```python
try:
    plik = open("dane.txt", "r")
    zawartosc = plik.read()
except FileNotFoundError:
    print("Plik nie istnieje!")
finally:
    # Ten blok wykona się ZAWSZE — nawet przy błędzie
    print("Kończymy pracę z plikiem")
```

**Kompletna struktura try/except/else/finally:**

```python
try:
    # Kod, który może spowodować błąd
    wynik = ryzykowna_operacja()
except TypBledu:
    # Obsługa konkretnego błędu
    print("Obsługa błędu")
except Exception as e:
    # Obsługa DOWOLNEGO innego błędu
    print(f"Nieoczekiwany błąd: {e}")
else:
    # Wykonuje się tylko gdy NIE było błędu
    print(f"Operacja udana: {wynik}")
finally:
    # Wykonuje się ZAWSZE
    print("Sprzątanie zasobów")
```

**Pętla z ponawianiem po błędzie:**

```python
while True:
    try:
        wiek = int(input("Podaj wiek (0-150): "))
        if not 0 <= wiek <= 150:
            raise ValueError("Wiek poza zakresem")
        break  # Poprawna wartość — wyjście z pętli
    except ValueError as e:
        print(f"Błąd: {e}. Spróbuj ponownie.")

print(f"Twój wiek: {wiek}")
```

W powyższym przykładzie `raise ValueError(...)` to ręczne rzucenie wyjątku — przydatne do walidacji danych.

### 1.9. Wczytywanie wielu wartości w jednej linii

Czasem programy wymagają pobrania kilku wartości w jednej linii, oddzielonych spacją lub innym separatorem. Python oferuje kilka eleganckich sposobów, aby to zrobić.

**Metoda `split()` + `map()`:**

Funkcja `map()` stosuje podaną funkcję (np. `int`) do każdego elementu uzyskanego z `split()`. To najczęstszy wzorzec wczytywania wielu liczb:

```python
# Wczytanie dwóch liczb z jednej linii
# Użytkownik wpisuje np.: 10 20
a, b = map(int, input("Podaj dwie liczby: ").split())
print(f"a = {a}, b = {b}")

# Wczytanie trzech wartości
x, y, z = map(float, input("Podaj x, y, z: ").split())

# Wczytanie wielu liczb do listy (gdy nie wiemy ile)
liczby = list(map(int, input("Podaj liczby: ").split()))
print(f"Podano {len(liczby)} liczb: {liczby}")
```

**Co się tu dzieje krok po kroku:**

| Krok | Wyrażenie | Wynik |
|---|---|---|
| 1. | `input("...")` | `"10 20 30"` (string) |
| 2. | `.split()` | `["10", "20", "30"]` (lista stringów) |
| 3. | `map(int, ...)` | Iterator: 10, 20, 30 (inty) |
| 4. | `list(...)` | `[10, 20, 30]` (lista intów) |

**Separator inny niż spacja:**

```python
# Wczytywanie wartości oddzielonych przecinkiem
dane = input("Podaj wartości (oddzielone przecinkiem): ")  # np. "Jan,25,Warszawa"
czesci = dane.split(",")
imie = czesci[0]
wiek = int(czesci[1])
miasto = czesci[2]

# Lub jednolinijkowo z rozpakowaniem
imie, wiek, miasto = input("Podaj dane: ").split(",")
wiek = int(wiek)  # Konwersja na int osobno
```

**Wczytywanie danych w pętli (n linii):**

```python
n = int(input("Ile osób? "))
osoby = []
for _ in range(n):
    imie, wiek = input("Podaj imię i wiek: ").split()
    osoby.append({"imie": imie, "wiek": int(wiek)})

for osoba in osoby:
    print(f"{osoba['imie']} ma {osoba['wiek']} lat")
```

---

## 2. Operatory

Operatory to symbole lub słowa kluczowe, które wykonują operacje na wartościach (operandach). Python oferuje bogaty zestaw operatorów, podzielonych na kilka kategorii.

### 2.1. Operatory arytmetyczne

Operatory arytmetyczne służą do wykonywania działań matematycznych. Warto zwrócić szczególną uwagę na różnicę między zwykłym dzieleniem `/` (które zawsze daje `float`) a dzieleniem całkowitym `//`.

| Operator | Nazwa | Przykład | Wynik | Uwagi |
|---|---|---|---|---|
| `+` | Dodawanie | `17 + 5` | `22` | |
| `-` | Odejmowanie | `17 - 5` | `12` | |
| `*` | Mnożenie | `17 * 5` | `85` | |
| `/` | Dzielenie | `17 / 5` | `3.4` | Zawsze zwraca `float`! |
| `//` | Dzielenie całkowite | `17 // 5` | `3` | Zaokrągla w dół |
| `%` | Modulo (reszta) | `17 % 5` | `2` | Kluczowy operator |
| `**` | Potęgowanie | `2 ** 10` | `1024` | |

```python
a = 17
b = 5

print(a + b)     # 22    — dodawanie
print(a - b)     # 12    — odejmowanie
print(a * b)     # 85    — mnożenie
print(a / b)     # 3.4   — dzielenie (ZAWSZE float, nawet 10/2 = 5.0)
print(a // b)    # 3     — dzielenie całkowite
print(a % b)     # 2     — reszta z dzielenia
print(a ** b)    # 1419857 — potęgowanie (17⁵)
```

**Operator modulo `%` — dlaczego jest tak ważny:**

Modulo zwraca resztę z dzielenia. To jeden z najczęściej używanych operatorów w programowaniu. Służy do:

1. **Sprawdzania parzystości** — jeśli `n % 2 == 0`, liczba jest parzysta
2. **Cyklicznego przechodzenia** — np. po alfabecie (po `z` wracamy do `a`)
3. **Walidacji danych** — np. suma kontrolna PESEL
4. **Okresowych powtórzeń** — np. co n-ty element

```python
# Sprawdzanie parzystości
liczba = 42
if liczba % 2 == 0:
    print("Parzysta")
else:
    print("Nieparzysta")

# Cykliczne przechodzenie po tablicy (po ostatnim elemencie → pierwszy)
tablica = ["A", "B", "C"]
for i in range(10):
    print(tablica[i % len(tablica)], end=" ")
# Wynik: A B C A B C A B C A

# Wyodrębnianie ostatniej cyfry liczby
liczba = 12345
ostatnia_cyfra = liczba % 10  # 5

# Sprawdzanie podzielności
if 100 % 7 == 0:
    print("100 jest podzielne przez 7")
else:
    print("100 NIE jest podzielne przez 7")
```

### 2.2. Operatory porównania

Operatory porównania porównują dwie wartości i zwracają wartość logiczną `True` lub `False`. Są fundamentalne dla instrukcji warunkowych `if` i pętli `while`.

| Operator | Znaczenie | Przykład | Wynik |
|---|---|---|---|
| `==` | Równe | `5 == 5` | `True` |
| `!=` | Różne | `5 != 3` | `True` |
| `<` | Mniejsze | `3 < 5` | `True` |
| `>` | Większe | `5 > 3` | `True` |
| `<=` | Mniejsze lub równe | `5 <= 5` | `True` |
| `>=` | Większe lub równe | `3 >= 5` | `False` |

Ważna uwaga: **`==` to porównanie**, a **`=` to przypisanie**. To częsty błąd początkujących programistów.

```python
a = 10
b = 20

print(a == b)    # False
print(a != b)    # True
print(a < b)     # True
print(a > b)     # False
print(a <= b)    # True
print(a >= b)    # False
```

Python pozwala na **łańcuchowe porównania**, co jest unikalną cechą tego języka:

```python
x = 15

# Zamiast: if x >= 1 and x <= 100:
if 1 <= x <= 100:
    print("x jest w zakresie 1-100")

# Zamiast: if a < b and b < c:
if a < b < c:
    print("a < b < c")
```

### 2.3. Operatory logiczne

Operatory logiczne służą do łączenia warunków. Python używa angielskich słów kluczowych `and`, `or`, `not` zamiast symboli `&&`, `||`, `!` znanych z C++ czy Javy.

| Operator | Znaczenie | Prawda gdy... |
|---|---|---|
| `and` | Koniunkcja (I) | Oba warunki są `True` |
| `or` | Alternatywa (LUB) | Przynajmniej jeden warunek jest `True` |
| `not` | Negacja (NIE) | Warunek jest `False` |

**Tabela prawdy:**

| `A` | `B` | `A and B` | `A or B` | `not A` |
|---|---|---|---|---|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

```python
wiek = 20
ma_bilet = True

if wiek >= 18 and ma_bilet:
    print("Możesz wejść")

x = 5
if x < 0 or x > 100:
    print("Poza zakresem")
else:
    print("W zakresie")

jest_zamkniety = False
if not jest_zamkniety:
    print("Sklep jest otwarty")
```

### 2.4. Operatory przypisania

Operatory przypisania to skrócona forma zapisu typowych operacji arytmetycznych na zmiennej:

| Operator | Równoważne | Przykład |
|---|---|---|
| `=` | — | `x = 10` |
| `+=` | `x = x + 5` | `x += 5` |
| `-=` | `x = x - 3` | `x -= 3` |
| `*=` | `x = x * 2` | `x *= 2` |
| `/=` | `x = x / 4` | `x /= 4` |
| `//=` | `x = x // 2` | `x //= 2` |
| `%=` | `x = x % 2` | `x %= 2` |
| `**=` | `x = x ** 3` | `x **= 3` |

```python
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x //= 5   # x = 4
x %= 3    # x = 1
```

### 2.5. Operatory przynależności i tożsamości

**Operator `in`** sprawdza, czy element znajduje się w kolekcji (liście, napisie, zbiorze, słowniku). Jest niesamowicie przydatny i czytelny:

```python
lista = [1, 2, 3, 4, 5]
print(3 in lista)         # True
print(6 in lista)         # False
print(6 not in lista)     # True

tekst = "Python"
print("th" in tekst)      # True
print("xyz" in tekst)     # False

# W słowniku sprawdza KLUCZE (nie wartości!)
slownik = {"imie": "Jan", "wiek": 25}
print("imie" in slownik)  # True
print("Jan" in slownik)   # False (to wartość, nie klucz)
```

**Operator `is`** sprawdza **tożsamość obiektów** — czy dwa obiekty to ten sam obiekt w pamięci (nie czy mają tę samą wartość). W praktyce używa się go głównie do porównywania z `None`:

```python
x = None

# ✅ Prawidłowo — porównanie z None zawsze przez is
if x is None:
    print("x jest None")

if x is not None:
    print("x nie jest None")

# ❌ Nieprawidłowo (choć zwykle zadziała)
# if x == None:
```

---

## 3. Instrukcje sterujące

Instrukcje sterujące kontrolują przepływ wykonania programu — pozwalają na podejmowanie decyzji (`if`) oraz wielokrotne wykonywanie bloków kodu (pętle `for`, `while`).

### 3.1. Instrukcja warunkowa `if` / `elif` / `else`

Instrukcja `if` to podstawowy mechanizm podejmowania decyzji w programie. Warunek jest wyrażeniem, które Python ewaluuje do `True` lub `False`. Jeśli jest prawdziwy, wykonywany jest blok kodu wcięty pod `if`.

Słowo kluczowe `elif` (skrót od „else if") pozwala na sprawdzanie kolejnych warunków, a `else` obsługuje przypadek, gdy żaden wcześniejszy warunek nie był spełniony.

```python
liczba = int(input("Podaj liczbę: "))

if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest zerem")
```

**Zagnieżdżone warunki** — instrukcje `if` mogą być umieszczone wewnątrz innych instrukcji `if`:

```python
wiek = 25
posiada_prawo_jazdy = True

if wiek >= 18:
    if posiada_prawo_jazdy:
        print("Może prowadzić")
    else:
        print("Brak prawa jazdy")
else:
    print("Za młody")
```

**Operator trójargumentowy (ternary operator):**

Python oferuje skróconą formę instrukcji warunkowej, zapisywaną w jednej linii. Jest bardzo przydatna przy prostych przypisaniach:

```python
wiek = 20
status = "dorosły" if wiek >= 18 else "niepełnoletni"
print(status)  # dorosły

# Przydatne do szybkiego wyboru wartości
a, b = 5, 10
maksimum = a if a > b else b  # 10
```

### 3.2. Pętla `for`

Pętla `for` w Pythonie działa inaczej niż w większości języków programowania. Zamiast klasycznej pętli liczącej (`for (int i = 0; i < n; i++)` z C++ lub Javy), Python iteruje bezpośrednio po elementach kolekcji — listy, napisu, zakresu liczb itp. To sprawia, że kod jest krótszy i bardziej czytelny, ale wymaga przyzwyczajenia, jeśli znasz inne języki.

Do tworzenia sekwencji liczbowych służy funkcja `range()`, która generuje ciąg wartości bez tworzenia listy w pamięci (to tzw. generator — leniwa ewaluacja).

**Funkcja `range()`** — generuje sekwencję liczb:

| Wywołanie | Generuje | Opis |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | Od 0 do n-1 |
| `range(2, 8)` | 2, 3, 4, 5, 6, 7 | Od start do stop-1 |
| `range(0, 20, 3)` | 0, 3, 6, 9, 12, 15, 18 | Z krokiem 3 |
| `range(10, 0, -1)` | 10, 9, 8, ..., 2, 1 | Odliczanie w dół |
| `range(5, 5)` | (pusto) | Start == stop → nic |

```python
# Iteracja po zakresie liczb
for i in range(5):
    print(i)    # 0, 1, 2, 3, 4

# Zakres od-do (UWAGA: koniec jest WYŁĄCZNY — do 7, nie do 8)
for i in range(2, 8):
    print(i)    # 2, 3, 4, 5, 6, 7

# Zakres z krokiem
for i in range(0, 20, 3):
    print(i)    # 0, 3, 6, 9, 12, 15, 18

# Odliczanie w dół
for i in range(10, 0, -1):
    print(i)    # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

**Iteracja po kolekcjach:**

```python
# Iteracja po liście — zmienna przybiera wartość kolejnego elementu
kolory = ["czerwony", "zielony", "niebieski"]
for kolor in kolory:
    print(kolor)

# Iteracja po napisie — każdy znak osobno
for znak in "Python":
    print(znak)  # P, y, t, h, o, n
```

### 3.3. Funkcja `enumerate()` — iteracja z indeksem

Funkcja `enumerate()` to niezwykle przydatne narzędzie, które podczas iteracji po kolekcji podaje jednocześnie **indeks** i **wartość** każdego elementu. Bez niej trzeba by ręcznie zarządzać licznikiem.

Składnia: `enumerate(kolekcja, start=0)` — domyślnie indeksy zaczynają się od 0, ale można zmienić wartość startową.

```python
owoce = ["jabłko", "banan", "wiśnia", "gruszka"]

# Bez enumerate — trzeba osobno zarządzać indeksem
i = 0
for owoc in owoce:
    print(f"{i}: {owoc}")
    i += 1

# Z enumerate — elegancko i bezpiecznie
for i, owoc in enumerate(owoce):
    print(f"{i}: {owoc}")
# 0: jabłko
# 1: banan
# 2: wiśnia
# 3: gruszka

# Indeksowanie od 1 zamiast od 0
for numer, owoc in enumerate(owoce, start=1):
    print(f"{numer}. {owoc}")
# 1. jabłko
# 2. banan
# 3. wiśnia
# 4. gruszka
```

`enumerate()` zwraca pary `(indeks, element)`, które rozpakowujemy do dwóch zmiennych. Jest szczególnie przydatna, gdy potrzebujemy jednocześnie pozycji elementu i jego wartości — na przykład przy wyszukiwaniu, modyfikowaniu listy, czy wyświetlaniu numerowanych wyników.

### 3.4. Pętla `while`

Pętla `while` powtarza blok kodu **dopóki warunek jest prawdziwy**. Jest odpowiednia, gdy nie wiemy z góry, ile razy pętla powinna się wykonać.

```python
# Podstawowa pętla while — odliczanie
licznik = 5
while licznik > 0:
    print(licznik)
    licznik -= 1
print("Start!")

# Pętla nieskończona z warunkiem wyjścia
while True:
    odpowiedz = input("Czy kontynuować? (t/n): ")
    if odpowiedz == "n":
        break
    print("Kontynuujemy...")
```

**Ważna uwaga:** Pętla `while True:` tworzy pętlę nieskończoną. Jedynym sposobem na wyjście z niej jest instrukcja `break`. Jest to częsty wzorzec w programowaniu — używany np. do menu programu, powtarzania operacji do momentu poprawnego wpisania danych itp.

### 3.5. `break`, `continue` i `else` w pętlach

W trakcie wykonywania pętli może zajść potrzeba przerwania jej działania, pominięcia pewnych iteracji, lub wykonania kodu po jej naturalnym zakończeniu. Do tego służą trzy słowa kluczowe, które dają precyzyjną kontrolę nad przebiegiem pętli:

| Słowo kluczowe | Działanie |
|---|---|
| `break` | Natychmiast kończy pętlę (wyjście) |
| `continue` | Pomija resztę bieżącej iteracji, przechodzi do następnej |
| `else` (po pętli) | Wykonuje się, gdy pętla zakończyła się **bez** `break` |

```python
# break — przerywa pętlę po znalezieniu elementu
for i in range(10):
    if i == 5:
        print(f"Znaleziono {i}, przerywam!")
        break
    print(i)
# Wypisze: 0, 1, 2, 3, 4, Znaleziono 5, przerywam!

# continue — pomija parzyste, wypisuje nieparzyste
for i in range(10):
    if i % 2 == 0:
        continue    # Pomiń tę iterację
    print(i)
# Wypisze: 1, 3, 5, 7, 9

# else w pętli — rzadko używane, ale przydatne
for i in range(10):
    if i == 100:  # Nigdy nie będzie True
        break
else:
    print("Pętla zakończyła się normalnie (bez break)")
# To się WYKONA, bo break nie został użyty
```

### 3.6. Pętle zagnieżdżone

Pętle zagnieżdżone to pętle umieszczone wewnątrz innych pętli. Zewnętrzna pętla wykonuje się raz, a dla każdej jej iteracji wewnętrzna pętla wykonuje się od początku do końca. Są niezbędne do pracy z tablicami dwuwymiarowymi i algorytmami sortowania.

```python
# Tabliczka mnożenia 5×5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4d}", end="")
    print()  # Nowa linia po każdym wierszu

# Wynik:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

---

## 4. Struktury danych

Python oferuje kilka wbudowanych typów kolekcji, z których każdy ma swoje zastosowanie. Wybór odpowiedniej struktury danych jest jedną z najważniejszych decyzji przy pisaniu programu — wpływa na wydajność, czytelność i łatwość modyfikacji kodu. Znajomość właściwości każdego typu pozwala wybrać ten najlepiej pasujący do danego problemu.

Poniższa tabela podsumowuje kluczowe różnice:

| Struktura | Modyfikowalna | Uporządkowana | Duplikaty | Składnia |
|---|---|---|---|---|
| `list` | ✅ Tak | ✅ Tak | ✅ Tak | `[1, 2, 3]` |
| `tuple` | ❌ Nie | ✅ Tak | ✅ Tak | `(1, 2, 3)` |
| `dict` | ✅ Tak | ✅ Tak (od 3.7) | ❌ Klucze unikalne | `{"a": 1}` |
| `set` | ✅ Tak | ❌ Nie | ❌ Nie | `{1, 2, 3}` |

### 4.1. Listy (`list`)

Lista jest **najważniejszą** i najczęściej używaną strukturą danych w Pythonie. Pełni rolę tablicy (array) z innych języków, ale jest znacznie bardziej elastyczna — może przechowywać elementy różnych typów, automatycznie zmienia swój rozmiar, i oferuje bogaty zestaw wbudowanych metod.

**Tworzenie list:**

```python
pusta_lista = []
liczby = [1, 2, 3, 4, 5]
mieszana = [1, "dwa", 3.0, True]         # Różne typy w jednej liście
zera = [0] * 10                           # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zakres = list(range(1, 11))               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
znaki = list("Python")                    # ['P', 'y', 't', 'h', 'o', 'n']
```

**Indeksowanie — dostęp do elementów:**

Indeksy w Pythonie zaczynają się od `0`. Można też używać indeksów ujemnych, które liczą od końca listy:

```
 Indeks dodatni:   0     1     2     3     4
                 [10,   20,   30,   40,   50]
 Indeks ujemny:   -5    -4    -3    -2    -1
```

```python
lista = [10, 20, 30, 40, 50]

print(lista[0])      # 10   — pierwszy element
print(lista[2])      # 30   — trzeci element
print(lista[-1])     # 50   — ostatni element
print(lista[-2])     # 40   — przedostatni element
```

**Wycinanie (slicing)** — pozwala wybrać fragment listy. Składnia: `lista[start:stop:krok]`, gdzie `stop` jest **wyłączny**:

```python
lista = [10, 20, 30, 40, 50]

print(lista[1:4])    # [20, 30, 40] — od indeksu 1 do 3 (4 jest wyłączny)
print(lista[:3])     # [10, 20, 30] — pierwsze 3 elementy
print(lista[2:])     # [30, 40, 50] — od indeksu 2 do końca
print(lista[::2])    # [10, 30, 50] — co drugi element
print(lista[::-1])   # [50, 40, 30, 20, 10] — odwrócona lista
```

**Modyfikacja listy:**

```python
lista = [1, 2, 3, 4, 5]

# Zmiana elementu pod konkretnym indeksem
lista[0] = 99                # [99, 2, 3, 4, 5]

# Dodawanie elementów
lista.append(6)              # Dodaje na koniec → [99, 2, 3, 4, 5, 6]
lista.insert(0, 0)           # Wstawia na indeks 0 → [0, 99, 2, 3, 4, 5, 6]
lista.extend([7, 8])         # Dodaje wiele elementów → [0, 99, 2, 3, 4, 5, 6, 7, 8]

# Usuwanie elementów
lista.remove(99)             # Usuwa PIERWSZE wystąpienie wartości 99
element = lista.pop()        # Usuwa i ZWRACA ostatni element
element = lista.pop(0)       # Usuwa i ZWRACA element o indeksie 0
del lista[2]                 # Usuwa element o indeksie 2 (bez zwracania)
lista.clear()                # Usuwa WSZYSTKIE elementy → []
```

**Przydatne metody i operacje:**

```python
lista = [3, 1, 4, 1, 5, 9, 2, 6]

# Informacje o liście
print(len(lista))            # 8    — liczba elementów
print(min(lista))            # 1    — wartość minimalna
print(max(lista))            # 9    — wartość maksymalna
print(sum(lista))            # 31   — suma elementów

# Wyszukiwanie
print(lista.index(4))        # 2    — indeks PIERWSZEGO wystąpienia
print(lista.count(1))        # 2    — ile razy wartość 1 występuje
print(5 in lista)            # True — czy element jest w liście

# Sortowanie
lista.sort()                 # Sortuje rosnąco NA MIEJSCU (modyfikuje listę)
lista.sort(reverse=True)     # Sortuje malejąco NA MIEJSCU

# Sortowanie BEZ modyfikacji oryginału — funkcja sorted()
nowa = sorted(lista)                # Zwraca NOWĄ posortowaną listę
nowa = sorted(lista, reverse=True)  # Malejąco

# Odwracanie
lista.reverse()              # Odwraca NA MIEJSCU
nowa = lista[::-1]           # Zwraca NOWĄ odwróconą listę (oryginał bez zmian)

# Kopiowanie listy
kopia = lista.copy()         # Tworzy płytką kopię
kopia = lista[:]             # Alternatywna forma kopiowania
# UWAGA: kopia = lista NIE kopiuje — obie zmienne wskazują na TĘ SAMĄ listę!
```

**List comprehension (wyrażenia listowe):**

List comprehension to elegancki, jednoliniowy sposób tworzenia list na podstawie wyrażenia. To jeden z najbardziej „pythonowych" wzorców — pozwala zastąpić kilka linii pętli `for` jednym czytelnym wyrażeniem:

```python
# Kwadraty liczb 0–9
kwadraty = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tylko parzyste z zakresu 0–19
parzyste = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformacja — zamiana na wielkie litery
imiona = ["jan", "anna", "piotr"]
wielkie = [imie.upper() for imie in imiona]
# ["JAN", "ANNA", "PIOTR"]

# Równoważna forma z pętlą (dłuższa):
wielkie = []
for imie in imiona:
    wielkie.append(imie.upper())
```

### 4.2. Krotki (`tuple`)

Krotka jest **niemodyfikowalną** (immutable) wersją listy. Po utworzeniu nie można zmienić jej elementów — nie można dodawać, usuwać ani modyfikować. Krotki są szybsze od list i mogą służyć jako klucze słownika (czego lista nie może).

```python
# Tworzenie krotek
punkt = (3, 5)
kolory = ("red", "green", "blue")
jeden = (42,)              # UWAGA: krotka jednoelementowa MUSI mieć przecinek!
nie_krotka = (42)          # To jest zwykła liczba 42, nie krotka!

# Dostęp do elementów — identycznie jak w liście
print(kolory[0])           # "red"
print(kolory[-1])          # "blue"
print(len(kolory))         # 3
```

**Rozpakowanie krotki (tuple unpacking):**

To niezwykle przydatna technika — pozwala przypisać elementy krotki do osobnych zmiennych w jednej instrukcji:

```python
punkt = (3, 5)
x, y = punkt
print(x, y)                # 3 5

# Funkcja zwracająca krotkę
def podziel(a, b):
    return a // b, a % b   # Python automatycznie tworzy krotkę

iloraz, reszta = podziel(17, 5)
print(iloraz, reszta)      # 3 2

# Zamiana wartości dwóch zmiennych — idiom Pythona
a, b = 1, 2
a, b = b, a    # Teraz a=2, b=1 (bez zmiennej tymczasowej!)
```

### 4.3. Słowniki (`dict`)

Słownik przechowuje pary **klucz → wartość** (key-value pairs). Klucze muszą być unikalne i niemodyfikowalne (np. `str`, `int`, `tuple`), a wartości mogą być dowolnego typu. Słowniki są zoptymalizowane pod kątem szybkiego wyszukiwania po kluczu.

```python
# Tworzenie słownika
pusty = {}
osoba = {"imie": "Jan", "wiek": 25, "miasto": "Warszawa"}

# Dostęp do wartości
print(osoba["imie"])                   # "Jan"
print(osoba.get("wiek"))              # 25
print(osoba.get("telefon", "brak"))   # "brak" — wartość domyślna gdy brak klucza
# osoba["telefon"]                     # KeyError! — klucz nie istnieje

# Dodawanie i modyfikacja
osoba["email"] = "jan@mail.com"       # Dodaje nowy klucz
osoba["wiek"] = 26                    # Modyfikuje istniejący

# Usuwanie
del osoba["miasto"]
wartosc = osoba.pop("email")          # Usuwa i zwraca wartość

# Sprawdzanie obecności klucza
if "imie" in osoba:
    print("Klucz 'imie' istnieje")
```

**Iteracja po słowniku:**

```python
osoba = {"imie": "Jan", "wiek": 25, "miasto": "Kraków"}

# Po kluczach (domyślnie)
for klucz in osoba:
    print(klucz)

# Po wartościach
for wartosc in osoba.values():
    print(wartosc)

# Po parach (klucz, wartość)
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")
```

**Zastosowanie: liczenie wystąpień — bardzo częsty wzorzec:**

```python
tekst = "programowanie"
wystapienia = {}

for znak in tekst:
    if znak in wystapienia:
        wystapienia[znak] += 1
    else:
        wystapienia[znak] = 1

print(wystapienia)
# {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 2, 'm': 1, ...}
```

**Zastosowanie: mapowanie wartości — konwersja liczba → tekst:**

```python
slownie = {
    1: "jeden", 2: "dwa", 3: "trzy",
    4: "cztery", 5: "pięć", 6: "sześć"
}

liczba = 3
print(slownie[liczba])            # "trzy"
print(slownie.get(7, "nieznana")) # "nieznana" — bezpieczne pobranie
```

### 4.4. Zbiory (`set`)

Zbiór to kolekcja **unikalnych** elementów — automatycznie eliminuje duplikaty. Nie zachowuje kolejności elementów. Jest zoptymalizowany do sprawdzania, czy element istnieje w zbiorze (operacja `in` jest bardzo szybka).

```python
# Tworzenie zbiorów
pusty = set()              # UWAGA: {} to pusty SŁOWNIK, nie zbiór!
liczby = {1, 2, 3, 4, 5}
z_listy = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} — duplikaty usunięte

# Operacje
liczby.add(6)              # Dodaje element
liczby.remove(3)           # Usuwa (błąd jeśli nie istnieje)
liczby.discard(99)         # Usuwa (BEZ błędu jeśli nie istnieje)

# Operacje na zbiorach
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}  — suma (union)
print(a & b)   # {3, 4}              — przecięcie (intersection)
print(a - b)   # {1, 2}              — różnica (difference)
```

**Praktyczne zastosowanie — usuwanie duplikatów z listy:**

```python
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unikalne = list(set(lista))
print(unikalne)  # [1, 2, 3, 4] (kolejność może się różnić)
```

### 4.5. Zagnieżdżone struktury danych

W praktyce rzadko pracujemy z prostymi, płaskimi listami. Znacznie częściej spotykamy się z danymi złożonymi — listami słowników, słownikami list, a nawet listami list słowników. Umiejętność swobodnego poruszania się po takich strukturach jest kluczowa.

**Lista słowników — najczęstszy wzorzec:**

To podstawowy sposób przechowywania kolekcji obiektów (np. lista uczniów, produktów, zamówień):

```python
uczniowie = [
    {"imie": "Jan", "wiek": 17, "oceny": [4, 5, 3]},
    {"imie": "Anna", "wiek": 16, "oceny": [5, 5, 5]},
    {"imie": "Piotr", "wiek": 18, "oceny": [3, 4, 2]}
]

# Dostęp do danych
print(uczniowie[0]["imie"])            # "Jan"
print(uczniowie[1]["oceny"][2])        # 5 (trzecia ocena Anny)

# Iteracja po liście słowników
for uczen in uczniowie:
    srednia = sum(uczen["oceny"]) / len(uczen["oceny"])
    print(f"{uczen['imie']}: średnia {srednia:.2f}")
# Jan: średnia 4.00
# Anna: średnia 5.00
# Piotr: średnia 3.00
```

**Sortowanie listy słowników:**

```python
# Sortowanie po imieniu (alfabetycznie)
posortowani = sorted(uczniowie, key=lambda u: u["imie"])

# Sortowanie po wieku (malejąco)
posortowani = sorted(uczniowie, key=lambda u: u["wiek"], reverse=True)

# Sortowanie po średniej ocen
posortowani = sorted(uczniowie, key=lambda u: sum(u["oceny"]) / len(u["oceny"]), reverse=True)
```

**Słownik list — grupowanie danych:**

```python
katalog = {
    "owoce": ["jabłko", "banan", "gruszka"],
    "warzywa": ["marchew", "ziemniak", "cebula"],
    "napoje": ["woda", "sok", "herbata"]
}

# Dostęp
print(katalog["owoce"][0])           # "jabłko"

# Dodanie elementu do konkretnej listy
katalog["owoce"].append("pomarańcza")

# Iteracja po grupach
for kategoria, produkty in katalog.items():
    print(f"\n{kategoria.upper()}:")
    for produkt in produkty:
        print(f"  - {produkt}")
```

**Wyszukiwanie w zagnieżdżonych strukturach:**

```python
# Znajdź ucznia po imieniu
def znajdz_ucznia(uczniowie, imie):
    for uczen in uczniowie:
        if uczen["imie"] == imie:
            return uczen
    return None

uczen = znajdz_ucznia(uczniowie, "Anna")
if uczen:
    print(f"Znaleziono: {uczen['imie']}, wiek: {uczen['wiek']}")
else:
    print("Nie znaleziono")
```

---

## 5. Funkcje

Funkcje to wielokrotnie używalne bloki kodu, które wykonują określone zadanie. Pozwalają na organizację programu w logiczne, niezależne części. Poprawiają czytelność kodu i eliminują powtórzenia.

W Pythonie funkcje definiujemy słowem kluczowym `def`, po którym następuje nazwa funkcji, nawiasy z ewentualnymi parametrami i dwukropek.

### 5.1. Definicja i wywoływanie funkcji

Funkcja może nie przyjmować parametrów, przyjmować jeden lub wiele, a także może (ale nie musi) zwracać wartość.

```python
# Funkcja bez parametrów i bez wartości zwracanej
def powitanie():
    print("Witaj w programie!")

powitanie()  # Wywołanie — samo wpisanie nazwy z nawiasami

# Funkcja z parametrami
def powitaj(imie):
    print(f"Cześć, {imie}!")

powitaj("Anna")  # Cześć, Anna!

# Funkcja z wartością zwracaną (return)
def dodaj(a, b):
    return a + b

wynik = dodaj(3, 5)
print(wynik)  # 8

# Funkcja z wieloma wartościami zwracanymi (krotka)
def podziel_z_reszta(a, b):
    iloraz = a // b
    reszta = a % b
    return iloraz, reszta

i, r = podziel_z_reszta(17, 5)
print(f"Iloraz: {i}, Reszta: {r}")  # Iloraz: 3, Reszta: 2
```

Jeśli funkcja nie ma instrukcji `return` lub ma `return` bez wartości, domyślnie zwraca `None`.

### 5.2. Parametry domyślne

Parametry domyślne pozwalają na wywoływanie funkcji bez podawania wszystkich argumentów — te z wartością domyślną zostaną automatycznie uzupełnione. Parametry z wartościami domyślnymi muszą być **na końcu** listy parametrów.

```python
def powitaj(imie, powitanie="Cześć"):
    print(f"{powitanie}, {imie}!")

powitaj("Jan")                    # Cześć, Jan!
powitaj("Jan", "Witaj")           # Witaj, Jan!
powitaj("Jan", powitanie="Hej")   # Hej, Jan!
```

**Wzorzec z `None` — zamiennik przeciążania funkcji:**

W Pythonie nie można mieć dwóch funkcji o tej samej nazwie, ale z różnymi parametrami (tak jak w Javie czy C++). Zamiast tego stosuje się parametr domyślny `None` i sprawdzanie warunku wewnątrz funkcji:

```python
def utworz_element(wartosc=None):
    if wartosc is None:
        print("Tworzenie pustego elementu")
        return 0
    else:
        print(f"Tworzenie elementu z wartością: {wartosc}")
        return wartosc

utworz_element()          # Tworzenie pustego elementu
utworz_element(42)        # Tworzenie elementu z wartością: 42
```

Ten wzorzec jest szczególnie ważny w kontekście konstruktorów klas (omówiony szczegółowo w rozdziale 12).

### 5.3. Argumenty pozycyjne i nazwane

Python pozwala na przekazywanie argumentów zarówno na podstawie pozycji, jak i nazwy:

```python
def info(imie, wiek, miasto):
    print(f"{imie}, {wiek} lat, {miasto}")

# Argumenty pozycyjne — kolejność ma znaczenie
info("Jan", 25, "Warszawa")

# Argumenty nazwane — kolejność NIE ma znaczenia
info(miasto="Kraków", imie="Anna", wiek=30)

# Mieszane — pozycyjne MUSZĄ być przed nazwanymi
info("Piotr", miasto="Gdańsk", wiek=22)
```

### 5.4. Zmienna liczba argumentów — *args i **kwargs

W sytuacjach, gdy nie wiemy z góry, ile argumentów zostanie przekazanych do funkcji, z pomocą przychodzą specjalne operatory `*args` oraz `**kwargs`. Są one szczególnie przydatne, gdy chcemy napisać elastyczne funkcje, dekoratory, lub przekazywać argumenty w dziedziczeniu klas (do `super().__init__()`).

**Argumenty zmiennej długości — `*args` (Arbitrary Arguments):**

Użycie pojedynczej gwiazdki `*` przed nazwą parametru sprawia, że funkcja staje się zdolna do przyjęcia dowolnej liczby argumentów **pozycyjnych**. Wewnątrz funkcji stają się one dostępne jako krotka (tuple).

```python
def suma_wielu(*args):
    # args to tuple, np. (1, 2, 3, 4)
    suma = 0
    for liczba in args:
        suma += liczba
    return suma

print(suma_wielu(5, 10))          # 15
print(suma_wielu(1, 2, 3, 4, 5))  # 15
print(suma_wielu())               # 0

def powitaj_grupe(*imiona):
    for imie in imiona:
        print(f"Cześć, {imie}!")

powitaj_grupe("Jan", "Anna", "Piotr")
```

👉 *Wskazówka:* Nazwa `args` to tylko konwencja (od ang. *arguments*). Ważny jest znak `*`, możesz nazwać parametr `*imiona` czy `*liczby`.

**Pary klucz-wartość — `**kwargs` (Arbitrary Keyword Arguments):**

Dwie gwiazdki `**` pozwalają na przekazanie dowolnej liczby argumentów **nazwanych** (klucz=wartość). Wewnątrz funkcji są one zapisywane jako słownik (dictionary).

```python
def wyswietl_dane_osobowe(**kwargs):
    # kwargs to słownik, np. {'imie': 'Jan', 'wiek': 25}
    for klucz, wartosc in kwargs.items():
        print(f"{klucz.capitalize()}: {wartosc}")

wyswietl_dane_osobowe(imie="Jan", wiek=25, miasto="Warszawa")
# Imie: Jan
# Wiek: 25
# Miasto: Warszawa

wyswietl_dane_osobowe(stanowisko="Programista", pensja=5000)
```

👉 *Wskazówka:* Podobnie jak z `args`, nazwa `kwargs` (od *keyword arguments*) to konwencja. Kluczowe są znaki `**`.

**Łączenie zwykłych argumentów, `*args` i `**kwargs`:**

Możesz łączyć te mechanizmy w jednej funkcji, jednak musisz bezwzględnie zachować następującą kolejność w definicji:
1. Argumenty podstawowe (pozycyjne)
2. `*args`
3. Parametry ze zdefiniowaną wartością domyślną
4. `**kwargs`

```python
def zloz_zamowienie(klient, *produkty, dostawa="Standard", **opcje_dodatkowe):
    print(f"Zamówienie dla: {klient}")
    
    print("Mój koszyk:")
    for produkt in produkty:
        print(f"- {produkt}")
        
    print(f"Typ dostawy: {dostawa}")
    
    if opcje_dodatkowe:
        print("Opcje dodatkowe:")
        for opcja, wartosc in opcje_dodatkowe.items():
            print(f"- {opcja}: {wartosc}")

zloz_zamowienie(
    "Anna Nowak",            # argument podstawowy (klient)
    "Myszka", "Klawiatura",  # *args (produkty)
    dostawa="Express",       # nadpisanie parametru domyślnego
    faktura=True,            # **kwargs (opcje_dodatkowe)
    pakowanie_prezent=False  # **kwargs (opcje_dodatkowe)
)
```

**Rozpakowywanie argumentów (Unpacking):**

Gwiazdki działają również w drugą stronę! Jeśli masz już listę lub słownik układający się w odpowiednie parametry, możesz użyć `*` by "rozpakować" listę na argumenty pozycyjne lub `**` by rozpakować słownik na nazwane.

```python
dane = [3, 4, 5]
print(suma_wielu(*dane))  # równe wywołaniu suma_wielu(3, 4, 5)

osoba = {"imie": "Marek", "wiek": 40}
wyswietl_dane_osobowe(**osoba) # równe wywołaniu wyswietl_dane_osobowe(imie="Marek", wiek=40)
```

To używany wzorzec m.in. przy rozszerzaniu konstruktorów z użyciem funkcji `super()`, gdy podrzędna klasa przyjmuje szerszą liczbę argumentów, które po prostu podaje dalej do konstruktora rodzica.

### 5.5. Argumenty tylko pozycyjne (/) i tylko nazwane (*)

W nowszych wersjach Pythona (3.8+) wprowadzono symbole `/` oraz `*` w definicji parametrów funkcji, aby jawnie określić, jak argumenty mogą być przekazywane. Pozwala to na większą kontrolę nad API funkcji i zapobiega pomyłkom.

**Argumenty tylko pozycyjne (`/`):**

Wszystkie parametry znajdujące się **przed** symbolem `/` muszą zostać przekane wyłącznie na podstawie pozycji. Nie można użyć ich nazw.

```python
def pole_prostokata(a, b, /):
    return a * b

print(pole_prostokata(5, 10))    # ✅ OK (pozycyjne)
# print(pole_prostokata(a=5, b=10)) # ❌ TypeError: positional-only arguments
```

**Argumenty tylko nazwane (`*`):**

Wszystkie parametry znajdujące się **po** symbolu `*` muszą zostać przekazane wyłącznie jako argumenty nazwane. Często stosowane, aby uniknąć pomyłek przy wielu parametrach logicznych.

```python
def wyslij_wiadomosc(tresc, *, pilne=False, do_logow=True):
    print(f"Wysyłanie: {tresc} (Pilne: {pilne})")

wyslij_wiadomosc("Dzień dobry", pilne=True) # ✅ OK
# wyslij_wiadomosc("Hej", True)            # ❌ TypeError: takes 1 positional argument but 2 were given
```

**Kompletna składnia mieszana:**

```python
def func(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)

func(10, standard=20, kw_only=30) # ✅ OK
func(10, 20, kw_only=30)          # ✅ OK
```

### 5.6. Zasięg zmiennych (scope)

Zmienne utworzone wewnątrz funkcji są **lokalne** — nie istnieją poza funkcją. Zmienne utworzone poza funkcjami są **globalne** — są widoczne w całym programie. Zrozumienie tego mechanizmu jest kluczowe do unikania błędów.

```python
x = 10  # Zmienna globalna

def funkcja():
    x = 20  # Zmienna LOKALNA — to inna zmienna niż globalne x!
    print(f"Wewnątrz: {x}")  # 20

funkcja()
print(f"Na zewnątrz: {x}")  # 10 — globalne x nie zostało zmienione

# Aby zmodyfikować zmienną globalną wewnątrz funkcji, trzeba użyć 'global'
def funkcja_global():
    global x
    x = 99

funkcja_global()
print(f"Po zmianie: {x}")  # 99
```

W praktyce należy unikać `global` — lepiej przekazywać dane jako parametry i zwracać wyniki przez `return`.

### 5.7. Funkcja `lambda` — funkcje anonimowe

Lambda to krótka, jednolinijkowa funkcja anonimowa (bez nazwy). Składnia: `lambda parametry: wyrażenie`. Lambda automatycznie zwraca wynik wyrażenia — nie używamy słowa `return`.

```python
# Zwykła funkcja
def kwadrat(x):
    return x ** 2

# Odpowiednik lambda
kwadrat = lambda x: x * 2

print(kwadrat(5))  # 10

# Lambda jest szczególnie przydatna jako argument sortowania
osoby = [("Jan", 30), ("Anna", 25), ("Piotr", 35)]
osoby.sort(key=lambda osoba: osoba[1])
print(osoby)  # [('Anna', 25), ('Jan', 30), ('Piotr', 35)]

# Sortowanie listy słowników
pracownicy = [
    {"imie": "Jan", "pensja": 5000},
    {"imie": "Anna", "pensja": 7000},
    {"imie": "Piotr", "pensja": 4500}
]
pracownicy.sort(key=lambda p: p["pensja"], reverse=True)
# Posortowani malejąco wg pensji
```

### 5.8. Funkcje wbudowane — przegląd najważniejszych

Python oferuje wiele wbudowanych funkcji, które nie wymagają importowania żadnego modułu:

| Funkcja | Opis | Przykład |
|---|---|---|
| `len()` | Długość kolekcji/napisu | `len([1,2,3])` → `3` |
| `print()` | Wyświetlanie | `print("Hej")` |
| `input()` | Pobieranie danych | `input("Podaj: ")` |
| `type()` | Typ obiektu | `type(42)` → `<class 'int'>` |
| `int()`, `float()`, `str()` | Konwersja typów | `int("5")` → `5` |
| `abs()` | Wartość bezwzględna | `abs(-7)` → `7` |
| `round()` | Zaokrąglenie | `round(3.7)` → `4` |
| `min()`, `max()` | Minimum / maksimum | `min(3,1,7)` → `1` |
| `sum()` | Suma elementów | `sum([1,2,3])` → `6` |
| `sorted()` | Sortowanie (nowa lista) | `sorted([3,1,2])` → `[1,2,3]` |
| `range()` | Zakres liczb | `range(5)` → 0,1,2,3,4 |
| `enumerate()` | Iteracja z indeksem | Patrz 3.3 |
| `zip()` | Łączenie kolekcji | Patrz niżej |
| `map()` | Zastosowanie funkcji | `map(str, [1,2])` → "1","2" |
| `isinstance()` | Sprawdzenie typu | `isinstance(5, int)` → `True` |

**Funkcja `zip()` — łączenie kolekcji:**

Funkcja `zip()` łączy elementy z dwóch (lub więcej) kolekcji w pary, krotkę po krotce:

```python
imiona = ["Jan", "Anna", "Piotr"]
wiek = [25, 30, 22]

# zip() tworzy pary z elementów o tym samym indeksie
for imie, w in zip(imiona, wiek):
    print(f"{imie}: {w} lat")
# Jan: 25 lat
# Anna: 30 lat
# Piotr: 22 lat

# Przydatne do tworzenia słowników
slownik = dict(zip(imiona, wiek))
print(slownik)  # {'Jan': 25, 'Anna': 30, 'Piotr': 22}

# zip() z wagami — częste w algorytmach walidacji
cyfry = [1, 2, 3, 4]
wagi = [7, 3, 1, 9]
suma = sum(c * w for c, w in zip(cyfry, wagi))
print(suma)  # 1*7 + 2*3 + 3*1 + 4*9 = 52
```

**Funkcja `map()` — zastosowanie funkcji do każdego elementu:**

```python
# Konwersja listy stringów na inty
numery_str = ["1", "2", "3", "4", "5"]
numery_int = list(map(int, numery_str))
print(numery_int)  # [1, 2, 3, 4, 5]

# Podniesienie do kwadratu
kwadraty = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(kwadraty)  # [1, 4, 9, 16]
```

---

## 6. Przetwarzanie łańcuchów znaków

Łańcuchy znaków (`str`) w Pythonie są **niemodyfikowalne** (immutable) — nie można zmienić pojedynczego znaku w istniejącym napisie. Każda operacja „modyfikująca" napis tak naprawdę tworzy nowy napis. Python natywnie obsługuje Unicode, więc polskie i inne znaki diakrytyczne działają bezproblemowo.

### 6.1. Podstawowe operacje na napisach

```python
tekst = "Programowanie w Pythonie"

# Długość napisu
print(len(tekst))           # 24

# Indeksowanie — identycznie jak w listach
print(tekst[0])             # "P"
print(tekst[-1])            # "e"
print(tekst[5])             # "a"

# Slicing (wycinanie)
print(tekst[0:5])           # "Progr"
print(tekst[:5])            # "Progr"
print(tekst[16:])           # "Pythonie"
print(tekst[::-1])          # "einohtyP w einawomargorP" — odwrócenie

# Konkatenacja (łączenie napisów)
imie = "Jan"
nazwisko = "Kowalski"
pelne = imie + " " + nazwisko  # "Jan Kowalski"

# Powtarzanie napisu
kreska = "-" * 40            # "----------------------------------------"
print(kreska)
```

### 6.2. Metody napisów — kompletny przegląd

Metody napisów nie modyfikują oryginału — zwracają nowy napis. Oto najważniejsze:

**Zmiana wielkości liter:**

| Metoda | Opis | Przykład | Wynik |
|---|---|---|---|
| `.upper()` | Wszystkie wielkie | `"abc".upper()` | `"ABC"` |
| `.lower()` | Wszystkie małe | `"ABC".lower()` | `"abc"` |
| `.capitalize()` | Pierwsza wielka | `"abc def".capitalize()` | `"Abc def"` |
| `.title()` | Każde słowo wielka | `"abc def".title()` | `"Abc Def"` |
| `.swapcase()` | Zamiana wielkości | `"AbC".swapcase()` | `"aBc"` |

**Wyszukiwanie i analiza:**

| Metoda | Opis | Wynik gdy znaleziono | Wynik gdy nie |
|---|---|---|---|
| `.find(x)` | Indeks pierwszego wystąpienia | Indeks (int) | `-1` |
| `.index(x)` | Indeks pierwszego wystąpienia | Indeks (int) | `ValueError` |
| `.count(x)` | Liczba wystąpień | Liczba (int) | `0` |
| `.startswith(x)` | Czy zaczyna się od x | `True` | `False` |
| `.endswith(x)` | Czy kończy się na x | `True` | `False` |

```python
tekst = "Programowanie w Pythonie"

print(tekst.find("Python"))     # 16
print(tekst.find("Java"))       # -1 (nie znaleziono)
print(tekst.count("o"))         # 2
print(tekst.startswith("Progr"))# True
print("@" in "email@domena.pl") # True — operator in działa też na napisach
```

**Modyfikacja (tworzenie nowego napisu):**

```python
tekst = "  Witaj, Świecie!  "

# Usuwanie białych znaków
print(tekst.strip())        # "Witaj, Świecie!" — z obu stron
print(tekst.lstrip())       # "Witaj, Świecie!  " — tylko z lewej
print(tekst.rstrip())       # "  Witaj, Świecie!" — tylko z prawej

# Zamiana fragmentu
tekst2 = "Programowanie w Pythonie"
print(tekst2.replace("Python", "Java"))  # "Programowanie w Javie"

# Dzielenie na listę
zdanie = "jeden,dwa,trzy,cztery"
czesci = zdanie.split(",")         # ["jeden", "dwa", "trzy", "cztery"]

slowa = "Witaj swiecie jak tam".split()  # Domyślnie dzieli po spacjach
# ["Witaj", "swiecie", "jak", "tam"]

# Łączenie listy w napis — metoda wywoływana na SEPARATORZE
lista = ["A", "B", "C"]
print(", ".join(lista))          # "A, B, C"
print(" | ".join(lista))         # "A | B | C"
print("".join(lista))            # "ABC"
```

### 6.3. Sprawdzanie rodzaju znaków

Te metody są bardzo przydatne przy walidacji danych wejściowych:

| Metoda | Zwraca `True` gdy... | Przykład |
|---|---|---|
| `.isdigit()` | Same cyfry | `"123".isdigit()` → `True` |
| `.isalpha()` | Same litery | `"abc".isalpha()` → `True` |
| `.isalnum()` | Litery i/lub cyfry | `"abc123".isalnum()` → `True` |
| `.isspace()` | Same białe znaki | `"   ".isspace()` → `True` |
| `.isupper()` | Same wielkie litery | `"ABC".isupper()` → `True` |
| `.islower()` | Same małe litery | `"abc".islower()` → `True` |

### 6.4. Kody znaków — `ord()` i `chr()`

Te dwie funkcje pozwalają na konwersję między znakiem a jego kodem numerycznym (ASCII/Unicode). Są fundamentalne przy algorytmach szyfrujących, przetwarzaniu na poziomie pojedynczych znaków i operacjach na alfabecie.

| Funkcja | Kierunek | Przykład | Wynik |
|---|---|---|---|
| `ord(znak)` | Znak → liczba | `ord('A')` | `65` |
| `chr(liczba)` | Liczba → znak | `chr(65)` | `'A'` |

**Kluczowe zakresy kodów ASCII:**

| Znaki | Zakres kodów | Pierwszy | Ostatni |
|---|---|---|---|
| Cyfry `0`–`9` | 48–57 | `ord('0')` = 48 | `ord('9')` = 57 |
| Wielkie `A`–`Z` | 65–90 | `ord('A')` = 65 | `ord('Z')` = 90 |
| Małe `a`–`z` | 97–122 | `ord('a')` = 97 | `ord('z')` = 122 |
| Spacja | 32 | `ord(' ')` = 32 | — |

```python
print(ord('A'))    # 65
print(ord('a'))    # 97
print(ord('0'))    # 48
print(chr(65))     # 'A'
print(chr(97))     # 'a'
```

**Przesunięcie znaku w alfabecie z zawijaniem:**

To kluczowy wzorzec stosowany w szyfrach i algorytmach operujących na literach. Zawijanie oznacza, że po `z` wracamy do `a`:

```python
def przesun_znak(znak, przesuniecie):
    if 'a' <= znak <= 'z':
        numer = ord(znak) - ord('a')           # a=0, b=1, ..., z=25
        nowy_numer = (numer + przesuniecie) % 26  # Modulo 26 = zawijanie
        return chr(nowy_numer + ord('a'))
    return znak  # Znak spoza zakresu a-z zwracamy bez zmian

print(przesun_znak('a', 3))    # 'd'
print(przesun_znak('x', 5))    # 'c' (zawinięcie: x→y→z→a→b→c)
print(przesun_znak('d', -3))   # 'a'
print(przesun_znak(' ', 5))    # ' ' (spacja — bez zmian)
```

### 6.5. Iteracja po znakach i budowanie nowego napisu

Ponieważ napisy w Pythonie są niemodyfikowalne, tworzenie nowego napisu wymaga jednej z dwóch technik:

```python
tekst = "Python"

# Technika 1: Konkatenacja (łączenie) — prosta, ale wolna dla długich napisów
nowy = ""
for znak in tekst:
    nowy += znak.upper()
print(nowy)  # "PYTHON"

# Technika 2: Lista + join — efektywniejsza
nowy = "".join([znak.upper() for znak in tekst])
print(nowy)  # "PYTHON"
```

### 6.6. Obsługa polskich znaków

Python 3 natywnie obsługuje Unicode, więc polskie znaki nie wymagają żadnej specjalnej konfiguracji. Warto jednak pamiętać o nich przy operacjach na literach (np. zliczanie samogłosek):

```python
samogloski = "aąeęiouóyAĄEĘIOUÓY"

def policz_samogloski(tekst):
    licznik = 0
    for znak in tekst:
        if znak in samogloski:
            licznik += 1
    return licznik

print(policz_samogloski("Zażółć gęślą jaźń"))  # 6
```

### 6.7. Przydatne wzorce przetwarzania tekstu

Kilka często spotykanych wzorców przetwarzania napisów, które warto znać:

**Odwracanie kolejności słów w zdaniu:**

```python
zdanie = "Python jest super"
slowa = zdanie.split()           # ["Python", "jest", "super"]
slowa.reverse()                  # ["super", "jest", "Python"]
wynik = " ".join(slowa)          # "super jest Python"

# Lub jednolinijkowo:
wynik = " ".join(zdanie.split()[::-1])
```

**Sprawdzanie czy napis jest palindromem:**

Palindrom to napis, który czyta się tak samo od przodu i od tyłu (np. "kajak", "racecar"):

```python
def jest_palindromem(tekst):
    tekst = tekst.lower().replace(" ", "")  # Ignorujemy wielkość liter i spacje
    return tekst == tekst[::-1]

print(jest_palindromem("kajak"))      # True
print(jest_palindromem("Python"))     # False
print(jest_palindromem("Kobyła ma mały bok".replace(" ", "")))  # True
```

**Zamiana pierwszej litery każdego słowa na wielką:**

```python
tekst = "jan kowalski z warszawy"
wynik = tekst.title()
print(wynik)  # "Jan Kowalski Z Warszawy"

# Ręcznie — gdy potrzebujemy większej kontroli:
slowa = tekst.split()
wynik = " ".join(s[0].upper() + s[1:] for s in slowa)
```

**Zliczanie słów w tekście:**

```python
tekst = "Python jest super i Python jest prosty"
slowa = tekst.lower().split()

wystapienia = {}
for slowo in slowa:
    wystapienia[slowo] = wystapienia.get(slowo, 0) + 1

for slowo, ile in sorted(wystapienia.items(), key=lambda x: x[1], reverse=True):
    print(f"{slowo}: {ile}")
# python: 2
# jest: 2
# super: 1
# i: 1
# prosty: 1
```

Metoda `dict.get(klucz, domyslna)` jest tu kluczowa — zwraca wartość domyślną `0` zamiast rzucania `KeyError`, gdy klucz nie istnieje. Dzięki temu nie potrzebujemy bloku `if/else`.

---

## 7. Obsługa plików

Praca z plikami to podstawowa umiejętność programisty. Python oferuje prosty i wygodny interfejs do odczytu i zapisu plików tekstowych oraz binarnych. Najważniejszą zasadą jest **zawsze zamykanie pliku po zakończeniu pracy** — najwygodniej osiągnąć to za pomocą instrukcji `with`.

### 7.1. Otwieranie i zamykanie plików

Funkcja `open()` otwiera plik i zwraca obiekt pliku. Przyjmuje dwa główne argumenty: ścieżkę do pliku i tryb otwarcia.

**Tryby otwarcia pliku:**

| Tryb | Opis | Tworzenie pliku | Nadpisuje |
|---|---|---|---|
| `"r"` | Odczyt (read) — domyślny | ❌ Plik musi istnieć | — |
| `"w"` | Zapis (write) — nadpisuje | ✅ Tak | ✅ Tak |
| `"a"` | Dopisywanie (append) | ✅ Tak | ❌ Dopisuje na koniec |
| `"x"` | Tworzenie (exclusive) | ✅ Tak | ❌ Błąd jeśli istnieje |
| `"r+"` | Odczyt i zapis | ❌ Plik musi istnieć | Zależy od pozycji |
| `"rb"` | Odczyt binarny | ❌ Plik musi istnieć | — |
| `"wb"` | Zapis binarny | ✅ Tak | ✅ Tak |

**Instrukcja `with` — zalecany sposób pracy z plikami:**

Blok `with` automatycznie zamyka plik po zakończeniu bloku kodu, nawet jeśli wystąpi błąd. To najlepszy i najbezpieczniejszy sposób pracy z plikami:

```python
# ✅ ZALECANY sposób — with
with open("dane.txt", "r") as plik:
    zawartosc = plik.read()
    print(zawartosc)
# Plik jest automatycznie zamknięty po wyjściu z bloku with

# ❌ STARSZY sposób — wymaga ręcznego zamykania
plik = open("dane.txt", "r")
zawartosc = plik.read()
plik.close()  # Łatwo zapomnieć!
```

### 7.2. Odczyt pliku tekstowego

Python oferuje kilka sposobów odczytu zawartości pliku. Wybór zależy od rozmiaru pliku i tego, w jaki sposób chcemy przetworzyć dane.

**`read()` — odczyt całego pliku jako jednego stringa:**

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    calosc = plik.read()
    print(calosc)
    print(f"Plik ma {len(calosc)} znaków")
```

Parametr `encoding="utf-8"` zapewnia poprawne odczytywanie polskich znaków i powinien być stosowany zawsze.

**`readline()` — odczyt jednej linii:**

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    linia1 = plik.readline()    # Pierwsza linia (ze znakiem \n na końcu)
    linia2 = plik.readline()    # Druga linia
    print(linia1.strip())       # strip() usuwa \n z końca
    print(linia2.strip())
```

**`readlines()` — odczyt wszystkich linii jako listy:**

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    linie = plik.readlines()    # Lista stringów — każdy to jedna linia

for i, linia in enumerate(linie, start=1):
    print(f"Linia {i}: {linia.strip()}")
```

**Iteracja po liniach — najbardziej efektywny sposób:**

Najbardziej „pythonowym" i efektywnym sposobem czytania pliku linia po linii jest bezpośrednia iteracja po obiekcie pliku. Nie ładuje całego pliku do pamięci:

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()   # Usuwamy \n z końca
        if linia:               # Pomijamy puste linie
            print(linia)
```

### 7.3. Zapis do pliku tekstowego

**`write()` — zapis tekstu:**

Metoda `write()` nie dodaje automatycznie znaku nowej linii — trzeba go dodać samodzielnie jako `\n`:

```python
with open("wynik.txt", "w", encoding="utf-8") as plik:
    plik.write("Pierwsza linia\n")
    plik.write("Druga linia\n")
    plik.write(f"Wynik: {42}\n")
```

Tryb `"w"` (write) **nadpisuje** cały plik — jeśli plik istniał wcześniej, jego zawartość zostanie usunięta!

**`writelines()` — zapis listy linii:**

```python
linie = ["Linia 1\n", "Linia 2\n", "Linia 3\n"]

with open("wynik.txt", "w", encoding="utf-8") as plik:
    plik.writelines(linie)
```

**Dopisywanie na koniec pliku — tryb `"a"` (append):**

Tryb `"a"` nie nadpisuje pliku — dodaje nową treść na końcu. Jeśli plik nie istnieje, zostanie utworzony:

```python
with open("log.txt", "a", encoding="utf-8") as plik:
    plik.write("Nowy wpis w logu\n")
    plik.write("Kolejny wpis\n")
```

### 7.4. Praca z plikami CSV (dane tabelaryczne)

Pliki CSV (Comma-Separated Values) to prosty format przechowywania danych tabelarycznych, gdzie wartości w wierszu są oddzielone separatorem (zwykle przecinkiem lub średnikiem).

**Ręczne parsowanie CSV (bez modułu):**

```python
# Odczyt CSV
dane = []
with open("uczniowie.csv", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()
        if linia:
            pola = linia.split(";")  # Dzielenie po separatorze
            dane.append(pola)

# Wyświetlanie
for wiersz in dane:
    print(wiersz)
# ['Imię', 'Nazwisko', 'Ocena']
# ['Jan', 'Kowalski', '4']
# ['Anna', 'Nowak', '5']
```

**Zapis danych w formacie CSV:**

```python
uczniowie = [
    ["Imię", "Nazwisko", "Ocena"],
    ["Jan", "Kowalski", "4"],
    ["Anna", "Nowak", "5"],
    ["Piotr", "Wiśniewski", "3"]
]

with open("uczniowie.csv", "w", encoding="utf-8") as plik:
    for wiersz in uczniowie:
        linia = ";".join(wiersz)   # Łączenie listy w string z separatorem
        plik.write(linia + "\n")
```

**Moduł `csv` — profesjonalne podejście:**

Python posiada wbudowany moduł `csv`, który obsługuje trudniejsze przypadki (np. wartości zawierające separator):

```python
import csv

# Odczyt
with open("dane.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik, delimiter=";")
    for wiersz in czytnik:
        print(wiersz)  # Lista wartości

# Zapis
with open("dane.csv", "w", encoding="utf-8", newline="") as plik:
    pisarz = csv.writer(plik, delimiter=";")
    pisarz.writerow(["Imię", "Wiek", "Miasto"])
    pisarz.writerow(["Jan", "25", "Warszawa"])
    pisarz.writerow(["Anna", "30", "Kraków"])
```

### 7.5. Sprawdzanie istnienia pliku

Przed otwarciem pliku warto sprawdzić, czy istnieje. Do tego służy moduł `os`:

```python
import os

sciezka = "dane.txt"

# Sprawdzenie czy plik istnieje
if os.path.exists(sciezka):
    print("Plik istnieje")
else:
    print("Plik nie istnieje")

# Sprawdzenie czy to plik (nie folder)
if os.path.isfile(sciezka):
    print("To jest plik")

# Sprawdzenie czy to folder
if os.path.isdir("moj_folder"):
    print("To jest folder")

# Rozmiar pliku w bajtach
if os.path.exists(sciezka):
    rozmiar = os.path.getsize(sciezka)
    print(f"Rozmiar: {rozmiar} bajtów")
```

### 7.6. Obsługa błędów przy pracy z plikami

Pliki mogą nie istnieć, możemy nie mieć uprawnień, dysk może być pełny. Dlatego warto zabezpieczyć się blokem `try/except`:

```python
try:
    with open("nieistniejacy.txt", "r") as plik:
        zawartosc = plik.read()
except FileNotFoundError:
    print("Błąd: plik nie został znaleziony!")
except PermissionError:
    print("Błąd: brak uprawnień do odczytu pliku!")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
```

### 7.7. Operacje na ścieżkach — moduł `os.path`

```python
import os

sciezka = "/Users/jan/dokumenty/raport.txt"

# Wyodrębnianie nazwy pliku
print(os.path.basename(sciezka))     # "raport.txt"

# Wyodrębnianie katalogu
print(os.path.dirname(sciezka))      # "/Users/jan/dokumenty"

# Rozdzielenie nazwy i rozszerzenia
nazwa, rozszerzenie = os.path.splitext("raport.txt")
print(nazwa)          # "raport"
print(rozszerzenie)   # ".txt"

# Łączenie ścieżek (bezpieczne — działa na każdym systemie)
nowa = os.path.join("dokumenty", "raport.txt")
print(nowa)  # "dokumenty/raport.txt" (lub "dokumenty\raport.txt" na Windows)
```

### 7.8. Tworzenie i usuwanie plików/folderów

```python
import os

# Tworzenie folderu
os.makedirs("wyniki/raporty", exist_ok=True)
# exist_ok=True — nie rzuca błędu jeśli folder już istnieje

# Wylistowanie zawartości folderu
pliki = os.listdir(".")   # "." = bieżący folder
for nazwa in pliki:
    print(nazwa)

# Usuwanie pliku
if os.path.exists("tymczasowy.txt"):
    os.remove("tymczasowy.txt")

# Zmiana nazwy pliku
os.rename("stara_nazwa.txt", "nowa_nazwa.txt")
```

### 7.9. Wczytywanie danych z pliku do tablicy

To bardzo częsty wzorzec — wczytanie liczb z pliku do listy:

```python
# Plik dane.txt zawiera po jednej liczbie na linię:
# 42
# 17
# 85
# 3

def wczytaj_liczby(nazwa_pliku):
    """Wczytuje liczby z pliku — jedna liczba na linię."""
    liczby = []
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        for linia in plik:
            linia = linia.strip()
            if linia:
                liczby.append(int(linia))
    return liczby

# Użycie
dane = wczytaj_liczby("dane.txt")
print(dane)           # [42, 17, 85, 3]
print(sum(dane))      # 147
print(max(dane))      # 85
```

**Zapisywanie tablicy do pliku:**

```python
def zapisz_liczby(nazwa_pliku, liczby):
    """Zapisuje listę liczb do pliku — jedna na linię."""
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for liczba in liczby:
            plik.write(f"{liczba}\n")

wyniki = [10, 20, 30, 40, 50]
zapisz_liczby("wyniki.txt", wyniki)
```

### 7.10. Praca z plikami JSON

JSON (JavaScript Object Notation) to popularny format wymiany danych, który w Pythonie naturalnie mapuje się na słowniki i listy. Moduł `json` jest wbudowany.

**Zapis danych do pliku JSON:**

```python
import json

dane = {
    "imie": "Jan",
    "wiek": 25,
    "oceny": [4, 5, 3, 5, 4],
    "adres": {
        "miasto": "Warszawa",
        "ulica": "Nowa 15"
    }
}

with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump(dane, plik, indent=4, ensure_ascii=False)
    # indent=4 — czytelne formatowanie z wcięciami
    # ensure_ascii=False — zachowuje polskie znaki
```

Plik `dane.json` będzie wyglądał tak:

```json
{
    "imie": "Jan",
    "wiek": 25,
    "oceny": [4, 5, 3, 5, 4],
    "adres": {
        "miasto": "Warszawa",
        "ulica": "Nowa 15"
    }
}
```

**Odczyt danych z pliku JSON:**

```python
import json

with open("dane.json", "r", encoding="utf-8") as plik:
    dane = json.load(plik)

print(dane["imie"])              # Jan
print(dane["oceny"])             # [4, 5, 3, 5, 4]
print(dane["adres"]["miasto"])    # Warszawa
```

**Konwersja między JSON a stringiem (bez pliku):**

```python
import json

# Słownik → string JSON
słownik = {"klucz": "wartość", "liczba": 42}
json_str = json.dumps(słownik, ensure_ascii=False)
print(json_str)         # {"klucz": "wartość", "liczba": 42}
print(type(json_str))   # <class 'str'>

# String JSON → słownik
odczytany = json.loads(json_str)
print(odczytany["klucz"])  # wartość
print(type(odczytany))     # <class 'dict'>
```

**Mapowanie typów Python ↔ JSON:**

| Python | JSON |
|---|---|
| `dict` | `{}` (obiekt) |
| `list`, `tuple` | `[]` (tablica) |
| `str` | `"string"` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### 7.11. Podsumowanie metod pracy z plikami

| Operacja | Tryb | Metoda | Uwagi |
|---|---|---|---|
| Odczyt całego pliku | `"r"` | `plik.read()` | Cały plik jako jeden string |
| Odczyt linia po linii | `"r"` | `for linia in plik:` | Najefektywniejszy sposób |
| Odczyt wszystkich linii | `"r"` | `plik.readlines()` | Lista stringów |
| Zapis (nadpisanie) | `"w"` | `plik.write(tekst)` | Kasuje poprzednią zawartość! |
| Dopisanie na koniec | `"a"` | `plik.write(tekst)` | Bez kasowania |
| Zapis wielu linii | `"w"` | `plik.writelines(lista)` | Nie dodaje `\n` automatycznie |

---

## 8. Operacje matematyczne

### 8.1. Wbudowane funkcje matematyczne

Te funkcje nie wymagają importowania żadnego modułu:

| Funkcja | Opis | Przykład | Wynik |
|---|---|---|---|
| `abs(x)` | Wartość bezwzględna | `abs(-5)` | `5` |
| `round(x)` | Zaokrąglenie | `round(3.7)` | `4` |
| `round(x, n)` | Zaokr. do n miejsc | `round(3.14159, 2)` | `3.14` |
| `pow(x, y)` | Potęga x^y | `pow(2, 10)` | `1024` |
| `min(a, b, ...)` | Minimum | `min(3, 1, 7)` | `1` |
| `max(a, b, ...)` | Maksimum | `max(3, 1, 7)` | `7` |
| `divmod(a, b)` | Iloraz i reszta | `divmod(17, 5)` | `(3, 2)` |

```python
print(abs(-5))           # 5
print(round(3.7))        # 4
print(round(3.14159, 2)) # 3.14
print(pow(2, 10))        # 1024
print(min(3, 1, 7, 2))   # 1
print(max(3, 1, 7, 2))   # 7

iloraz, reszta = divmod(17, 5)
print(iloraz, reszta)    # 3 2
```

### 8.2. Moduł `math`

Moduł `math` zawiera bardziej zaawansowane funkcje matematyczne. Wymaga importowania:

```python
import math

print(math.sqrt(16))       # 4.0    — pierwiastek kwadratowy
print(math.floor(3.7))     # 3      — zaokrąglenie w DÓŁ (podłoga)
print(math.ceil(3.2))      # 4      — zaokrąglenie w GÓRĘ (sufit)
print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045

# Alternatywa dla math.sqrt() — potęgowanie ułamkowe
print(16 ** 0.5)           # 4.0
print(27 ** (1/3))         # 3.0 (pierwiastek sześcienny)
```

**Typowe zastosowanie `math.sqrt()` — ograniczenie pętli do √n:**

W wielu algorytmach (np. sito Eratostenesa, sprawdzanie czy liczba jest pierwsza) wystarczy sprawdzić dzielniki do pierwiastka z n:

```python
import math

n = 100
limit = int(math.sqrt(n))  # 10
for i in range(2, limit + 1):
    print(i, end=" ")
# 2 3 4 5 6 7 8 9 10
```

### 8.3. Dzielenie — porównanie operatorów

Zrozumienie różnic między operatorami dzielenia jest kluczowe:

| Wyrażenie | Wynik | Typ | Wyjaśnienie |
|---|---|---|---|
| `10 / 3` | `3.3333...` | `float` | Dzielenie dokładne |
| `10 / 2` | `5.0` | `float` | Mimo wyniku całkowitego — zawsze float! |
| `10 // 3` | `3` | `int` | Dzielenie całkowite (zaokr. w dół) |
| `-10 // 3` | `-4` | `int` | W dół = w kierunku -∞, nie ku zeru! |
| `10 % 3` | `1` | `int` | Reszta: 10 = 3*3 + **1** |

### 8.4. Konwersja systemów liczbowych

W programowaniu często pracujemy z liczbami w systemach innych niż dziesiętny — binarnym (2), ósemkowym (8) i szesnastkowym (16). Python oferuje wbudowane funkcje do konwersji między nimi.

**Funkcje konwertujące liczbę na string w danym systemie:**

| Funkcja | System | Prefiks | Przykład | Wynik |
|---|---|---|---|---|
| `bin(x)` | Dwójkowy (binarny) | `0b` | `bin(42)` | `'0b101010'` |
| `oct(x)` | Ósemkowy (oktalny) | `0o` | `oct(42)` | `'0o52'` |
| `hex(x)` | Szesnastkowy (heksadecymalny) | `0x` | `hex(42)` | `'0x2a'` |

```python
liczba = 42

print(bin(liczba))    # 0b101010
print(oct(liczba))    # 0o52
print(hex(liczba))    # 0x2a

# Bez prefiksu — usuwamy pierwsze 2 znaki
print(bin(liczba)[2:])  # 101010
print(hex(liczba)[2:])  # 2a

# Formatowanie z f-stringiem
print(f"{liczba:b}")    # 101010 (binarnie, bez prefiksu)
print(f"{liczba:o}")    # 52 (ósemkowo)
print(f"{liczba:x}")    # 2a (szesnastkowo, małe litery)
print(f"{liczba:X}")    # 2A (szesnastkowo, WIELKIE litery)
print(f"{liczba:08b}")  # 00101010 (8-bitowy zapis binarny)
```

**Konwersja z dowolnego systemu na dziesiętny — `int(string, baza)`:**

```python
# String w systemie binarnym -> int
print(int("101010", 2))     # 42
print(int("0b101010", 2))   # 42 (z prefiksem też działa)

# Ósemkowy -> int
print(int("52", 8))          # 42

# Szesnastkowy -> int
print(int("2a", 16))         # 42
print(int("FF", 16))         # 255

# Dowolna baza (2-36)
print(int("z", 36))          # 35
```

**Przydatne operacje na cyfrach liczby:**

```python
# Ile bitów potrzeba do zapisania liczby
liczba = 42
print(liczba.bit_length())   # 6 (bo 101010 ma 6 cyfr)

# Zamiana cyfr liczby na listę
cyfry = [int(c) for c in str(12345)]
print(cyfry)  # [1, 2, 3, 4, 5]

# Suma cyfr liczby
print(sum(int(c) for c in str(12345)))  # 15
```

---

## 9. Moduł random — generowanie losowych danych

Moduł `random` dostarcza narzędzia do generowania danych pseudolosowych. Są to wartości wyglądające na losowe, ale generowane algorytmicznie — przy tym samym „ziarnie" (seed) zawsze wygenerują te same wyniki. W praktyce dla potrzeb programowania to wystarczające.

Warto wiedzieć, że moduł `random` **nie jest** bezpieczny kryptograficznie — nie powinien być używany do generowania haseł czy kluczy szyfrowania. Do tych celów Python oferuje moduł `secrets`. Jednak do symulacji, gier, testowania i algorytmów `random` jest w zupełności wystarczający.

### 9.1. Importowanie

```python
import random

# Lub importowanie wybranych funkcji
from random import randint, choice, sample, shuffle
```

### 9.2. Generowanie liczb losowych

| Funkcja | Opis | Zakres | Typ wyniku |
|---|---|---|---|
| `random.randint(a, b)` | Losowa liczba całkowita | [a, b] (oba włącznie) | `int` |
| `random.random()` | Losowa liczba zmiennoprzecinkowa | [0.0, 1.0) | `float` |
| `random.uniform(a, b)` | Losowa liczba zmiennoprzecinkowa | [a, b] | `float` |

```python
import random

# Losowa liczba całkowita z zakresu [a, b] — OBA KOŃCE WŁĄCZNIE
x = random.randint(1, 100)     # Losowa 1–100
x = random.randint(1, 6)       # Symulacja rzutu kością (1–6)

# Losowa liczba zmiennoprzecinkowa z zakresu [0.0, 1.0)
x = random.random()            # np. 0.7342...

# Losowa zmiennoprzecinkowa z zakresu [a, b]
x = random.uniform(1.0, 10.0)  # np. 5.247...
```

### 9.3. Losowanie z kolekcji

```python
import random

kolory = ["czerwony", "zielony", "niebieski", "żółty"]

# Losowy element z listy
kolor = random.choice(kolory)        # np. "zielony"

# Losowanie n unikalnych elementów (BEZ powtórzeń)
wybrane = random.sample(kolory, 2)   # np. ["żółty", "czerwony"]

# Losowanie unikalnych liczb z zakresu
unikalne = random.sample(range(1, 50), 6)  # 6 unikalnych z 1-49

# Mieszanie listy na miejscu (modyfikuje oryginał)
random.shuffle(kolory)
print(kolory)  # np. ["niebieski", "żółty", "czerwony", "zielony"]
```

### 9.4. Wypełnianie tablicy losowymi danymi

```python
import random

# Tablica 50 losowych liczb z zakresu 1-100
tablica = [random.randint(1, 100) for _ in range(50)]

# Funkcja generująca tablicę
def wypelnij_losowo(rozmiar, minimum, maksimum):
    return [random.randint(minimum, maksimum) for _ in range(rozmiar)]

dane = wypelnij_losowo(30, 1, 100)
print(dane)
print(f"Długość: {len(dane)}")
```

Zmienna `_` (podkreślnik) to konwencja Pythona oznaczająca „ta zmienna nie będzie używana". Tu jest potrzebna tylko jako licznik iteracji.

### 9.5. Losowanie bez powtórzeń — trzy sposoby

Losowanie unikalnych wartości (np. 6 różnych numerów z zakresu 1–49) można zrealizować na kilka sposobów:

```python
import random

# Sposób 1: random.sample() — NAJPROSTSZY I ZALECANY
zestaw = random.sample(range(1, 50), 6)
# Zwraca listę 6 unikalnych liczb z zakresu 1–49

# Sposób 2: Pętla z kontrolą duplikatów
zestaw = []
while len(zestaw) < 6:
    liczba = random.randint(1, 49)
    if liczba not in zestaw:  # Sprawdzamy czy już nie wylosowaliśmy
        zestaw.append(liczba)

# Sposób 3: Przez zbiór (set) — automatycznie odrzuca duplikaty
zestaw = set()
while len(zestaw) < 6:
    zestaw.add(random.randint(1, 49))
zestaw = list(zestaw)  # Konwersja zbioru na listę
```

### 9.6. Ustawienie ziarna (seed) — powtarzalność wyników

Dla celów testowania i debugowania można ustawić „ziarno" generatora, co gwarantuje te same „losowe" wyniki:

```python
import random

random.seed(42)  # Ustawienie ziarna
print(random.randint(1, 100))  # Zawsze 82
print(random.randint(1, 100))  # Zawsze 15

random.seed(42)  # Reset ziarna
print(random.randint(1, 100))  # Znowu 82
```

---

## 10. Programowanie obiektowe — podstawy

Programowanie obiektowe (OOP — Object-Oriented Programming) to paradygmat, w którym program jest organizowany wokół **obiektów** — autonomicznych bytów łączących dane (atrybuty) i zachowania (metody).

### 10.1. Definicja klasy
Klasa to „szablon” lub „projekt”, na podstawie którego tworzymy obiekty. Nazwy klas w Pythonie zapisujemy zgodnie z konwencją **PascalCase** (np. `MojaKlasa`).

```python
class Robot:
    """Prosta klasa reprezentująca robota."""
    pass

# Tworzenie instancji (obiektu)
moj_robot = Robot()
print(type(moj_robot))  # <class '__main__.Robot'>
```

### 10.2. Konstruktor `__init__` i pola instancji
Metoda `__init__` jest wywoływana automatycznie podczas tworzenia nowego obiektu. Służy do nadawania obiektowi początkowego stanu (inicjalizacji pól).

```python
class Samochod:
    def __init__(self, marka, model, rok):
        # Pola instancji (unikalne dla każdego obiektu)
        self.marka = marka
        self.model = model
        self.rok = rok
        self.czy_odpalony = False

# Przekazujemy argumenty z pominięciem 'self'
auto1 = Samochod("Toyota", "Corolla", 2022)
auto2 = Samochod("Tesla", "Model 3", 2023)

print(auto1.marka)  # Toyota
print(auto2.marka)  # Tesla
```

### 10.3. Metody instancji
Metody to funkcje zdefiniowane wewnątrz klasy, które mają dostęp do danych obiektu poprzez parametr `self`.

```python
class Pies:
    def __init__(self, imie):
        self.imie = imie

    def szczekaj(self):
        print(f"{self.imie} mówi: Hau! Hau!")

    def przedstaw_sie(self, tytul="Pies"):
        print(f"Jestem {tytul} i nazywam się {self.imie}.")

reksio = Pies("Reksio")
reksio.szczekaj()              # Reksio mówi: Hau! Hau!
reksio.przedstaw_sie("Azor")   # Jestem Azor i nazywam się Reksio.
```

### 10.4. `self` — czym jest i dlaczego jest konieczne
`self` to pierwszy parametr każdej metody instancji. Reprezentuje on **konkretny obiekt**, na którym metoda została wywołana.

- **Dlaczego `self`?** Python nie używa słowa kluczowego `this` jak Java czy C#, a przekazywanie referencji do obiektu musi być jawne w definicji (choć niejawne przy wywołaniu).
- **Jak to działa pod spodem?** Wywołanie `auto.jedz(10)` jest przez Pythona zamieniane na `Samochod.jedz(auto, 10)`.

### 10.5. Metoda `__str__` — reprezentacja tekstowa obiektu
Pozwala zdefiniować, co ma się wyświetlić, gdy przekażemy obiekt do funkcji `print()` lub `str()`.

```python
class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    def __str__(self):
        return f"'{self.tytul}' autorstwa {self.autor}"

ksiazka = Ksiazka("Wiedźmin", "Andrzej Sapkowski")
print(ksiazka)  # 'Wiedźmin' autorstwa Andrzej Sapkowski
```

### 10.6. `__repr__` vs `__str__` — dwie reprezentacje tekstowe

| Metoda | Cel | Grupa docelowa | Wywołanie |
|---|---|---|---|
| `__str__` | Nieformalna, ładna reprezentacja. | Użytkownik końcowy. | `print(obj)`, `str(obj)` |
| `__repr__` | Formalna, techniczna informacja. | Programista (debugowanie). | Konsola, f-string `!r`, listy. |

**Zasada:** Jeśli nie zdefiniujesz `__str__`, Python użyje `__repr__`. Jeśli nie zdefiniujesz żadnej, zobaczysz adres w pamięci.

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __repr__(self):
        return f"Produkt(nazwa='{self.nazwa}', cena={self.cena})"

p = Produkt("Chleb", 4.50)
print(p)      # Produkt(nazwa='Chleb', cena=4.5)
lista = [p]
print(lista)  # [Produkt(nazwa='Chleb', cena=4.5)]
```

---

## 11. Programowanie obiektowe — hermetyzacja

Hermetyzacja (enkapsulacja) to ukrywanie danych wewnętrznych obiektu i udostępnianie ich tylko poprzez kontrolowany interfejs. Zapobiega to przypadkowej modyfikacji stanu obiektu.

### 11.1. Poziomy dostępu w Pythonie
W Pythonie nie ma ścisłych ograniczeń dostępu (jak `private` w Java). Stosujemy konwencje nazewnictwa.

| Typ | Zapis | Dostępność | Znaczenie |
|---|---|---|---|
| **Publiczne** | `self.nazwa` | Wszędzie. | Standardowe pole. |
| **Chronione** | `self._nazwa` | Klasa i podklasy. | "Proszę, nie ruszaj mnie poza klasą" (konwencja). |
| **Prywatne** | `self.__nazwa` | Tylko klasa. | Silnie ukryte (uruchamia mechanizm **Name Mangling**). |

**Name Mangling:** Atrybut `self.__tajne` w klasie `Konto` jest zamieniany na `_Konto__tajne`. Można się do niego dostać z zewnątrz, ale jest to celowo utrudnione.

### 11.2. Gettery i settery — metody dostępu
Klasyczne podejście (rzadziej stosowane w Pythonie na rzecz `@property`):

```python
class Pracownik:
    def __init__(self, pensja):
        self.__pensja = pensja

    def get_pensja(self):
        return self.__pensja

    def set_pensja(self, nowa_pensja):
        if nowa_pensja > 0:
            self.__pensja = nowa_pensja
```

### 11.3. Dekorator `@property` — pythoniczny getter/setter
Pozwala używać metod tak, jakby były zwykłymi polami (bez nawiasów `()`), co umożliwia dodanie walidacji bez zmiany API klasy.

```python
class Osoba:
    def __init__(self, wiek):
        self.__wiek = wiek

    @property
    def wiek(self):
        """Getter: wywoływany przy 'print(obj.wiek)'"""
        return self.__wiek

    @wiek.setter
    def wiek(self, wartosc):
        """Setter: wywoływany przy 'obj.wiek = 20'"""
        if 0 <= wartosc <= 150:
            self.__wiek = wartosc
        else:
            print("Nieprawidłowy wiek!")

o = Osoba(25)
o.wiek = 30    # Wywołuje setter
print(o.wiek)  # Wywołuje getter -> 30
o.wiek = -5    # Nieprawidłowy wiek!
```

---

## 12. Programowanie obiektowe — zmienne klasowe i metody statyczne

### 12.1. Zmienne klasowe (static fields)
Zmienne zdefiniowane bezpośrednio w klasie (poza `__init__`). Są współdzielone przez **wszystkie** instancje tej klasy.

```python
class Pracownik:
    liczba_pracownikow = 0  # Zmienna klasowa

    def __init__(self, imie):
        self.imie = imie
        Pracownik.liczba_pracownikow += 1

p1 = Pracownik("Adam")
p2 = Pracownik("Ewa")
print(Pracownik.liczba_pracownikow)  # 2
```

### 12.2. Zmienne klasowe — tablice i kolekcje (Pułapka!)
Jeśli zmienna klasowa jest mutowalna (np. lista), każda zmiana w jednym obiekcie wpłynie na wszystkie inne!

```python
class KlasaZBlędem:
    lista = []  # UWAGA: wspólna dla wszystkich!

obj1 = KlasaZBlędem()
obj2 = KlasaZBlędem()
obj1.lista.append(1)
print(obj2.lista)  # [1] -> Zmiana widoczna w drugim obiekcie!
```

### 12.3. Metody statyczne — `@staticmethod`
Metoda, która nie ma dostępu do `self` ani `cls`. Zachowuje się jak zwykła funkcja, ale jest umieszczona wewnątrz klasy dla lepszej organizacji.

```python
class Narzedzia:
    @staticmethod
    def czy_parzysta(n):
        return n % 2 == 0

print(Narzedzia.czy_parzysta(10))  # True
```

### 12.4. Metody klasowe — `@classmethod`
Jako pierwszy argument przyjmuje klasę (`cls`), a nie instancję. Często używana jako **alternatywny konstruktor** (wzorzec Fabryka).

```python
class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien, self.miesiac, self.rok = dzien, miesiac, rok

    @classmethod
    def z_tekstu(cls, tekst):
        """Tworzy obiekt na podstawie stringa 'DD-MM-YYYY'"""
        d, m, r = map(int, tekst.split("-"))
        return cls(d, m, r)  # Wywołuje __init__

data = Data.z_tekstu("15-05-2024")
print(data.rok)  # 2024
```

---

## 13. Programowanie obiektowe — konstruktory zaawansowane

### 13.1. Konstruktor z wartościami domyślnymi
Python nie obsługuje przeciążania metod (wiele metod o tej samej nazwie), dlatego używamy parametrów domyślnych.

```python
class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Punkt()      # (0, 0)
p2 = Punkt(5, 10) # (5, 10)
```

### 13.2. Wzorzec z `None` — pełny zamiennik dwóch konstruktorów
Jeśli chcemy, aby pole było inicjalizowane nową listą dla każdego obiektu, używamy `None`.

```python
class Student:
    def __init__(self, imie, oceny=None):
        self.imie = imie
        # Zapewnia unikalną listę dla każdego obiektu
        if oceny is None:
            self.oceny = []
        else:
            self.oceny = oceny
```

### 13.3. Walidacja w konstruktorze
Zawsze warto sprawdzić dane wejściowe przed ich przypisaniem.

```python
class Konto:
    def __init__(self, balans):
        if balans < 0:
            raise ValueError("Balans nie może być ujemny!")
        self.balans = balans
```

### 13.4. Kopiowanie obiektów
Standardowe przypisanie `obj2 = obj1` kopiuje tylko **referencję** (oba wskazują na ten sam obiekt). Aby stworzyć kopię, używamy modułu `copy`.

```python
import copy

class Graf:
    def __init__(self, wezly):
        self.wezly = wezly

g1 = Graf([1, 2, 3])

# Kopia płytka (Shallow copy)
g2 = copy.copy(g1) 

# Kopia głęboka (Deep copy) - kopiuje też zawartość list
g3 = copy.deepcopy(g1)
```

---

## 14. Programowanie obiektowe — dziedziczenie, polimorfizm i klasy abstrakcyjne

### 14.1. Podstawy dziedziczenia
Klasa pochodna (dziecko) dziedziczy wszystkie atrybuty i metody klasy bazowej (rodzica).

```python
class Zwierze:
    def oddychaj(self):
        print("Oddycham...")

class Pies(Zwierze):
    def szczekaj(self):
        print("Hau!")

p = Pies()
p.oddychaj() # Metoda z klasy Zwierze
p.szczekaj() # Metoda z klasy Pies
```

### 14.2. `super()` — wywoływanie metod rodzica
Służy głównie do wywoływania konstruktora klasy bazowej wewnątrz konstruktora klasy pochodnej.

```python
class Pojazd:
    def __init__(self, marka):
        self.marka = marka

class Auto(Pojazd):
    def __init__(self, marka, paliwo):
        super().__init__(marka)  # Wywołanie __init__ rodzica
        self.paliwo = paliwo
```

### 14.3. Hermetyzacja a dziedziczenie
- Pola **publiczne** i **chronione** (`_`) są dostępne w klasach pochodnych.
- Pola **prywatne** (`__`) **nie są** bezpośrednio dostępne (trzeba użyć gettera rodzica).

### 14.4. Wzorzec: logika stanów z dziedziczeniem
Dziedziczenie świetnie nadaje się do modelowania obiektów, które zmieniają swoje zachowanie w zależności od stanu (np. zamówienie, postać w grze).

```python
class StanZamowienia:
    def nastepny(self): pass
    def __str__(self): return self.__class__.__name__

class Nowe(StanZamowienia):
    def nastepny(self): return Opłacone()

class Opłacone(StanZamowienia):
    def nastepny(self): return Wyslane()

class Wyslane(StanZamowienia):
    def nastepny(self): return self # Koniec

class Zamowienie:
    def __init__(self):
        self.stan = Nowe()

    def pchnij_dalej(self):
        self.stan = self.stan.nastepny()
        print(f"Obecny stan: {self.stan}")

z = Zamowienie()
z.pchnij_dalej() # Obecny stan: Opłacone
z.pchnij_dalej() # Obecny stan: Wyslane
```

### 14.5. Sprawdzanie typu i dziedziczenia
Aby sprawdzić, czy obiekt jest instancją danej klasy (lub jej klasy pochodnej), używamy `isinstance()`. Aby sprawdzić relację między klasami — `issubclass()`.

```python
isinstance(p, Pies)      # True
isinstance(p, Zwierze)   # True (bo Pies dziedziczy po Zwierze)
issubclass(Pies, Zwierze) # True
```

### 14.6. Podsumowanie — kiedy co stosować w OOP

| Mechanizm | Kiedy stosować? |
|---|---|
| **Klasa** | Gdy potrzebujesz zgrupować dane i funkcje w jeden "byt". |
| **Pola prywatne (`__`)** | Zawsze dla danych, które nie powinny być zmieniane bezpośrednio (np. balans konta). |
| **`@property`** | Gdy chcesz, by dostęp do pola był prosty (`obj.x`), ale wymagał walidacji. |
| **`@classmethod`** | Gdy potrzebujesz stworzyć obiekt w nietypowy sposób (np. z pliku JSON). |
| **Dziedziczenie** | Tylko gdy zachodzi relacja **"jest rodzajem"** (np. Pies jest rodzajem Zwierzęcia). |
| **Kompozycja** | Gdy obiekt **"posiada"** inne obiekty (np. Samochód posiada Silnik). Zazwyczaj lepsza niż dziedziczenie! |
| **Klasa abstrakcyjna** | Gdy tworzysz fundament dla innych klas i chcesz wymusić na nich wspólny interfejs. |

### 14.7. Polimorfizm
Zdolność różnych obiektów do reagowania na to samo wywołanie metody w sposób specyficzny dla swojej klasy. W Pythonie opiera się to na **Duck Typing** ("Jeśli coś kwacze jak kaczka, to jest kaczką").

```python
class Kaczka:
    def kwacz(self): print("Kwa kwa!")

class Czlowiek:
    def kwacz(self): print("Naśladuję kaczkę!")

def wydaj_dzwiek(byt):
    byt.kwacz() # Polimorficzne wywołanie

wydaj_dzwiek(Kaczka())
wydaj_dzwiek(Czlowiek())
```

### 14.8. Klasy abstrakcyjne — moduł `abc`
Klasa abstrakcyjna to taka, z której nie można stworzyć obiektu. Służy jako interfejs wymuszający implementację konkretnych metod w klasach pochodnych.

```python
from abc import ABC, abstractmethod

class Ksztalt(ABC):
    @abstractmethod
    def pole(self):
        """Metoda musi być nadpisana w dziecku"""
        pass

class Kwadrat(Ksztalt):
    def __init__(self, a):
        self.a = a
    
    def pole(self):
        return self.a ** 2

# k = Ksztalt() # BŁĄD: Can't instantiate abstract class
kw = Kwadrat(4)
print(kw.pole()) # 16
```

### 14.9. Kompleksowa implementacja: System Quiz
Wzorcowy przykład łączący: klasy abstrakcyjne, dziedziczenie, hermetyzację i listę obiektów.

```python
from abc import ABC, abstractmethod

class Pytanie(ABC):
    def __init__(self, tresc, punkty):
        self._tresc = tresc      # Chronione
        self._punkty = punkty

    @abstractmethod
    def wyswietl(self): pass

    @abstractmethod
    def sprawdz(self, odpowiedz): pass

class PytanieZamkniete(Pytanie):
    def __init__(self, tresc, punkty, opcje, poprawna_index):
        super().__init__(tresc, punkty)
        self.__opcje = opcje      # Prywatne
        self.__poprawna = poprawna_index

    def wyswietl(self):
        print(f"\n[Pytanie za {self._punkty} pkt]: {self._tresc}")
        for i, o in enumerate(self.__opcje, 1):
            print(f"{i}. {o}")

    def sprawdz(self, odp):
        return str(odp) == str(self.__poprawna)

class PytanieOtwarte(Pytanie):
    def __init__(self, tresc, punkty, poprawna_odp):
        super().__init__(tresc, punkty)
        self.__poprawna = poprawna_odp.lower().strip()

    def wyswietl(self):
        print(f"\n[Pytanie OTWARTE za {self._punkty} pkt]: {self._tresc}")

    def sprawdz(self, odp):
        return odp.lower().strip() == self.__poprawna

class Quiz:
    def __init__(self, tytul):
        self.tytul = tytul
        self.__pytania = []
        self.__wynik = 0

    def dodaj_pytanie(self, p):
        if isinstance(p, Pytanie):
            self.__pytania.append(p)

    def uruchom(self):
        print(f"=== {self.tytul.upper()} ===")
        for p in self.__pytania:
            p.wyswietl()
            user_odp = input("Odpowiedź: ")
            if p.sprawdz(user_odp):
                print("DOBRZE!")
                self.__wynik += p._punkty
            else:
                print("ŹLE!")
        
        print(f"\nKONIEC. Twój wynik: {self.__wynik} pkt.")

# --- Demo ---
moj_quiz = Quiz("Test Wiedzy")
moj_quiz.dodaj_pytanie(PytanieZamkniete("Stolica Polski?", 1, ["Kraków", "Warszawa"], 2))
moj_quiz.dodaj_pytanie(PytanieOtwarte("Jak ma na imię twórca Pythona?", 2, "Guido"))

# moj_quiz.uruchom() # Odkomentuj, aby przetestować interaktywnie
```

## 15. Algorytmy w Pythonie

Algorytmy to precyzyjne przepisy na rozwiązanie problemu. Składają się z jednoznacznie określonych kroków, prowadzących od danych wejściowych do pożądanego wyniku. Poniżej przedstawione są najważniejsze algorytmy, pogrupowane tematycznie, z pełnymi implementacjami i wyjaśnieniami.

**Złożoność algorytmów — krótkie wprowadzenie:**

| Notacja | Nazwa | Opis | Przykład |
|---|---|---|---|
| O(1) | Stała | Czas nie zależy od rozmiaru danych | Dostęp do elementu listy po indeksie |
| O(n) | Liniowa | Czas rośnie proporcjonalnie | Wyszukiwanie liniowe |
| O(n²) | Kwadratowa | Czas rośnie kwadratowo | Sortowanie bąbelkowe, przez wybieranie |
| O(log n) | Logarytmiczna | Bardzo efektywna | Wyszukiwanie binarne |

---

### 15.1. Sortowanie przez wybieranie (Selection Sort)

**Idea:** W każdym kroku szukamy elementu minimalnego w nieposortowanej części tablicy i zamieniamy go z pierwszym nieposortowanym elementem.

```python
def sortowanie_przez_wybieranie(tablica):
    n = len(tablica)
    for i in range(n - 1):
        indeks_min = i
        for j in range(i + 1, n):
            if tablica[j] < tablica[indeks_min]:
                indeks_min = j
        # Zamiana miejscami
        tablica[i], tablica[indeks_min] = tablica[indeks_min], tablica[i]
```

### 15.2. Sortowanie bąbelkowe (Bubble Sort)

**Idea:** Porównujemy sąsiednie elementy i zamieniamy je, jeśli są w złej kolejności. Powtarzamy, aż tablica będzie posortowana.

```python
def sortowanie_babelkowe(tablica):
    n = len(tablica)
    for i in range(n - 1):
        zamieniono = False
        for j in range(n - 1 - i):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                zamieniono = True
        if not zamieniono:
            break  # Jeśli nie było zamiany, tablica jest posortowana
```

### 15.3. Sortowanie przez wstawianie (Insertion Sort)

**Idea:** Pobieramy kolejny element i "wstawiamy" go w odpowiednie miejsce wśród elementów już posortowanych (podobnie jak układanie kart w dłoni).

```python
def sortowanie_przez_wstawianie(tablica):
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        # Przesuwamy elementy większe od klucza o jedną pozycję w prawo
        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = klucz
```

### 15.4. Sortowanie przez scalanie (Merge Sort)

**Idea:** Strategia „dziel i zwyciężaj”. Dzielimy tablicę na połowy, aż zostaną pojedyncze elementy, a następnie scalamy je w porządku rosnącym.

```python
def merge_sort(tablica):
    if len(tablica) > 1:
        srodek = len(tablica) // 2
        L = tablica[:srodek]
        R = tablica[srodek:]

        merge_sort(L) # Sortuj lewą połowę
        merge_sort(R) # Sortuj prawą połowę

        i = j = k = 0
        # Scalanie
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tablica[k] = L[i]
                i += 1
            else:
                tablica[k] = R[j]
                j += 1
            k += 1
        
        # Dopisanie pozostałych elementów
        while i < len(L):
            tablica[k] = L[i]; i += 1; k += 1
        while j < len(R):
            tablica[k] = R[j]; j += 1; k += 1
```

### 15.5. Sortowanie szybkie (Quick Sort)

**Idea:** Wybieramy element obrotowy (pivot). Dzielimy tablicę na elementy mniejsze od pivota, równe mu i większe, a następnie rekurencyjnie sortujemy podtablice.

```python
def quick_sort(tablica):
    if len(tablica) <= 1:
        return tablica
    pivot = tablica[len(tablica) // 2]
    lewe = [x for x in tablica if x < pivot]
    srodkowe = [x for x in tablica if x == pivot]
    prawe = [x for x in tablica if x > pivot]
    return quick_sort(lewe) + srodkowe + quick_sort(prawe)
```

---

### 15.6. Wyszukiwanie liniowe

**Idea:** Sprawdzamy każdy element po kolei, aż znajdziemy szukaną wartość.

```python
def wyszukaj_liniowo(tablica, szukana):
    for i in range(len(tablica)):
        if tablica[i] == szukana:
            return i
    return -1
```

### 15.7. Wyszukiwanie z wartownikiem (Sentinel Search)

**Idea:** Dodajemy szukaną wartość na koniec tablicy jako "wartownika", aby uprościć warunek pętli (brak sprawdzania końca tablicy w każdym kroku).

```python
def wyszukaj_z_wartownikiem(tablica, szukana):
    n = len(tablica)
    tablica.append(szukana) # Dodaj wartownika
    i = 0
    while tablica[i] != szukana:
        i += 1
    tablica.pop() # Usuń wartownika
    return i if i < n else -1
```

### 15.8. Wyszukiwanie binarne (Binary Search)

**Idea:** W posortowanej tablicy sprawdzamy środkowy element. Jeśli to nie on, odrzucamy połowę tablicy, w której na pewno nie ma szukanej wartości.

```python
def wyszukiwanie_binarne(tablica, szukana):
    lewy, prawy = 0, len(tablica) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] == szukana:
            return srodek
        elif tablica[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1
```

---

### 15.9. Algorytm Euklidesa (NWD)

**Idea:** NWD dwóch liczb to największa liczba, która dzieli obie bez reszty. Opiera się na reszcie z dzielenia.

```python
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### 15.10. Najmniejsza Wspólna Wielokrotność (NWW)

**Idea:** Najmniejsza liczba będąca wielokrotnością obu liczb. Wykorzystuje zależność: `NWW(a, b) = |a * b| / NWD(a, b)`.

```python
def nww(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // nwd(a, b)
```

### 15.11. Sprawdzanie czy liczba jest pierwsza

**Idea:** Sprawdzamy dzielniki liczby od 2 do jej pierwiastka. Jeśli żaden nie dzieli liczby, jest ona pierwsza.

```python
import math

def jest_pierwsza(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
```

### 15.12. Sito Eratostenesa

**Idea:** Wykreślanie wielokrotności liczb pierwszych z tablicy, aby znaleźć wszystkie liczby pierwsze w podanym zakresie.

```python
def sito(n):
    pierwsze = [True] * (n + 1)
    pierwsze[0] = pierwsze[1] = False
    for p in range(2, int(n**0.5) + 1):
        if pierwsze[p]:
            for i in range(p * p, n + 1, p):
                pierwsze[i] = False
    return [i for i, b in enumerate(pierwsze) if b]
```

### 15.13. Rozkład liczby na czynniki pierwsze

**Idea:** Dzielenie liczby przez kolejne najmniejsze możliwe dzielniki (liczby pierwsze), aż pozostanie 1.

```python
def rozklad_na_czynniki(n):
    czynniki = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            czynniki.append(d)
            n //= d
        d += 1
    if n > 1:
        czynniki.append(n)
    return czynniki
```

### 15.14. Konwersja systemów liczbowych (Dziesiętny <-> Binarny)

```python
def dec_to_bin(n):
    if n == 0: return "0"
    wynik = ""
    while n > 0:
        wynik = str(n % 2) + wynik
        n //= 2
    return wynik

def bin_to_dec(b):
    wynik = 0
    for i, cyfra in enumerate(reversed(b)):
        if cyfra == '1':
            wynik += 2**i
    return wynik
```

---

### 15.15. Szyfr Cezara

**Idea:** Przesunięcie każdej litery tekstu o stałą liczbę pozycji (klucz) w alfabecie.

```python
def szyfruj_cezar(tekst, klucz):
    wynik = ""
    for znak in tekst.lower():
        if 'a' <= znak <= 'z':
            nowy = (ord(znak) - ord('a') + klucz) % 26
            wynik += chr(nowy + ord('a'))
        else:
            wynik += znak
    return wynik
```

### 15.16. Palindromy i Anagramy

```python
def czy_palindrom(tekst):
    t = tekst.replace(" ", "").lower()
    return t == t[::-1]

def czy_anagram(s1, s2):
    t1 = s1.replace(" ", "").lower()
    t2 = s2.replace(" ", "").lower()
    return sorted(t1) == sorted(t2)
```

---

### 15.17. Rekurencja

**Idea:** Technika, w której funkcja wywołuje samą siebie. Wymaga przypadku bazowego (stopu).

```python
# Silnia (n!)
def silnia(n):
    return 1 if n <= 1 else n * silnia(n - 1)

# Fibonacci
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
```

### 15.18. Walidacja danych z wagami (np. PESEL)

```python
def suma_kontrolna(liczby, wagi):
    suma = sum(int(l) * w for l, w in zip(liczby, wagi))
    return (10 - (suma % 10)) % 10
```

### 15.19. Usuwanie sąsiednich duplikatów

```python
def usun_duplikaty(tekst):
    if not tekst: return ""
    wynik = tekst[0]
    for i in range(1, len(tekst)):
        if tekst[i] != tekst[i-1]:
            wynik += tekst[i]
    return wynik
```

### 15.20. Zliczanie wystąpień wartości w danych

```python
def zlicz_wystapienia(tablica):
    liczniki = {}
    for x in tablica:
        liczniki[x] = liczniki.get(x, 0) + 1
    return liczniki
```

### 15.21. Obliczanie średniej arytmetycznej

```python
def srednia(tablica):
    return sum(tablica) / len(tablica) if tablica else 0
```

### 15.22. Wyodrębnianie elementów spełniających warunek

```python
def filtruj_parzyste(tablica):
    # Wykorzystanie list comprehension
    return [x for x in tablica if x % 2 == 0]
```

---

## 16. Tablice dwuwymiarowe

Tablica dwuwymiarowa (2D) to „tablica tablic" — lista, której każdy element jest również listą. Reprezentuje dane w formie wierszy i kolumn, jak tabela lub macierz. Jest niezbędna przy pracy z siatkami, planszami gier i zestawami danych.

### 16.1. Tworzenie tablic 2D

```python
# Ręczne tworzenie
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dynamiczne tworzenie — n wierszy × m kolumn, wypełnione zerami
wiersze = 4
kolumny = 6
tablica = [[0] * kolumny for _ in range(wiersze)]
```

**Częsty błąd — multiplikacja listy:**

```python
# ❌ BŁĄD — wszystkie wiersze to referencje do TEGO SAMEGO obiektu!
tablica = [[0] * 3] * 3
tablica[0][0] = 99
print(tablica)  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] — zmienione wszystkie!

# ✅ POPRAWNIE — każdy wiersz jest osobnym obiektem
tablica = [[0] * 3 for _ in range(3)]
tablica[0][0] = 99
print(tablica)  # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] — zmieniony tylko pierwszy
```

### 16.2. Dostęp i iteracja

```python
macierz = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# Dostęp: [wiersz][kolumna]
print(macierz[0][0])    # 10
print(macierz[1][2])    # 60
print(macierz[2][1])    # 80

# Iteracja po elementach
for wiersz in macierz:
    for element in wiersz:
        print(f"{element:>4}", end="")
    print()

# Iteracja z indeksami
for i in range(len(macierz)):
    for j in range(len(macierz[i])):
        print(f"[{i}][{j}]={macierz[i][j]}", end="  ")
    print()
```

### 16.3. Wypełnianie i wyświetlanie

```python
import random

def stworz_tablice_losowa(wiersze, kolumny, minimum, maksimum):
    """Tworzy tablicę 2D wypełnioną losowymi liczbami."""
    return [[random.randint(minimum, maksimum) for _ in range(kolumny)]
            for _ in range(wiersze)]

def wyswietl_tablice(tablica, szerokosc=5):
    """Wyświetla tablicę 2D z wyrównaniem kolumn."""
    for i, wiersz in enumerate(tablica):
        print(f"Wiersz {i+1}: ", end="")
        for element in wiersz:
            print(f"{element:>{szerokosc}}", end="")
        print()

dane = stworz_tablice_losowa(3, 6, 1, 49)
wyswietl_tablice(dane)
```

### 16.4. Operacje na tablicach 2D

Kilka przydatnych operacji na tablicach dwuwymiarowych:

**Suma elementów w wierszu i kolumnie:**

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Suma każdego wiersza
for i, wiersz in enumerate(macierz):
    print(f"Wiersz {i}: suma = {sum(wiersz)}")
# Wiersz 0: suma = 6
# Wiersz 1: suma = 15
# Wiersz 2: suma = 24

# Suma każdej kolumny
kolumny = len(macierz[0])
for j in range(kolumny):
    suma_kol = 0
    for wiersz in macierz:
        suma_kol += wiersz[j]
    print(f"Kolumna {j}: suma = {suma_kol}")
# Kolumna 0: suma = 12
# Kolumna 1: suma = 15
# Kolumna 2: suma = 18
```

**Wyszukiwanie elementu w tablicy 2D:**

```python
def szukaj_2d(macierz, szukana):
    """Zwraca (wiersz, kolumna) lub None jeśli nie znaleziono."""
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == szukana:
                return (i, j)
    return None

pozycja = szukaj_2d(macierz, 5)
if pozycja:
    print(f"Znaleziono na pozycji [{pozycja[0]}][{pozycja[1]}]")
# Znaleziono na pozycji [1][1]
```

**Transpozycja macierzy** (zamiana wierszy z kolumnami):

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpozycja
transpozycja = []
for j in range(len(macierz[0])):
    nowy_wiersz = []
    for i in range(len(macierz)):
        nowy_wiersz.append(macierz[i][j])
    transpozycja.append(nowy_wiersz)

print(transpozycja)
# [[1, 4], [2, 5], [3, 6]]

# Lub jednolinijkowo z zip:
transpozycja = [list(wiersz) for wiersz in zip(*macierz)]
```

---

## 17. Testowanie jednostkowe — unittest i pytest

### 17.1. Czym jest testowanie jednostkowe

Testowanie jednostkowe (unit testing) polega na automatycznym sprawdzaniu poprawności **pojedynczych** jednostek kodu (funkcji, metod, klas) w izolacji od reszty programu. Każdy test to oddzielna metoda, która:

1. **Przygotowuje** dane wejściowe (Arrange)
2. **Wywołuje** testowaną funkcję/metodę (Act)
3. **Sprawdza**, czy wynik jest zgodny z oczekiwanym — asercja (Assert)

Testy automatyczne pozwalają szybko wykryć, gdy zmiana w kodzie zepsuje istniejącą funkcjonalność. Zamiast ręcznie testować program po każdej modyfikacji, uruchamiamy zestaw testów, które w kilka sekund sprawdzą wszystkie kluczowe scenariusze.

### 17.2. Moduł `unittest` — podstawy

`unittest` jest wbudowany w Pythona — nie wymaga instalacji. Testy piszemy jako metody klasy dziedziczącej po `unittest.TestCase`. Każda metoda testowa musi zaczynać się od `test_`.

```python
import unittest

# Funkcje do przetestowania
def dodaj(a, b):
    return a + b

def jest_parzysta(liczba):
    return liczba % 2 == 0

# Klasa testowa — dziedziczy po unittest.TestCase
class TestMatematyki(unittest.TestCase):

    def test_dodawanie_liczb_dodatnich(self):
        wynik = dodaj(2, 3)
        self.assertEqual(wynik, 5)   # Czy wynik == 5?

    def test_dodawanie_z_zerem(self):
        self.assertEqual(dodaj(5, 0), 5)

    def test_dodawanie_liczb_ujemnych(self):
        self.assertEqual(dodaj(-2, -3), -5)

    def test_parzysta(self):
        self.assertTrue(jest_parzysta(4))    # Czy True?

    def test_nieparzysta(self):
        self.assertFalse(jest_parzysta(3))   # Czy False?


# Uruchomienie testów
if __name__ == "__main__":
    unittest.main()
```

**Uruchomienie z terminala:**

```bash
python -m unittest test_plik.py           # Uruchom testy z pliku
python -m unittest test_plik.py -v        # Tryb verbose (szczegółowy)
```

### 17.3. Asercje — kompletna lista

Asercje to metody sprawdzające warunki. Jeśli warunek nie jest spełniony, test jest oznaczany jako **FAIL**.

| Asercja | Sprawdza | Przykład |
|---|---|---|
| `assertEqual(a, b)` | `a == b` | `self.assertEqual(2+2, 4)` |
| `assertNotEqual(a, b)` | `a != b` | `self.assertNotEqual(2+2, 5)` |
| `assertTrue(x)` | `x is True` | `self.assertTrue(5 > 3)` |
| `assertFalse(x)` | `x is False` | `self.assertFalse(3 > 5)` |
| `assertIsNone(x)` | `x is None` | `self.assertIsNone(None)` |
| `assertIsNotNone(x)` | `x is not None` | `self.assertIsNotNone(42)` |
| `assertIn(a, b)` | `a in b` | `self.assertIn(3, [1,2,3])` |
| `assertNotIn(a, b)` | `a not in b` | `self.assertNotIn(5, [1,2,3])` |
| `assertGreater(a, b)` | `a > b` | `self.assertGreater(5, 3)` |
| `assertGreaterEqual(a, b)` | `a >= b` | `self.assertGreaterEqual(5, 5)` |
| `assertLess(a, b)` | `a < b` | `self.assertLess(3, 5)` |
| `assertLessEqual(a, b)` | `a <= b` | `self.assertLessEqual(3, 3)` |
| `assertAlmostEqual(a, b)` | `a ≈ b` (float) | `self.assertAlmostEqual(0.1+0.2, 0.3, places=5)` |
| `assertIsInstance(a, T)` | `isinstance(a, T)` | `self.assertIsInstance(42, int)` |
| `assertRaises(E)` | Czy rzuca wyjątek | `with self.assertRaises(ValueError):` |

### 17.4. Struktura projektu z testami

Typowa organizacja plików:

```
projekt/
├── modul.py             # Kod z testowanymi funkcjami/klasami
├── main.py              # Program główny
└── test_modul.py        # Plik z testami
```

**modul.py:**

```python
def szyfruj(tekst, klucz):
    wynik = ""
    for znak in tekst:
        if 'a' <= znak <= 'z':
            numer = ord(znak) - ord('a')
            nowy = (numer + klucz) % 26
            wynik += chr(nowy + ord('a'))
        else:
            wynik += znak
    return wynik
```

**test_modul.py:**

```python
import unittest
from modul import szyfruj

class TestSzyfrowania(unittest.TestCase):

    def test_klucz_dodatni(self):
        """Klucz dodatni, wartość mniejsza niż 26."""
        self.assertEqual(szyfruj("abc", 3), "def")

    def test_zawijanie(self):
        """Litery wychodzą poza alfabet — zawijanie."""
        self.assertEqual(szyfruj("xyz", 3), "abc")

    def test_odszyfrowanie(self):
        """Klucz ujemny — odszyfrowanie."""
        self.assertEqual(szyfruj("def", -3), "abc")

    def test_klucz_wiekszy_niz_26(self):
        """Klucz większy niż długość alfabetu."""
        self.assertEqual(szyfruj("abc", 29), "def")

    def test_spacja(self):
        """Spacja pozostaje bez zmian."""
        self.assertEqual(szyfruj("ab cd", 2), "cd ef")

    def test_klucz_zero(self):
        """Klucz 0 — tekst bez zmian."""
        self.assertEqual(szyfruj("abc", 0), "abc")

    def test_pusty_tekst(self):
        """Pusty łańcuch znaków."""
        self.assertEqual(szyfruj("", 5), "")


if __name__ == "__main__":
    unittest.main()
```

### 17.5. Nazewnictwo testów

Dobre nazwy testów są kluczowe — powinny opisywać **co jest testowane** i **jaki jest oczekiwany wynik**:

```python
# ✅ Dobra konwencja: test_co_testujemy_jaki_scenariusz
def test_szyfruj_klucz_dodatni_przesuwa_litery(self): ...
def test_szyfruj_spacja_pozostaje_bez_zmian(self): ...
def test_rzut_wartosc_w_zakresie_1_do_6(self): ...
def test_blokowanie_kost_nie_zmienia_wartosci(self): ...

# ❌ Zła konwencja — niejasna
def test_1(self): ...
def test_cos(self): ...
```

### 17.6. `setUp` i `tearDown` — przygotowanie i sprzątanie

Metoda `setUp` wykonuje się **przed każdym** testem, a `tearDown` **po każdym**. Przydatne, gdy wiele testów potrzebuje tych samych obiektów:

```python
class TestKalkulatora(unittest.TestCase):

    def setUp(self):
        """Wywoływana PRZED każdym testem — przygotowanie danych."""
        self.dane = [3, 1, 4, 1, 5, 9, 2, 6]
        self.puste = []

    def tearDown(self):
        """Wywoływana PO każdym teście — sprzątanie."""
        pass  # Np. zamknięcie pliku, usunięcie danych tymczasowych

    def test_dlugosc(self):
        self.assertEqual(len(self.dane), 8)

    def test_pusty(self):
        self.assertEqual(len(self.puste), 0)
```

### 17.7. Testowanie klas i obiektów

```python
import unittest

class Licznik:
    def __init__(self, poczatkowa=0):
        self.__wartosc = poczatkowa

    def zwieksz(self):
        self.__wartosc += 1

    def pobierz(self):
        return self.__wartosc

    def resetuj(self):
        self.__wartosc = 0


class TestLicznika(unittest.TestCase):

    def setUp(self):
        self.licznik = Licznik()

    def test_wartosc_poczatkowa_domyslna(self):
        self.assertEqual(self.licznik.pobierz(), 0)

    def test_wartosc_poczatkowa_niestandardowa(self):
        l = Licznik(10)
        self.assertEqual(l.pobierz(), 10)

    def test_zwiekszanie(self):
        self.licznik.zwieksz()
        self.assertEqual(self.licznik.pobierz(), 1)

    def test_wielokrotne_zwiekszanie(self):
        for _ in range(5):
            self.licznik.zwieksz()
        self.assertEqual(self.licznik.pobierz(), 5)

    def test_resetowanie(self):
        self.licznik.zwieksz()
        self.licznik.zwieksz()
        self.licznik.resetuj()
        self.assertEqual(self.licznik.pobierz(), 0)


if __name__ == "__main__":
    unittest.main()
```

### 17.8. Testowanie wartości losowych

Testowanie kodu korzystającego z generatora losowego wymaga sprawdzania **zakresów**, nie konkretnych wartości:

```python
import unittest
import random

class TestLosowan(unittest.TestCase):

    def test_zakres_1_do_6(self):
        """Czy wylosowana wartość mieści się w zakresie 1-6."""
        for _ in range(1000):   # Wielokrotne sprawdzenie
            wartosc = random.randint(1, 6)
            self.assertGreaterEqual(wartosc, 1)
            self.assertLessEqual(wartosc, 6)

    def test_sample_unikalne(self):
        """Czy losowanie sample daje unikalne wartości."""
        zestaw = random.sample(range(1, 50), 6)
        self.assertEqual(len(zestaw), len(set(zestaw)))  # Brak duplikatów
```

### 17.9. `pytest` — prostsza alternatywa

`pytest` to popularna alternatywa dla `unittest` z prostszą składnią — nie wymaga klas ani specjalnych metod, zamiast `self.assertEqual()` używamy zwykłego `assert`:

**Instalacja:**

```bash
pip install pytest
```

**Pisanie testów:**

```python
# test_funkcje.py
from modul import dodaj, szyfruj

def test_dodawanie():
    assert dodaj(2, 3) == 5

def test_dodawanie_ujemnych():
    assert dodaj(-1, -2) == -3

def test_szyfruj_klucz_3():
    assert szyfruj("abc", 3) == "def"

def test_szyfruj_zawijanie():
    assert szyfruj("xyz", 3) == "abc"
```

**Uruchomienie:**

```bash
pytest test_funkcje.py                    # Uruchom testy
pytest test_funkcje.py -v                 # Tryb verbose
pytest test_funkcje.py -v --tb=short      # Krótki traceback
```

**Porównanie assert w pytest:**

Pytest automatycznie rozpisuje szczegóły nieudanej asercji — nie trzeba używać specjalnych metod:

```python
# W pytest - jasny komunikat o błędzie
def test_lista():
    wynik = [1, 2, 3]
    assert len(wynik) == 3
    assert 2 in wynik
    assert wynik[0] == 1

def test_slownik():
    dane = {"imie": "Jan", "wiek": 25}
    assert "imie" in dane
    assert dane["wiek"] > 18
```

**Parametryzacja testów (pytest):**

Pytest pozwala na eleganckie uruchamianie tego samego testu z różnymi danymi wejściowymi:

```python
import pytest

@pytest.mark.parametrize("wejscie, oczekiwany", [
    ("abc", "def"),
    ("xyz", "abc"),
    ("", ""),
])
def test_szyfruj(wejscie, oczekiwany):
    assert szyfruj(wejscie, 3) == oczekiwany
```

**Porównanie `unittest` vs `pytest`:**

| Cecha | `unittest` | `pytest` |
|---|---|---|
| Instalacja | Wbudowany w Pythona | `pip install pytest` |
| Klasy testowe | Wymagane (`TestCase`) | Opcjonalne |
| Asercje | `self.assertEqual(a, b)` | `assert a == b` |
| Uruchomienie | `python -m unittest` | `pytest` |
| Składnia | Bardziej formalna | Prostsza, krótsza |

### 17.10. Podsumowanie — uruchamianie testów

```bash
# unittest
python -m unittest test_plik.py                          # Cały plik
python -m unittest test_plik.py -v                       # Szczegółowo
python -m unittest test_plik.TestKlasa                   # Konkretna klasa
python -m unittest test_plik.TestKlasa.test_metoda       # Konkretny test

# pytest
pytest                                                    # Wszystko w katalogu
pytest test_plik.py                                       # Konkretny plik
pytest test_plik.py -v                                    # Szczegółowo
pytest test_plik.py::test_nazwa                           # Konkretna funkcja
pytest test_plik.py::TestKlasa::test_metoda               # Konkretna metoda
```

---

## 18. Przydatne wzorce i idiomy Pythona

Na zakończenie — zbiór przydatnych wzorców i idiomów, które pojawiają się regularnie w programowaniu w Pythonie. Znajomość tych wzorców pozwala pisać kod bardziej idiomatyczny ("pythoniczny"), czyli taki, który jest naturalny i czytelny dla innych programistów Pythona.

### 18.1. Zamiana wartości dwóch zmiennych

Python pozwala na zamianę bez zmiennej tymczasowej:

```python
a, b = 5, 10
a, b = b, a    # Teraz a=10, b=5

# W kontekście listy — zamiana elementów
tablica = [1, 2, 3, 4, 5]
tablica[0], tablica[4] = tablica[4], tablica[0]
# [5, 2, 3, 4, 1]
```

### 18.2. `if __name__ == "__main__":`

Ten warunek sprawdza, czy plik jest uruchamiany bezpośrednio (nie importowany). Kod wewnątrz tego bloku wykona się tylko przy bezpośrednim uruchomieniu skryptu:

```python
def moja_funkcja():
    return 42

class MojaKlasa:
    pass

# Ten kod wykona się TYLKO przy: python plik.py
# NIE wykona się przy: from plik import MojaKlasa
if __name__ == "__main__":
    print("Program uruchomiony bezpośrednio")
    wynik = moja_funkcja()
    print(f"Wynik: {wynik}")
```

To jest szczególnie ważne przy testach jednostkowych — moduł z testowanym kodem musi pozwalać na importowanie bez uruchamiania programu głównego.

### 18.3. Rozpakowywanie z `*` (operatorem gwiazdki)

Gwiazdka `*` pozwala na rozpakowywanie dowolnej liczby elementów:

```python
# Rozpakowywanie z resztą
lista = [1, 2, 3, 4, 5]
pierwszy, *srodek, ostatni = lista
print(pierwszy)  # 1
print(srodek)    # [2, 3, 4]
print(ostatni)   # 5

# Połączenie dwóch list
a = [1, 2, 3]
b = [4, 5, 6]
polaczone = [*a, *b]  # [1, 2, 3, 4, 5, 6]
```

### 18.4. Dictionary comprehension

Analogicznie do list comprehension, ale tworzy słowniki:

```python
# Kwadraty liczb jako słownik
kwadraty = {x: x**2 for x in range(1, 6)}
print(kwadraty)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Konwersja dwóch list na słownik
klucze = ["a", "b", "c"]
wartosci = [1, 2, 3]
słownik = {k: v for k, v in zip(klucze, wartosci)}
print(słownik)  # {'a': 1, 'b': 2, 'c': 3}
```

### 18.5. Formatowanie wypisywania tabel w konsoli

Przy wyświetlaniu danych tabelarycznych warto zadbać o wyrównanie kolumn:

```python
# Wyrównanie kolumn za pomocą f-stringów
dane = [
    ("Jan", 25, "Warszawa"),
    ("Anna", 30, "Kraków"),
    ("Piotr Wiśniewski", 22, "Gdańsk")
]

print(f"{'Imię':<20}{'Wiek':>5}  {'Miasto':<15}")
print("-" * 42)
for imie, wiek, miasto in dane:
    print(f"{imie:<20}{wiek:>5}  {miasto:<15}")

# Wynik:
# Imię                 Wiek  Miasto
# ------------------------------------------
# Jan                     25  Warszawa
# Anna                    30  Kraków
# Piotr Wiśniewski        22  Gdańsk
```

### 18.6. Podkreślnik `_` — konwencje

Podkreślnik ma kilka konwencji w Pythonie:

| Użycie | Znaczenie | Przykład |
|---|---|---|
| `_` | Zmienna, której nie używamy | `for _ in range(5):` |
| `_pole` | Pole chronione (konwencja) | `self._saldo` |
| `__pole` | Pole prywatne (name mangling) | `self.__haslo` |
| `__metoda__` | Metoda specjalna Pythona | `__init__`, `__str__` |

### 18.7. Najczęstsze pułapki i błędy w Pythonie

Poniżej zebrane są najczęstsze pułapki, na które warto uważać:

**1. Modyfikowalna wartość domyślna parametru:**

```python
# ❌ PUŁAPKA — lista jest współdzielona między wywołaniami!
def dodaj_element(element, lista=[]):
    lista.append(element)
    return lista

print(dodaj_element(1))  # [1]
print(dodaj_element(2))  # [1, 2] — nie [2]!
print(dodaj_element(3))  # [1, 2, 3] — nie [3]!

# ✅ POPRAWNIE — używamy None jako domyślnej wartości
def dodaj_element(element, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista
```

**2. Porównanie `==` vs `is`:**

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)    # True  — te same WARTOŚCI
print(a is b)    # False — to RÓŻNE obiekty w pamięci

# Dla None ZAWSZE używaj 'is'
x = None
if x is None:     # ✅ Poprawnie
    print("None")
```

**3. Kopiowanie listy — referencja vs kopia:**

```python
oryg = [1, 2, 3]

# ❌ REFERENCJA — obie zmienne wskazują na TĘ SAMĄ listę
kopia = oryg
kopia.append(4)
print(oryg)   # [1, 2, 3, 4] — oryginał też się zmienił!

# ✅ KOPIA — nowa, niezależna lista
kopia = oryg.copy()    # lub: kopia = oryg[:]
kopia.append(5)
print(oryg)   # [1, 2, 3, 4] — oryginał bez zmian
```

**4. Dzielenie zwraca float:**

```python
wynik = 10 / 2
print(wynik)        # 5.0 (float, nie int!)
print(type(wynik))  # <class 'float'>

# Gdy potrzebujesz int:
wynik = 10 // 2     # 5 (int)
```

**5. Indeksowanie od 0:**

```python
lista = ["A", "B", "C"]

# ❌ Częsty błąd — lista[3] nie istnieje
# print(lista[3])  # IndexError!

# ✅ Ostatni element: lista[-1] lub lista[len(lista)-1]
print(lista[-1])   # "C"
print(lista[2])    # "C"
```

### 18.8. Wzorzec menu programu (pętla główna)

Najczęstszy wzorzec programu konsolowego — nieskończona pętla wyświetlająca menu opcji, pobierająca wybór użytkownika i wykonująca odpowiednią akcję. Program działa, dopóki użytkownik nie wybierze opcji wyjścia.

```python
def menu():
    """Wyświetla menu główne i zwraca wybór użytkownika."""
    print("\n" + "=" * 30)
    print("   MENU GŁÓWNE")
    print("=" * 30)
    print("1. Dodaj element")
    print("2. Wyświetl elementy")
    print("3. Wyszukaj element")
    print("4. Sortuj elementy")
    print("0. Wyjście")
    print("=" * 30)
    return input("Wybierz opcję: ")


def dodaj(lista):
    element = input("Podaj element: ")
    lista.append(element)
    print(f"Dodano: {element}")


def wyswietl(lista):
    if not lista:
        print("Lista jest pusta.")
    else:
        for i, el in enumerate(lista, 1):
            print(f"{i}. {el}")


def wyszukaj(lista):
    szukany = input("Podaj szukany element: ")
    if szukany in lista:
        print(f"Znaleziono na pozycji {lista.index(szukany) + 1}")
    else:
        print("Nie znaleziono.")


# PETLA GLOWNA PROGRAMU
dane = []

while True:
    wybor = menu()

    if wybor == "1":
        dodaj(dane)
    elif wybor == "2":
        wyswietl(dane)
    elif wybor == "3":
        wyszukaj(dane)
    elif wybor == "4":
        dane.sort()
        print("Posortowano.")
    elif wybor == "0":
        print("Do widzenia!")
        break
    else:
        print("Nieprawidlowa opcja, sprobuj ponownie.")
```

Ten wzorzec jest fundamentem wielu programów konsolowych. Kluczowe elementy:
- **`while True`** — nieskończona pętla
- **`break`** — wyjście z pętli (opcja 0)
- **Oddzielne funkcje** — każda opcja menu to osobna funkcja
- **`elif`** — obsługa wielu opcji

### 18.9. Sortowanie obiektów — parametr `key`

Sortowanie list zawierających obiekty (instancje klas) wymaga wskazania, po jakim polu (atrybucie) chcemy sortować. Do tego służy parametr `key` w funkcjach `sorted()` i `.sort()`.

```python
class Uczen:
    def __init__(self, imie, wiek, srednia):
        self.imie = imie
        self.wiek = wiek
        self.srednia = srednia

    def __repr__(self):
        return f"Uczen('{self.imie}', {self.wiek}, {self.srednia})"


uczniowie = [
    Uczen("Jan", 17, 4.2),
    Uczen("Anna", 16, 5.0),
    Uczen("Piotr", 18, 3.5),
    Uczen("Maria", 17, 4.8)
]

# Sortowanie po imieniu (alfabetycznie)
wg_imienia = sorted(uczniowie, key=lambda u: u.imie)
# [Anna, Jan, Maria, Piotr]

# Sortowanie po średniej (malejąco — najlepsi pierwsi)
wg_sredniej = sorted(uczniowie, key=lambda u: u.srednia, reverse=True)
# [Anna(5.0), Maria(4.8), Jan(4.2), Piotr(3.5)]

# Sortowanie po wielu kryteriach — krotka w key
# Najpierw po wieku (rosnaco), potem po imieniu (rosnaco)
wg_wielu = sorted(uczniowie, key=lambda u: (u.wiek, u.imie))

# Sortowanie NA MIEJSCU (modyfikuje oryginalną listę)
uczniowie.sort(key=lambda u: u.srednia)
```

**Aby wyświetlić posortowaną listę:**

```python
for u in sorted(uczniowie, key=lambda u: u.srednia, reverse=True):
    print(f"{u.imie}: średnia {u.srednia}")
# Anna: średnia 5.0
# Maria: średnia 4.8
# Jan: średnia 4.2
# Piotr: srednia 3.5
```



Zamiast `lambda` można użyć `attrgetter` z modułu `operator`. Robi to samo, ale jest nieco szybszy:

```python
from operator import attrgetter

wg_sredniej = sorted(uczniowie, key=attrgetter("srednia"), reverse=True)
wg_wielu = sorted(uczniowie, key=attrgetter("wiek", "imie"))
```