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
  - [5.4. Zasięg zmiennych (scope)](#54-zasięg-zmiennych-scope)
  - [5.5. Funkcja `lambda` — funkcje anonimowe](#55-funkcja-lambda--funkcje-anonimowe)
  - [5.6. Funkcje wbudowane — przegląd najważniejszych](#56-funkcje-wbudowane--przegląd-najważniejszych)
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
- [15. Algorytmy w Pythonie](#15-algorytmy-w-pythonie)
  - [15.1. Sortowanie przez wybieranie (Selection Sort)](#151-sortowanie-przez-wybieranie-selection-sort)
  - [15.2. Sortowanie bąbelkowe (Bubble Sort)](#152-sortowanie-bąbelkowe-bubble-sort)
  - [15.3. Wyszukiwanie liniowe](#153-wyszukiwanie-liniowe)
  - [15.4. Wyszukiwanie z wartownikiem (Sentinel Search)](#154-wyszukiwanie-z-wartownikiem-sentinel-search)
  - [15.5. Algorytm Euklidesa (NWD — Największy Wspólny Dzielnik)](#155-algorytm-euklidesa-nwd--największy-wspólny-dzielnik)
  - [15.6. Sito Eratostenesa](#156-sito-eratostenesa)
  - [15.7. Szyfr Cezara](#157-szyfr-cezara)
  - [15.8. Walidacja danych z wagami](#158-walidacja-danych-z-wagami)
  - [15.9. Usuwanie sąsiednich duplikatów](#159-usuwanie-sąsiednich-duplikatów)
  - [15.10. Zliczanie wystąpień wartości w danych](#1510-zliczanie-wystąpień-wartości-w-danych)
  - [15.11. Obliczanie średniej arytmetycznej](#1511-obliczanie-średniej-arytmetycznej)
  - [15.12. Wyodrębnianie elementów spełniających warunek](#1512-wyodrębnianie-elementów-spełniających-warunek)
  - [15.13. Sprawdzanie czy liczba jest pierwsza](#1513-sprawdzanie-czy-liczba-jest-pierwsza)
  - [15.14. Rekurencja](#1514-rekurencja)
  - [15.15. Wyszukiwanie binarne (Binary Search)](#1515-wyszukiwanie-binarne-binary-search)
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

### 5.4. Zasięg zmiennych (scope)

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

### 5.5. Funkcja `lambda` — funkcje anonimowe

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

### 5.6. Funkcje wbudowane — przegląd najważniejszych

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

Programowanie obiektowe (OOP — Object-Oriented Programming) to paradygmat, w którym program jest organizowany wokół **obiektów** — bytów łączących dane (pola/atrybuty) i zachowania (metody). Klasa jest „szablonem" opisującym jakie pola i metody będą miały jej obiekty, a obiekt to konkretna instancja klasy.

Analogicznie: klasa jest jak **przepis na ciasto** — opisuje składniki (pola) i kroki przygotowania (metody). Obiekt to **konkretne ciasto** upieczone według tego przepisu. Z jednego przepisu (klasy) możemy upiec wiele ciast (obiektów), każde z innym nadzieniem (wartościami pól).

W programowaniu obiektowym wyróżniamy cztery główne filary:

| Filar | Opis |
|---|---|
| **Abstrakcja** | Ukrywanie złożoności — pokazujemy tylko to, co potrzebne |
| **Hermetyzacja** | Kontrola dostępu do danych (private, protected, public) |
| **Dziedziczenie** | Klasa dziecko przejmuje cechy klasy rodzica |
| **Polimorfizm** | Ta sama metoda zachowuje się inaczej w różnych klasach |

### 10.1. Definicja klasy

Klasę definiujemy słowem kluczowym `class`, po którym następuje nazwa klasy (konwencja: `PascalCase` — każde słowo od wielkiej litery) i dwukropek:

```python
class Samochod:
    pass  # Pusta klasa — placeholder, gdy jeszcze nie ma kodu

# Tworzenie obiektu (instancji klasy) — nawiasy po nazwie klasy
auto = Samochod()
print(type(auto))  # <class '__main__.Samochod'>
```

### 10.2. Konstruktor `__init__` i pola instancji

Konstruktor to specjalna metoda `__init__`, która jest **automatycznie** wywoływana podczas tworzenia obiektu. Służy do inicjalizacji pól (atrybutów) obiektu. Słowo `self` to referencja do aktualnego obiektu — jest wymagane jako pierwszy parametr każdej metody instancji.

```python
class Samochod:
    def __init__(self, marka, rok):
        self.marka = marka        # Pole instancji — unikalne dla każdego obiektu
        self.rok = rok            # Pole instancji
        self.predkosc = 0         # Pole z wartością domyślną

# Tworzenie obiektów — argumenty trafiają do __init__
auto1 = Samochod("Toyota", 2020)
auto2 = Samochod("BMW", 2022)

# Każdy obiekt ma SWOJE, niezależne pola
print(auto1.marka)     # Toyota
print(auto2.marka)     # BMW
print(auto1.predkosc)  # 0
```

### 10.3. Metody instancji

Metody to funkcje zdefiniowane wewnątrz klasy. Ich pierwszym parametrem jest zawsze `self`, dzięki czemu mają dostęp do pól obiektu. Metody definiują **zachowania** obiektu.

```python
class Samochod:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok
        self.predkosc = 0

    def przyspiesz(self, wartosc):
        """Zwiększa prędkość o podaną wartość."""
        self.predkosc += wartosc

    def hamuj(self, wartosc):
        """Zmniejsza prędkość, ale nie poniżej 0."""
        self.predkosc = max(0, self.predkosc - wartosc)

    def wyswietl_info(self):
        """Wyświetla informacje o samochodzie."""
        print(f"{self.marka} ({self.rok}), prędkość: {self.predkosc} km/h")

    def pobierz_predkosc(self):
        """Zwraca aktualną prędkość (metoda z wartością zwrotną)."""
        return self.predkosc
```

**Użycie metod — wywołujemy je na obiekcie za pomocą kropki:**

```python
auto = Samochod("Toyota", 2020)
auto.przyspiesz(50)
auto.wyswietl_info()          # Toyota (2020), prędkość: 50 km/h
print(auto.pobierz_predkosc())  # 50
auto.hamuj(30)
auto.wyswietl_info()          # Toyota (2020), prędkość: 20 km/h
```

### 10.4. `self` — czym jest i dlaczego jest konieczne

`self` to nie jest słowo kluczowe — to konwencja nazewnicza (technicznie możesz nazwać ten parametr dowolnie, ale **każdy** programista Python używa `self`). Odnosi się do konkretnego obiektu, na którym wywoływana jest metoda.

Kluczowa różnica: `self.pole` to pole obiektu (trwałe), a zwykła zmienna wewnątrz metody jest lokalna (znika po wyjściu z metody):

```python
class Przyklad:
    def __init__(self):
        self.wartosc = 0           # POLE obiektu — istnieje tak długo jak obiekt

    def ustaw(self, nowa_wartosc):
        self.wartosc = nowa_wartosc  # Modyfikuje POLE obiektu

    def wyswietl(self):
        wartosc = 99                 # ZMIENNA LOKALNA — znika po wyjściu z metody
        print(f"Pole obiektu: {self.wartosc}")
        print(f"Zmienna lokalna: {wartosc}")

obj = Przyklad()
obj.ustaw(42)
obj.wyswietl()
# Pole obiektu: 42
# Zmienna lokalna: 99
```

### 10.5. Metoda `__str__` — reprezentacja tekstowa obiektu

Metoda `__str__` definiuje, co się wyświetli, gdy użyjemy `print()` na obiekcie. Bez niej `print(obiekt)` wypisze coś w stylu `<__main__.Samochod object at 0x...>`:

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f"Produkt: {self.nazwa}, Cena: {self.cena} zł"

p = Produkt("Laptop", 3500)
print(p)  # Produkt: Laptop, Cena: 3500 zł (zamiast <...object...>)
```

### 10.6. `__repr__` vs `__str__` — dwie reprezentacje tekstowe

Python oferuje dwie metody specjalne do tworzenia tekstowej reprezentacji obiektu. Zrozumienie różnicy między nimi jest ważne:

| Metoda | Cel | Wywoływana przez | Odbiorca |
|---|---|---|---|
| `__str__` | Czytelna reprezentacja | `print()`, `str()`, f-string | Użytkownik końcowy |
| `__repr__` | Jednoznaczna reprezentacja | `repr()`, konsola interaktywna | Programista (debugowanie) |

`__repr__` powinna zwracać string, który — idealnie — pozwoliłby odtworzyć obiekt. `__str__` powinna zwracać przystępną, ładną formę do wyświetlania.

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Dla programisty — jednoznaczna, techniczna
        return f"Punkt(x={self.x}, y={self.y})"

    def __str__(self):
        # Dla użytkownika — ładna, czytelna
        return f"({self.x}, {self.y})"

p = Punkt(3, 5)

print(p)          # (3, 5)          <- wywołuje __str__
print(repr(p))    # Punkt(x=3, y=5) <- wywołuje __repr__
print(f"Punkt: {p}")  # Punkt: (3, 5) <- f-string wywołuje __str__
```

**Ważna zasada:** Jeśli klasa ma zdefiniowaną tylko `__repr__` (bez `__str__`), to `print()` użyje `__repr__` jako zapasowej. Jeśli zdefiniujesz tylko `__str__`, to `repr()` pokaże domyślną `<__main__.Klasa object at 0x...>`.

**Praktyczna rada:** Zawsze definiuj przynajmniej `__repr__`. Jeśli potrzebujesz ładnego wyświetlania dla użytkownika, dodaj też `__str__`.

```python
class Ocena:
    def __init__(self, przedmiot, wartosc):
        self.przedmiot = przedmiot
        self.wartosc = wartosc

    def __repr__(self):
        return f"Ocena('{self.przedmiot}', {self.wartosc})"

    def __str__(self):
        return f"{self.przedmiot}: {self.wartosc}"

# Różnica widoczna np. przy listach:
oceny = [Ocena("Matematyka", 5), Ocena("Polski", 4)]
print(oceny)         # [Ocena('Matematyka', 5), Ocena('Polski', 4)] <- __repr__!
print(oceny[0])      # Matematyka: 5 <- __str__
```

Zauważ: `print(lista)` wyświetla elementy listy za pomocą `__repr__`, nie `__str__`. To dlatego, że lista używa `repr()` na swoich elementach.

---

## 11. Programowanie obiektowe — hermetyzacja

Hermetyzacja (enkapsulacja) to mechanizm **ukrywania wewnętrznych szczegółów implementacji** klasy. Zamiast pozwalać na bezpośredni dostęp do pól, udostępniamy kontrolowane metody (gettery/settery). Dzięki temu klasa ma pełną kontrolę nad swoimi danymi — może np. walidować wartości przed ich zapisaniem.

### 11.1. Poziomy dostępu w Pythonie

W Pythonie nie ma słów kluczowych `public`, `private`, `protected` jak w Javie czy C#. Zamiast tego stosowana jest **konwencja nazewnicza** oparta na podkreślnikach:

| Konwencja | Zapis | Dostęp z zewnątrz | Klasy potomne | Odpowiednik Java/C# |
|---|---|---|---|---|
| Publiczne | `self.pole` | ✅ Pełny | ✅ Tak | `public` |
| Chronione | `self._pole` | ⚠️ Możliwy (niezalecany) | ✅ Tak | `protected` |
| Prywatne | `self.__pole` | ❌ Name mangling | ❌ Nie | `private` |

**Jeden podkreślnik `_` (protected)** — to jedynie sygnał dla innych programistów: „nie dotykaj tego pola z zewnątrz klasy". Python tego nie wymusza — ale łamanie tej konwencji jest uważane za złą praktykę.

**Dwa podkreślniki `__` (private)** — Python stosuje mechanizm zwany **name mangling**: pole `self.__pensja` w klasie `Pracownik` jest wewnętrznie zmieniane na `self._Pracownik__pensja`. To nie jest prawdziwe ukrywanie (nadal można się dostać), ale skutecznie chroni przed przypadkowym dostępem.

```python
class Pracownik:
    def __init__(self, imie, pensja, stanowisko):
        self.imie = imie               # PUBLIC
        self._stanowisko = stanowisko  # PROTECTED
        self.__pensja = pensja         # PRIVATE (name mangling)

p = Pracownik("Jan", 5000, "Programista")

print(p.imie)              # ✅ OK
print(p._stanowisko)       # ⚠️ Działa, ale jest niezalecane
# print(p.__pensja)        # ❌ AttributeError!
print(p._Pracownik__pensja)# ⚠️ Technicznie możliwe, ale NIGDY tego nie rób
```

### 11.2. Gettery i settery — metody dostępu

Getter (pobierz) i setter (ustaw) to metody publiczne, które kontrolują dostęp do prywatnych pól. Setter może zawierać walidację — odrzucanie niepoprawnych wartości:

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.__nazwa = nazwa
        self.__cena = cena

    # Getter — odczyt
    def pobierz_nazwe(self):
        return self.__nazwa

    def pobierz_cene(self):
        return self.__cena

    # Setter z walidacją
    def ustaw_cene(self, nowa_cena):
        if nowa_cena >= 0:
            self.__cena = nowa_cena
        else:
            print("Cena nie może być ujemna!")

p = Produkt("Laptop", 3500)
print(p.pobierz_cene())    # 3500
p.ustaw_cene(4000)         # OK
p.ustaw_cene(-100)         # Cena nie może być ujemna!
print(p.pobierz_cene())    # 4000 (nie -100)
```

### 11.3. Dekorator `@property` — pythoniczny getter/setter

Dekorator `@property` pozwala na dostęp do pola jak do zwykłego atrybutu (bez nawiasów), ale z kontrolą gettera i settera. To bardziej „pythonowy" sposób niż tradycyjne metody `pobierz_X()` / `ustaw_X()`:

```python
class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        """Getter — wywoływany przy ODCZYCIE: t.celsius"""
        return self.__celsius

    @celsius.setter
    def celsius(self, wartosc):
        """Setter — wywoływany przy ZAPISIE: t.celsius = 30"""
        if wartosc < -273.15:
            raise ValueError("Temperatura poniżej zera absolutnego!")
        self.__celsius = wartosc

    @property
    def fahrenheit(self):
        """Właściwość tylko do odczytu (brak settera)."""
        return self.__celsius * 9/5 + 32

# Użycie — wygląda jak bezpośredni dostęp do pola, ale działa getter/setter!
t = Temperatura(25)
print(t.celsius)       # 25   (getter)
print(t.fahrenheit)    # 77.0 (getter obliczeniowy)

t.celsius = 30         # Setter z walidacją
print(t.celsius)       # 30
```

---

## 12. Programowanie obiektowe — zmienne klasowe i metody statyczne

### 12.1. Zmienne klasowe (static fields)

Zmienne klasowe należą **do klasy**, nie do konkretnego obiektu. Są wspólne dla WSZYSTKICH instancji — zmiana przez jedną instancję jest widoczna dla wszystkich. Typowe zastosowanie: zliczanie utworzonych obiektów, przechowywanie stałych.

```python
class Uzytkownik:
    # Zmienna KLASOWA — wspólna dla wszystkich instancji
    licznik = 0

    def __init__(self, nazwa):
        Uzytkownik.licznik += 1          # Inkrementacja przez NAZWĘ KLASY
        self.id = Uzytkownik.licznik     # Automatyczne nadanie unikalnego ID
        self.nazwa = nazwa

    def wyswietl(self):
        print(f"ID: {self.id}, Nazwa: {self.nazwa}")

u1 = Uzytkownik("Jan")
u2 = Uzytkownik("Anna")
u3 = Uzytkownik("Piotr")

u1.wyswietl()   # ID: 1, Nazwa: Jan
u2.wyswietl()   # ID: 2, Nazwa: Anna
u3.wyswietl()   # ID: 3, Nazwa: Piotr

# Dostęp do zmiennej klasowej — przez nazwę klasy
print(f"Łączna liczba użytkowników: {Uzytkownik.licznik}")  # 3
```

**Kluczowa pułapka — modyfikacja zmiennej klasowej:**

```python
class Licznik:
    wartosc = 0

    def __init__(self):
        # ✅ POPRAWNIE — modyfikuje zmienną KLASY
        Licznik.wartosc += 1

        # ❌ BŁĄD — tworzy NOWĄ zmienną INSTANCJI o tej samej nazwie!
        # self.wartosc += 1
        # Odczyt self.wartosc znajdzie zmienną klasową, ale += utworzy NOWĄ instancji
```

Zasada jest prosta: do **modyfikacji** zmiennej klasowej zawsze używaj nazwy klasy (`NazwaKlasy.pole`), nie `self`.

### 12.2. Zmienne klasowe — tablice i kolekcje

Zmienne klasowe mogą przechowywać tablice wspólne dla wszystkich obiektów, np. nazwy plików zasobów:

```python
class Gracz:
    dozwolone_klasy = ["Wojownik", "Mag", "Łucznik", "Złodziej"]
    ikony = ["icon_0.png", "icon_1.png", "icon_2.png", "icon_3.png"]

    def __init__(self, nazwa, klasa_id):
        self.nazwa = nazwa
        self.klasa_id = klasa_id

    def pobierz_klase(self):
        return Gracz.dozwolone_klasy[self.klasa_id]

    def pobierz_ikone(self):
        return Gracz.ikony[self.klasa_id]
```

### 12.3. Metody statyczne — `@staticmethod`

Metoda statyczna nie potrzebuje dostępu do instancji (`self`) ani do klasy (`cls`). Jest po prostu funkcją umieszczoną w kontekście klasy jako organizacja kodu. Wywoływana jest na **klasie**, nie na obiekcie — nie trzeba tworzyć instancji, aby ją wywołać.

```python
class Narzedzia:
    @staticmethod
    def jest_parzysta(liczba):
        return liczba % 2 == 0

    @staticmethod
    def policz_samogloski(tekst):
        samogloski = "aąeęiouóyAĄEĘIOUÓY"
        return sum(1 for z in tekst if z in samogloski)

    @staticmethod
    def odwroc_napis(tekst):
        return tekst[::-1]

# Wywołanie — BEZ tworzenia obiektu!
print(Narzedzia.jest_parzysta(4))              # True
print(Narzedzia.policz_samogloski("Python"))   # 1
print(Narzedzia.odwroc_napis("Python"))        # nohtyP
```

### 12.4. Metody klasowe — `@classmethod`

Metoda klasowa otrzymuje referencję do **klasy** jako pierwszy argument (`cls`). Różni się od `@staticmethod` tym, że ma dostęp do zmiennych klasowych i może tworzyć nowe instancje:

```python
class Pracownik:
    liczba_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    @classmethod
    def ile_pracownikow(cls):
        return cls.liczba_pracownikow

    @classmethod
    def stworz_programiste(cls, imie):
        """Metoda fabrykująca — tworzy instancję z domyślnym stanowiskiem."""
        return cls(imie, "Programista")

p1 = Pracownik("Jan", "Tester")
p2 = Pracownik.stworz_programiste("Anna")

print(p2.stanowisko)                   # Programista
print(Pracownik.ile_pracownikow())     # 2
```

**Porównanie: `@staticmethod` vs `@classmethod`:**

| Cecha | `@staticmethod` | `@classmethod` |
|---|---|---|
| Pierwszy argument | Brak | `cls` (klasa) |
| Dostęp do pól klasy | ❌ Nie | ✅ Tak (przez `cls`) |
| Tworzenie instancji | Ręcznie | Przez `cls(...)` |
| Zastosowanie | Funkcje narzędziowe | Fabryki obiektów, dostęp do klasy |

---

## 13. Programowanie obiektowe — konstruktory zaawansowane

### 13.1. Konstruktor z wartościami domyślnymi

W Pythonie nie ma przeciążania konstruktorów (overloading) — nie można mieć dwóch `__init__` z różnymi listami parametrów. Zamiast tego stosuje się **jeden konstruktor z parametrami domyślnymi**:

```python
class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def wyswietl(self):
        print(f"({self.x}, {self.y})")

# Różne sposoby tworzenia — jeden konstruktor, wiele wariantów
p1 = Punkt()           # (0, 0) — oba domyślne
p2 = Punkt(5)          # (5, 0) — x podane, y domyślne
p3 = Punkt(3, 7)       # (3, 7) — oba podane
p4 = Punkt(y=10)       # (0, 10) — argument nazwany
```

### 13.2. Wzorzec z `None` — pełny zamiennik dwóch konstruktorów

Gdy konstruktor musi się zachowywać **zupełnie inaczej** w zależności od tego, czy argumenty zostały podane:

```python
class Element:
    licznik = 0

    def __init__(self, wartosc=None):
        Element.licznik += 1
        self.id = Element.licznik

        if wartosc is None:
            # KONSTRUKTOR BEZPARAMETROWY — losujemy wartość
            import random
            self.wartosc = random.randint(1, 6)
        else:
            # KONSTRUKTOR Z PARAMETREM — używamy podanej wartości
            if 1 <= wartosc <= 6:
                self.wartosc = wartosc
            else:
                self.wartosc = 0  # Walidacja — wartość poza zakresem

    def wyswietl(self):
        print(f"ID: {self.id}, Wartość: {self.wartosc}")

e1 = Element()          # Losowa wartość 1-6
e2 = Element(4)         # Wartość 4
e3 = Element(99)        # Wartość 0 (poza zakresem)
```

### 13.3. Walidacja w konstruktorze

Konstruktor to idealne miejsce na sprawdzanie poprawności danych:

```python
class Ocena:
    def __init__(self, wartosc):
        if isinstance(wartosc, int) and 1 <= wartosc <= 6:
            self.wartosc = wartosc
        else:
            self.wartosc = 0
            print(f"Uwaga: {wartosc} to niepoprawna ocena, ustawiono 0")

o1 = Ocena(5)     # OK
o2 = Ocena(9)     # Uwaga: 9 to niepoprawna ocena, ustawiono 0
o3 = Ocena(-1)    # Uwaga: -1 to niepoprawna ocena, ustawiono 0
```

### 13.4. Kopiowanie obiektów

W Pythonie nie ma konstruktora kopiującego jak w C++. Istnieją dwa główne sposoby kopiowania obiektów:

```python
# Sposób 1: Metoda kopiująca w klasie
class Notatka:
    def __init__(self, tytul="", tresc=""):
        self.tytul = tytul
        self.tresc = tresc

    def kopiuj_z(self, inna):
        """Kopiuje dane z innego obiektu."""
        self.tytul = inna.tytul
        self.tresc = inna.tresc

oryg = Notatka("Zakupy", "Mleko, chleb")
kopia = Notatka()
kopia.kopiuj_z(oryg)

# Sposób 2: Moduł copy
import copy

kopia_plytka = copy.copy(oryg)      # Płytka kopia
kopia_gleb = copy.deepcopy(oryg)    # Głęboka kopia (kopiuje zagnieżdżone obiekty)
```

Różnica: **płytka kopia** kopiuje obiekt „na powierzchni" — jeśli obiekt zawiera referencje do innych obiektów (np. listę), kopia będzie wskazywać na tę samą listę. **Głęboka kopia** kopiuje rekurencyjnie wszystko.

---

## 14. Programowanie obiektowe — dziedziczenie, polimorfizm i klasy abstrakcyjne

Dziedziczenie pozwala tworzyć nowe klasy na bazie istniejących. Klasa potomna (dziecko) automatycznie otrzymuje wszystkie pola i metody klasy bazowej (rodzica) i może je rozszerzać lub nadpisywać.

### 14.1. Podstawy dziedziczenia

Dziedziczenie deklarujemy, podając nazwę klasy bazowej w nawiasie po nazwie klasy potomnej:

```python
# Klasa bazowa (rodzic/nadklasa)
class Zwierze:
    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem {self.nazwa}, mam {self.wiek} lat")

    def wydaj_dzwiek(self):
        print("...")


# Klasa potomna (dziecko/podklasa)
class Pies(Zwierze):     # Pies DZIEDZICZY po Zwierze
    def __init__(self, nazwa, wiek, rasa):
        super().__init__(nazwa, wiek)   # Wywołanie konstruktora RODZICA
        self.rasa = rasa                # Dodatkowe pole tylko dla Pies

    def wydaj_dzwiek(self):             # NADPISANIE metody rodzica (override)
        print("Hau hau!")

    def aportuj(self):                  # Nowa metoda — tylko dla Pies
        print(f"{self.nazwa} aportuje!")


class Kot(Zwierze):
    def __init__(self, nazwa, wiek, kolor):
        super().__init__(nazwa, wiek)
        self.kolor = kolor

    def wydaj_dzwiek(self):
        print("Miau!")
```

**Użycie — klasa potomna ma dostęp do metod rodzica:**

```python
pies = Pies("Burek", 5, "Labrador")
pies.przedstaw_sie()   # Jestem Burek, mam 5 lat (ODZIEDZICZONA metoda)
pies.wydaj_dzwiek()    # Hau hau! (NADPISANA metoda)
pies.aportuj()         # Burek aportuje! (WŁASNA metoda)
```

### 14.2. `super()` — wywoływanie metod rodzica

Funkcja `super()` zwraca referencję do klasy bazowej, co pozwala wywoływać jej metody z poziomu klasy potomnej. Jest szczególnie ważna w konstruktorze — jeśli nie wywołamy `super().__init__()`, pola zdefiniowane w rodzicu nie zostaną zainicjalizowane.

```python
class Bazowa:
    def __init__(self):
        self.pole_bazowe = "wartość bazowa"

    def komunikat(self, tekst):
        print(f"[INFO] {tekst}")


class Potomna(Bazowa):
    def __init__(self):
        super().__init__()                # KONIECZNE — inicjalizuje pola rodzica
        self.pole_potomne = "wartość potomna"

    def akcja(self, tekst):
        self.komunikat(tekst)             # Wywołanie odziedziczonej metody
        # Albo: super().komunikat(tekst) — to samo, ale jawne
```

### 14.3. Hermetyzacja a dziedziczenie

Ważne pytanie: jakie pola rodzica są widoczne w dziecku?

```python
class Rodzic:
    def __init__(self):
        self.publiczne = "dostępne wszędzie"
        self._chronione = "dostępne w klasach potomnych"
        self.__prywatne = "NIEDOSTĘPNE w klasach potomnych"


class Dziecko(Rodzic):
    def __init__(self):
        super().__init__()

    def test(self):
        print(self.publiczne)      # ✅ Publiczne — OK
        print(self._chronione)     # ✅ Chronione — OK (to jego przeznaczenie!)
        # print(self.__prywatne)   # ❌ AttributeError — prywatne rodzica
```

### 14.4. Wzorzec: logika stanów z dziedziczeniem

Połączenie dziedziczenia z logiką stanów — klasa bazowa z wspólną metodą, klasy potomne z własną logiką:

```python
class Urzadzenie:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def komunikat(self, tekst):
        print(f"[{self.nazwa}] {tekst}")


class Przelacznik(Urzadzenie):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.__wlaczony = False    # Stan wewnętrzny

    def wlacz(self):
        if not self.__wlaczony:     # Tylko jeśli wyłączony
            self.__wlaczony = True
            self.komunikat("Włączono")
        # Jeśli już włączony — nic nie rób (ochrona)

    def wylacz(self):
        if self.__wlaczony:         # Tylko jeśli włączony
            self.__wlaczony = False
            self.komunikat("Wyłączono")

p = Przelacznik("Lampa")
p.wlacz()       # [Lampa] Włączono
p.wlacz()       # (nic — już włączona)
p.wylacz()      # [Lampa] Wyłączono
p.wylacz()      # (nic — już wyłączona)
```

### 14.5. Sprawdzanie typu i dziedziczenia

```python
pies = Pies("Burek", 5, "Labrador")

# isinstance — czy obiekt jest danego typu (uwzględnia dziedziczenie)
print(isinstance(pies, Pies))     # True
print(isinstance(pies, Zwierze))  # True (Pies JEST Zwierzęciem)
print(isinstance(pies, Kot))      # False

# issubclass — czy klasa jest podklasą
print(issubclass(Pies, Zwierze))  # True
print(issubclass(Pies, Kot))      # False
```

### 14.6. Podsumowanie — kiedy co stosować w OOP

| Mechanizm | Kiedy stosować | Przykład |
|---|---|---|
| Klasa z polami | Gdy obiekty przechowują dane | Osoba, Produkt, Notatka |
| Metody instancji | Gdy metoda operuje na danych obiektu | `wyswietl()`, `oblicz()` |
| Pola prywatne `__` | Gdy pole nie powinno być dostępne z zewnątrz | Saldo konta, hasło |
| Pola chronione `_` | Gdy pole ma być dostępne w klasach potomnych | Wewnętrzny stan urządzenia |
| `@property` | Kontrolowany dostęp do pola (getter/setter) | Walidacja przy ustawianiu |
| Zmienne klasowe | Dane wspólne dla WSZYSTKICH obiektów | Licznik instancji, stałe |
| `@staticmethod` | Funkcja narzędziowa powiązana z klasą | Walidacja, konwersja |
| `@classmethod` | Alternatywne sposoby tworzenia obiektów | Metody fabrykujące |
| Dziedziczenie | Klasy o wspólnych cechach, ale z różnicami | Zwierzę → Pies, Kot |
| `super()` | Wywołanie metody/konstruktora rodzica | Inicjalizacja pól bazowych |

Programowanie obiektowe to potężne narzędzie organizacji kodu. Kluczowe jest zrozumienie, że klasa to nie tylko "zbiór zmiennych i funkcji" — to **model** rzeczywistego lub abstrakcyjnego bytu, który łączy dane z zachowaniami w spójną całość.

### 14.7. Polimorfizm

Polimorfizm (z greckiego „wiele form") to zdolność obiektów różnych klas do reagowania na tę samą metodę w sposób specyficzny dla danej klasy. Innymi słowy: ta sama nazwa metody, ale różne zachowania w zależności od tego, na jakim obiekcie jest wywoływana.

Polimorfizm jest ściśle powiązany z dziedziczeniem — klasy potomne **nadpisują** (override) metody klasy bazowej, dostarczając własną implementację.

```python
class Figura:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def pole(self):
        """Metoda do nadpisania w klasach potomnych."""
        return 0

    def wyswietl(self):
        print(f"{self.nazwa}: pole = {self.pole():.2f}")


class Kwadrat(Figura):
    def __init__(self, bok):
        super().__init__("Kwadrat")
        self.bok = bok

    def pole(self):                    # Nadpisanie metody
        return self.bok ** 2


class Kolo(Figura):
    def __init__(self, promien):
        super().__init__("Koło")
        self.promien = promien

    def pole(self):                    # Nadpisanie metody
        import math
        return math.pi * self.promien ** 2


class Trojkat(Figura):
    def __init__(self, podstawa, wysokosc):
        super().__init__("Trójkąt")
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def pole(self):                    # Nadpisanie metody
        return 0.5 * self.podstawa * self.wysokosc
```

**Polimorfizm w akcji — jedna pętla, różne zachowania:**

```python
figury = [
    Kwadrat(5),
    Kolo(3),
    Trojkat(6, 4)
]

# Ta sama metoda wyswietl() — każda figura reaguje po swojemu
for figura in figury:
    figura.wyswietl()
# Kwadrat: pole = 25.00
# Koło: pole = 28.27
# Trójkąt: pole = 12.00
```

To jest sedno polimorfizmu: **nie musimy wiedzieć**, jakiego dokładnie typu jest obiekt w liście — wystarczy, że wiemy, iż ma metodę `pole()` i `wyswietl()`. Każdy obiekt sam „wie", jak obliczyć swoje pole.

**Polimorfizm bez dziedziczenia — duck typing:**

W Pythonie polimorfizm nie wymaga formalnego dziedziczenia. Wystarczy, że obiekty mają metodę o tej samej nazwie. To podejście nazywa się **duck typing** — „jeśli coś chodzi jak kaczka i kwacze jak kaczka, to jest kaczką":

```python
class Pies:
    def glos(self):
        return "Hau!"

class Kot:
    def glos(self):
        return "Miau!"

class Kaczka:
    def glos(self):
        return "Kwak!"

# Nie muszą dziedziczyć po wspólnej klasie!
zwierzeta = [Pies(), Kot(), Kaczka()]
for z in zwierzeta:
    print(z.glos())  # Hau! Miau! Kwak!
```

### 14.8. Klasy abstrakcyjne — moduł `abc`

Klasa abstrakcyjna to klasa, której **nie można bezpośrednio instancjonować** (utworzyć z niej obiektu). Służy wyłącznie jako baza dla klas potomnych. Wymusza na klasach potomnych zaimplementowanie określonych metod — dzięki temu mamy gwarancję, że każda podklasa będzie miała wymagane metody.

W Pythonie klasy abstrakcyjne tworzymy za pomocą modułu `abc` (Abstract Base Classes):

```python
from abc import ABC, abstractmethod


class Figura(ABC):    # Dziedziczy po ABC — jest klasą abstrakcyjną

    def __init__(self, nazwa):
        self.nazwa = nazwa

    @abstractmethod
    def pole(self):
        """Każda figura MUSI zaimplementować tę metodę."""
        pass

    @abstractmethod
    def obwod(self):
        """Każda figura MUSI zaimplementować tę metodę."""
        pass

    def wyswietl(self):
        """Metoda konkretna — wspólna dla wszystkich figur."""
        print(f"{self.nazwa}: pole={self.pole():.2f}, obwód={self.obwod():.2f}")
```

**Co to oznacza w praktyce:**

```python
# ❌ NIE MOŻNA utworzyć obiektu klasy abstrakcyjnej
# f = Figura("test")  # TypeError: Can't instantiate abstract class

# ❌ Klasa potomna BEZ implementacji wszystkich metod abstrakcyjnych
# class Kwadrat(Figura):
#     def pole(self):
#         return self.bok ** 2
#     # Brak obwod() → TypeError przy próbie utworzenia!

# ✅ Klasa potomna z PEŁNĄ implementacją
class Prostokat(Figura):
    def __init__(self, a, b):
        super().__init__("Prostokąt")
        self.a = a
        self.b = b

    def pole(self):          # Implementacja metody abstrakcyjnej
        return self.a * self.b

    def obwod(self):         # Implementacja metody abstrakcyjnej
        return 2 * (self.a + self.b)


class Kolo(Figura):
    def __init__(self, promien):
        super().__init__("Koło")
        self.promien = promien

    def pole(self):
        import math
        return math.pi * self.promien ** 2

    def obwod(self):
        import math
        return 2 * math.pi * self.promien


# Użycie — polimorfizm z gwarancją interfejsu
figury = [Prostokat(4, 6), Kolo(5)]
for f in figury:
    f.wyswietl()
# Prostokąt: pole=24.00, obwód=20.00
# Koło: pole=78.54, obwód=31.42
```

**Kiedy stosować klasy abstrakcyjne:**

| Scenariusz | Zwykła klasa bazowa | Klasa abstrakcyjna |
|---|---|---|
| Klasa bazowa powinna mieć swoje obiekty | ✅ Tak | ❌ Nie |
| Chcemy WYMUSIĆ implementację metod | ❌ Nie gwarantuje | ✅ Wymusza |
| Klasa bazowa to tylko "szablon" | ⚠️ Może, ale nie musi | ✅ Idealnie |
| Potrzebujemy wspólnych metod konkretnych | ✅ Tak | ✅ Tak (obok abstrakcyjnych) |

---

## 15. Algorytmy w Pythonie

Algorytmy to precyzyjne przepisy na rozwiązanie problemu. Składają się z jednoznacznie określonych kroków, prowadzących od danych wejściowych do pożądanego wyniku. Poniżej przedstawione są najważniejsze algorytmy, które warto znać — każdy z pełną implementacją w Pythonie, wyjaśnieniem idei działania i przebiegiem krok po kroku.

**Złożoność algorytmów — krótkie wprowadzenie:**

| Notacja | Nazwa | Opis | Przykład |
|---|---|---|---|
| O(1) | Stała | Czas nie zależy od rozmiaru danych | Dostęp do elementu listy po indeksie |
| O(n) | Liniowa | Czas rośnie proporcjonalnie | Wyszukiwanie liniowe |
| O(n²) | Kwadratowa | Czas rośnie kwadratowo | Sortowanie bąbelkowe, przez wybieranie |
| O(log n) | Logarytmiczna | Bardzo efektywna | Wyszukiwanie binarne |

W praktyce nie musimy dokładnie obliczać złożoności — wystarczy wiedzieć, że algorytmy O(n²) są wolne dla dużych danych, a O(n) i O(log n) są szybkie.

### 15.1. Sortowanie przez wybieranie (Selection Sort)

**Idea algorytmu:** W każdym kroku szukamy elementu ekstremalnego (minimum lub maksimum) w nieposortowanej części tablicy i zamieniamy go z pierwszym nieposortowanym elementem. Po każdym kroku posortowana część tablicy rośnie o jeden element.

**Złożoność czasowa:** O(n²) — dla tablicy n elementów wykonujemy n przejść, każde przeszukuje malejący fragment.

**Sortowanie rosnąco (szukanie minimum):**

```python
def sortowanie_przez_wybieranie_rosnaco(tablica):
    n = len(tablica)
    for i in range(n - 1):
        # Zakładamy, że minimum jest na pozycji i
        indeks_min = i
        # Szukamy mniejszego elementu w reszcie tablicy
        for j in range(i + 1, n):
            if tablica[j] < tablica[indeks_min]:
                indeks_min = j
        # Zamiana elementów — Python pozwala na elegancki swap
        tablica[i], tablica[indeks_min] = tablica[indeks_min], tablica[i]
```

**Przebieg krok po kroku** (dla tablicy `[5, 3, 8, 1, 4]`):

| Krok | Tablica przed | Znalezione min | Zamiana | Tablica po |
|---|---|---|---|---|
| i=0 | **[5**, 3, 8, 1, 4] | min=1 (indeks 3) | 5 ↔ 1 | [**1**, 3, 8, 5, 4] |
| i=1 | [1, **3**, 8, 5, 4] | min=3 (indeks 1) | bez zamiany | [1, **3**, 8, 5, 4] |
| i=2 | [1, 3, **8**, 5, 4] | min=4 (indeks 4) | 8 ↔ 4 | [1, 3, **4**, 5, 8] |
| i=3 | [1, 3, 4, **5**, 8] | min=5 (indeks 3) | bez zamiany | [1, 3, 4, **5**, 8] |

Wynik: `[1, 3, 4, 5, 8]` ✅

**Sortowanie malejąco (szukanie maksimum):**

Wystarczy zamienić `<` na `>` w porównaniu. Warto też wyodrębnić szukanie maksimum do osobnej metody — na niektórych arkuszach jest to wymagane:

```python
def znajdz_indeks_max(tablica, od_indeksu):
    """Znajduje indeks elementu maksymalnego od podanego indeksu do końca."""
    indeks_max = od_indeksu
    for i in range(od_indeksu + 1, len(tablica)):
        if tablica[i] > tablica[indeks_max]:
            indeks_max = i
    return indeks_max

def sortowanie_przez_wybieranie_malejaco(tablica):
    for i in range(len(tablica) - 1):
        indeks_max = znajdz_indeks_max(tablica, i)
        tablica[i], tablica[indeks_max] = tablica[indeks_max], tablica[i]
```

### 15.2. Sortowanie bąbelkowe (Bubble Sort)

**Idea algorytmu:** Porównujemy sąsiednie elementy i zamieniamy je, jeśli są w złej kolejności. Powtarzamy przejścia aż tablica będzie posortowana. Największy element „bąbelkuje" na koniec w każdym przejściu.

**Złożoność czasowa:** O(n²), ale z optymalizacją (flaga) może zakończyć się wcześniej.

```python
def sortowanie_babelkowe(tablica):
    n = len(tablica)
    for i in range(n - 1):
        for j in range(n - 1 - i):  # -i bo koniec jest już posortowany
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

# Wersja z optymalizacją — flaga „czy była zamiana"
def sortowanie_babelkowe_optymalne(tablica):
    n = len(tablica)
    for i in range(n - 1):
        zamieniono = False
        for j in range(n - 1 - i):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                zamieniono = True
        if not zamieniono:
            break  # Brak zamiany = tablica posortowana → koniec
```

**Przebieg krok po kroku** (dla tablicy `[5, 3, 8, 1]`):

| Przejście | Porównania | Zamiany | Tablica po przejściu |
|---|---|---|---|
| 1 (i=0) | 5>3✅ 5>8❌ 8>1✅ | 5↔3, 8↔1 | [3, 5, 1, **8**] |
| 2 (i=1) | 3>5❌ 5>1✅ | 5↔1 | [3, 1, **5**, 8] |
| 3 (i=2) | 3>1✅ | 3↔1 | [**1**, **3**, 5, 8] |

Wynik: `[1, 3, 5, 8]` ✅

### 15.3. Wyszukiwanie liniowe

**Idea:** Przeglądamy tablicę element po elemencie, szukając wartości. Zwracamy indeks pierwszego trafienia lub -1 gdy brak.

```python
def wyszukaj_liniowo(tablica, szukana):
    """Zwraca indeks pierwszego wystąpienia lub -1 gdy nie znaleziono."""
    for i in range(len(tablica)):
        if tablica[i] == szukana:
            return i
    return -1

# Wersja z enumerate
def wyszukaj_liniowo_v2(tablica, szukana):
    for i, element in enumerate(tablica):
        if element == szukana:
            return i
    return -1
```

### 15.4. Wyszukiwanie z wartownikiem (Sentinel Search)

**Idea:** Optymalizacja wyszukiwania liniowego — dodajemy szukany element na koniec tablicy (wartownik). Dzięki temu nie musimy w pętli sprawdzać, czy nie wyszliśmy poza granice tablicy. Po zakończeniu sprawdzamy, czy znaleźliśmy prawdziwy element czy wartownika.

```python
def wyszukaj_z_wartownikiem(tablica, szukana):
    n = len(tablica)
    tablica.append(szukana)  # Dodajemy wartownika na końcu

    i = 0
    while tablica[i] != szukana:  # Na pewno się zatrzyma — wartownik gwarantuje
        i += 1

    tablica.pop()  # Usuwamy wartownika — przywracamy oryginalną tablicę

    if i < n:
        return i     # Element znaleziony PRZED wartownikiem
    else:
        return -1    # Trafiliśmy na wartownika → elementu nie ma
```

### 15.5. Algorytm Euklidesa (NWD — Największy Wspólny Dzielnik)

**Idea:** Wielokrotnie zastępujemy większą liczbę resztą z dzielenia przez mniejszą, aż reszta wyniesie 0. Ostatnia niezerowa wartość to NWD.

Przykład: NWD(48, 18) → 48%18=12 → 18%12=6 → 12%6=**0** → NWD = **6**

```python
# Wersja iteracyjna
def nwd(a, b):
    while b != 0:
        a, b = b, a % b  # Jednoczesne przypisanie — idiom Pythona
    return a

# Wersja rekurencyjna
def nwd_rekurencyjnie(a, b):
    if b == 0:
        return a
    return nwd_rekurencyjnie(b, a % b)

# Testy
print(nwd(48, 18))    # 6
print(nwd(100, 75))   # 25
print(nwd(17, 5))     # 1 (liczby względnie pierwsze)
```

### 15.6. Sito Eratostenesa

**Idea:** Algorytm do znajdowania wszystkich liczb pierwszych w zakresie 2..n. Tworzymy tablicę logiczną, gdzie `True` oznacza „jest liczbą pierwszą". Następnie wykreślamy (ustawiamy `False`) wielokrotności każdej znalezionej liczby pierwszej. Wystarczy sprawdzać do √n.

```python
def sito_eratostenesa(n):
    """Zwraca listę liczb pierwszych z zakresu 2..n."""
    # Tablica logiczna — indeksy od 0 do n
    jest_pierwsza = [True] * (n + 1)
    jest_pierwsza[0] = False  # 0 nie jest liczbą pierwszą
    jest_pierwsza[1] = False  # 1 nie jest liczbą pierwszą

    i = 2
    while i * i <= n:           # Sprawdzamy do √n
        if jest_pierwsza[i]:
            # Wykreślamy wielokrotności: 2i, 3i, 4i, ...
            for j in range(i * 2, n + 1, i):
                jest_pierwsza[j] = False
        i += 1

    # Zbieramy liczby pierwsze (indeksy z wartością True)
    pierwsze = [i for i in range(2, n + 1) if jest_pierwsza[i]]
    return pierwsze

wynik = sito_eratostenesa(100)
print(wynik)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
#  53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(f"Znaleziono {len(wynik)} liczb pierwszych do 100")
```

### 15.7. Szyfr Cezara

**Idea:** Szyfr polega na przesunięciu każdej litery o stałą liczbę pozycji (klucz) w alfabecie. Po `z` wracamy do `a` (zawijanie). Klucz może być dodatni (przesunięcie w prawo), ujemny (w lewo), a nawet większy niż 26 — modulo 26 zapewnia poprawne zawijanie.

```python
def szyfruj_cezar(tekst_jawny, klucz):
    """
    Szyfruje tekst szyfrem Cezara.
    Obsługuje: małe litery a-z i spacje.
    Klucz: dowolna liczba całkowita.
    """
    wynik = ""
    for znak in tekst_jawny:
        if 'a' <= znak <= 'z':
            # 1. Numer litery w alfabecie (a=0, b=1, ..., z=25)
            numer = ord(znak) - ord('a')
            # 2. Przesunięcie z zawijaniem (modulo 26)
            nowy_numer = (numer + klucz) % 26
            # 3. Konwersja z powrotem na literę
            wynik += chr(nowy_numer + ord('a'))
        else:
            # Znaki spoza a-z (spacja, interpunkcja) — bez zmian
            wynik += znak
    return wynik

# Testowanie różnych kluczy
print(szyfruj_cezar("abc", 3))       # "def"   — klucz dodatni
print(szyfruj_cezar("xyz", 3))       # "abc"   — zawijanie
print(szyfruj_cezar("def", -3))      # "abc"   — klucz ujemny (odszyfrowanie)
print(szyfruj_cezar("abc", 29))      # "def"   — klucz > 26 (29 % 26 = 3)
print(szyfruj_cezar("ab cd", 2))     # "cd ef" — spacja bez zmian
print(szyfruj_cezar("abc", 0))       # "abc"   — klucz 0 = bez zmian
```

### 15.8. Walidacja danych z wagami

Wiele systemów walidacji (np. numery PESEL, kart kredytowych, NIP) opiera się na sumie kontrolnej liczonej za pomocą wag:

```python
def sprawdz_plec(pesel):
    """Zwraca 'K' (kobieta) lub 'M' (mężczyzna) na podstawie PESEL."""
    przedostatnia = int(pesel[-2])  # Przedostatnia cyfra
    if przedostatnia % 2 == 0:
        return 'K'
    else:
        return 'M'

def sprawdz_sume_kontrolna(pesel, wagi):
    """Sprawdza poprawność sumy kontrolnej."""
    S = 0
    for i in range(len(wagi)):
        S += int(pesel[i]) * wagi[i]
    M = S % 10
    R = 0 if M == 0 else 10 - M
    return R == int(pesel[-1])  # Porównanie z ostatnią cyfrą

# Wagi dla PESEL
wagi_pesel = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
```

### 15.9. Usuwanie sąsiednich duplikatów

Algorytm przetwarzania tekstu — usuwanie powtarzających się znaków występujących bezpośrednio obok siebie:

```python
def usun_duplikaty_obok(tekst):
    """Usuwa powtarzające się znaki obok siebie."""
    if not tekst:     # Obsługa pustego napisu
        return ""

    wynik = tekst[0]  # Pierwszy znak zawsze zostaje
    for i in range(1, len(tekst)):
        if tekst[i] != tekst[i - 1]:  # Różny od poprzedniego?
            wynik += tekst[i]
    return wynik

print(usun_duplikaty_obok("aabbbcc"))       # "abc"
print(usun_duplikaty_obok("Abba;;;to"))     # "Aba;to"
print(usun_duplikaty_obok(""))              # "" (pusty → pusty)
```

### 15.10. Zliczanie wystąpień wartości w danych

```python
def zlicz_wystapienia(dane, zakres_od, zakres_do):
    """Zlicza ile razy każda wartość z zakresu występuje w danych."""
    wystapienia = {}
    for wartosc in range(zakres_od, zakres_do + 1):
        wystapienia[wartosc] = 0

    for element in dane:
        if element in wystapienia:
            wystapienia[element] += 1

    return wystapienia

# Wyświetlanie
def wyswietl_statystyki(wystapienia):
    for wartosc, liczba in sorted(wystapienia.items()):
        if liczba > 0:
            print(f"Wartość {wartosc:>3}: {'█' * liczba} ({liczba})")
```

### 15.11. Obliczanie średniej arytmetycznej

Średnia arytmetyczna to suma elementów podzielona przez ich liczbę. Choć Python oferuje wbudowane `sum()` i `len()`, warto też wiedzieć, jak zaimplementować to ręcznie:

```python
# Sposób 1: Wbudowane funkcje (najkrótszy)
def srednia_wbudowana(tablica):
    if not tablica:  # Ochrona przed dzieleniem przez zero
        return 0
    return sum(tablica) / len(tablica)

# Sposób 2: Ręczna implementacja
def srednia_reczna(tablica):
    if not tablica:
        return 0
    suma = 0
    for element in tablica:
        suma += element
    return suma / len(tablica)

dane = [10, 20, 30, 40, 50]
print(f"Średnia: {srednia_wbudowana(dane):.2f}")  # Średnia: 30.00
```

### 15.12. Wyodrębnianie elementów spełniających warunek

Częsty wzorzec — z tablicy wybrać tylko elementy spełniające konkretny warunek (np. nieparzyste, większe od progu, itd.):

```python
def wyswietl_nieparzyste(tablica):
    """Wyświetla nieparzyste elementy i zwraca ich liczbę."""
    licznik = 0
    for element in tablica:
        if element % 2 != 0:
            print(element, end=" ")
            licznik += 1
    print()  # Nowa linia
    return licznik

def filtruj_w_zakresie(tablica, minimum, maksimum):
    """Zwraca nową listę z elementami w podanym zakresie."""
    wynik = []
    for element in tablica:
        if minimum <= element <= maksimum:
            wynik.append(element)
    return wynik

# Lub z list comprehension:
def filtruj_v2(tablica, minimum, maksimum):
    return [x for x in tablica if minimum <= x <= maksimum]

dane = [3, 12, 7, 25, 1, 18, 9, 42]
print(filtruj_w_zakresie(dane, 5, 20))  # [12, 7, 18, 9]
```

### 15.13. Sprawdzanie czy liczba jest pierwsza

Liczba pierwsza to liczba naturalna większa od 1, która dzieli się tylko przez 1 i przez siebie. Jest to fundamentalne pojęcie w algorytmice:

```python
import math

def jest_pierwsza(n):
    """Sprawdza czy n jest liczbą pierwszą."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # Parzyste > 2 nie są pierwsze

    # Sprawdzamy dzielniki nieparzyste do √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Testy
print(jest_pierwsza(2))    # True
print(jest_pierwsza(17))   # True
print(jest_pierwsza(4))    # False
print(jest_pierwsza(1))    # False
print(jest_pierwsza(97))   # True

# Wylistowanie wszystkich liczb pierwszych do 50
liczby_pierwsze = [n for n in range(2, 51) if jest_pierwsza(n)]
print(liczby_pierwsze)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

Dlaczego sprawdzamy tylko do √n? Jeśli n ma dzielnik d > √n, to n/d < √n, więc mniejszy dzielnik znaleźlibyśmy wcześniej.

### 15.14. Rekurencja

Rekurencja to technika, w której **funkcja wywołuje samą siebie**. Każde wywołanie rekurencyjne rozwiązuje mniejszy podproblem, aż do osiągnięcia **przypadku bazowego** (warunek stopu), który kończy łańcuch wywołań.

Rekurencja opiera się na dwóch elementach:
1. **Przypadek bazowy** — warunek kończący rekurencję (bez niego funkcja będzie się wywoływać w nieskończoność)
2. **Przypadek rekurencyjny** — wywołanie funkcji z mniejszym/prostszym argumentem

**Silnia (n!) — klasyczny przykład rekurencji:**

Silnia to iloczyn wszystkich liczb naturalnych od 1 do n: `5! = 5 * 4 * 3 * 2 * 1 = 120`

```python
def silnia(n):
    # Przypadek bazowy
    if n <= 1:
        return 1
    # Przypadek rekurencyjny
    return n * silnia(n - 1)

print(silnia(5))   # 120
print(silnia(0))   # 1
print(silnia(10))  # 3628800
```

**Przebieg wywołań dla `silnia(4)`:**

```
silnia(4)
  -> 4 * silnia(3)
    -> 3 * silnia(2)
      -> 2 * silnia(1)
        -> 1              <- przypadek bazowy
      <- 2 * 1 = 2
    <- 3 * 2 = 6
  <- 4 * 6 = 24          <- wynik końcowy
```

**Ciąg Fibonacciego — kolejny klasyczny przykład:**

Każda liczba w ciągu to suma dwóch poprzednich: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

```python
def fibonacci(n):
    """Zwraca n-tą liczbę ciągu Fibonacciego."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Wyświetlenie pierwszych 10 elementów
for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

**NWD — wersja rekurencyjna (przypomnienie):**

```python
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

print(nwd(48, 18))  # 6
```

**Rekurencja vs iteracja — porównanie:**

| Cecha | Rekurencja | Iteracja (pętla) |
|---|---|---|
| Czytelność | Często prostsza | Czasem mniej intuicyjna |
| Wydajność | Narzut wywołań | Szybsza |
| Pamięć | Stos wywołań | Mniejsze zużycie |
| Limit głębokości | ~1000 (Python) | Brak limitu |
| Kiedy stosować | Struktury drzewiaste, podział problemu | Proste iteracje, duże dane |

**Ważna uwaga:** Python ma domyślny limit **996-1000 wywołań rekurencyjnych**. Przy przekroczeniu tego limitu pojawi się `RecursionError`. Dla algorytmów z dużymi danymi lepiej użyć wersji iteracyjnej.

```python
import sys
print(sys.getrecursionlimit())  # 1000 (domyślnie)
```

### 15.15. Wyszukiwanie binarne (Binary Search)

**Idea:** Wyszukiwanie binarne działa tylko na **posortowanych** tablicach. Zamiast sprawdzać każdy element po kolei (jak wyszukiwanie liniowe), dzieli tablicę na pół w każdym kroku. Porównuje szukany element ze środkowym i decyduje, w której połowie kontynuować.

**Złożoność:** O(log n) — niesamowicie szybkie. Dla tablicy 1 000 000 elementów potrzeba maksymalnie ~20 porównań.

```python
def wyszukiwanie_binarne(tablica, szukana):
    """
    Szuka elementu w POSORTOWANEJ tablicy.
    Zwraca indeks lub -1 gdy nie znaleziono.
    """
    lewy = 0
    prawy = len(tablica) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2    # Indeks środka

        if tablica[srodek] == szukana:
            return srodek                 # Znaleziono!
        elif tablica[srodek] < szukana:
            lewy = srodek + 1             # Szukamy w prawej połowie
        else:
            prawy = srodek - 1            # Szukamy w lewej połowie

    return -1  # Nie znaleziono
```

**Przebieg krok po kroku** (szukamy `23` w tablicy `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`):

| Krok | Lewy | Prawy | Środek | Wartość | Decyzja |
|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 16 | 23 > 16 -> szukaj prawo |
| 2 | 5 | 9 | 7 | 56 | 23 < 56 -> szukaj lewo |
| 3 | 5 | 6 | 5 | **23** | Znaleziono! Indeks = 5 |

```python
# Testowanie
tablica = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(wyszukiwanie_binarne(tablica, 23))   # 5
print(wyszukiwanie_binarne(tablica, 2))    # 0
print(wyszukiwanie_binarne(tablica, 91))   # 9
print(wyszukiwanie_binarne(tablica, 50))   # -1 (nie ma)
```

**Wersja rekurencyjna:**

```python
def wyszukiwanie_binarne_rek(tablica, szukana, lewy=0, prawy=None):
    if prawy is None:
        prawy = len(tablica) - 1

    if lewy > prawy:
        return -1

    srodek = (lewy + prawy) // 2

    if tablica[srodek] == szukana:
        return srodek
    elif tablica[srodek] < szukana:
        return wyszukiwanie_binarne_rek(tablica, szukana, srodek + 1, prawy)
    else:
        return wyszukiwanie_binarne_rek(tablica, szukana, lewy, srodek - 1)
```

**Porównanie wyszukiwań:**

| Algorytm | Złożoność | Wymaga sortowania | Maks. porównań (n=1000) |
|---|---|---|---|
| Liniowe | O(n) | Nie | 1000 |
| Z wartownikiem | O(n) | Nie | 1000 |
| Binarne | O(log n) | Tak | 10 |

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
| Na stanowisku | ✅ Zawsze dostępny | ✅ Jeśli zainstalowany |

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