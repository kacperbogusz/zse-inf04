# Dokumentacja: React

## Spis treści

- [1. Jak korzystać z dokumentacji](#1-jak-korzystac-z-dokumentacji)
  - [1.1. Cel dokumentu](#11-cel-dokumentu)
  - [1.2. Mapa tematów](#12-mapa-tematow)
  - [1.3. Minimalny zestaw na małe aplikacje](#13-minimalny-zestaw-na-male-aplikacje)
- [2. React, SPA i środowisko pracy](#2-react-spa-i-srodowisko-pracy)
  - [2.1. Czym jest React](#21-czym-jest-react)
  - [2.2. Czym jest Single Page Application](#22-czym-jest-single-page-application)
  - [2.3. Create React App dzisiaj](#23-create-react-app-dzisiaj)
  - [2.4. Node.js, npm i npx](#24-nodejs-npm-i-npx)
- [3. Instalacja projektu w Create React App](#3-instalacja-projektu-w-create-react-app)
  - [3.1. Tworzenie aplikacji](#31-tworzenie-aplikacji)
  - [3.2. Uruchamianie](#32-uruchamianie)
  - [3.3. Struktura katalogów](#33-struktura-katalogow)
  - [3.4. Skrypty npm](#34-skrypty-npm)
  - [3.5. Czyszczenie projektu startowego](#35-czyszczenie-projektu-startowego)
- [4. Podstawy JavaScript potrzebne w React](#4-podstawy-javascript-potrzebne-w-react)
  - [4.1. Zmienne](#41-zmienne)
  - [4.2. Typy danych](#42-typy-danych)
  - [4.3. Operatory](#43-operatory)
  - [4.4. Warunki](#44-warunki)
  - [4.5. Funkcje](#45-funkcje)
  - [4.6. Tablice](#46-tablice)
  - [4.7. Obiekty](#47-obiekty)
  - [4.8. Destrukturyzacja](#48-destrukturyzacja)
  - [4.9. Import i export](#49-import-i-export)
- [5. JSX](#5-jsx)
  - [5.1. JSX jako HTML w JavaScript](#51-jsx-jako-html-w-javascript)
  - [5.2. Atrybuty](#52-atrybuty)
  - [5.3. Wstawianie wartości](#53-wstawianie-wartosci)
  - [5.4. Zasady jednego elementu](#54-zasady-jednego-elementu)
  - [5.5. Fragmenty](#55-fragmenty)
- [6. Komponenty](#6-komponenty)
  - [6.1. Komponent funkcyjny](#61-komponent-funkcyjny)
  - [6.2. Komponent statyczny](#62-komponent-statyczny)
  - [6.3. Kompozycja](#63-kompozycja)
  - [6.4. Podział plików](#64-podzial-plikow)
  - [6.5. Props](#65-props)
- [7. Stylowanie bez Bootstrapa](#7-stylowanie-bez-bootstrapa)
  - [7.1. CSS w CRA](#71-css-w-cra)
  - [7.2. className](#72-classname)
  - [7.3. Style inline](#73-style-inline)
  - [7.4. Dynamiczne style](#74-dynamiczne-style)
  - [7.5. Organizacja CSS](#75-organizacja-css)
- [8. Zdarzenia](#8-zdarzenia)
  - [8.1. onClick](#81-onclick)
  - [8.2. onChange](#82-onchange)
  - [8.3. onSubmit](#83-onsubmit)
  - [8.4. onBlur](#84-onblur)
  - [8.5. Przekazywanie argumentów](#85-przekazywanie-argumentow)
- [9. Stan komponentu useState](#9-stan-komponentu-usestate)
  - [9.1. Czym jest stan](#91-czym-jest-stan)
  - [9.2. Aktualizacja licznika](#92-aktualizacja-licznika)
  - [9.3. Stan tekstowy](#93-stan-tekstowy)
  - [9.4. Stan boolean](#94-stan-boolean)
  - [9.5. Poprzedni stan](#95-poprzedni-stan)
  - [9.6. Reset](#96-reset)
- [10. Formularze kontrolowane](#10-formularze-kontrolowane)
  - [10.1. input text](#101-input-text)
  - [10.2. input number](#102-input-number)
  - [10.3. password](#103-password)
  - [10.4. select](#104-select)
  - [10.5. textarea](#105-textarea)
  - [10.6. checkbox](#106-checkbox)
  - [10.7. radio](#107-radio)
  - [10.8. range](#108-range)
  - [10.9. Walidacja](#109-walidacja)
- [11. Tablice i renderowanie list](#11-tablice-i-renderowanie-list)
  - [11.1. map](#111-map)
  - [11.2. key](#112-key)
  - [11.3. Lista numerowana](#113-lista-numerowana)
  - [11.4. Dodawanie elementu](#114-dodawanie-elementu)
  - [11.5. Usuwanie](#115-usuwanie)
  - [11.6. Aktualizacja jednego elementu](#116-aktualizacja-jednego-elementu)
- [12. Obiekty i listy obiektów](#12-obiekty-i-listy-obiektow)
  - [12.1. Model danych](#121-model-danych)
  - [12.2. Kopiowanie obiektu](#122-kopiowanie-obiektu)
  - [12.3. Kopiowanie tablicy](#123-kopiowanie-tablicy)
  - [12.4. Formularz jako obiekt](#124-formularz-jako-obiekt)
  - [12.5. Dane z pliku przepisane do kodu](#125-dane-z-pliku-przepisane-do-kodu)
- [13. Renderowanie warunkowe](#13-renderowanie-warunkowe)
  - [13.1. if przed return](#131-if-przed-return)
  - [13.2. operator trójargumentowy](#132-operator-trojargumentowy)
  - [13.3. &&](#133-)
  - [13.4. komunikaty błędów](#134-komunikaty-bledow)
  - [13.5. puste listy](#135-puste-listy)
- [14. Bootstrap w React](#14-bootstrap-w-react)
  - [14.1. Instalacja](#141-instalacja)
  - [14.2. Import CSS](#142-import-css)
  - [14.3. Kontenery](#143-kontenery)
  - [14.4. Formularze](#144-formularze)
  - [14.5. Przyciski](#145-przyciski)
  - [14.6. Grid](#146-grid)
  - [14.7. Karty](#147-karty)
  - [14.8. Switche](#148-switche)
  - [14.9. Alerty](#149-alerty)
  - [14.10. Tabele](#1410-tabele)
- [15. Obrazy i zasoby](#15-obrazy-i-zasoby)
  - [15.1. public](#151-public)
  - [15.2. src i import](#152-src-i-import)
  - [15.3. Obraz zależny od stanu](#153-obraz-zalezny-od-stanu)
  - [15.4. Obrazy w kolekcjach](#154-obrazy-w-kolekcjach)
  - [15.5. alt](#155-alt)
  - [15.6. Błędy ścieżek](#156-bledy-sciezek)
- [16. Wzorce formularzy w małych aplikacjach](#16-wzorce-formularzy-w-malych-aplikacjach)
  - [16.1. Rejestracja](#161-rejestracja)
  - [16.2. Zapisy na kurs](#162-zapisy-na-kurs)
  - [16.3. Formularz filmu](#163-formularz-filmu)
  - [16.4. Formularz z podsumowaniem](#164-formularz-z-podsumowaniem)
  - [16.5. Kod pocztowy](#165-kod-pocztowy)
  - [16.6. Zakres liczby](#166-zakres-liczby)
- [17. Wzorce aplikacji listowych i widoków kart](#17-wzorce-aplikacji-listowych-i-widokow-kart)
  - [17.1. Lista notatek](#171-lista-notatek)
  - [17.2. Widok kart z kategoriami](#172-widok-kart-z-kategoriami)
  - [17.3. Licznik pobrań](#173-licznik-pobran)
  - [17.4. Filtrowanie checkboxami](#174-filtrowanie-checkboxami)
  - [17.5. Paginacja](#175-paginacja)
- [18. Wzorce suwaków, kolorów i dynamicznego UI](#18-wzorce-suwakow-kolorow-i-dynamicznego-ui)
  - [18.1. Suwak rozmiaru](#181-suwak-rozmiaru)
  - [18.2. RGB](#182-rgb)
  - [18.3. Opacity](#183-opacity)
  - [18.4. Dynamiczna klasa](#184-dynamiczna-klasa)
  - [18.5. Podgląd na żywo](#185-podglad-na-zywo)
- [19. Logika aplikacji poza JSX](#19-logika-aplikacji-poza-jsx)
  - [19.1. Funkcje pomocnicze](#191-funkcje-pomocnicze)
  - [19.2. Moduły](#192-moduly)
  - [19.3. Klasy](#193-klasy)
  - [19.4. Testowanie logiki ręcznie](#194-testowanie-logiki-recznie)
  - [19.5. Oddzielenie UI od obliczeń](#195-oddzielenie-ui-od-obliczen)
- [20. useEffect i efekty uboczne](#20-useeffect-i-efekty-uboczne)
  - [20.1. Po co jest useEffect](#201-po-co-jest-useeffect)
  - [20.2. Start aplikacji](#202-start-aplikacji)
  - [20.3. localStorage](#203-localstorage)
  - [20.4. fetch](#204-fetch)
  - [20.5. Typowe pułapki](#205-typowe-pulapki)
- [21. Dane lokalne, JSON i pliki tekstowe](#21-dane-lokalne-json-i-pliki-tekstowe)
  - [21.1. Tablice w kodzie](#211-tablice-w-kodzie)
  - [21.2. import JSON](#212-import-json)
  - [21.3. fetch z public](#213-fetch-z-public)
  - [21.4. Parsowanie tekstu](#214-parsowanie-tekstu)
  - [21.5. Kiedy nie komplikować](#215-kiedy-nie-komplikowac)
- [22. Proste algorytmy w React](#22-proste-algorytmy-w-react)
  - [22.1. Losowanie](#221-losowanie)
  - [22.2. Generator hasła](#222-generator-hasla)
  - [22.3. Szyfr Cezara](#223-szyfr-cezara)
  - [22.4. Kości](#224-kosci)
  - [22.5. Sumowanie i zliczanie](#225-sumowanie-i-zliczanie)
- [23. Projekt przykładowy: kursy](#23-projekt-przykladowy-kursy)
  - [23.1. Cel](#231-cel)
  - [23.2. Kod](#232-kod)
  - [23.3. Omówienie](#233-omowienie)
  - [23.4. Rozszerzenia](#234-rozszerzenia)
- [24. Projekt przykładowy: widok kart](#24-projekt-przykladowy-widok-kart)
  - [24.1. Cel](#241-cel)
  - [24.2. Kod](#242-kod)
  - [24.3. Omówienie](#243-omowienie)
  - [24.4. Uwagi do implementacji](#244-uwagi-do-implementacji)
- [25. Projekt przykładowy: RGB](#25-projekt-przykladowy-rgb)
  - [25.1. Cel](#251-cel)
  - [25.2. Kod](#252-kod)
  - [25.3. Omówienie](#253-omowienie)
  - [25.4. Rozszerzenia](#254-rozszerzenia)
- [26. Organizacja projektu](#26-organizacja-projektu)
  - [26.1. Nazewnictwo](#261-nazewnictwo)
  - [26.2. Folder components](#262-folder-components)
  - [26.3. Folder data](#263-folder-data)
  - [26.4. Folder utils](#264-folder-utils)
  - [26.5. Kiedy dzielić komponent](#265-kiedy-dzielic-komponent)
- [27. Debugowanie](#27-debugowanie)
  - [27.1. Konsola](#271-konsola)
  - [27.2. React DevTools](#272-react-devtools)
  - [27.3. Błędy składni](#273-bledy-skladni)
  - [27.4. Błędy stanu](#274-bledy-stanu)
  - [27.5. Błędy formularzy](#275-bledy-formularzy)
- [28. Testowanie i sprawdzanie działania](#28-testowanie-i-sprawdzanie-dzialania)
  - [28.1. Test ręczny](#281-test-reczny)
  - [28.2. Scenariusze](#282-scenariusze)
  - [28.3. npm test](#283-npm-test)
  - [28.4. Checklisty](#284-checklisty)
- [29. Build i publikacja projektu](#29-build-i-publikacja-projektu)
  - [29.1. npm run build](#291-npm-run-build)
  - [29.2. Co zawiera projekt](#292-co-zawiera-projekt)
  - [29.3. Zrzuty ekranu](#293-zrzuty-ekranu)
  - [29.4. Typowe problemy](#294-typowe-problemy)
- [30. Co warto jeszcze dodać do nauki Reacta](#30-co-warto-jeszcze-dodac-do-nauki-reacta)
  - [30.1. Lista brakujących tematów](#301-lista-brakujacych-tematow)
  - [30.2. Przydatność tematów w małych aplikacjach](#302-przydatnosc-tematow-w-malych-aplikacjach)
  - [30.3. Jak czytać przykłady kodu](#303-jak-czytac-przyklady-kodu)
- [31. Jak działa projekt React od wejścia do App.js](#31-jak-dziala-projekt-react-od-wejscia-do-appjs)
  - [31.1. public/index.html](#311-publicindexhtml)
  - [31.2. src/index.js](#312-srcindexjs)
  - [31.3. src/App.js](#313-srcappjs)
  - [31.4. StrictMode](#314-strictmode)
  - [31.5. Typowa kolejność pracy](#315-typowa-kolejnosc-pracy)
- [32. Renderowanie, stan i przepływ danych](#32-renderowanie-stan-i-przeplyw-danych)
  - [32.1. Render komponentu](#321-render-komponentu)
  - [32.2. Zmienna lokalna kontra stan](#322-zmienna-lokalna-kontra-stan)
  - [32.3. Dane płyną z góry na dół](#323-dane-plyna-z-gory-na-dol)
  - [32.4. Stan pochodny](#324-stan-pochodny)
- [33. JavaScript, którego naprawdę potrzebujesz w React](#33-javascript-ktorego-naprawde-potrzebujesz-w-react)
  - [33.1. Template stringi](#331-template-stringi)
  - [33.2. Truthy i falsy](#332-truthy-i-falsy)
  - [33.3. Konwersje liczb](#333-konwersje-liczb)
  - [33.4. Metody napisów](#334-metody-napisow)
  - [33.5. Bezpieczna praca na tablicach](#335-bezpieczna-praca-na-tablicach)
- [34. JSX dokładniej](#34-jsx-dokladniej)
  - [34.1. Co można wstawić w klamrach](#341-co-mozna-wstawic-w-klamrach)
  - [34.2. Komentarze w JSX](#342-komentarze-w-jsx)
  - [34.3. Atrybuty boolean](#343-atrybuty-boolean)
  - [34.4. Dynamiczny JSX z map i warunkami](#344-dynamiczny-jsx-z-map-i-warunkami)
- [35. Props, children i lifting state up](#35-props-children-i-lifting-state-up)
  - [35.1. Props jako parametry komponentu](#351-props-jako-parametry-komponentu)
  - [35.2. children](#352-children)
  - [35.3. Callback z dziecka do rodzica](#353-callback-z-dziecka-do-rodzica)
  - [35.4. Lifting state up](#354-lifting-state-up)
- [36. useState dokładniej](#36-usestate-dokladniej)
  - [36.1. Aktualizacja nie jest natychmiastowym przypisaniem](#361-aktualizacja-nie-jest-natychmiastowym-przypisaniem)
  - [36.2. Funkcyjna aktualizacja stanu](#362-funkcyjna-aktualizacja-stanu)
  - [36.3. Lazy initial state](#363-lazy-initial-state)
  - [36.4. Reset większego formularza](#364-reset-wiekszego-formularza)
- [37. Formularze w kilku wariantach](#37-formularze-w-kilku-wariantach)
  - [37.1. Jeden stan na każde pole](#371-jeden-stan-na-kazde-pole)
  - [37.2. Jeden obiekt formularza](#372-jeden-obiekt-formularza)
  - [37.3. Błędy per pole](#373-bledy-per-pole)
  - [37.4. Checkboxy jako tablica](#374-checkboxy-jako-tablica)
  - [37.5. useRef i formularz niekontrolowany](#375-useref-i-formularz-niekontrolowany)
  - [37.6. FormData](#376-formdata)
- [38. useEffect, dane lokalne i efekty uboczne](#38-useeffect-dane-lokalne-i-efekty-uboczne)
  - [38.1. Tablica zależności](#381-tablica-zaleznosci)
  - [38.2. Cleanup](#382-cleanup)
  - [38.3. Fetch z loading i error](#383-fetch-z-loading-i-error)
  - [38.4. localStorage jako praktyczny wzorzec](#384-localstorage-jako-praktyczny-wzorzec)
- [39. Dobre praktyki UI](#39-dobre-praktyki-ui)
  - [39.1. button type](#391-button-type)
  - [39.2. Dostępność formularzy](#392-dostepnosc-formularzy)
  - [39.3. Semantyczny układ strony](#393-semantyczny-uklad-strony)
  - [39.4. Wzorce przydatne w małych aplikacjach](#394-wzorce-przydatne-w-malych-aplikacjach)
- [40. Rozbudowane projekty wzorcowe](#40-rozbudowane-projekty-wzorcowe)
  - [40.1. Generator hasła z formularzem](#401-generator-hasla-z-formularzem)
  - [40.2. Widok kart z kategoriami, wyszukiwaniem i sortowaniem](#402-widok-kart-z-kategoriami-wyszukiwaniem-i-sortowaniem)
  - [40.3. Kości z blokowaniem](#403-kosci-z-blokowaniem)
- [41. Kompletny Projekt: Lista Zadań (Todo App) [Wieloplikowy]](#41-kompletny-projekt-lista-zadan-todo-app-wieloplikowy)
  - [41.1. Struktura plików](#411-struktura-plikow)
  - [41.2. App.js (Rodzic trzymający stan)](#412-appjs-rodzic-trzymajacy-stan)
  - [41.3. TaskForm.js (Komponent dodawania)](#413-taskformjs-komponent-dodawania)
  - [41.4. TaskList.js (Komponent listy)](#414-tasklistjs-komponent-listy)
  - [41.5. Podsumowanie przepływu danych](#415-podsumowanie-przeplywu-danych)
- [42. Najczęstsze pułapki i jak ich unikać](#42-najczestsze-pulapki-i-jak-ich-unikać)
  - [42.1. Brak `key` w pętli map()](#421-brak-key-w-petli-map)
  - [42.2. Mutowanie stanu zamiast tworzenia kopii](#422-mutowanie-stanu-zamiast-tworzenia-kopii)
  - [42.3. Próba odczytu stanu zaraz po jego ustawieniu](#423-proba-odczytu-stanu-zaraz-po-jego-ustawieniu)
  - [42.4. Brak `event.preventDefault()` w formularzu](#424-brak-eventpreventdefault-w-formularzu)


---

> **Jak korzystać z tego poradnika:** Dokument prowadzi od absolutnych podstaw do wzorców, które najczęściej pojawiają się w prostych aplikacjach front-endowych. Uczy mechanik Reacta przez neutralne przykłady: formularze, stan, listy, obrazy, suwaki, liczniki, walidację i Bootstrap.

> **Uwaga o Create React App:** Create React App jest obecnie narzędziem przestarzałym dla nowych projektów produkcyjnych, ale nadal bywa spotykane w starszych materiałach i starszych projektach. W tej dokumentacji używamy go świadomie, ponieważ pozwala szybko rozpocząć naukę podstaw Reacta. Dla nowych zawodowych projektów warto znać także Vite albo frameworki rekomendowane przez React.

---


## 1. Jak korzystać z dokumentacji


### 1.1. Cel dokumentu

React jest biblioteką JavaScript do budowania interfejsów użytkownika.
Najważniejsza myśl jest prosta: widok jest funkcją danych.
Jeżeli zmienią się dane w stanie komponentu, React ponownie wyliczy wygląd odpowiedniego fragmentu strony.
Dzięki temu nie trzeba ręcznie wyszukiwać elementów w DOM i ustawiać im tekstu przez `document.querySelector()`.
W prostych aplikacjach edukacyjnych React najczęściej służy do formularzy, widoków kart, liczników, list i przełączników.
Ten poradnik buduje wiedzę krok po kroku.
Najpierw uczysz się składni JavaScript i JSX.
Potem przechodzisz przez komponenty, zdarzenia i `useState`.
Dopiero później pojawiają się formularze, listy obiektów, filtrowanie i bardziej złożone wzorce.


### 1.2. Mapa tematów

| Obszar | Co trzeba umieć | Po co |
| --- | --- | --- |
| Środowisko | `node`, `npm`, `npx`, `npm start` | uruchomienie projektu |
| JSX | `className`, `{zmienna}`, fragmenty | pisanie widoku |
| Komponenty | funkcje zwracające JSX | dzielenie UI |
| Props | przekazywanie danych do komponentu | ponowne użycie |
| Stan | `useState` | reakcja na akcje użytkownika |
| Zdarzenia | `onClick`, `onChange`, `onSubmit` | obsługa interakcji |
| Formularze | kontrolowane pola | odczyt danych |
| Listy | `map`, `filter`, `key` | dynamiczne dane |
| Bootstrap | klasy CSS | szybki wygląd |
| Zasoby | obrazy z `public` i `src` | karty, miniatury i ikony |


### 1.3. Minimalny zestaw na małe aplikacje

- Utworzyć projekt przez `npx create-react-app nazwa-projektu`.
- Uruchomić projekt przez `npm start`.
- Wyczyścić `App.js` i zacząć od własnego komponentu.
- Napisać statyczny JSX z nagłówkami, etykietami, polami i przyciskami.
- Podpiąć Bootstrap przez `import 'bootstrap/dist/css/bootstrap.css';`.
- Zamienić `class` na `className` oraz `for` na `htmlFor`.
- Użyć `useState` do tekstu, liczby, booleanów i tablic.
- Obsłużyć `onChange` dla pól formularza.
- Obsłużyć `onSubmit` formularza i wykonać `event.preventDefault()`.
- Wyrenderować tablicę przez `map()`.
- Filtrować dane przez `filter()`.
- Aktualizować jeden element tablicy bez mutowania starej tablicy.
- Dodać obraz zależny od stanu.
- Zrobić walidację pustych pól, zakresu liczby i prostego formatu tekstu.
- Sprawdzić działanie w konsoli przeglądarki.


## 2. React, SPA i środowisko pracy


### 2.1. Czym jest React

React nie jest pełnym frameworkiem typu wszystko w jednym.
React jest biblioteką do budowania widoku.
Widok składa się z komponentów.
Komponent to funkcja JavaScript, która zwraca JSX.
JSX wygląda jak HTML, ale działa wewnątrz JavaScriptu.
React renderuje komponenty do prawdziwego DOM przeglądarki.
Kiedy zmienisz stan komponentu, React odświeża tylko potrzebne fragmenty interfejsu.
Dlatego w React nie myślisz: znajdź etykietę i zmień jej tekst.
Myślisz raczej: zmień wartość stanu, a widok sam pokaże nową wartość.


### 2.2. Czym jest Single Page Application

SPA, czyli Single Page Application, to aplikacja działająca na jednej stronie HTML.
Przeglądarka ładuje plik `index.html`, JavaScript i CSS.
Potem widok zmienia się bez pełnego przeładowania strony.
Proste aplikacje Reactowe zwykle są właśnie małymi SPA.
Często nie ma w nich backendu, bazy danych ani routingu.
Dane są zapisane w tablicy, obiekcie, pliku JSON albo w stanie komponentu.


### 2.3. Create React App dzisiaj

Create React App, często skracane do CRA, przez lata było standardowym sposobem startu nauki Reacta.
CRA tworzy gotowy projekt z Reactem, Babel, webpackiem, testami i skryptami npm.
Nie trzeba ręcznie konfigurować bundlera.
To jest wygodne w edukacji, bo można szybko przejść do pisania komponentów.
Oficjalny zespół Reacta ogłosił jednak wygaszanie CRA dla nowych aplikacji.
W praktyce oznacza to, że do nauki i starszych projektów CRA nadal jest zrozumiałe, ale w nowoczesnych projektach warto znać alternatywy.
Jeżeli pracujesz w starszym projekcie opartym o CRA, używaj CRA zgodnie z istniejącą strukturą.
Jeżeli tworzysz własny nowy projekt, rozważ Vite albo framework Reactowy.


### 2.4. Node.js, npm i npx

| Narzędzie | Znaczenie | Przykład |
| --- | --- | --- |
| Node.js | uruchamia JavaScript poza przeglądarką | `node -v` |
| npm | menedżer pakietów | `npm install bootstrap` |
| npx | uruchamia paczkę bez globalnej instalacji | `npx create-react-app app` |
| package.json | opis projektu i skrypty | `npm start` |
| node_modules | pobrane zależności | nie edytujemy ręcznie |

```bash
node -v
npm -v
npx --version
```


### 2.5. Model mentalny: Imperatywność vs Deklaratywność

Dla początkującego programisty przesiadka z czystego JavaScriptu na Reacta może być trudna z powodu zmiany sposobu myślenia.

- **Podejście Imperatywne (JavaScript/DOM):** Mówisz krok po kroku, *jak* coś zrobić. "Znajdź przycisk, dodaj do niego zdalzenie, znajdź akapit, zmień jego tekst na 'Cześć'". Musisz ręcznie pilnować każdego elementu na stronie.
- **Podejście Deklaratywne (React):** Mówisz, *co* chcesz osiągnąć (opisujesz stan końcowy). "Chcę, aby ten akapit zawsze wyświetlał to, co jest w zmiennej `imie`". React sam zajmie się aktualizacją DOM, gdy zmienna `imie` ulegnie zmianie.

To jak zamawianie pizzy: w podejściu imperatywnym musiałbyś wejść do kuchni i instruować kucharza, ile mąki i wody ma dodać. W podejściu deklaratywnym (React) po prostu składasz zamówienie: "Chcę margheritę". To restauracja (React) dba o to, byś ją otrzymał.


### 2.6. Co się dzieje "pod maską" (Virtual DOM)

Zrozumienie, jak React aktualizuje stronę, pomaga pisać lepszy kod:

1. **Komponenty** to Twoje "klocki" (funkcje zwracające widok).
2. Gdy zmienia się **stan** (`useState`), React tworzy w pamięci nową kopię widoku (tzw. **Virtual DOM**).
3. React porównuje tę kopię z tym, co aktualnie widzi użytkownik na ekranie.
4. React znajduje tylko te różnice (np. zmienił się tekst w jednym polu) i **tylko je** przesyła do prawdziwego DOM przeglądarki.

Dzięki temu aplikacje są szybkie, a Ty jako programista nie musisz martwić się o ręczne usuwanie czy dodawanie klas i elementów HTML.



## 3. Instalacja projektu w Create React App


### 3.1. Tworzenie aplikacji

Projekt tworzysz w folderze, w którym chcesz mieć katalog aplikacji.
Nazwa projektu powinna być małymi literami, bez spacji i polskich znaków.
Dobra nazwa to `moja-aplikacja`, `kursy-react` albo `kolekcja-zdjec`.
Polecenie `npx create-react-app` pobiera generator i tworzy kompletny projekt.

```bash
npx create-react-app moja-aplikacja
cd moja-aplikacja
npm start
```

Po uruchomieniu `npm start` przeglądarka powinna otworzyć adres `http://localhost:3000`.
Jeżeli port jest zajęty, terminal może zaproponować inny port.
W czasie pracy serwer deweloperski obserwuje pliki.
Po zapisaniu zmian strona odświeża się automatycznie.


### 3.2. Uruchamianie

| Polecenie | Kiedy używać | Efekt |
| --- | --- | --- |
| `npm start` | podczas pisania kodu | serwer developerski |
| `npm test` | przy testach | tryb obserwowania testów |
| `npm run build` | przed publikacją/wdrożeniem | folder `build` |
| `npm install nazwa` | gdy dodajesz bibliotekę | aktualizacja `package.json` |


### 3.3. Struktura katalogów

```text
moja-aplikacja/
  package.json
  node_modules/
  public/
    index.html
    favicon.ico
  src/
    App.js
    App.css
    index.js
    index.css
```

- `public/index.html` jest głównym plikiem HTML aplikacji.
- `src/index.js` montuje Reacta do elementu HTML.
- `src/App.js` zwykle zawiera główny komponent aplikacji.
- `src/App.css` może zawierać style głównego komponentu.
- `src/index.css` może zawierać style globalne.
- `package.json` zawiera zależności i skrypty.
- `node_modules` zawiera pobrane biblioteki i nie powinien być edytowany ręcznie.


### 3.4. Skrypty npm

Skrypty są zapisane w `package.json`.
Nie trzeba pamiętać pełnych poleceń bundlera.
Wystarczy używać krótkich komend npm.

```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

Polecenia `eject` prawie nigdy nie używaj w prostych projektach.
Eject wyciąga ukrytą konfigurację webpacka i komplikuje projekt.
Do prostych aplikacji z formularzem, widokiem kart i Bootstrapem nie jest potrzebny.


### 3.5. Czyszczenie projektu startowego

Po utworzeniu CRA warto usunąć startowe logo i przykładową zawartość.
Najczęściej pracujesz w `App.js`.
Na początku zostaw prosty komponent i sprawdź, czy aplikacja działa.

```jsx
import "./App.css";

function App() {
  return (
    <main className="container mt-4">
      <h1>Moja aplikacja React</h1>
      <p>Projekt działa poprawnie.</p>
    </main>
  );
}

export default App;
```


## 4. Podstawy JavaScript potrzebne w React


### 4.1. Zmienne

React używa JavaScriptu, więc podstawy języka są konieczne.
`const` oznacza stałą referencję.
`let` oznacza zmienną, której wartość można później przypisać ponownie.
`var` jest starszym sposobem deklarowania zmiennych i w nowym kodzie React raczej go unikamy.

```js
const nazwa = "React";
let licznik = 0;

licznik = licznik + 1;
```

| Słowo | Czy można przypisać ponownie | Typowe użycie |
| --- | --- | --- |
| `const` | nie | tablice, obiekty, funkcje, stałe teksty |
| `let` | tak | licznik w pętli, zmienna pomocnicza |
| `var` | tak | stary kod, niezalecane w nowych komponentach |


### 4.2. Typy danych

| Typ | Opis | Przykład |
| --- | --- | --- |
| string | tekst | `'Ala'`, `"React"` |
| number | liczba całkowita lub zmiennoprzecinkowa | `5`, `3.14` |
| boolean | prawda/fałsz | `true`, `false` |
| undefined | brak przypisanej wartości | `let x;` |
| null | celowy brak wartości | `selected = null` |
| array | tablica | `[1, 2, 3]` |
| object | obiekt | `{ id: 1, title: 'Film' }` |

```js
const kurs = "Programowanie w React";
const numer = 2;
const aktywny = true;
const kursy = ["HTML", "CSS", "React"];
const film = { tytul: "Matrix", rodzaj: "Sensacyjny" };
```


### 4.3. Operatory

| Operator | Znaczenie | Przykład |
| --- | --- | --- |
| `+` | dodawanie lub łączenie tekstu | `2 + 3`, `'A' + 'B'` |
| `-` | odejmowanie | `10 - 4` |
| `*` | mnożenie | `3 * 4` |
| `/` | dzielenie | `10 / 2` |
| `%` | reszta z dzielenia | `7 % 2` |
| `===` | równość bez konwersji typów | `x === 5` |
| `!==` | różność bez konwersji typów | `x !== 0` |
| `&&` | i | `a && b` |
| `||` | lub | `a || b` |
| `!` | negacja | `!aktywny` |


### 4.4. Warunki

```js
const email = "jan@example.com";

if (!email.includes("@")) {
  console.log("Nieprawidłowy email");
} else {
  console.log("Email poprawny");
}
```

W React warunki często decydują o komunikacie, klasie CSS albo tym, czy element ma być widoczny.
Do prostych komunikatów używa się też operatora trójargumentowego.

```jsx
<p>{czyPoprawne ? "Dane poprawne" : "Popraw formularz"}</p>
```


### 4.5. Funkcje

```js
function dodaj(a, b) {
  return a + b;
}

const pomnoz = (a, b) => {
  return a * b;
};

const podwoj = (x) => x * 2;
```

Komponent Reacta też jest funkcją.
Obsługa kliknięcia najczęściej jest funkcją zdefiniowaną wewnątrz komponentu.
Funkcje pomocnicze można wynieść poza komponent, jeśli nie potrzebują stanu.


### 4.6. Tablice

```js
const kursy = ["Programowanie w C#", "Angular", "React", "Bazy danych"];

console.log(kursy.length);
console.log(kursy[0]);

const kursyHtml = kursy.map((kurs) => kurs.toUpperCase());
const krotkie = kursy.filter((kurs) => kurs.length < 8);
```

| Metoda | Zwraca | Typowe użycie w React |
| --- | --- | --- |
| `map()` | nową tablicę | renderowanie listy elementów |
| `filter()` | nową przefiltrowaną tablicę | kategorie i wyszukiwarka |
| `find()` | pierwszy pasujący element | wyszukanie rekordu po id |
| `some()` | boolean | czy istnieje element |
| `reduce()` | jedną wartość | suma, zliczanie |


### 4.7. Obiekty

```js
const zdjecie = {
  id: 1,
  nazwa: "kwiat.jpg",
  kategoria: "kwiaty",
  pobrania: 0
};

console.log(zdjecie.nazwa);
console.log(zdjecie["kategoria"]);
```

Obiekty są podstawą modelowania danych w aplikacjach React.
Zdjęcie, kurs, film, notatka, urządzenie albo album mogą być obiektami.
W stanie często trzymasz tablicę obiektów.


### 4.8. Destrukturyzacja

```js
const film = { tytul: "Incepcja", rodzaj: "Sensacyjny" };
const { tytul, rodzaj } = film;

const kolory = [120, 80, 200];
const [r, g, b] = kolory;
```

Destrukturyzacja jest bardzo częsta w React.
`useState` zwraca tablicę dwóch elementów.
Pierwszy element to aktualna wartość.
Drugi element to funkcja do zmiany tej wartości.

```jsx
const [licznik, setLicznik] = useState(0);
```


### 4.9. Import i export

```js
// utils/math.js
export function suma(a, b) {
  return a + b;
}

// App.js
import { suma } from "./utils/math";
```

```jsx
// components/Header.js
function Header() {
  return <h1>Aplikacja</h1>;
}

export default Header;

// App.js
import Header from "./components/Header";
```


## 5. JSX


### 5.1. JSX jako HTML w JavaScript

JSX przypomina HTML, ale jest składnią JavaScriptu.
W JSX możesz pisać znaczniki, a w nawiasach klamrowych wstawiać wyrażenia JavaScript.
Każdy komponent musi zwrócić jeden główny element albo fragment.

```jsx
function Powitanie() {
  const imie = "Jan";

  return <h1>Witaj, {imie}</h1>;
}
```


### 5.2. Atrybuty

| HTML | JSX | Powód |
| --- | --- | --- |
| `class` | `className` | `class` jest słowem specjalnym w JS |
| `for` | `htmlFor` | `for` jest słowem specjalnym w JS |
| `onclick` | `onClick` | React używa camelCase |
| `tabindex` | `tabIndex` | camelCase |
| `readonly` | `readOnly` | camelCase |

```jsx
<label htmlFor="email" className="form-label">
  Email
</label>
<input id="email" className="form-control" />
```


### 5.3. Wstawianie wartości

Wstawianie wartości w JSX to jedna z najczęściej używanych czynności w React.
Jeżeli masz zmienną JavaScript i chcesz pokazać ją w widoku, wkładasz ją między nawiasy klamrowe `{}`.
Klamry oznaczają: „w tym miejscu wykonaj wyrażenie JavaScript i wstaw wynik do JSX”.
To może być zwykła zmienna, działanie matematyczne, wynik funkcji albo operator warunkowy.

```jsx
// Ten fragment może znajdować się wewnątrz komponentu, np. w src/App.js.
const tytul = "Lista kursów";
const liczba = 4;

return (
  <section>
    {/* Zmienna tekstowa trafia do nagłówka */}
    <h2>{tytul}</h2>

    {/* Zmienna liczbowa zostanie zamieniona na tekst w widoku */}
    <p>Liczba kursów: {liczba}</p>

    {/* W klamrach można wykonać proste działanie */}
    <p>Następny numer: {liczba + 1}</p>
  </section>
);
```

- W nawiasach `{}` można wstawić zmienną.
- W nawiasach `{}` można wstawić wyrażenie.
- W nawiasach `{}` można wywołać funkcję, jeśli nie zmienia ona stanu podczas renderu.
- Nie wstawiaj instrukcji `if` bezpośrednio w JSX.
- Do warunków w JSX używaj operatora trójargumentowego albo przygotuj zmienną przed `return`.

| Chcesz wstawić | Przykład | Uwagi |
| --- | --- | --- |
| tekst ze zmiennej | `{imie}` | najprostszy przypadek |
| liczbę | `{wiek}` | React sam pokaże ją jako tekst |
| działanie | `{cena * ilosc}` | dobre dla krótkich obliczeń |
| wynik funkcji | `{formatPrice(price)}` | funkcja nie powinna zmieniać stanu |
| warunek | `{active ? "Tak" : "Nie"}` | dobre dla krótkich komunikatów |

Jeżeli wyrażenie robi się długie, lepiej przygotować zmienną przed `return`.
JSX powinien pozostać czytelny.
Widok ma pokazywać strukturę interfejsu, a nie ukrywać w sobie całą logikę aplikacji.


### 5.4. Zasady jednego elementu

Komponent musi zwrócić jeden główny element.
Nie oznacza to, że widok może mieć tylko jeden nagłówek albo jeden akapit.
Oznacza to, że kilka sąsiednich elementów trzeba opakować we wspólnego rodzica.
Najczęściej jest to `div`, `main`, `section` albo fragment `<>...</>`.

```jsx
return (
  <div>
    <h1>Tytuł</h1>
    <p>Opis</p>
  </div>
);
```

Nie można zwrócić dwóch sąsiednich elementów bez wspólnego rodzica.
Jeśli nie chcesz dodawać prawdziwego elementu HTML, użyj fragmentu.

Przykład błędny:

```jsx
// Błąd: dwa elementy obok siebie bez wspólnego rodzica.
return (
  <h1>Tytuł</h1>
  <p>Opis</p>
);
```

Przykład poprawny z elementem semantycznym:

```jsx
return (
  <main>
    <h1>Tytuł</h1>
    <p>Opis</p>
  </main>
);
```

W praktyce wybieraj rodzica zgodnie ze znaczeniem.
Jeżeli to główna treść strony, użyj `main`.
Jeżeli to część większej strony, użyj `section`.
Jeżeli rodzic jest potrzebny tylko technicznie i nie chcesz dodawać elementu do HTML, użyj fragmentu.


### 5.5. Fragmenty

Fragment nie tworzy dodatkowego elementu w HTML.
Jest przydatny wtedy, gdy komponent musi zwrócić kilka elementów, ale nie chcesz dodawać zbędnego `div`.
To pomaga utrzymać czystszy HTML i nie psuje układów CSS, np. siatki Bootstrapa.

```jsx
return (
  <>
    <h1>Tytuł</h1>
    <p>Opis</p>
  </>
);
```

Fragment jest szczególnie wygodny w małych komponentach pomocniczych.
Na przykład komponent może zwracać etykietę i pole formularza, ale nie musi opakowywać ich w dodatkowy `div`, jeśli rodzic już kontroluje układ.


## 6. Komponenty


### 6.1. Komponent funkcyjny

Komponent funkcyjny to zwykła funkcja JavaScript, która zwraca JSX.
W React większość współczesnych komponentów pisze się właśnie jako funkcje.
Nazwa komponentu musi zaczynać się wielką literą, ponieważ React po tym rozpoznaje, że ma do czynienia z komponentem, a nie zwykłym znacznikiem HTML.

```jsx
// src/App.js

// Definicja funkcji, która jest komponentem. 
// MUSI zaczynać się wielką literą (App, nie app).
function App() {
  // Komponent zawsze zwraca (return) kawałek widoku napisanego w JSX.
  // JSX wygląda jak HTML, ale pozwala na wstawianie logiki JS.
  return (
    <div>
      <h1>Witaj w React!</h1>
      <p>To jest Twój pierwszy komponent.</p>
    </div>
  );
}

// Export default pozwala na użycie tego komponentu w innych plikach (np. index.js).
export default App;
```


Nazwa komponentu musi zaczynać się wielką literą.
Komponent może być używany jak własny znacznik HTML.
Komponent może zawierać zmienne, funkcje pomocnicze, stan i JSX.

| Element komponentu | Do czego służy |
| --- | --- |
| nazwa funkcji | nazwa komponentu używana w JSX, np. `<App />` |
| `return` | zwraca JSX, czyli opis widoku |
| `export default` | pozwala zaimportować komponent w innym pliku |
| wielka litera | odróżnia komponent od zwykłego znacznika HTML |

Najprostszy sposób nauki komponentów to tworzenie małych, samodzielnych fragmentów interfejsu.
Najpierw komponent statyczny, potem komponent z propsami, a dopiero później komponent ze stanem.


### 6.2. Komponent statyczny

Komponent statyczny zawsze pokazuje to samo.
Nie ma `useState`, nie ma zdarzeń i nie zależy od danych z zewnątrz.
To nie jest wada.
Takie komponenty są bardzo dobre do budowania stałych części strony: nagłówków, stopek, opisów, prostych paneli i sekcji informacyjnych.

```jsx
function Stopka() {
  return (
    <footer className="mt-5 text-muted">
      <p>Autor: Jan Kowalski</p>
    </footer>
  );
}
```

Komponent statyczny nie ma stanu i nie reaguje na zdarzenia.
Nadaje się do nagłówków, stopek, opisów, prostych sekcji i powtarzalnych bloków.
Od komponentu statycznego warto zaczynać naukę.

Jeżeli jakiś fragment JSX zaczyna się powtarzać, spróbuj najpierw zrobić z niego komponent statyczny.
Później możesz dodać propsy, żeby różnił się tekstem, kolorem albo zawartością.
To naturalna droga od prostego kodu do bardziej elastycznej struktury.


### 6.3. Kompozycja

Kompozycja oznacza budowanie większego komponentu z mniejszych komponentów.
Zamiast pisać cały interfejs w jednym ogromnym `return`, możesz wydzielić części takie jak `Header`, `CourseList`, `UserForm`, `PhotoCard`.
React zachęca właśnie do takiego myślenia: aplikacja to drzewo komponentów.

```jsx
// Mały komponent odpowiedzialny tylko za nagłówek.
function Header() {
  return <h1>Panel kursów</h1>;
}

// Główny komponent składa widok z mniejszych części.
function App() {
  return (
    <main className="container">
      {/* Używamy własnego komponentu tak jak znacznika HTML */}
      <Header />
      <p>Treść aplikacji.</p>
    </main>
  );
}
```

W tym przykładzie `App` jest rodzicem, a `Header` dzieckiem.
`App` decyduje, gdzie nagłówek zostanie umieszczony.
`Header` decyduje, jak nagłówek wygląda.
Dzięki temu każdy komponent ma prostą odpowiedzialność.

| Pytanie | Odpowiedź |
| --- | --- |
| Kiedy wydzielić komponent? | Gdy fragment JSX jest powtarzalny albo robi się zbyt duży. |
| Czy każdy element musi być komponentem? | Nie. Zbyt wiele małych komponentów może utrudnić czytanie. |
| Gdzie trzymać stan? | Zwykle w najbliższym wspólnym rodzicu komponentów, które go potrzebują. |
| Czy dziecko może być w tym samym pliku? | Tak, na początku to często najprostsze rozwiązanie. |

Jak możesz to zastosować:

```jsx
function App() {
  return (
    <main className="container">
      <PageTitle />
      <CourseList />
      <CourseForm />
    </main>
  );
}
```

Taki kod od razu mówi, z jakich części składa się strona.
Nie musisz czytać kilkudziesięciu linii JSX, żeby zauważyć strukturę.


### 6.4. Podział plików

Podział plików nie jest obowiązkowy od pierwszej minuty pracy.
Jest jednak bardzo pomocny, gdy aplikacja rośnie.
Zamiast trzymać wszystko w `App.js`, możesz wydzielić komponenty, dane i funkcje pomocnicze.

```text
src/
  components/
    Header.js
    CourseList.js
    CourseForm.js
  data/
    courses.js
  utils/
    validation.js
  App.js
```

Na początku możesz pisać wszystko w `App.js`.
Gdy plik robi się długi, wydziel komponenty.
W małej aplikacji z jednym komponentem nie komplikuj struktury bez potrzeby.
W dokumentacji uczymy jednak także podziału, bo pomaga w większych aplikacjach.

Przykład użycia komponentu z osobnego pliku:

```jsx
// src/components/Header.js
function Header() {
  return <h1>Aplikacja React</h1>;
}

export default Header;
```

```jsx
// src/App.js
import Header from "./components/Header";

function App() {
  return (
    <main className="container">
      <Header />
    </main>
  );
}

export default App;
```


```jsx
// src/App.js
import Header from "./components/Header";

function App() {
  return (
    <main className="container">
      <Header />
    </main>
  );
}

export default App;
```

Najważniejsze jest poprawne importowanie.
Ścieżka `./components/Header` oznacza: z tego samego folderu co `App.js`, wejdź do folderu `components` i znajdź plik `Header.js`.


### 6.5. Props

Props to dane przekazywane do komponentu.
Można myśleć o nich jak o argumentach funkcji.
Jeżeli komponent `Kurs` ma pokazywać różne kursy, nie powinien mieć nazwy wpisanej na sztywno.
Powinien dostać nazwę i numer jako propsy.

```jsx
function Kurs({ nazwa, numer }) {
  // Komponent nie wie, skąd pochodzą dane.
  // Dostaje je jako propsy i tylko je wyświetla.
  return <li>{numer}. {nazwa}</li>;
}

function ListaKursow() {
  return (
    <ol>
      {/* numer i nazwa są przekazane do komponentu Kurs */}
      <Kurs numer={1} nazwa="HTML" />
      <Kurs numer={2} nazwa="React" />
    </ol>
  );
}
```

Props to dane przekazane z komponentu rodzica do komponentu dziecka.
Props są tylko do odczytu.
Jeśli dziecko ma zmienić dane rodzica, rodzic przekazuje funkcję jako props.

| Co przekazujesz przez props | Przykład | Zastosowanie |
| --- | --- | --- |
| tekst | `title="React"` | nagłówki, etykiety, nazwy |
| liczbę | `count={5}` | liczniki, indeksy, wartości |
| boolean | `active={true}` | widoczność, stan przełącznika |
| obiekt | `photo={photo}` | karta, rekord, element listy |
| funkcję | `onClick={handleClick}` | akcja dziecka zgłaszana rodzicowi |

Nie modyfikuj propsów w dziecku.
Jeżeli komponent dostaje `nazwa`, powinien ją wyświetlić albo użyć do obliczeń.
Jeżeli chcesz zmienić dane, zmieniasz stan w komponencie rodzica i przekazujesz nowe propsy w kolejnym renderze.


## 7. Stylowanie bez Bootstrapa


### 7.1. CSS w CRA

W Create React App pliki CSS możesz importować bezpośrednio w JavaScript.
Najczęściej `App.css` zawiera style głównego komponentu, a `index.css` style globalne dla całej strony.
Import CSS nie tworzy zmiennej.
Po prostu mówi bundlerowi: dołącz ten plik ze stylami do aplikacji.

```jsx
import "./App.css";

function App() {
  return <h1 className="main-title">Aplikacja</h1>;
}
```

```css
.main-title {
  color: #2f4f4f;
  margin-top: 24px;
}
```

Ten przykład składa się z dwóch plików.
Pierwszy fragment trafia do `src/App.js`.
Drugi fragment trafia do `src/App.css`.
Klasa `.main-title` działa dlatego, że `App.js` importuje plik CSS.

| Plik | Typowe zastosowanie |
| --- | --- |
| `src/index.css` | style globalne: `body`, font, tło strony |
| `src/App.css` | style głównej aplikacji |
| `src/components/X.css` | style konkretnego komponentu, jeśli projekt jest większy |


### 7.2. className

W JSX nie piszemy `class`, tylko `className`.
To jedna z najczęstszych pomyłek przy przepisywaniu kodu z dokumentacji HTML lub Bootstrapa.

```jsx
<button className="btn btn-primary">Zapisz</button>
```

`className` działa tak samo jak `class` w HTML: przypisuje elementowi klasy CSS.
Różnica wynika z tego, że JSX jest bliżej JavaScriptu niż czystego HTML.
Słowo `class` ma w JavaScript inne znaczenie, dlatego React używa nazwy `className`.

Przykład z wieloma klasami:

```jsx
<main className="container mt-4">
  <button className="btn btn-success">
    Zapisz
  </button>
</main>
```

Klasy Bootstrapa możesz łączyć z własnymi klasami:

```jsx
<section className="card custom-panel">
  <div className="card-body">Treść</div>
</section>
```


### 7.3. Style inline

Style inline są przydatne, gdy wygląd zależy od zmiennej lub stanu.
Na przykład rozmiar tekstu może zależeć od suwaka, kolor tła od wartości RGB, a przezroczystość od tego, czy element jest aktywny.
Nie używaj inline style do wszystkiego.
Stały wygląd lepiej trzymać w CSS, a dynamiczny można wygodnie zapisać w `style`.

```jsx
const rozmiar = 24;

return (
  <p style={{ fontSize: rozmiar, color: "darkblue" }}>
    Tekst dynamiczny
  </p>
);
```

- Style inline są obiektem JavaScript.
- Nazwy właściwości CSS zapisujemy camelCase: `fontSize`, `backgroundColor`.
- Wartości tekstowe wpisujemy w cudzysłowie.
- Wartości liczbowe dla pikseli można podać jako liczbę.

Porównanie:

| Sytuacja | Lepszy wybór |
| --- | --- |
| stały margines sekcji | klasa CSS albo Bootstrap |
| kolor zależny od stanu | `style` |
| rozmiar czcionki z suwaka | `style` |
| wygląd przycisku | klasy Bootstrap |
| powtarzalny wygląd karty | klasa CSS |


### 7.4. Dynamiczne style

Dynamiczny styl powstaje wtedy, gdy wartość CSS zależy od danych.
W poniższym przykładzie `opacity` zależy od zmiennej `aktywny`.
Gdy `aktywny` jest prawdą, element jest w pełni widoczny.
Gdy `aktywny` jest fałszem, element jest półprzezroczysty.

```jsx
const aktywny = true;

return (
  <div style={{ opacity: aktywny ? 1 : 0.5 }}>
    Element zależny od stanu
  </div>
);
```

Ten sam pomysł możesz zastosować do wielu właściwości:

```jsx
const color = aktywny ? "white" : "black";
const backgroundColor = aktywny ? "seagreen" : "lightgray";

return (
  <button style={{ color, backgroundColor }}>
    Status
  </button>
);
```

Jeżeli dynamicznych stylów robi się dużo, rozważ dynamiczną klasę zamiast dużego obiektu `style`.


### 7.5. Organizacja CSS

- Globalne style zapisuj w `index.css` albo `App.css`.
- Klasy komponentu nazywaj konkretnie, np. `.item-card`, `.dice-row`, `.form-panel`.
- Nie używaj zbyt ogólnych selektorów, jeśli mogą popsuć Bootstrap.
- Do dynamicznych kolorów i rozmiarów często wygodniejszy jest `style`.
- Do stałego wyglądu wygodniejsze są klasy CSS.


## 8. Zdarzenia


### 8.1. onClick

`onClick` obsługuje kliknięcie elementu.
Najczęściej używa się go na przyciskach, ale może działać też na innych elementach.
W React nazwy zdarzeń zapisujemy camelCase, więc jest `onClick`, a nie `onclick`.

```jsx
function App() {
  function pokazKomunikat() {
    console.log("Kliknięto przycisk");
  }

  return <button onClick={pokazKomunikat}>Kliknij</button>;
}
```

Do `onClick` przekazujesz funkcję, a nie wynik jej wywołania.
Poprawnie: `onClick={pokazKomunikat}`.
Niepoprawnie w prostym przypadku: `onClick={pokazKomunikat()}`.

Dlaczego?
`onClick={pokazKomunikat}` oznacza: „uruchom tę funkcję dopiero po kliknięciu”.
`onClick={pokazKomunikat()}` oznacza: „uruchom funkcję natychmiast podczas renderowania i przypisz jej wynik do onClick”.
To drugie prawie zawsze jest błędem.

| Zapis | Co się stanie |
| --- | --- |
| `onClick={save}` | funkcja `save` wykona się po kliknięciu |
| `onClick={() => save(id)}` | po kliknięciu wykona się `save` z argumentem |
| `onClick={save(id)}` | funkcja wykona się od razu podczas renderu |


### 8.2. onChange

`onChange` obsługuje zmianę wartości pola formularza.
W kontrolowanych formularzach jest to podstawowy sposób aktualizowania stanu.
Użytkownik wpisuje tekst, React odbiera zdarzenie, a setter zapisuje nową wartość w stanie.

```jsx
function App() {
  const [tekst, setTekst] = useState("");

  return (
    <input
      value={tekst}
      onChange={(event) => setTekst(event.target.value)}
    />
  );
}
```

Wartość wpisana w pole znajduje się w `event.target.value`.
`event.target` to element HTML, który wywołał zdarzenie.
Dla pola tekstowego będzie to input.

Przepływ jest następujący:

1. Użytkownik wpisuje literę.
2. Przeglądarka wywołuje `onChange`.
3. Funkcja pobiera `event.target.value`.
4. `setTekst` aktualizuje stan.
5. Komponent renderuje się ponownie.
6. `value={tekst}` pokazuje aktualną wartość w polu.


### 8.3. onSubmit

`onSubmit` obsługuje zatwierdzenie formularza.
To lepszy wybór niż samo `onClick` na przycisku, bo formularz można zatwierdzić także klawiszem Enter.
W React prawie zawsze dodajemy `event.preventDefault()`, żeby przeglądarka nie przeładowała strony.

```jsx
function App() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log("Formularz zatwierdzony");
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Zapisz</button>
    </form>
  );
}
```

`event.preventDefault()` blokuje domyślne przeładowanie strony.
W React formularz najczęściej obsługuje `onSubmit`, a przycisk ma `type="submit"`.

Jeżeli w formularzu masz przycisk, który nie ma zatwierdzać formularza, ustaw mu `type="button"`.

```jsx
<form onSubmit={handleSubmit}>
  <button type="button" onClick={generatePassword}>
    Generuj
  </button>

  <button type="submit">
    Zapisz
  </button>
</form>
```


### 8.4. onBlur

`onBlur` uruchamia się wtedy, gdy użytkownik opuszcza pole.
Można go użyć do walidacji po zakończeniu wpisywania albo do uruchomienia dodatkowej logiki dopiero wtedy, gdy pole przestaje być aktywne.
To jest delikatniejsze niż walidowanie przy każdym znaku.

```jsx
function App() {
  const [numer, setNumer] = useState("");

  function zaladujObrazy() {
    console.log("Użytkownik opuścił pole numeru:", numer);
  }

  return (
    <input
      value={numer}
      onChange={(e) => setNumer(e.target.value)}
      onBlur={zaladujObrazy}
    />
  );
}
```

`onBlur` uruchamia się, gdy pole traci fokus.
Ten wzorzec przydaje się przy dynamicznych obrazach zależnych od numeru albo przy walidacji po opuszczeniu pola.

Przykład zastosowania:

```jsx
function validateName() {
  if (name.trim() === "") {
    setNameError("Pole nie może być puste");
  } else {
    setNameError("");
  }
}

<input
  value={name}
  onChange={(event) => setName(event.target.value)}
  onBlur={validateName}
/>;
```

Tutaj błąd nie pojawia się przy pierwszym pustym renderze.
Pojawia się dopiero wtedy, gdy użytkownik wejdzie w pole i je opuści.


### 8.5. Przekazywanie argumentów

Jeżeli funkcja obsługi zdarzenia potrzebuje argumentu, najczęściej owijamy ją w funkcję strzałkową.
To pozwala wykonać funkcję dopiero po kliknięciu i jednocześnie przekazać jej dane.

```jsx
function App() {
  function pobierz(id) {
    console.log("Kliknięto element:", id);
  }

  return <button onClick={() => pobierz(5)}>Pobierz</button>;
}
```

Ten wzorzec jest bardzo częsty przy listach.
Każdy element listy ma własne `id`, a przycisk przy tym elemencie przekazuje je do funkcji.

```jsx
{items.map((item) => (
  <button key={item.id} onClick={() => removeItem(item.id)}>
    Usuń {item.name}
  </button>
))}
```


## 9. Stan komponentu useState


### 9.1. Czym jest stan

Stan to dane, których zmiana ma odświeżyć widok.
Zwykła zmienna lokalna nie wystarczy, bo React nie wie, że ma ponownie wyrenderować komponent.
`useState` tworzy wartość stanu i funkcję do jej zmiany.
Hooki, takie jak `useState`, wywołuje się na górnym poziomie komponentu.

```jsx
// Na początku pliku musimy zaimportować funkcję useState z biblioteki 'react'.
import { useState } from "react";

function App() {
  // useState zwraca tablicę dwóch elementów:
  // 1. licznik: aktualna wartość (na starcie 0).
  // 2. setLicznik: funkcja, którą wywołujemy, aby zmienić tę wartość.
  const [licznik, setLicznik] = useState(0);

  // Funkcja pomocnicza wywoływana przy kliknięciu.
  function zwiekszLicznik() {
    setLicznik(licznik + 1); // Powiedz Reactowi: "zmień licznik na nowy i odśwież widok".
  }

  return (
    <div className="container mt-5">
      <p>Liczba kliknięć: {licznik}</p>
      {/* Podpinamy funkcję zwiekszLicznik pod zdarzenie onClick */}
      <button className="btn btn-primary" onClick={zwiekszLicznik}>
        Dodaj +1
      </button>
    </div>
  );
}

export default App;
```


`useState(0)` oznacza, że początkowa wartość stanu to `0`.
Nazwa `licznik` jest dowolna, ale konwencja jest taka, że setter nazywa się `setLicznik`.
To bardzo pomaga w czytaniu kodu.

| Stan przechowuje | Przykład stanu | Kiedy użyć |
| --- | --- | --- |
| tekst | `const [name, setName] = useState("")` | pole formularza |
| liczbę | `const [count, setCount] = useState(0)` | licznik, suwak, wynik |
| boolean | `const [open, setOpen] = useState(false)` | przełącznik, widoczność |
| tablicę | `const [items, setItems] = useState([])` | lista elementów |
| obiekt | `const [form, setForm] = useState({})` | większy formularz |

Jeżeli dana wartość nigdy nie zmienia się po renderze, nie musi być stanem.
Może być zwykłą stałą poza komponentem albo zmienną obliczoną przed `return`.


### 9.2. Aktualizacja licznika

```jsx
function App() {
  const [polubienia, setPolubienia] = useState(0);

  function dodaj() {
    // Prosta aktualizacja: nowa wartość to obecna wartość + 1.
    setPolubienia(polubienia + 1);
  }

  function odejmij() {
    // Wersja funkcyjna jest bezpieczna, gdy nowy stan zależy od poprzedniego.
    // Math.max pilnuje, żeby licznik nie spadł poniżej zera.
    setPolubienia((poprzednie) => Math.max(0, poprzednie - 1));
  }

  return (
    <>
      <p>Liczba polubień: {polubienia}</p>
      <button onClick={dodaj}>POLUB</button>
      <button onClick={odejmij}>USUŃ</button>
    </>
  );
}
```

Ten przykład pokazuje dwa sposoby aktualizacji.
`setPolubienia(polubienia + 1)` jest czytelne i działa w prostych przypadkach.
`setPolubienia((poprzednie) => ...)` jest bezpieczniejsze, gdy wykonujesz kilka aktualizacji po kolei albo opierasz się na poprzedniej wartości.

Warto zapamiętać wzór:

```jsx
setWartosc((poprzedniaWartosc) => nowaWartosc);
```

To nie musi być tylko licznik.
Tak samo działa przełączanie booleanów, dodawanie do tablicy albo aktualizacja obiektu.


### 9.3. Stan tekstowy

```jsx
const [email, setEmail] = useState("");
const [komunikat, setKomunikat] = useState("");
```

Stan tekstowy najczęściej służy do pól formularza i komunikatów.
Pusty tekst `""` jest dobrym stanem początkowym dla inputa, ponieważ pole startuje jako puste.
Jeżeli komunikat jest pusty, można go ukryć przez warunek `{komunikat && ...}`.

Przykład zastosowania:

```jsx
const [name, setName] = useState("");

return (
  <>
    <input value={name} onChange={(event) => setName(event.target.value)} />
    <p>Wpisano: {name}</p>
  </>
);
```

Ten sam stan zasila pole i tekst podglądu.
Dzięki temu widok zawsze pokazuje aktualne dane.


### 9.4. Stan boolean

```jsx
const [wlaczony, setWlaczony] = useState(false);

function przelacz() {
  setWlaczony((stan) => !stan);
}
```

```jsx
<button onClick={przelacz}>
  {wlaczony ? "Wyłącz" : "Włącz"}
</button>
<p>{wlaczony ? "Urządzenie włączone" : "Urządzenie wyłączone"}</p>
```

Boolean przechowuje informację typu tak/nie.
To świetny wybór dla przełączników, widoczności paneli, zaznaczenia opcji, otwarcia modala albo blokady elementu.

| Sytuacja | Przykładowy stan |
| --- | --- |
| panel jest otwarty | `const [open, setOpen] = useState(false)` |
| opcja jest zaznaczona | `const [checked, setChecked] = useState(false)` |
| element jest aktywny | `const [active, setActive] = useState(true)` |
| trwa ładowanie | `const [loading, setLoading] = useState(false)` |

Najczęstszy wzór przełączania to:

```jsx
setOpen((previousOpen) => !previousOpen);
```


### 9.5. Poprzedni stan

Jeżeli nowy stan zależy od poprzedniego, użyj wersji funkcyjnej settera.
To jest szczególnie ważne przy licznikach, przełącznikach i aktualizacji tablic.

```jsx
setLicznik((poprzedni) => poprzedni + 1);
setAktywny((poprzedni) => !poprzedni);
```

Wersja funkcyjna daje Reactowi instrukcję: weź najnowszą znaną wartość i na jej podstawie policz nową.
To chroni przed sytuacją, w której funkcja korzysta ze starej wartości zamkniętej w aktualnym renderze.

Przykłady:

```jsx
setItems((previousItems) => [...previousItems, newItem]);
setUser((previousUser) => ({ ...previousUser, name: "Anna" }));
setVisible((previousVisible) => !previousVisible);
```


### 9.6. Reset

```jsx
function reset() {
  setEmail("");
  setHaslo("");
  setPowtorzHaslo("");
  setKomunikat("");
}
```

Reset polega na przywróceniu stanów do wartości początkowych.
W małym formularzu można wywołać kilka setterów.
W większym formularzu wygodniejsze jest trzymanie wartości początkowej w obiekcie:

```jsx
const initialForm = {
  name: "",
  email: "",
  accepted: false
};

const [form, setForm] = useState(initialForm);

function resetForm() {
  setForm(initialForm);
}
```

Taki zapis jest łatwiejszy do utrzymania, gdy pól jest dużo.


## 10. Formularze kontrolowane

Formularz kontrolowany to formularz, którego wartości są przechowywane w stanie Reacta.
Input nie „żyje własnym życiem”.
Jego wartość pochodzi z `value={...}`, a każda zmiana przechodzi przez `onChange`.
Dzięki temu komponent zawsze wie, co użytkownik wpisał.

Schemat kontrolowanego pola:

1. Tworzysz stan, np. `const [imie, setImie] = useState("")`.
2. Podpinasz stan do inputa przez `value={imie}`.
3. W `onChange` zapisujesz nową wartość przez `setImie(event.target.value)`.
4. Przy zatwierdzaniu formularza korzystasz z wartości `imie`.

| Element formularza | Właściwość kontrolująca | Wartość ze zdarzenia |
| --- | --- | --- |
| `input text` | `value` | `event.target.value` |
| `input number` | `value` | `event.target.value` i konwersja na liczbę |
| `textarea` | `value` | `event.target.value` |
| `select` | `value` | `event.target.value` |
| `checkbox` | `checked` | `event.target.checked` |
| `radio` | `checked` | `event.target.value` |


### 10.1. input text

```jsx
// 1. Definiujemy stan dla pol
const [imie, setImie] = useState("");

// 2. W JSX łączymy stan z elementem HTML
return (
  <div className="mb-3">
    <label htmlFor="imie" className="form-label">Twoje Imię:</label>
    <input
      id="imie"
      type="text"
      className="form-control"
      // VALUE: To sprawia, że pole pokazuje to, co jest w stanie 'imie'.
      value={imie}
      // ONCHANGE: Ta funkcja uruchamia się przy każdym naciśnięciu klawisza.
      // 'e' to obiekt zdarzenia, a 'e.target.value' to aktualny tekst w polu.
      onChange={(e) => setImie(e.target.value)}
    />
    <p>Witaj, {imie}!</p>
  </div>
);
```

**Dlaczego to jest ważne?**
Dzięki temu, że React kontroluje wartość pola, możesz w każdej chwili (np. przy kliknięciu przycisku) odczytać zmienną `imie` i wysłać ją do bazy danych lub wyświetlić w innym miejscu, mając pewność, że jest aktualna.


Pole kontrolowane ma wartość w stanie Reacta.
Każda zmiana pola wywołuje `onChange`.
Dzięki temu w handlerze zatwierdzenia formularza masz aktualne dane.

Jeżeli usuniesz `onChange`, pole z `value` stanie się praktycznie tylko do odczytu.
Jeżeli usuniesz `value`, React przestanie kontrolować pole.
Dlatego w formularzach kontrolowanych te dwie rzeczy zwykle występują razem.


### 10.2. input number

```jsx
const [numerKursu, setNumerKursu] = useState("");

<input
  type="number"
  className="form-control"
  value={numerKursu}
  onChange={(e) => setNumerKursu(e.target.value)}
/>;
```

Nawet `input type="number"` zwraca wartość jako tekst.
Przed porównaniem z liczbą użyj `Number()` albo `parseInt()`.

```js
const numer = Number(numerKursu);
if (Number.isNaN(numer)) {
  console.log("To nie jest liczba");
}
```

Warto trzymać wartość pola liczbowego jako tekst, dopóki użytkownik pisze.
Dlaczego?
Bo użytkownik może chwilowo wyczyścić pole albo wpisać znak minus.
Konwersję na liczbę najlepiej wykonać w momencie walidacji albo zatwierdzenia.

Przykład walidacji zakresu:

```jsx
function handleSubmit(event) {
  event.preventDefault();

  const number = Number(numerKursu);

  if (!Number.isInteger(number) || number < 1 || number > 10) {
    setKomunikat("Podaj liczbę od 1 do 10");
    return;
  }

  setKomunikat(`Wybrano numer ${number}`);
}
```


### 10.3. password

Pole hasła działa tak samo jak zwykłe pole tekstowe, ale przeglądarka ukrywa wpisywane znaki.
W React nadal kontrolujesz je przez `value` i `onChange`.

```jsx
<input
  type="password"
  className="form-control"
  value={haslo}
  onChange={(e) => setHaslo(e.target.value)}
/>;
```

Typowe zastosowania:

- formularz logowania,
- formularz rejestracji,
- powtórzenie hasła,
- prosta walidacja długości hasła.

Przykład sprawdzenia zgodności:

```jsx
if (password !== repeatPassword) {
  setMessage("Hasła muszą być takie same");
}
```


### 10.4. select

`select` pozwala wybrać jedną wartość z listy.
Stan początkowy powinien odpowiadać jednej z opcji.
Jeżeli `value` ma wartość, której nie ma w żadnym `<option>`, interfejs może zachowywać się nieintuicyjnie.

```jsx
const [rodzaj, setRodzaj] = useState("Komedia");

<select
  className="form-select"
  value={rodzaj}
  onChange={(e) => setRodzaj(e.target.value)}
>
  <option>Komedia</option>
  <option>Obyczajowy</option>
  <option>Sensacyjny</option>
  <option>Horror</option>
</select>;
```

Jeżeli chcesz mieć osobną wartość techniczną i osobny tekst dla użytkownika, użyj atrybutu `value`.

```jsx
<select value={category} onChange={(event) => setCategory(event.target.value)}>
  <option value="flowers">Kwiaty</option>
  <option value="animals">Zwierzęta</option>
  <option value="cars">Samochody</option>
</select>
```

Wtedy w stanie zapisze się `flowers`, `animals` albo `cars`, a użytkownik zobaczy polskie etykiety.


### 10.5. textarea

`textarea` służy do dłuższego tekstu.
W React nie wpisujemy tekstu między `<textarea>...</textarea>`, jeśli pole ma być kontrolowane.
Używamy `value`, tak jak przy inputach.

```jsx
const [opis, setOpis] = useState("");

<textarea
  className="form-control"
  rows="5"
  value={opis}
  onChange={(e) => setOpis(e.target.value)}
/>;
```

Praktyczny dodatek to licznik znaków:

```jsx
<textarea
  value={opis}
  onChange={(event) => setOpis(event.target.value)}
/>
<p>Wpisano znaków: {opis.length}</p>
```


### 10.6. checkbox

Checkbox różni się od inputa tekstowego.
Nie kontrolujesz go przez `value`, tylko przez `checked`.
`checked` jest booleanem: `true` oznacza zaznaczony, `false` oznacza niezaznaczony.

```jsx
const [pokazKwiaty, setPokazKwiaty] = useState(true);

<input
  type="checkbox"
  className="form-check-input"
  checked={pokazKwiaty}
  onChange={(e) => setPokazKwiaty(e.target.checked)}
/>;
```

Dla checkboxa używaj `checked`, nie `value`.
`event.target.checked` daje `true` albo `false`.

Checkbox jest dobry do:

- zgody regulaminowej,
- pokazania/ukrycia kategorii,
- włączenia dodatkowej opcji,
- ustawień typu „czy zawiera cyfry”.


### 10.7. radio

Radio buttony służą do wyboru jednej wartości z kilku.
Wszystkie przyciski radio z jednej grupy powinny mieć ten sam atrybut `name`.
Każdy z nich ma inną wartość `value`.

```jsx
const [typ, setTyp] = useState("list");

<input
  type="radio"
  name="typ"
  value="list"
  checked={typ === "list"}
  onChange={(e) => setTyp(e.target.value)}
/>;
```

Przykład pełniejszej grupy:

```jsx
<label>
  <input
    type="radio"
    name="delivery"
    value="standard"
    checked={delivery === "standard"}
    onChange={(event) => setDelivery(event.target.value)}
  />
  Standard
</label>

<label>
  <input
    type="radio"
    name="delivery"
    value="express"
    checked={delivery === "express"}
    onChange={(event) => setDelivery(event.target.value)}
  />
  Express
</label>
```


### 10.8. range

`input type="range"` tworzy suwak.
Wartość z suwaka też przychodzi jako tekst, dlatego często od razu zamieniamy ją na liczbę przez `Number(...)`.

```jsx
const [rozmiar, setRozmiar] = useState(20);

<input
  type="range"
  min="10"
  max="60"
  value={rozmiar}
  onChange={(e) => setRozmiar(Number(e.target.value))}
/>;

<p style={{ fontSize: rozmiar }}>Tekst testowy</p>;
```

Suwak jest bardzo wygodny do dynamicznego podglądu.
Nie trzeba klikać przycisku.
Każdy ruch suwaka aktualizuje stan i od razu zmienia widok.

Typowe zastosowania:

| Zastosowanie | Stan | Efekt w widoku |
| --- | --- | --- |
| rozmiar tekstu | `fontSize` | `style={{ fontSize }}` |
| kolor RGB | `r`, `g`, `b` | `backgroundColor` |
| wiek/liczba | `age` | tekst z aktualną wartością |
| głośność/procent | `volume` | pasek lub etykieta |


### 10.9. Walidacja

Walidacja to sprawdzanie, czy dane wpisane przez użytkownika spełniają wymagania aplikacji.
Najlepiej pisać ją jako osobne funkcje, bo wtedy można je łatwo czytać i testować.
Funkcja walidująca nie powinna zmieniać widoku.
Powinna tylko powiedzieć, czy dane są poprawne.

```js
function walidujEmail(email) {
  return email.includes("@");
}

function czyPuste(value) {
  return value.trim() === "";
}

function czySameCyfry(value) {
  return /^\d+$/.test(value);
}
```

| Walidacja | Warunek | Przykład |
| --- | --- | --- |
| puste pole | `value.trim() === ''` | imię, nazwisko, tytuł |
| email | `email.includes('@')` | formularz rejestracji |
| zgodne hasła | `haslo === powtorz` | konto |
| numer z zakresu | `n >= 1 && n <= 12` | program prania |
| 5 cyfr | `/^\d{5}$/.test(kod)` | kod pocztowy |
| poprawny wybór | `opcje.includes(value)` | select |

Przykład pełniejszej walidacji formularza:

```jsx
function validateForm() {
  if (name.trim() === "") {
    return "Podaj imię";
  }

  if (!email.includes("@")) {
    return "Email musi zawierać znak @";
  }

  return "";
}

function handleSubmit(event) {
  event.preventDefault();

  const error = validateForm();

  if (error) {
    setMessage(error);
    return;
  }

  setMessage("Dane są poprawne");
}
```

Taki układ jest czytelny.
Najpierw walidujesz.
Jeżeli jest błąd, zapisujesz komunikat i przerywasz funkcję przez `return`.
Jeżeli błędu nie ma, wykonujesz właściwą akcję.


## 11. Tablice i renderowanie list

Tablice są w React podstawą dynamicznych widoków.
Jeżeli masz wiele podobnych elementów, nie tworzysz ręcznie dziesięciu takich samych bloków JSX.
Tworzysz tablicę danych i renderujesz ją przez `map()`.
Dzięki temu widok automatycznie dopasowuje się do liczby elementów.

Typowy przepływ:

1. Masz tablicę danych.
2. Używasz `map()`, żeby zamienić każdy element danych na JSX.
3. Każdy element dostaje `key`.
4. Jeżeli tablica się zmieni, React odświeży listę.


### 11.1. map

```jsx
const kursy = ["HTML", "CSS", "React"];

function ListaKursow() {
  return (
    <ul>
      {/* 
        Przechodzimy przez tablicę 'kursy' używając .map(). 
        Dla każdego kursu tworzymy element <li>.
      */}
      {kursy.map((kurs, index) => (
        // KEY: Klucz pozwala Reactowi na szybką aktualizację listy.
        // Jeśli dane mają własne ID, użyj ID. Jeśli nie, użyj indeksu z mapy.
        <li key={index}>{kurs}</li>
      ))}
    </ul>
  );
}
```

**Jak to działa?**
Funkcja `.map()` to "fabryka elementów JSX". Bierze ona zwykłe dane (np. teksty) i dla każdego z nich "produkuje" kawałek widoku. React potrafi wyświetlać tablice elementów JSX bezpośrednio, co czyni listowanie danych bardzo prostym.


`map()` zamienia tablicę danych na tablicę elementów JSX.
To najważniejsza metoda do renderowania list w React.

`map()` nie zmienia oryginalnej tablicy.
Tworzy nową tablicę wyników.
W React tym wynikiem są zwykle elementy JSX.

Porównanie myślenia:

| Bez React | W React |
| --- | --- |
| ręcznie kopiujesz wiele elementów HTML | opisujesz jeden wzorzec elementu |
| sam pilnujesz liczby elementów | liczba elementów wynika z tablicy |
| trudniej aktualizować dane | zmieniasz tablicę, a widok się odświeża |


### 11.2. key

`key` pomaga Reactowi rozpoznać, który element listy jest który.
Najlepszy `key` to stabilne `id` z danych.
Indeks tablicy może być awaryjny w bardzo statycznych listach, ale przy dodawaniu/usuwaniu lepiej go unikać.

```jsx
{zdjecia.map((zdjecie) => (
  <article key={zdjecie.id}>
    <img src={zdjecie.plik} alt={zdjecie.alt} />
  </article>
))}
```

Dobry `key` powinien być:

- unikalny w ramach danej listy,
- stabilny między renderami,
- związany z danymi, a nie z przypadkowym losowaniem.

Nie rób tak:

```jsx
{items.map((item) => (
  <li key={Math.random()}>{item.name}</li>
))}
```

Losowy `key` zmienia się przy każdym renderze.
React traci wtedy informację o tym, który element jest który.
Może to pogorszyć wydajność i powodować dziwne zachowania w formularzach wewnątrz list.


### 11.3. Lista numerowana

```jsx
<ol>
  {kursy.map((kurs) => (
    <li key={kurs}>{kurs}</li>
  ))}
</ol>
```

Lista numerowana (`ol`) automatycznie dodaje numery.
Nie musisz samodzielnie wypisywać `1`, `2`, `3`.
To dobre rozwiązanie dla kolejności kroków, kursów, instrukcji albo rankingów.

Jeżeli numer jest częścią danych albo ma zaczynać się od nietypowej wartości, możesz użyć indeksu z `map`.

```jsx
{kursy.map((kurs, index) => (
  <li key={kurs}>
    {index + 1}. {kurs}
  </li>
))}
```

Pamiętaj: indeks jako wyświetlany numer jest w porządku.
Indeks jako `key` bywa problemem, gdy lista może się zmieniać.


### 11.4. Dodawanie elementu

```jsx
const [notatki, setNotatki] = useState(["Zakupy", "Nauka"]);
const [nowa, setNowa] = useState("");

function dodajNotatke(event) {
  event.preventDefault();
  if (nowa.trim() === "") return;
  setNotatki((poprzednie) => [...poprzednie, nowa]);
  setNowa("");
}
```

Dodawanie elementu do tablicy w stanie polega na utworzeniu nowej tablicy.
Nie używamy `notatki.push(nowa)`, bo `push` zmienia istniejącą tablicę.
Zamiast tego tworzymy nową tablicę przez spread:

```jsx
setNotatki((poprzednie) => [...poprzednie, nowa]);
```

Czytamy to tak:

- weź poprzednią tablicę,
- rozpakuj jej elementy,
- dopisz nową wartość na końcu,
- zapisz nową tablicę jako stan.

`setNowa("")` na końcu czyści pole formularza.
To mały detal, ale bardzo poprawia wygodę używania interfejsu.


### 11.5. Usuwanie

```jsx
function usunNotatke(indeksDoUsuniecia) {
  setNotatki((poprzednie) =>
    poprzednie.filter((_, indeks) => indeks !== indeksDoUsuniecia)
  );
}
```

Usuwanie przez `filter()` oznacza: zbuduj nową tablicę tylko z tych elementów, które mają zostać.
W przykładzie usuwamy element o konkretnym indeksie.
Jeżeli dane mają `id`, zwykle lepiej usuwać po `id`.

```jsx
function removeItem(idToRemove) {
  setItems((previousItems) =>
    previousItems.filter((item) => item.id !== idToRemove)
  );
}
```

Ten wariant jest stabilniejszy, bo `id` nie zależy od aktualnej pozycji elementu w tablicy.


### 11.6. Aktualizacja jednego elementu

```jsx
function zwiekszPobrania(id) {
  setZdjecia((poprzednie) =>
    poprzednie.map((zdjecie) =>
      zdjecie.id === id
        ? { ...zdjecie, pobrania: zdjecie.pobrania + 1 }
        : zdjecie
    )
  );
}
```

Nie zmieniaj obiektu bezpośrednio przez `zdjecie.pobrania++`.
React oczekuje nowej tablicy i nowego obiektu dla zmienionego elementu.
Ten wzorzec jest kluczowy dla widoków kart, koszyków, list elementów i liczników pobrań.

Czytanie tego kodu krok po kroku:

1. `setZdjecia` zmienia stan tablicy.
2. `map()` przechodzi po wszystkich elementach.
3. Jeżeli `zdjecie.id === id`, zwracamy nowy obiekt z większą liczbą pobrań.
4. Jeżeli to inny element, zwracamy go bez zmian.

Ten sam wzorzec możesz zastosować do przełączania stanu:

```jsx
function toggleDone(id) {
  setItems((previousItems) =>
    previousItems.map((item) =>
      item.id === id ? { ...item, done: !item.done } : item
    )
  );
}
```


## 12. Obiekty i listy obiektów

Obiekty pozwalają trzymać kilka powiązanych informacji w jednym miejscu.
Zamiast osobnych tablic `nazwy`, `kategorie`, `liczniki`, lepiej mieć jedną tablicę obiektów.
Każdy obiekt opisuje jeden element.
To ułatwia renderowanie, filtrowanie i aktualizację.


### 12.1. Model danych

```js
const initialPhotos = [
  { id: 1, plik: "/img/kwiat.jpg", kategoria: "kwiaty", pobrania: 0 },
  { id: 2, plik: "/img/kot.jpg", kategoria: "zwierzeta", pobrania: 3 },
  { id: 3, plik: "/img/auto.jpg", kategoria: "samochody", pobrania: 1 }
];
```

Dobrze nazwany model danych upraszcza cały komponent.
Jeśli w widoku potrzebujesz pliku, kategorii i licznika, te pola powinny być w obiekcie.
Nie trzymaj wielu równoległych tablic, jeśli jedna tablica obiektów lepiej opisuje dane.

Przykład złego kierunku:

```js
const nazwy = ["Kwiat", "Kot"];
const pliki = ["/img/kwiat.jpg", "/img/kot.jpg"];
const pobrania = [0, 3];
```

Taki układ szybko robi się trudny.
Musisz pilnować, żeby indeks `0` w każdej tablicy oznaczał ten sam element.
Lepiej zapisać dane razem:

```js
const items = [
  { id: 1, nazwa: "Kwiat", plik: "/img/kwiat.jpg", pobrania: 0 },
  { id: 2, nazwa: "Kot", plik: "/img/kot.jpg", pobrania: 3 }
];
```

| Pole | Dlaczego jest przydatne |
| --- | --- |
| `id` | stabilny identyfikator do `key` i aktualizacji |
| `nazwa` / `title` | tekst wyświetlany użytkownikowi |
| `plik` / `file` | ścieżka do obrazu lub zasobu |
| `kategoria` / `category` | filtrowanie |
| `pobrania` / `downloads` | licznik aktualizowany w stanie |


### 12.2. Kopiowanie obiektu

```js
const film = { tytul: "Film", wypozyczenia: 0 };
const nowszyFilm = { ...film, wypozyczenia: film.wypozyczenia + 1 };
```

Operator spread `...film` kopiuje pola starego obiektu do nowego.
Potem `wypozyczenia: film.wypozyczenia + 1` nadpisuje tylko jedno pole.
To jest podstawowa technika aktualizacji obiektów w stanie.

Rozpisane:

```js
const nowszyFilm = {
  ...film,
  wypozyczenia: film.wypozyczenia + 1
};
```

Nie robimy:

```js
film.wypozyczenia++;
```

Taka mutacja zmienia istniejący obiekt.
W React lepiej tworzyć nowy obiekt, żeby zmiana była jasna i przewidywalna.


### 12.3. Kopiowanie tablicy

```js
const liczby = [1, 2, 3];
const zDodana = [...liczby, 4];
const bezDwojki = liczby.filter((x) => x !== 2);
```

Tablice w stanie też traktujemy niemutowalnie.
To oznacza, że zamiast zmieniać starą tablicę, tworzymy nową.

| Operacja | Wzorzec |
| --- | --- |
| dodanie na końcu | `[...items, newItem]` |
| dodanie na początku | `[newItem, ...items]` |
| usunięcie | `items.filter(...)` |
| zamiana elementu | `items.map(...)` |
| sortowanie | `[...items].sort(...)` |

Najważniejsza zasada: jeśli metoda zmienia oryginalną tablicę, zrób najpierw kopię.
`sort()` zmienia tablicę, więc przy stanie używaj `[...items].sort(...)`.


### 12.4. Formularz jako obiekt

Przy większych formularzach osobny `useState` dla każdego pola może być męczący.
Wtedy można trzymać cały formularz w jednym obiekcie.
Kluczowe jest to, żeby każde pole formularza miało atrybut `name` zgodny z nazwą pola w obiekcie.

```jsx
const [form, setForm] = useState({
  tytul: "",
  rodzaj: "Komedia"
});

function updateField(event) {
  const { name, value } = event.target;
  // [name] oznacza dynamiczną nazwę pola, np. "tytul" albo "rodzaj".
  setForm((prev) => ({ ...prev, [name]: value }));
}
```

```jsx
<input
  name="tytul"
  value={form.tytul}
  onChange={updateField}
/>;

<select
  name="rodzaj"
  value={form.rodzaj}
  onChange={updateField}
>
  <option>Komedia</option>
  <option>Horror</option>
</select>;
```

Jak to działa:

1. Input ma `name="tytul"`.
2. Użytkownik wpisuje tekst.
3. `updateField` pobiera z inputa `name` i `value`.
4. `setForm` kopiuje stary obiekt.
5. `[name]: value` aktualizuje tylko jedno pole.

Ten wzorzec jest bardzo wygodny, gdy formularz ma wiele pól:

```jsx
const [form, setForm] = useState({
  firstName: "",
  lastName: "",
  email: "",
  city: ""
});
```

Wtedy jedna funkcja `updateField` może obsłużyć wszystkie pola tekstowe.


### 12.5. Dane z pliku przepisane do kodu

W prostych aplikacjach front-endowych dane z małego pliku tekstowego często można przepisać do tablicy w kodzie.
Jeżeli projekt wymaga tylko front-endu bez serwera, to jest najprostsze rozwiązanie.
Jeżeli plik ma być naprawdę pobierany przez aplikację, umieść go w `public` i użyj `fetch`.

Neutralny przykład danych w kodzie:

```js
const courses = [
  "HTML i CSS",
  "JavaScript",
  "React",
  "Bazy danych"
];
```

Przykład danych obiektowych:

```js
const products = [
  { id: 1, name: "Monitor", price: 699 },
  { id: 2, name: "Klawiatura", price: 149 },
  { id: 3, name: "Mysz", price: 89 }
];
```

Jeżeli dane są krótkie i stałe, tablica w pliku `src/data/products.js` jest w porządku.
Jeżeli dane mają udawać zewnętrzne źródło, lepszy będzie plik JSON w `public/data`.


## 13. Renderowanie warunkowe

Renderowanie warunkowe oznacza, że React pokazuje różny JSX zależnie od danych.
To podstawa komunikatów błędów, pustych list, widocznych paneli, aktywnych przycisków i przełączników.
Warunek możesz obsłużyć przed `return` albo bezpośrednio w JSX.


### 13.1. if przed return

`if` przed `return` jest dobry, gdy cały komponent ma zwrócić zupełnie inny widok.
Przykład: jeśli jest błąd, pokaż komunikat błędu, a jeśli go nie ma, pokaż sukces.

```jsx
function Komunikat({ blad }) {
  if (blad) {
    return <p className="text-danger">Wystąpił błąd</p>;
  }

  return <p className="text-success">Dane poprawne</p>;
}
```

Ten wzorzec jest bardzo czytelny.
Najpierw obsługujesz specjalny przypadek, a dopiero potem normalny widok.

Można go użyć także przy ładowaniu danych:

```jsx
if (loading) {
  return <p>Ładowanie...</p>;
}

if (error) {
  return <p className="text-danger">{error}</p>;
}

return <ProductList products={products} />;
```


### 13.2. operator trójargumentowy

```jsx
<p>{aktywny ? "Włączony" : "Wyłączony"}</p>
```

Operator trójargumentowy ma postać:

```js
warunek ? wartoscGdyPrawda : wartoscGdyFalsz
```

Jest dobry do krótkich wyborów.
Jeżeli warunek zajmuje kilka linii albo zwraca duże fragmenty JSX, czasem lepiej przygotować zmienną przed `return`.

Przykład z klasą:

```jsx
<button className={active ? "btn btn-success" : "btn btn-secondary"}>
  {active ? "Aktywny" : "Nieaktywny"}
</button>
```


### 13.3. &&

```jsx
{komunikat && <div className="alert alert-info">{komunikat}</div>}
```

Operator `&&` jest wygodny, gdy chcesz pokazać element tylko wtedy, gdy warunek jest prawdziwy.
Jeżeli potrzebujesz dwóch różnych wersji tekstu, użyj operatora trójargumentowego.

Ten zapis czytamy tak:

- jeżeli `komunikat` istnieje, pokaż alert,
- jeżeli `komunikat` jest pusty, nie pokazuj nic.

Uważaj na liczby.
Jeżeli warunkiem jest `count`, a `count` wynosi `0`, React może pokazać `0`.
Bezpieczniej pisać warunek jawnie:

```jsx
{count > 0 && <p>Liczba elementów: {count}</p>}
```


### 13.4. komunikaty błędów

Komunikaty błędów najczęściej zapisuje się w stanie.
Pusty tekst oznacza brak błędu.
Tekst z komunikatem oznacza, że należy pokazać alert albo opis pod polem.

```jsx
{blad && (
  <div className="alert alert-danger" role="alert">
    {blad}
  </div>
)}
```

`role="alert"` pomaga technologiom wspierającym zauważyć ważny komunikat.
Bootstrap daje wygląd, ale to React decyduje, czy komunikat w ogóle jest renderowany.

Przykład z polem formularza:

```jsx
{emailError && (
  <p className="text-danger">
    {emailError}
  </p>
)}
```


### 13.5. puste listy

Pusta lista powinna być obsłużona świadomie.
Jeżeli `map()` renderuje pustą tablicę, użytkownik może zobaczyć po prostu pustą stronę.
Lepiej pokazać neutralny komunikat.

```jsx
{widoczneZdjecia.length === 0 ? (
  <p>Brak elementów do wyświetlenia.</p>
) : (
  widoczneZdjecia.map((zdjecie) => (
    <PhotoCard key={zdjecie.id} photo={zdjecie} />
  ))
)}
```

Ten wzorzec sprawdza się dla wyników wyszukiwania, filtrowania, list notatek, produktów albo rekordów z pliku.
Najpierw obliczasz widoczne dane, potem decydujesz, czy pokazać listę, czy komunikat.


## 14. Bootstrap w React

Bootstrap w React jest po prostu biblioteką CSS.
Nie zastępuje komponentów, stanu ani zdarzeń.
Daje gotowe klasy, dzięki którym formularze, przyciski, siatka i karty wyglądają lepiej bez pisania dużej ilości własnego CSS.
W React najważniejsza różnica jest taka, że zamiast `class` używasz `className`.


### 14.1. Instalacja

Bootstrap dostarcza gotowe klasy CSS dla formularzy, przycisków, siatki, kart, alertów i tabel.
W Create React App najprościej zainstalować go przez npm.

```bash
npm install bootstrap
```

Po instalacji paczka pojawi się w `package.json`.
Nie kopiuj plików Bootstrapa ręcznie do `src`.
Wystarczy instalacja przez npm i import CSS.


### 14.2. Import CSS

Import Bootstrapa dodaj zwykle w `src/index.js` albo w `src/App.js`.
W prostych projektach edukacyjnych najczęściej wystarczy import CSS.

```js
import "bootstrap/dist/css/bootstrap.css";
```

Jeżeli korzystasz z komponentów JavaScript Bootstrapa, takich jak modal albo dropdown, potrzebny może być także JavaScript Bootstrapa.
W prostych formularzach i widokach z kartami zwykle nie jest potrzebny.

Najprostsza zasada:

| Chcesz używać | Co importować |
| --- | --- |
| klas typu `btn`, `container`, `form-control` | tylko CSS |
| własnej logiki Reacta i klas Bootstrapa | tylko CSS |
| dropdownów/modali Bootstrapa bez własnej logiki | CSS oraz JS Bootstrapa |

W tej dokumentacji większość przykładów używa tylko CSS.


### 14.3. Kontenery

```jsx
<main className="container mt-4">
  <h1>Aplikacja</h1>
</main>
```

| Klasa | Znaczenie |
| --- | --- |
| `container` | responsywny kontener o ograniczonej szerokości |
| `container-fluid` | kontener na całą szerokość |
| `mt-4` | margin-top |
| `mb-3` | margin-bottom |
| `p-3` | padding |

`container` jest dobrym domyślnym wyborem dla małych aplikacji.
Dodaje czytelną szerokość i marginesy boczne.
`mt-4` oznacza odstęp od góry.
Bootstrap ma wiele klas odstępów: `m` dla margin, `p` dla padding, a liczba określa rozmiar.

Przykład:

```jsx
<section className="container mt-4 mb-5">
  <h1 className="mb-3">Tytuł</h1>
  <p className="text-muted">Opis sekcji.</p>
</section>
```


### 14.4. Formularze

Bootstrap daje gotowe klasy dla pól formularza.
Najczęstszy układ to `div.mb-3`, w środku `label.form-label` i input z klasą `form-control`.
Ten układ daje odstęp między polami i spójny wygląd.

```jsx
<div className="mb-3">
  <label htmlFor="tytul" className="form-label">Tytuł filmu</label>
  <input id="tytul" className="form-control" />
</div>

<div className="mb-3">
  <label htmlFor="rodzaj" className="form-label">Rodzaj</label>
  <select id="rodzaj" className="form-select">
    <option>Komedia</option>
  </select>
</div>
```

W React nadal musisz dodać `value` i `onChange`, jeżeli pole ma być kontrolowane.
Bootstrap odpowiada tylko za wygląd.
React odpowiada za dane.

```jsx
<input
  id="name"
  className="form-control"
  value={name}
  onChange={(event) => setName(event.target.value)}
/>
```


### 14.5. Przyciski

| Klasa | Wygląd |
| --- | --- |
| `btn btn-primary` | główny niebieski przycisk |
| `btn btn-secondary` | neutralny przycisk |
| `btn btn-success` | pozytywna akcja |
| `btn btn-danger` | niebezpieczna akcja |
| `btn btn-outline-primary` | przycisk konturowy |

```jsx
<button type="submit" className="btn btn-primary">
  Zapisz
</button>
```

Klasa `btn` daje bazowy wygląd przycisku.
Druga klasa, np. `btn-primary`, określa wariant kolorystyczny.
W React pamiętaj też o typie przycisku.
W formularzu przycisk zatwierdzający powinien mieć `type="submit"`, a zwykły przycisk akcji `type="button"`.

```jsx
<button type="button" className="btn btn-outline-secondary">
  Anuluj
</button>
```


### 14.6. Grid

Grid Bootstrapa służy do układania elementów w kolumnach.
To bardzo przydatne przy kartach, formularzach z dwoma polami w jednym wierszu albo panelach.

```jsx
<div className="row g-3">
  <div className="col-12 col-md-6 col-lg-4">Kolumna 1</div>
  <div className="col-12 col-md-6 col-lg-4">Kolumna 2</div>
  <div className="col-12 col-md-6 col-lg-4">Kolumna 3</div>
</div>
```

- `row` tworzy wiersz siatki.
- `col-12` oznacza pełną szerokość na małym ekranie.
- `col-md-6` oznacza połowę szerokości od rozmiaru medium.
- `col-lg-4` oznacza jedną trzecią szerokości od rozmiaru large.
- `g-3` dodaje odstępy między kolumnami.

Ten zapis oznacza:

- na telefonie każda kolumna zajmuje całą szerokość,
- na średnim ekranie są dwie kolumny w rzędzie,
- na dużym ekranie są trzy kolumny w rzędzie.

To daje responsywny układ bez pisania media queries.


### 14.7. Karty

Karta to wygodny kontener dla powtarzalnego elementu: produktu, zdjęcia, użytkownika, notatki albo ustawienia.
Karta zwykle ma obraz, tytuł, opis i przycisk.

```jsx
<div className="card">
  <img src="/img/kwiat.jpg" className="card-img-top" alt="Kwiat" />
  <div className="card-body">
    <h5 className="card-title">Kwiat</h5>
    <p className="card-text">Pobrania: 0</p>
    <button className="btn btn-primary">Pobierz</button>
  </div>
</div>
```

W aplikacji React karty najczęściej renderujesz przez `map()`:

```jsx
{items.map((item) => (
  <div className="col-md-4" key={item.id}>
    <div className="card h-100">
      <div className="card-body">
        <h2 className="h5">{item.name}</h2>
      </div>
    </div>
  </div>
))}
```


### 14.8. Switche

Switch Bootstrapa to checkbox z innym wyglądem.
Od strony Reacta nadal obsługujesz go tak samo jak checkbox: przez `checked` i `onChange`.

```jsx
<div className="form-check form-switch">
  <input
    className="form-check-input"
    type="checkbox"
    role="switch"
    id="kwiatySwitch"
    checked={pokazKwiaty}
    onChange={(e) => setPokazKwiaty(e.target.checked)}
  />
  <label className="form-check-label" htmlFor="kwiatySwitch">
    Kwiaty
  </label>
</div>
```

Switch jest dobry do opcji włącz/wyłącz.
Jeżeli wybierasz jedną wartość z kilku, lepszy może być `select` albo radio buttony.


### 14.9. Alerty

```jsx
<div className="alert alert-warning" role="alert">
  Nieprawidłowy numer kursu
</div>
```

Alerty służą do komunikatów.
Możesz używać różnych wariantów:

| Klasa | Zastosowanie |
| --- | --- |
| `alert-info` | neutralna informacja |
| `alert-success` | powodzenie |
| `alert-warning` | ostrzeżenie |
| `alert-danger` | błąd |

W React zwykle pokazujesz alert warunkowo:

```jsx
{message && (
  <div className="alert alert-info" role="alert">
    {message}
  </div>
)}
```


### 14.10. Tabele

```jsx
<table className="table table-striped">
  <thead>
    <tr>
      <th>Nazwa</th>
      <th>Liczba</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>React</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
```


## 15. Obrazy i zasoby


### 15.1. public

Pliki w folderze `public` są dostępne od korzenia strony.
Jeżeli umieścisz obraz `public/img/kosc1.png`, w JSX możesz użyć ścieżki `/img/kosc1.png`.

```jsx
<img src="/img/kosc1.png" alt="Kość z jednym oczkiem" />
```


### 15.2. src i import

Obrazy z folderu `src` można importować jak moduły.
To daje kontrolę bundlera nad plikiem.

```jsx
import logo from "./assets/logo.png";

function App() {
  return <img src={logo} alt="Logo" />;
}
```


### 15.3. Obraz zależny od stanu

```jsx
const [oczka, setOczka] = useState(1);
const src = `/img/kosc${oczka}.png`;

return <img src={src} alt={`Kość: ${oczka}`} />;
```


### 15.4. Obrazy w kolekcjach

```jsx
{zdjecia.map((zdjecie) => (
  <img
    key={zdjecie.id}
    src={zdjecie.plik}
    alt={zdjecie.opis}
    className="img-fluid"
  />
))}
```


### 15.5. alt

`alt` opisuje obraz dla czytników ekranu i jako tekst zastępczy.
Nie zostawiaj pustego `alt`, jeśli obraz niesie znaczenie.
Dla obrazów dekoracyjnych można użyć `alt=""`, ale w materiałach naukowych lepiej podać opis.


### 15.6. Błędy ścieżek

- Sprawdź wielkość liter w nazwie pliku.
- Sprawdź rozszerzenie: `.jpg`, `.jpeg`, `.png`, `.webp`.
- Jeśli używasz `/img/plik.png`, plik powinien być w `public/img/plik.png`.
- Jeśli importujesz z `src`, ścieżka jest względna do pliku komponentu.
- Nie używaj ścieżek z dysku typu `C:\Users\...` w `src` obrazka.


## 16. Wzorce formularzy w małych aplikacjach


### 16.1. Rejestracja

```jsx
function Rejestracja() {
  const [email, setEmail] = useState("");
  const [haslo, setHaslo] = useState("");
  const [powtorz, setPowtorz] = useState("");
  const [komunikat, setKomunikat] = useState("");

  function zatwierdz(event) {
    event.preventDefault();

    if (!email.includes("@")) {
      setKomunikat("Nieprawidłowy adres e-mail");
    } else if (haslo !== powtorz) {
      setKomunikat("Hasła nie są zgodne");
    } else {
      setKomunikat("Witaj " + email);
    }
  }

  return (
    <form onSubmit={zatwierdz} className="container mt-4">
      <h2>Rejestruj konto</h2>
      <input className="form-control mb-2" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input className="form-control mb-2" type="password" value={haslo} onChange={(e) => setHaslo(e.target.value)} />
      <input className="form-control mb-2" type="password" value={powtorz} onChange={(e) => setPowtorz(e.target.value)} />
      <button className="btn btn-primary">ZATWIERDŹ</button>
      <p className="mt-3">{komunikat}</p>
    </form>
  );
}
```


### 16.2. Zapisy na kurs

Ten wzorzec łączy tablicę danych, listę numerowaną, formularz, walidację numeru i wypisanie wyniku.
Numer wpisany przez użytkownika zwykle jest liczony od 1.
Indeks tablicy jest liczony od 0.
Dlatego element tablicy to `kursy[numer - 1]`.


### 16.3. Formularz filmu

```jsx
function FormularzFilmu() {
  const [tytul, setTytul] = useState("");
  const [rodzaj, setRodzaj] = useState("Komedia");

  function dodaj(event) {
    event.preventDefault();
    console.log(`tytul: ${tytul}; rodzaj: ${rodzaj}`);
  }

  return (
    <form onSubmit={dodaj}>
      <label htmlFor="tytul" className="form-label">Tytuł filmu</label>
      <input id="tytul" className="form-control" value={tytul} onChange={(e) => setTytul(e.target.value)} />
      <label htmlFor="rodzaj" className="form-label mt-3">Rodzaj</label>
      <select id="rodzaj" className="form-select" value={rodzaj} onChange={(e) => setRodzaj(e.target.value)}>
        <option>Komedia</option>
        <option>Obyczajowy</option>
        <option>Sensacyjny</option>
        <option>Horror</option>
      </select>
      <button className="btn btn-primary mt-3">Dodaj</button>
    </form>
  );
}
```


### 16.4. Formularz z podsumowaniem

```jsx
function PodsumowanieWizyty() {
  const [wlasciciel, setWlasciciel] = useState("");
  const [gatunek, setGatunek] = useState("Pies");
  const [wiek, setWiek] = useState(1);
  const [cel, setCel] = useState("");
  const [czas, setCzas] = useState("12:00");
  const [wynik, setWynik] = useState("");

  function zatwierdz() {
    setWynik(`${wlasciciel}, ${gatunek}, ${wiek}, ${cel}, ${czas}`);
  }
}
```


### 16.5. Kod pocztowy

```js
function sprawdzKod(kod) {
  if (kod.length !== 5) {
    return "Nieprawidłowa liczba cyfr w kodzie pocztowym";
  }

  if (!/^\d+$/.test(kod)) {
    return "Kod pocztowy powinien składać się z samych cyfr";
  }

  return "Dane przesyłki zostały wprowadzone";
}
```


### 16.6. Zakres liczby

```js
function programPrania(value) {
  const numer = Number(value);

  if (!Number.isInteger(numer) || numer < 1 || numer > 12) {
    return "Numer programu musi być od 1 do 12";
  }

  return `Numer prania: ${numer}`;
}
```


## 17. Wzorce aplikacji listowych i widoków kart


### 17.1. Lista notatek

```jsx
function Notatki() {
  const [notatki, setNotatki] = useState(["Zakupy", "Spacer", "Nauka"]);
  const [nowa, setNowa] = useState("");

  function dodaj(event) {
    event.preventDefault();
    if (nowa.trim() === "") return;
    setNotatki((prev) => [...prev, nowa.trim()]);
    setNowa("");
  }

  return (
    <section>
      <form onSubmit={dodaj} className="d-flex gap-2 mb-3">
        <input className="form-control" value={nowa} onChange={(e) => setNowa(e.target.value)} />
        <button className="btn btn-primary">DODAJ</button>
      </form>
      <ul className="list-group">
        {notatki.map((notatka, index) => (
          <li className="list-group-item" key={index}>{notatka}</li>
        ))}
      </ul>
    </section>
  );
}
```


### 17.2. Widok kart z kategoriami

Widok kart z kategoriami jest jednym z najważniejszych wzorców.
Wymaga tablicy obiektów, checkboxów, filtrowania i aktualizacji licznika jednego elementu.
To naturalne połączenie `useState`, `filter`, `map` i Bootstrapa.


### 17.3. Licznik pobrań

```jsx
function pobierz(id) {
  setPhotos((prev) =>
    prev.map((photo) =>
      photo.id === id
        ? { ...photo, downloads: photo.downloads + 1 }
        : photo
    )
  );
}
```


### 17.4. Filtrowanie checkboxami

```js
const widoczne = zdjecia.filter((zdjecie) => {
  if (zdjecie.kategoria === "kwiaty") return pokazKwiaty;
  if (zdjecie.kategoria === "zwierzeta") return pokazZwierzeta;
  if (zdjecie.kategoria === "samochody") return pokazSamochody;
  return true;
});
```


### 17.5. Paginacja

```jsx
const [index, setIndex] = useState(0);
const aktualny = albumy[index];

function nastepny() {
  setIndex((prev) => (prev + 1) % albumy.length);
}

function poprzedni() {
  setIndex((prev) => (prev - 1 + albumy.length) % albumy.length);
}
```

Paginacja cykliczna przydaje się w przeglądarkach ofert, albumów i zdjęć.
Wzór z modulo pozwala zawinąć indeks na końcu i początku tablicy.


## 18. Wzorce suwaków, kolorów i dynamicznego UI


### 18.1. Suwak rozmiaru

```jsx
function SuwakCzcionki() {
  const [rozmiar, setRozmiar] = useState(24);

  return (
    <section>
      <label htmlFor="rozmiar" className="form-label">
        Rozmiar: {rozmiar}
      </label>
      <input
        id="rozmiar"
        type="range"
        min="10"
        max="60"
        value={rozmiar}
        onChange={(e) => setRozmiar(Number(e.target.value))}
        className="form-range"
      />
      <p style={{ fontSize: rozmiar }}>Dzień dobry</p>
    </section>
  );
}
```


### 18.2. RGB

```js
function toHex(value) {
  return value.toString(16).padStart(2, "0").toUpperCase();
}

function rgbToHex(r, g, b) {
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}
```


### 18.3. Opacity

```jsx
<img
  src={src}
  alt="Kość"
  style={{ opacity: dostepna ? 1 : 0.5 }}
  onClick={przelaczDostepnosc}
/>;
```


### 18.4. Dynamiczna klasa

```jsx
<button className={aktywny ? "btn btn-success" : "btn btn-outline-secondary"}>
  {aktywny ? "Aktywny" : "Nieaktywny"}
</button>
```


### 18.5. Podgląd na żywo

Podgląd na żywo oznacza, że UI zmienia się już podczas przesuwania suwaka albo pisania w polu.
W React jest to naturalne: zmiana pola aktualizuje stan, a stan aktualizuje widok.
Dobre przykłady to rozmiar czcionki, kolor RGB, licznik znaków i podgląd generowanego tekstu.


## 19. Logika aplikacji poza JSX


### 19.1. Funkcje pomocnicze

Kod w JSX powinien być czytelny.
Jeśli warunek albo obliczenie jest dłuższe, wynieś je do funkcji.
Funkcję czystą łatwiej przetestować i wykorzystać ponownie.

```js
export function caesar(text, shift) {
  return text
    .split("")
    .map((char) => shiftChar(char, shift))
    .join("");
}
```


### 19.2. Moduły

```text
src/
  utils/
    password.js
    caesar.js
    dice.js
```

```js
import { generatePassword } from "./utils/password";
```


### 19.3. Klasy

React nie wymaga klas do komponentów, ale klasy mogą być częścią logiki domenowej.
Jeżeli aplikacja ma obiekty typu urządzenie, album albo kość, możesz zapisać je jako zwykłe obiekty albo klasy.
W prostych aplikacjach tablica obiektów zwykle wystarcza.

```js
class Dice {
  constructor(value = 1, locked = false) {
    this.value = value;
    this.locked = locked;
  }
}
```


### 19.4. Testowanie logiki ręcznie

```js
console.log(sprawdzKod("12345"));
console.log(sprawdzKod("12A45"));
console.log(rgbToHex(205, 133, 63));
```


### 19.5. Oddzielenie UI od obliczeń

| Warstwa | Przykład | Dlaczego |
| --- | --- | --- |
| UI | formularz, przyciski, obrazy | kontakt z użytkownikiem |
| Stan | `useState` | pamięć komponentu |
| Logika | `caesar`, `rgbToHex`, `rollDice` | obliczenia niezależne od widoku |
| Dane | tablice obiektów | źródło renderowania |


## 20. useEffect i efekty uboczne


### 20.1. Po co jest useEffect

`useEffect` służy do efektów ubocznych.
Efektem ubocznym jest na przykład pobranie danych, zapis do `localStorage`, ustawienie tytułu strony albo subskrypcja zdarzenia.
Nie używaj `useEffect` do wszystkiego.
Do obliczeń wynikających bezpośrednio ze stanu często wystarczy zwykła zmienna przed `return`.

```jsx
import { useEffect, useState } from "react";

function App() {
  const [licznik, setLicznik] = useState(0);

  useEffect(() => {
    document.title = `Licznik: ${licznik}`;
  }, [licznik]);
}
```


### 20.2. Start aplikacji

```jsx
useEffect(() => {
  console.log("Komponent został zamontowany");
}, []);
```

Pusta tablica zależności oznacza uruchomienie efektu po pierwszym renderze.
To przydaje się do pobrania danych startowych.


### 20.3. localStorage

```jsx
const [notatki, setNotatki] = useState(() => {
  const saved = localStorage.getItem("notatki");
  return saved ? JSON.parse(saved) : [];
});

useEffect(() => {
  localStorage.setItem("notatki", JSON.stringify(notatki));
}, [notatki]);
```


### 20.4. fetch

```jsx
useEffect(() => {
  fetch("/data/photos.json")
    .then((response) => response.json())
    .then((data) => setPhotos(data));
}, []);
```


### 20.5. Typowe pułapki

- Nie wywołuj settera stanu bezpośrednio w ciele komponentu bez warunku.
- Nie zapominaj o tablicy zależności, jeśli efekt ma działać tylko raz.
- Nie rób fetchowania w pętli renderowania.
- Nie zapisuj do localStorage obiektów bez `JSON.stringify`.
- Nie czytaj z localStorage bez obsługi braku danych.


## 21. Dane lokalne, JSON i pliki tekstowe


### 21.1. Tablice w kodzie

```js
export const courses = [
  "Programowanie w C#",
  "Angular dla początkujących",
  "Kurs Django",
  "React od podstaw"
];
```


### 21.2. import JSON

```json
[
  { "id": 1, "title": "Kwiat", "category": "kwiaty", "downloads": 0 },
  { "id": 2, "title": "Kot", "category": "zwierzeta", "downloads": 2 }
]
```

```jsx
import initialPhotos from "./data/photos.json";

const [photos, setPhotos] = useState(initialPhotos);
```


### 21.3. fetch z public

```text
public/
  data/
    photos.json
```

```jsx
useEffect(() => {
  fetch("/data/photos.json")
    .then((res) => res.json())
    .then(setPhotos);
}, []);
```


### 21.4. Parsowanie tekstu

```js
function parseLines(text) {
  return text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
}
```


### 21.5. Kiedy nie komplikować

- Jeżeli projekt wymaga tylko przepisania danych z pliku do aplikacji, tablica w kodzie jest wystarczająca.
- Jeżeli projekt ma naprawdę odczytywać plik, użyj `fetch` z folderu `public`.
- Jeżeli nie ma backendu, nie twórz go tylko po to, żeby wczytać kilka rekordów.
- Jeżeli dane nie zmieniają się po stronie serwera, lokalny JSON jest prosty i czytelny.


## 22. Proste algorytmy w React


### 22.1. Losowanie

```js
function losujOdDo(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```


### 22.2. Generator hasła

```js
function generatePassword(length, useUpper, useDigits, useSpecial) {
  let chars = "abcdefghijklmnopqrstuvwxyz";
  if (useUpper) chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (useDigits) chars += "0123456789";
  if (useSpecial) chars += "!@#$%^&*";

  let password = "";
  for (let i = 0; i < length; i++) {
    const index = Math.floor(Math.random() * chars.length);
    password += chars[index];
  }

  return password;
}
```


### 22.3. Szyfr Cezara

```js
function caesar(text, shift) {
  const normalizedShift = ((shift % 26) + 26) % 26;

  return text.replace(/[a-z]/gi, (char) => {
    const base = char >= "a" && char <= "z" ? 97 : 65;
    const code = char.charCodeAt(0) - base;
    return String.fromCharCode(((code + normalizedShift) % 26) + base);
  });
}
```


### 22.4. Kości

```js
function rollDice(count = 5) {
  return Array.from({ length: count }, () => losujOdDo(1, 6));
}

function sumDice(values) {
  return values.reduce((sum, value) => sum + value, 0);
}
```


### 22.5. Sumowanie i zliczanie

```js
const sumaPobran = photos.reduce((sum, photo) => sum + photo.downloads, 0);
const liczbaKwiatow = photos.filter((photo) => photo.category === "kwiaty").length;
```


## 23. Projekt przykładowy: kursy


### 23.1. Cel

Ten projekt pokazuje podstawowy zestaw: tablica, lista numerowana, formularz, walidacja numeru i `console.log`.
Jest to jeden z najważniejszych wzorców dla prostych aplikacji React.


### 23.2. Kod

```jsx
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const courses = [
  "Programowanie w C#",
  "Angular dla początkujących",
  "Kurs Django",
  "React od podstaw"
];

function App() {
  const [name, setName] = useState("");
  const [courseNumber, setCourseNumber] = useState("");
  const [message, setMessage] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    const number = Number(courseNumber);
    const course = courses[number - 1];

    console.log(name);

    if (course) {
      console.log(course);
      setMessage(`Zapisano: ${name} - ${course}`);
    } else {
      console.log("Nieprawidłowy numer kursu");
      setMessage("Nieprawidłowy numer kursu");
    }
  }

  return (
    <main className="container mt-4">
      <h1>Zapisy na kursy</h1>
      <h2>Liczba kursów: {courses.length}</h2>

      <ol>
        {courses.map((course) => (
          <li key={course}>{course}</li>
        ))}
      </ol>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Imię i nazwisko:</label>
          <input id="name" className="form-control" value={name} onChange={(e) => setName(e.target.value)} />
        </div>

        <div className="mb-3">
          <label htmlFor="courseNumber" className="form-label">Numer kursu:</label>
          <input id="courseNumber" type="number" className="form-control" value={courseNumber} onChange={(e) => setCourseNumber(e.target.value)} />
        </div>

        <button className="btn btn-primary">Zapisz do kursu</button>
      </form>

      {message && <p className="mt-3">{message}</p>}
    </main>
  );
}

export default App;
```


### 23.3. Omówienie

- `courses` jest tablicą stałą, bo użytkownik jej nie modyfikuje.
- `name` i `courseNumber` są stanem, bo pochodzą z pól formularza.
- `courseNumber` jest tekstem, więc przed użyciem zamieniamy go na liczbę.
- `courses[number - 1]` uwzględnia różnicę między numeracją użytkownika i indeksem tablicy.
- `event.preventDefault()` blokuje przeładowanie strony.


### 23.4. Rozszerzenia

- Dodaj walidację pustego imienia i nazwiska.
- Dodaj listę zapisanych osób w stanie.
- Dodaj przycisk resetujący formularz.
- Dodaj alert Bootstrap dla błędnego numeru.


## 24. Projekt przykładowy: widok kart


### 24.1. Cel

Widok kart pokazuje bardziej złożony, ale bardzo praktyczny wzorzec.
Używa listy obiektów, switchy kategorii, filtrowania i aktualizacji jednego elementu.


### 24.2. Kod

```jsx
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const initialPhotos = [
  { id: 1, title: "Kwiat", category: "kwiaty", file: "/img/kwiat.jpg", downloads: 0 },
  { id: 2, title: "Kot", category: "zwierzeta", file: "/img/kot.jpg", downloads: 2 },
  { id: 3, title: "Samochód", category: "samochody", file: "/img/auto.jpg", downloads: 1 }
];

function App() {
  const [photos, setPhotos] = useState(initialPhotos);
  const [showFlowers, setShowFlowers] = useState(true);
  const [showAnimals, setShowAnimals] = useState(true);
  const [showCars, setShowCars] = useState(true);

  const visiblePhotos = photos.filter((photo) => {
    if (photo.category === "kwiaty") return showFlowers;
    if (photo.category === "zwierzeta") return showAnimals;
    if (photo.category === "samochody") return showCars;
    return true;
  });

  function downloadPhoto(id) {
    setPhotos((prev) =>
      prev.map((photo) =>
        photo.id === id
          ? { ...photo, downloads: photo.downloads + 1 }
          : photo
      )
    );
  }

  return (
    <main className="container mt-4">
      <h1>Kolekcja zdjęć</h1>

      <div className="d-flex gap-4 my-3">
        <Switch id="flowers" label="Kwiaty" checked={showFlowers} onChange={setShowFlowers} />
        <Switch id="animals" label="Zwierzęta" checked={showAnimals} onChange={setShowAnimals} />
        <Switch id="cars" label="Samochody" checked={showCars} onChange={setShowCars} />
      </div>

      <div className="row g-3">
        {visiblePhotos.map((photo) => (
          <div className="col-12 col-md-6 col-lg-4" key={photo.id}>
            <div className="card h-100">
              <img src={photo.file} className="card-img-top" alt={photo.title} />
              <div className="card-body">
                <h5 className="card-title">{photo.title}</h5>
                <p className="card-text">Pobrania: {photo.downloads}</p>
                <button className="btn btn-primary" onClick={() => downloadPhoto(photo.id)}>
                  Pobierz
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}

function Switch({ id, label, checked, onChange }) {
  return (
    <div className="form-check form-switch">
      <input
        id={id}
        className="form-check-input"
        type="checkbox"
        role="switch"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
      />
      <label className="form-check-label" htmlFor={id}>{label}</label>
    </div>
  );
}

export default App;
```


### 24.3. Omówienie

- `photos` musi być w stanie, bo liczba pobrań się zmienia.
- Switche kategorii są osobnymi stanami boolean.
- `visiblePhotos` jest obliczane z aktualnego stanu i nie musi być osobnym stanem.
- Przycisk `Pobierz` przekazuje `photo.id` do funkcji aktualizującej.
- Aktualizacja odbywa się przez `map` i spread obiektu.


### 24.4. Uwagi do implementacji

- Brak `key` w `map()`.
- Użycie `class` zamiast `className`.
- Użycie `checked` bez `onChange`.
- Modyfikowanie `photo.downloads++` zamiast utworzenia nowego obiektu.
- Błędna ścieżka do obrazka.


## 25. Projekt przykładowy: RGB


### 25.1. Cel

Projekt RGB pokazuje trzy suwaki, dynamiczny styl, konwersję liczby na kolor i rozdzielenie stanu bieżącego od zapisanego.


### 25.2. Kod

```jsx
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function toHex(value) {
  return value.toString(16).padStart(2, "0").toUpperCase();
}

function rgbToHex(r, g, b) {
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function App() {
  const [r, setR] = useState(205);
  const [g, setG] = useState(133);
  const [b, setB] = useState(63);
  const [saved, setSaved] = useState({ r: 0, g: 0, b: 0 });

  const currentColor = rgbToHex(r, g, b);
  const savedColor = rgbToHex(saved.r, saved.g, saved.b);

  return (
    <main className="container mt-4">
      <h1>Wzornik kolorów RGB</h1>
      <ColorSlider label="R" value={r} onChange={setR} />
      <ColorSlider label="G" value={g} onChange={setG} />
      <ColorSlider label="B" value={b} onChange={setB} />

      <div className="border my-3" style={{ height: 120, backgroundColor: currentColor }} />
      <p>Aktualny kolor: {currentColor}</p>

      <button className="btn btn-primary" onClick={() => setSaved({ r, g, b })}>
        Pobierz
      </button>

      <div className="border mt-3 p-3" style={{ backgroundColor: savedColor }}>
        Zapisany kolor: {savedColor}
      </div>
    </main>
  );
}

function ColorSlider({ label, value, onChange }) {
  return (
    <div className="mb-3">
      <label className="form-label">{label}: {value}</label>
      <input
        type="range"
        min="0"
        max="255"
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        className="form-range"
      />
    </div>
  );
}

export default App;
```


### 25.3. Omówienie

- Trzy suwaki przechowują wartości `r`, `g`, `b`.
- `currentColor` jest obliczany przy każdym renderze.
- Przycisk `Pobierz` zapisuje osobny obiekt z aktualnym kolorem.
- Bieżący podgląd zmienia się od razu.
- Zapisany podgląd zmienia się dopiero po kliknięciu.


### 25.4. Rozszerzenia

- Dodaj pola numeryczne obok suwaków.
- Dodaj walidację zakresu 0-255.
- Dodaj listę ostatnio zapisanych kolorów.
- Dodaj przycisk kopiowania wartości HEX.


## 26. Organizacja projektu


### 26.1. Nazewnictwo

- Komponenty nazywaj wielką literą: `CourseForm`, `PhotoCard`, `RgbPicker`.
- Zmienne stanu nazywaj rzeczowo: `email`, `photos`, `selectedCategory`.
- Settery stanu nazywaj z prefiksem `set`: `setEmail`, `setPhotos`.
- Funkcje obsługi zdarzeń mogą mieć prefix `handle`: `handleSubmit`, `handleClick`.
- Funkcje domenowe nazywaj od działania: `validateEmail`, `rollDice`, `rgbToHex`.


### 26.2. Folder components

```text
src/components/
  CourseForm.js
  CourseList.js
  PhotoCard.js
  CategorySwitch.js
```


### 26.3. Folder data

```text
src/data/
  courses.js
  photos.js
  movies.js
```

```js
export const movieTypes = ["Komedia", "Obyczajowy", "Sensacyjny", "Horror"];
```


### 26.4. Folder utils

```text
src/utils/
  validation.js
  rgb.js
  dice.js
  caesar.js
```


### 26.5. Kiedy dzielić komponent

| Sytuacja | Decyzja |
| --- | --- |
| Plik ma mniej niż 100-150 linii | może zostać w `App.js` |
| Powtarzasz ten sam blok wiele razy | wydziel komponent |
| Masz kartę z obrazem | wydziel `PhotoCard` |
| Masz jeden mały formularz | może zostać w `App.js` |
| Masz osobną logikę algorytmiczną | wydziel do `utils` |


## 27. Debugowanie


### 27.1. Konsola

```js
console.log("name:", name);
console.log("courseNumber:", courseNumber);
console.log("photos:", photos);
```

Konsola przeglądarki jest podstawowym narzędziem debugowania.
W materiałach edukacyjnych czasem wynik jest wypisywany właśnie w konsoli.
Nie zostawiaj jednak przypadkowych logów w większych projektach produkcyjnych.


### 27.2. React DevTools

React DevTools pozwala podejrzeć komponenty, propsy i stan.
To bardzo pomaga przy problemach z formularzem i listą.


### 27.3. Błędy składni

- Sprawdź zamknięcie nawiasów `()`, `{}` i `<>`.
- Sprawdź, czy JSX ma jeden główny element.
- Sprawdź, czy `return` obejmuje cały JSX.
- Sprawdź, czy używasz `className` zamiast `class`.
- Sprawdź, czy importujesz `useState`.


### 27.4. Błędy stanu

- Nie modyfikuj tablicy bezpośrednio przez `push`.
- Nie modyfikuj obiektu bezpośrednio przez zmianę pola.
- Nie oczekuj, że `setState` natychmiast zmieni wartość w tej samej linii.
- Jeżeli nowy stan zależy od starego, użyj funkcji w setterze.


### 27.5. Błędy formularzy

- Dla `input` tekstowego używaj `value` i `onChange`.
- Dla checkboxa używaj `checked` i `onChange`.
- Dla formularza używaj `onSubmit` i `event.preventDefault()`.
- Dla pól liczbowych pamiętaj, że wartość z inputa jest tekstem.
- Dla `select` ustaw stan początkowy zgodny z jedną z opcji.


## 28. Testowanie i sprawdzanie działania


### 28.1. Test ręczny

W prostych aplikacjach najważniejszy jest dobry test ręczny.
Uruchom aplikację, przejdź wszystkie scenariusze i sprawdź konsolę.
Nie testuj tylko szczęśliwej ścieżki.


### 28.2. Scenariusze

| Funkcja | Scenariusze do sprawdzenia |
| --- | --- |
| formularz email | brak `@`, zgodne hasła, różne hasła |
| numer kursu | poprawny numer, 0, za duży numer, tekst |
| widok kart | każda kombinacja switchy, kliknięcie pobrania |
| lista | dodanie tekstu, próba dodania pustego tekstu |
| suwak | minimum, maksimum, środek |
| obrazy | stan startowy, zmiana po kliknięciu, reset |


### 28.3. npm test

CRA tworzy konfigurację testów, ale w prostych projektach zwykle wystarczy test ręczny.
Jeżeli piszesz funkcje pomocnicze, możesz dodać testy jednostkowe.

```bash
npm test
```


### 28.4. Checklisty

- Aplikacja uruchamia się bez błędów w terminalu.
- Konsola przeglądarki nie pokazuje błędów Reacta.
- Każdy input ma kontrolowany stan.
- Każda lista renderowana przez `map()` ma `key`.
- W formularzu jest `preventDefault()`.
- Bootstrap jest zaimportowany.
- Obrazy mają poprawne ścieżki i atrybuty `alt`.
- Walidacje pokazują właściwe komunikaty.
- Przyciski zmieniają stan zgodnie z oczekiwanym działaniem interfejsu.


## 29. Build i publikacja projektu


### 29.1. npm run build

```bash
npm run build
```

Build tworzy zoptymalizowany folder `build`.
Jeżeli build przechodzi bez błędów, projekt ma większą szansę działać poprawnie po oddaniu.
Błędy builda często ujawniają literówki w importach i nieużywane zmienne traktowane przez konfigurację jako problem.


### 29.2. Co zawiera projekt

- Kod źródłowy projektu, szczególnie folder `src` i `public`.
- `package.json` oraz `package-lock.json`.
- Nie trzeba zwykle pakować `node_modules`, bo można je odtworzyć przez `npm install`.
- Jeżeli wymagane są zrzuty ekranu, wykonaj je po sprawdzeniu scenariuszy.


### 29.3. Zrzuty ekranu

- Stan początkowy aplikacji.
- Formularz po wpisaniu danych.
- Wynik poprawnej walidacji.
- Wynik błędnej walidacji.
- Widok kart po zmianie filtrów.
- Stan po kliknięciu przycisku licznika.


### 29.4. Typowe problemy

| Problem | Możliwa przyczyna | Naprawa |
| --- | --- | --- |
| biała strona | błąd JS | sprawdź konsolę |
| Bootstrap nie działa | brak importu CSS | dodaj import |
| formularz przeładowuje stronę | brak `preventDefault` | dodaj w `onSubmit` |
| obraz nie działa | zła ścieżka | sprawdź `public` lub import |
| lista nie odświeża się | mutacja tablicy | użyj nowej tablicy |


## 30. Co warto jeszcze dodać do nauki Reacta

Ten rozdział zbiera tematy, których wcześniejsza wersja dokumentacji dotykała za szybko albo wcale.
Nie chodzi o to, żeby uczyć się całego ekosystemu Reacta na poziomie zawodowym.
Chodzi o to, żeby osoba zaczynająca od zera rozumiała, co robi, do którego pliku trafia kod, dlaczego przykład działa i jak przerobić go na podobny komponent.
To jest szczególnie ważne przy małych aplikacjach praktycznych, bo wymagania często dotyczą konkretnego zachowania interfejsu.
Opis funkcji mówi raczej: zrób formularz, policz wynik, zmień obraz, pokaż komunikat, obsłuż przycisk.
React jest wtedy narzędziem do zbudowania tego zachowania.

### 30.1. Lista brakujących tematów

| Temat | Dlaczego warto dodać | Poziom |
| --- | --- | --- |
| `index.html`, `index.js`, `App.js` | początkujący musi wiedzieć, gdzie zaczyna się aplikacja | podstawa |
| `createRoot` i `root.render` | tłumaczy, jak React trafia do strony HTML | podstawa |
| `StrictMode` | wyjaśnia dziwne podwójne uruchomienia w trybie developerskim | podstawa+ |
| render komponentu | bez tego `useState` jest magiczne | podstawa |
| różnica zmienna lokalna vs stan | bardzo częsty błąd przy licznikach | podstawa |
| przepływ danych rodzic -> dziecko | potrzebne przy podziale na komponenty | podstawa |
| callback dziecko -> rodzic | potrzebne przy karcie z przyciskiem | podstawa+ |
| `children` | przydatne do kart, paneli i prostych layoutów | podstawa+ |
| lifting state up | klucz do większych formularzy i list | podstawa+ |
| stan pochodny | zapobiega dublowaniu danych | podstawa+ |
| bardziej praktyczny JavaScript | `trim`, `split`, `join`, `Number`, `some`, `sort` | podstawa |
| formularz jako obiekt | skraca duże formularze | podstawa+ |
| błędy per pole | czytelna walidacja formularza | podstawa+ |
| checkboxy jako lista | kategorie, opcje hasła, filtry | podstawa+ |
| `useRef` | fokus pola, formularz niekontrolowany | dodatek |
| `FormData` | szybki odczyt formularza bez wielu stanów | dodatek |
| `useEffect` dokładniej | dane z pliku, localStorage, tytuł, timer | podstawa+ |
| loading/error/data | praktyczne pobieranie danych | podstawa+ |
| dostępność formularzy | poprawne `label`, `alt`, `button type` | podstawa |
| semantyka HTML | lepszy układ i mniej błędów | podstawa |

### 30.2. Przydatność tematów w małych aplikacjach

Najbardziej przydatne są tematy, które pomagają budować małe aplikacje z jednym ekranem.
Najpierw warto rozbudować fundamenty: projekt, JSX, stan, propsy, formularze, tablice i Bootstrap.
Potem warto dodać tematy półzaawansowane, ale tylko wtedy, gdy dają realną przewagę w prostych projektach.
`useReducer`, `Context` albo React Router są ważne w większych aplikacjach, ale w typowych małych aplikacjach front-endowych zwykle nie są potrzebne.
`useRef`, `useEffect`, `localStorage`, pobieranie JSON i callbacki z komponentów potomnych są dużo bardziej praktyczne.

| Przydatność | Temat | Przykład użycia |
| --- | --- | --- |
| bardzo wysoki | formularze kontrolowane | rejestracja, kurs, film, wizyta |
| bardzo wysoki | tablice obiektów | lista notatek, albumy, katalog elementów |
| bardzo wysoki | aktualizacja jednego elementu | licznik pobrań, polubienia, stan urządzenia |
| wysoki | filtrowanie | kategorie zdjęć, wyszukiwarka, widoczne elementy |
| wysoki | obrazy z `public` | karty, kości, oferta, profil |
| wysoki | Bootstrap | formularze, grid, karty, switche |
| średni | `useEffect` | dane startowe, JSON, localStorage |
| średni | `useRef` | fokus, formularz niekontrolowany |
| średni | lifting state up | komponent karty z przyciskiem |
| niski dla prostych projektów | Router | wiele podstron |
| niski dla prostych projektów | Context | globalny stan aplikacji |

### 30.3. Jak czytać przykłady kodu

W tej dokumentacji przy dłuższych przykładach warto zawsze patrzeć na trzy rzeczy.
Pierwsza rzecz to nazwa pliku.
Jeżeli przykład zaczyna się komentarzem `// src/App.js`, oznacza to, że można wkleić go do pliku `src/App.js`.
Jeżeli przykład zaczyna się od `// src/components/Nazwa.js`, to najpierw trzeba utworzyć folder `components`, potem plik, a potem zaimportować komponent w `App.js`.
Druga rzecz to importy.
Jeżeli kod używa `useState`, musi mieć `import { useState } from "react";`.
Jeżeli kod używa Bootstrapa, najczęściej wystarczy raz zaimportować `import "bootstrap/dist/css/bootstrap.css";`, zwykle w `src/index.js` albo `src/App.js`.
Trzecia rzecz to stan.
Jeżeli coś ma się zmieniać na ekranie po kliknięciu, wpisaniu tekstu albo przesunięciu suwaka, prawdopodobnie powinno być w `useState`.

Przykład czytania kodu:

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Ten stan przechowuje tekst wpisany przez użytkownika.
  // Ponieważ tekst ma być widoczny i aktualny po każdej zmianie pola,
  // zapisujemy go w useState.
  const [name, setName] = useState("");

  return (
    <main className="container mt-4">
      <label htmlFor="name" className="form-label">
        Imię
      </label>

      <input
        id="name"
        className="form-control"
        value={name}
        onChange={(event) => setName(event.target.value)}
      />

      <p className="mt-3">Wpisano: {name}</p>
    </main>
  );
}

export default App;
```

Ten przykład nie jest tylko polem tekstowym.
Pokazuje cały mechanizm Reacta w miniaturze.
Użytkownik wpisuje znak.
Przeglądarka wywołuje `onChange`.
`setName` zmienia stan.
React ponownie renderuje komponent.
Nowa wartość `name` pojawia się w polu oraz w akapicie.


## 31. Jak działa projekt React od wejścia do App.js

Początkujący często zaczyna od edycji `App.js`, ale nie wie, dlaczego ten plik w ogóle działa.
To jest jak wejście do budynku bocznymi drzwiami: można pracować, ale łatwo się zgubić.
W Create React App najważniejsze są trzy miejsca: `public/index.html`, `src/index.js` i `src/App.js`.
Pierwszy plik daje pusty punkt zaczepienia w HTML.
Drugi plik uruchamia Reacta.
Trzeci plik zawiera główny komponent aplikacji.

### 31.1. public/index.html

Plik `public/index.html` jest zwykłym plikiem HTML.
Nie pisze się w nim całego interfejsu aplikacji.
Najważniejszy jest element z identyfikatorem `root`.
React znajdzie ten element i wstawi do niego całą aplikację.

```html
<!-- public/index.html -->
<!doctype html>
<html lang="pl">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Aplikacja React</title>
  </head>
  <body>
    <noscript>Do działania aplikacji potrzebny jest JavaScript.</noscript>
    <div id="root"></div>
  </body>
</html>
```

W prostych projektach zwykle nie trzeba mocno edytować tego pliku.
Możesz zmienić `title`, język dokumentu albo dodać ikonę.
Nie dodawaj tu formularzy, przycisków i widoków kart.
Interfejs aplikacji buduj w komponentach Reacta, najczęściej od `src/App.js`.

### 31.2. src/index.js

Plik `src/index.js` jest punktem startowym JavaScriptu.
To tutaj React łączy komponent `App` z elementem `div#root`.
W nowoczesnym React używa się `createRoot`.

```jsx
// src/index.js
import React from "react";
import ReactDOM from "react-dom/client";
import "bootstrap/dist/css/bootstrap.css";
import "./index.css";
import App from "./App";

const rootElement = document.getElementById("root");
const root = ReactDOM.createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

Komentarz do kodu:

- `document.getElementById("root")` znajduje element z `public/index.html`.
- `ReactDOM.createRoot(...)` tworzy miejsce, w którym React będzie renderował aplikację.
- `<App />` to główny komponent.
- `root.render(...)` mówi: wyrenderuj komponent `App` w elemencie `root`.
- Import Bootstrapa w `index.js` działa globalnie dla całej aplikacji.

Jeżeli aplikacja ma jeden główny komponent, zwykle nie musisz ruszać `index.js`.
Wystarczy, że Bootstrap jest zaimportowany i `App` jest renderowany.

### 31.3. src/App.js

`src/App.js` to główne miejsce pracy w prostych projektach.
Tutaj możesz zbudować formularz, widok kart, suwak RGB, licznik lub prostą grę.
Na początku warto mieć bardzo prosty plik.

```jsx
// src/App.js
function App() {
  return (
    <main className="container mt-4">
      <h1>Moja aplikacja</h1>
      <p>Tu pojawi się właściwy interfejs.</p>
    </main>
  );
}

export default App;
```

Ważne są dwie rzeczy.
Po pierwsze, komponent `App` musi coś zwracać.
Po drugie, `export default App` pozwala zaimportować ten komponent w `index.js`.
Jeżeli usuniesz eksport, aplikacja nie będzie mogła znaleźć komponentu.

### 31.4. StrictMode

`React.StrictMode` jest narzędziem developerskim.
Pomaga wykrywać niebezpieczne wzorce.
W trybie developerskim może powodować, że niektóre funkcje uruchamiają się dwa razy.
To potrafi zaskoczyć, zwłaszcza przy `useEffect` albo `console.log`.
Nie oznacza to, że aplikacja w produkcji będzie robiła wszystko podwójnie.
To jest kontrolne zachowanie podczas pracy.

Jeżeli widzisz dwa logi w konsoli, najpierw sprawdź, czy aplikacja jest owinięta w `<React.StrictMode>`.
Nie usuwaj go od razu.
Lepiej zrozumieć, czy kod jest odporny na ponowne uruchomienie.
W małych projektach zwykle nie ma to dużego znaczenia, ale warto wiedzieć, skąd bierze się takie zachowanie.

### 31.5. Typowa kolejność pracy

Przy prostej aplikacji Reactowej możesz pracować według takiego schematu:

1. Utwórz projekt.
2. Zaimportuj Bootstrap w `src/index.js` albo `src/App.js`.
3. Wyczyść startową zawartość `App.js`.
4. Zbuduj statyczny widok bez logiki.
5. Dodaj `useState` dla danych, które mają się zmieniać.
6. Podłącz `onChange`, `onClick`, `onSubmit`.
7. Dodaj walidację.
8. Dodaj renderowanie list przez `map`.
9. Dodaj style Bootstrap i ewentualnie własny CSS.
10. Sprawdź scenariusze ręcznie.

Ten porządek jest ważny.
Jeżeli od razu zaczniesz pisać logikę bez widoku, możesz nie wiedzieć, jakie dane są potrzebne.
Jeżeli od razu zaczniesz dzielić wszystko na komponenty, możesz zrobić z prostego projektu mały labirynt.
Najpierw działający widok, potem stan, potem porządkowanie.


## 32. Renderowanie, stan i przepływ danych

React renderuje komponent, czyli wykonuje funkcję komponentu i sprawdza, jaki JSX ma pojawić się na ekranie.
Render nie jest tym samym co pełne odświeżenie strony.
To React decyduje, które elementy DOM trzeba faktycznie zmienić.
Dla osoby uczącej się najważniejsze jest to: komponent renderuje się ponownie, gdy zmieni się jego stan albo propsy.

### 32.1. Render komponentu

Spójrz na ten przykład.
Kod możesz wkleić do `src/App.js`.

```jsx
// src/App.js
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  console.log("Render komponentu App. Aktualny count:", count);

  return (
    <main className="container mt-4">
      <h1>Licznik</h1>
      <p>Wartość: {count}</p>
      <button className="btn btn-primary" onClick={() => setCount(count + 1)}>
        Dodaj
      </button>
    </main>
  );
}

export default App;
```

Po każdym kliknięciu przycisku zmienia się stan `count`.
React ponownie wykonuje funkcję `App`.
Dlatego `console.log` uruchomi się ponownie.
Nowy JSX zawiera nową wartość licznika.
React aktualizuje tekst na stronie.

Wniosek praktyczny: nie wkładaj do ciała komponentu operacji, które mają wykonać się tylko raz, np. zapisu do pliku, pobierania danych albo losowania startowych danych bez kontroli.
Kod w ciele komponentu może wykonać się wiele razy.

### 32.2. Zmienna lokalna kontra stan

To jest jeden z najczęstszych błędów początkujących.
Zwykła zmienna zmienia się w kodzie, ale React nie wie, że ma odświeżyć widok.

```jsx
// Przykład błędny: nie używać jako wzorca
function App() {
  let count = 0;

  function add() {
    count = count + 1;
    console.log(count);
  }

  return (
    <main>
      <p>{count}</p>
      <button onClick={add}>Dodaj</button>
    </main>
  );
}
```

W konsoli możesz zobaczyć zmianę, ale widok nie zadziała tak, jak oczekujesz.
React nie renderuje komponentu ponownie po zmianie zwykłej zmiennej.
Poprawny wzorzec używa `useState`.

```jsx
// src/App.js
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  function add() {
    setCount((previous) => previous + 1);
  }

  return (
    <main className="container mt-4">
      <p>Wartość: {count}</p>
      <button className="btn btn-primary" onClick={add}>
        Dodaj
      </button>
    </main>
  );
}

export default App;
```

Zasada do zapamiętania: jeżeli zmiana wartości ma być widoczna na ekranie, użyj stanu.
Jeżeli wartość jest tylko chwilową zmienną pomocniczą wewnątrz funkcji, zwykła zmienna wystarczy.

### 32.3. Dane płyną z góry na dół

W React rodzic przekazuje dane dziecku przez propsy.
Dziecko nie powinno samodzielnie sięgać do zmiennych rodzica.
Jeżeli dziecko ma zgłosić akcję, rodzic przekazuje mu funkcję.
To jest podstawa listy notatek i każdego widoku z kartami.

```jsx
// src/App.js
import { useState } from "react";

function App() {
  const [downloads, setDownloads] = useState(0);

  function handleDownload() {
    setDownloads((previous) => previous + 1);
  }

  return (
    <main className="container mt-4">
      <PhotoCard
        title="Kwiat"
        image="/img/kwiat.jpg"
        downloads={downloads}
        onDownload={handleDownload}
      />
    </main>
  );
}

function PhotoCard({ title, image, downloads, onDownload }) {
  return (
    <article className="card" style={{ maxWidth: 320 }}>
      <img src={image} className="card-img-top" alt={title} />
      <div className="card-body">
        <h2 className="h5">{title}</h2>
        <p>Pobrania: {downloads}</p>
        <button className="btn btn-primary" onClick={onDownload}>
          Pobierz
        </button>
      </div>
    </article>
  );
}

export default App;
```

`App` trzyma stan, bo `App` decyduje o danych.
`PhotoCard` tylko pokazuje dane i informuje, że kliknięto przycisk.
Ten podział jest bardzo wygodny przy wielu kartach.

### 32.4. Stan pochodny

Stan pochodny to wartość, którą można obliczyć z innego stanu.
Nie trzeba jej osobno zapisywać w `useState`.
Jeżeli masz tablicę zdjęć i checkboxy kategorii, lista widocznych zdjęć może być zwykłą zmienną obliczoną przed `return`.

```jsx
const visiblePhotos = photos.filter((photo) => {
  if (photo.category === "kwiaty") return showFlowers;
  if (photo.category === "zwierzeta") return showAnimals;
  if (photo.category === "samochody") return showCars;
  return true;
});
```

Nie rób tak bez potrzeby:

```jsx
// Zwykle niepotrzebne
const [visiblePhotos, setVisiblePhotos] = useState([]);
```

Jeżeli `visiblePhotos` zależy wyłącznie od `photos`, `showFlowers`, `showAnimals` i `showCars`, można ją obliczyć w renderze.
Dzięki temu nie trzeba pilnować, żeby dwa stany zawsze były zgodne.
Mniej stanu oznacza mniej błędów.


## 33. JavaScript, którego naprawdę potrzebujesz w React

React nie wymaga znajomości całego JavaScriptu naraz.
W praktycznych aplikacjach najczęściej potrzebujesz małego, ale dobrze opanowanego zestawu.
Ten zestaw obejmuje napisy, liczby, tablice, obiekty, funkcje i bezpieczne kopiowanie danych.

### 33.1. Template stringi

Template stringi pomagają składać komunikaty.
Używa się znaku backtick, czyli odwrotnego apostrofu.

```js
const name = "Anna";
const course = "React";
const message = `Użytkownik ${name} zapisany na kurs ${course}`;
```

W React przydaje się to przy komunikatach po formularzu.

```jsx
setMessage(`Zapisano: ${fullName}, kurs: ${selectedCourse}`);
```

Można też budować ścieżki do obrazów.

```jsx
const diceValue = 4;
const imagePath = `/img/kosc${diceValue}.png`;
```

To jest bardzo przydatne przy kościach, kolekcjach obrazów zależnych od numeru albo ikonach urządzeń.

### 33.2. Truthy i falsy

JavaScript w warunkach traktuje niektóre wartości jak fałsz.
Nazywa się je falsy.

| Wartość | Jak zachowuje się w warunku |
| --- | --- |
| `""` | fałsz |
| `0` | fałsz |
| `null` | fałsz |
| `undefined` | fałsz |
| `NaN` | fałsz |
| `"tekst"` | prawda |
| `[]` | prawda |
| `{}` | prawda |

Dlatego taki zapis działa dla komunikatu:

```jsx
{message && <p className="alert alert-info">{message}</p>}
```

Jeżeli `message` jest pustym tekstem, akapit się nie pokaże.
Jeżeli `message` ma treść, akapit się pokaże.
Uważaj jednak na liczbę `0`.

```jsx
// Jeżeli count wynosi 0, React może wyrenderować samo 0.
{count && <p>Licznik istnieje</p>}
```

Bezpieczniej napisać warunek jawnie:

```jsx
{count > 0 && <p>Licznik jest większy od zera</p>}
```

### 33.3. Konwersje liczb

Wartość z pola formularza jest tekstem.
Dotyczy to także `input type="number"`.
Dlatego przy walidacji zakresu trzeba wykonać konwersję.

```js
const valueFromInput = "12";
const number = Number(valueFromInput);
```

Praktyczna funkcja do walidacji liczby całkowitej:

```js
function parseIntegerInRange(value, min, max) {
  const number = Number(value);

  if (!Number.isInteger(number)) {
    return { ok: false, message: "Wpisz liczbę całkowitą" };
  }

  if (number < min || number > max) {
    return { ok: false, message: `Liczba musi być od ${min} do ${max}` };
  }

  return { ok: true, value: number };
}
```

Zastosowanie w komponencie:

```jsx
const result = parseIntegerInRange(program, 1, 12);

if (!result.ok) {
  setError(result.message);
  return;
}

setMessage(`Numer prania: ${result.value}`);
```

Ten wzorzec przydaje się przy numerze kursu, programie prania, wieku zwierzęcia, przesunięciu szyfru Cezara i suwakach.

### 33.4. Metody napisów

| Metoda | Co robi | Przykład zastosowania |
| --- | --- | --- |
| `trim()` | usuwa spacje z początku i końca | sprawdzanie pustego pola |
| `includes()` | sprawdza, czy tekst zawiera fragment | email zawiera `@` |
| `toLowerCase()` | zamienia na małe litery | wyszukiwarka bez znaczenia wielkości liter |
| `split()` | dzieli tekst na tablicę | parsowanie pliku tekstowego |
| `join()` | łączy tablicę w tekst | składanie wyniku |
| `replace()` | zamienia fragment tekstu | proste czyszczenie danych |

Przykład wyszukiwarki:

```jsx
const visibleMovies = movies.filter((movie) =>
  movie.title.toLowerCase().includes(search.trim().toLowerCase())
);
```

To można wykorzystać w liście filmów, albumów, kursów albo notatek.

### 33.5. Bezpieczna praca na tablicach

W React nie mutujemy tablicy w stanie.
Nie chodzi o zakaz dla samego zakazu.
React porównuje referencje i łatwiej rozpoznaje zmianę, gdy tworzysz nową tablicę.

| Cel | Nie rób | Rób |
| --- | --- | --- |
| dodanie | `items.push(item)` | `setItems(prev => [...prev, item])` |
| usunięcie | `items.splice(...)` | `setItems(prev => prev.filter(...))` |
| zmiana | `items[index].done = true` | `setItems(prev => prev.map(...))` |
| sortowanie | `items.sort(...)` na stanie | `[...items].sort(...)` |

Przykład sortowania bez mutowania oryginalnej tablicy:

```jsx
const sortedPhotos = [...photos].sort((a, b) => b.downloads - a.downloads);
```

Przykład zliczania:

```jsx
const totalDownloads = photos.reduce(
  (sum, photo) => sum + photo.downloads,
  0
);
```

Przykład sprawdzenia, czy istnieje błąd:

```jsx
const hasEmptyTitle = movies.some((movie) => movie.title.trim() === "");
```


## 34. JSX dokładniej

JSX jest wygodny, ale ma kilka zasad, które trzeba dobrze zrozumieć.
Nie jest to czysty HTML.
To składnia, która zostanie przetworzona na wywołania JavaScript.
Dlatego część rzeczy wygląda podobnie jak HTML, ale zachowuje się inaczej.

### 34.1. Co można wstawić w klamrach

W JSX klamry `{}` oznaczają: teraz wracamy do JavaScriptu.
Możesz wstawić wartość, działanie matematyczne, wynik funkcji albo operator warunkowy.

```jsx
const name = "Jan";
const downloads = 4;

return (
  <article>
    <h2>{name}</h2>
    <p>Pobrania: {downloads}</p>
    <p>Następna wartość: {downloads + 1}</p>
    <p>{downloads > 0 ? "Już pobrano" : "Brak pobrań"}</p>
  </article>
);
```

Nie wstawiasz tam instrukcji `if` bezpośrednio.
Jeżeli warunek jest dłuższy, przygotuj zmienną przed `return`.

```jsx
let statusClass = "text-muted";

if (downloads > 10) {
  statusClass = "text-success";
}

return <p className={statusClass}>Pobrania: {downloads}</p>;
```

### 34.2. Komentarze w JSX

Komentarz w JSX wygląda inaczej niż w HTML.

```jsx
return (
  <main>
    {/* To jest komentarz wewnątrz JSX */}
    <h1>Aplikacja</h1>
  </main>
);
```

Komentarze warto dodawać oszczędnie.
Dobre komentarze tłumaczą powód, nie opisują oczywistego znacznika.

```jsx
// Dobre: wyjaśnia decyzję.
// Numer kursu w formularzu jest liczony od 1, a indeks tablicy od 0.
const selectedCourse = courses[courseNumber - 1];
```

### 34.3. Atrybuty boolean

W JSX atrybuty takie jak `disabled`, `checked`, `readOnly` i `required` często dostają wartość boolean.

```jsx
<button className="btn btn-primary" disabled={name.trim() === ""}>
  Zapisz
</button>
```

To jest bardzo praktyczne w formularzach.
Możesz zablokować przycisk, dopóki dane są niepoprawne.

```jsx
const isFormInvalid = email.trim() === "" || !email.includes("@");

return (
  <button type="submit" className="btn btn-primary" disabled={isFormInvalid}>
    Zarejestruj
  </button>
);
```

Nie myl `checked` z `value`.
Checkbox kontrolowany wygląda tak:

```jsx
<input
  type="checkbox"
  checked={showAnimals}
  onChange={(event) => setShowAnimals(event.target.checked)}
/>
```

### 34.4. Dynamiczny JSX z map i warunkami

W prawdziwych interfejsach rzadko kończy się na jednym stałym akapicie.
Często trzeba wygenerować listę na podstawie tablicy.

```jsx
const courses = ["HTML", "CSS", "React"];

return (
  <ol>
    {courses.map((course) => (
      <li key={course}>{course}</li>
    ))}
  </ol>
);
```

Jeżeli lista może być pusta, dodaj komunikat.

```jsx
return (
  <section>
    {visiblePhotos.length === 0 ? (
      <p className="alert alert-warning">Brak zdjęć w wybranych kategoriach.</p>
    ) : (
      <div className="row g-3">
        {visiblePhotos.map((photo) => (
          <div className="col-md-4" key={photo.id}>
            <PhotoCard photo={photo} />
          </div>
        ))}
      </div>
    )}
  </section>
);
```

Taki kod łączy trzy umiejętności: warunek, `map` i komponent potomny.
To jest typowy poziom prostego komponentu front-endowego.


## 35. Props, children i lifting state up

Propsy są jednym z najważniejszych tematów po `useState`.
Jeżeli komponent ma być używany więcej niż raz, powinien przyjmować dane przez propsy.
Jeżeli komponent ma być kartą zdjęcia, nie wpisuj w nim na sztywno jednego tytułu i jednego obrazka.
Przekaż tytuł, obraz i licznik jako dane.

### 35.1. Props jako parametry komponentu

Przykład pliku komponentu:

```jsx
// src/components/InfoBox.js
function InfoBox({ title, text, variant = "info" }) {
  return (
    <section className={`alert alert-${variant}`}>
      <h2 className="h5">{title}</h2>
      <p className="mb-0">{text}</p>
    </section>
  );
}

export default InfoBox;
```

Użycie w `App.js`:

```jsx
// src/App.js
import InfoBox from "./components/InfoBox";

function App() {
  return (
    <main className="container mt-4">
      <InfoBox
        title="Wskazówka"
        text="Uzupełnij wszystkie pola formularza."
        variant="warning"
      />
    </main>
  );
}

export default App;
```

`variant = "info"` jest wartością domyślną.
Jeżeli rodzic nie przekaże `variant`, komponent użyje klasy `alert-info`.
To jest wygodne przy powtarzalnych komunikatach.

### 35.2. children

`children` to specjalny prop.
Oznacza zawartość umieszczoną między znacznikiem otwierającym i zamykającym komponentu.
Przydaje się do paneli, kart, sekcji i uniwersalnych ramek.

```jsx
// src/components/Panel.js
function Panel({ title, children }) {
  return (
    <section className="border rounded p-3 mb-3">
      <h2 className="h5">{title}</h2>
      {children}
    </section>
  );
}

export default Panel;
```

Użycie:

```jsx
// src/App.js
import Panel from "./components/Panel";

function App() {
  return (
    <main className="container mt-4">
      <Panel title="Dane użytkownika">
        <label className="form-label" htmlFor="name">Imię</label>
        <input id="name" className="form-control" />
      </Panel>

      <Panel title="Podsumowanie">
        <p>Tu pojawi się wynik po zatwierdzeniu formularza.</p>
      </Panel>
    </main>
  );
}
```

Dzięki `children` komponent `Panel` nie musi wiedzieć, co dokładnie będzie w środku.
To daje elastyczność bez komplikowania kodu.

### 35.3. Callback z dziecka do rodzica

Dziecko nie zmienia stanu rodzica bezpośrednio.
Rodzic przekazuje funkcję, a dziecko wywołuje ją w odpowiednim momencie.
To brzmi abstrakcyjnie, ale w widoku kart jest bardzo naturalne.

```jsx
// src/components/PhotoCard.js
function PhotoCard({ photo, onDownload }) {
  return (
    <article className="card h-100">
      <img src={photo.file} className="card-img-top" alt={photo.title} />
      <div className="card-body">
        <h2 className="h5">{photo.title}</h2>
        <p>Pobrania: {photo.downloads}</p>
        <button
          type="button"
          className="btn btn-primary"
          onClick={() => onDownload(photo.id)}
        >
          Pobierz
        </button>
      </div>
    </article>
  );
}

export default PhotoCard;
```

Rodzic:

```jsx
// src/App.js
import { useState } from "react";
import PhotoCard from "./components/PhotoCard";

const initialPhotos = [
  { id: 1, title: "Kwiat", file: "/img/kwiat.jpg", downloads: 0 },
  { id: 2, title: "Kot", file: "/img/kot.jpg", downloads: 0 }
];

function App() {
  const [photos, setPhotos] = useState(initialPhotos);

  function handleDownload(id) {
    setPhotos((previousPhotos) =>
      previousPhotos.map((photo) =>
        photo.id === id
          ? { ...photo, downloads: photo.downloads + 1 }
          : photo
      )
    );
  }

  return (
    <main className="container mt-4">
      <div className="row g-3">
        {photos.map((photo) => (
          <div className="col-md-4" key={photo.id}>
            <PhotoCard photo={photo} onDownload={handleDownload} />
          </div>
        ))}
      </div>
    </main>
  );
}

export default App;
```

W tym wzorcu `PhotoCard` jest komponentem prezentacyjnym.
Zna wygląd karty.
Nie musi znać sposobu aktualizacji całej tablicy.
`App` trzyma dane i wie, jak je zmienić.

### 35.4. Lifting state up

Lifting state up oznacza przeniesienie stanu do wspólnego rodzica.
Robisz to wtedy, gdy kilka komponentów musi korzystać z tych samych danych.
Przykład: formularz dodaje notatkę, a lista pokazuje notatki.
Stan `notes` nie powinien być tylko w formularzu ani tylko w liście.
Powinien być w rodzicu.

```jsx
// src/App.js
import { useState } from "react";

function App() {
  const [notes, setNotes] = useState(["Pierwsza notatka"]);

  function addNote(text) {
    setNotes((previousNotes) => [...previousNotes, text]);
  }

  return (
    <main className="container mt-4">
      <NoteForm onAddNote={addNote} />
      <NoteList notes={notes} />
    </main>
  );
}

function NoteForm({ onAddNote }) {
  const [text, setText] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    if (text.trim() === "") {
      return;
    }

    onAddNote(text.trim());
    setText("");
  }

  return (
    <form onSubmit={handleSubmit} className="d-flex gap-2 mb-3">
      <input
        className="form-control"
        value={text}
        onChange={(event) => setText(event.target.value)}
      />
      <button className="btn btn-primary">Dodaj</button>
    </form>
  );
}

function NoteList({ notes }) {
  return (
    <ul className="list-group">
      {notes.map((note, index) => (
        <li className="list-group-item" key={`${note}-${index}`}>
          {note}
        </li>
      ))}
    </ul>
  );
}

export default App;
```

To jest bardzo praktyczny wzorzec.
Masz pole tekstowe, przycisk i listę.
Formularz nie musi wiedzieć, jak lista wygląda.
Lista nie musi wiedzieć, skąd biorą się dane.
Rodzic spina całość.


## 36. useState dokładniej

`useState` wygląda prosto, ale wiele błędów bierze się ze złego rozumienia aktualizacji.
Setter stanu nie jest tym samym co zwykłe przypisanie `x = 5`.
Setter prosi Reacta o zaplanowanie nowego renderu z nową wartością.

### 36.1. Aktualizacja nie jest natychmiastowym przypisaniem

Ten przykład często myli początkujących:

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count);
}
```

`console.log(count)` pokaże starą wartość z aktualnego renderu.
Nowa wartość będzie dostępna w następnym renderze.
Jeżeli chcesz zobaczyć zmiany, możesz logować w ciele komponentu albo w `useEffect`.

```jsx
console.log("Aktualny count po renderze:", count);
```

W praktyce nie powinieneś pisać logiki, która zakłada natychmiastową zmianę zmiennej po `setCount`.
Myśl o setterze jak o poleceniu: React, przygotuj nowy render z tą wartością.

### 36.2. Funkcyjna aktualizacja stanu

Jeżeli nowa wartość zależy od poprzedniej, użyj funkcji.

```jsx
setCount((previousCount) => previousCount + 1);
```

To jest bezpieczniejsze przy licznikach i wielu szybkich aktualizacjach.
Przykład z trzema dodaniami:

```jsx
function addThree() {
  setCount((previous) => previous + 1);
  setCount((previous) => previous + 1);
  setCount((previous) => previous + 1);
}
```

Gdyby użyć `setCount(count + 1)` trzy razy, wszystkie trzy wywołania mogłyby bazować na tej samej starej wartości.
Wersja funkcyjna bierze najnowszą wartość z kolejki aktualizacji.

### 36.3. Lazy initial state

Czasem stan początkowy wymaga obliczenia.
Jeżeli obliczenie jest droższe albo czyta z `localStorage`, warto przekazać funkcję do `useState`.
Taka funkcja wykona się tylko przy inicjalizacji stanu.

```jsx
const [notes, setNotes] = useState(() => {
  const saved = localStorage.getItem("notes");
  return saved ? JSON.parse(saved) : [];
});
```

To jest przydatne w aplikacjach, które mają pamiętać dane po odświeżeniu strony.
Nie jest to zawsze wymagane, ale jako wzorzec praktyczny jest bardzo dobry.

### 36.4. Reset większego formularza

Przy kilku polach łatwo zrobić reset przez kilka setterów.
Przy większym formularzu wygodniejszy jest obiekt startowy.

```jsx
const initialForm = {
  fullName: "",
  email: "",
  courseNumber: "",
  acceptRules: false
};

function App() {
  const [form, setForm] = useState(initialForm);

  function resetForm() {
    setForm(initialForm);
  }
}
```

Jeżeli w formularzu masz 8 pól, reset przez jeden obiekt jest czytelniejszy.
W większych formularzach często pojawiają się pola typu: właściciel, gatunek, wiek, cel wizyty, czas, imię, nazwisko, numer, kolor itd.


## 37. Formularze w kilku wariantach

Formularze są jednym z najważniejszych typów interfejsu w prostym React.
Trzeba umieć je zrobić na kilka sposobów.
Nie dlatego, że każdy sposób jest zawsze potrzebny, ale dlatego, że różne wymagania naturalnie pasują do różnych rozwiązań.

### 37.1. Jeden stan na każde pole

To najlepszy sposób na start.
Każde pole ma osobny `useState`.
Kod jest dłuższy, ale bardzo czytelny.

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [message, setMessage] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    if (!email.includes("@")) {
      setMessage("Nieprawidłowy adres email");
      return;
    }

    if (password !== repeatPassword) {
      setMessage("Hasła nie są zgodne");
      return;
    }

    setMessage(`Konto ${email} zostało zarejestrowane`);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: 520 }}>
      <h1>Rejestruj konto</h1>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email</label>
          <input
            id="email"
            className="form-control"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label">Hasło</label>
          <input
            id="password"
            type="password"
            className="form-control"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="repeatPassword" className="form-label">Powtórz hasło</label>
          <input
            id="repeatPassword"
            type="password"
            className="form-control"
            value={repeatPassword}
            onChange={(event) => setRepeatPassword(event.target.value)}
          />
        </div>

        <button className="btn btn-primary">ZATWIERDŹ</button>
      </form>

      {message && <p className="mt-3">{message}</p>}
    </main>
  );
}

export default App;
```

Ten wzorzec jest idealny, gdy pól jest mało.
Łatwo zobaczyć, które pole odpowiada któremu stanowi.
Wadą jest powtarzalność przy dużych formularzach.

### 37.2. Jeden obiekt formularza

Przy większej liczbie pól wygodny jest jeden obiekt.
Każde pole ma atrybut `name`.
Jedna funkcja `handleChange` aktualizuje odpowiednie pole.

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const initialForm = {
  owner: "",
  animal: "Pies",
  age: 1,
  purpose: "",
  time: "12:00"
};

function App() {
  const [form, setForm] = useState(initialForm);
  const [summary, setSummary] = useState("");

  function handleChange(event) {
    const { name, value } = event.target;

    setForm((previousForm) => ({
      ...previousForm,
      [name]: value
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    setSummary(
      `${form.owner}, ${form.animal}, ${form.age}, ${form.purpose}, ${form.time}`
    );
  }

  return (
    <main className="container mt-4" style={{ maxWidth: 620 }}>
      <h1>Wizyta</h1>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="owner" className="form-label">Właściciel</label>
          <input
            id="owner"
            name="owner"
            className="form-control"
            value={form.owner}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="animal" className="form-label">Gatunek</label>
          <select
            id="animal"
            name="animal"
            className="form-select"
            value={form.animal}
            onChange={handleChange}
          >
            <option>Pies</option>
            <option>Kot</option>
            <option>Świnka morska</option>
          </select>
        </div>

        <div className="mb-3">
          <label htmlFor="age" className="form-label">Wiek: {form.age}</label>
          <input
            id="age"
            name="age"
            type="range"
            min="1"
            max="20"
            className="form-range"
            value={form.age}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="purpose" className="form-label">Cel wizyty</label>
          <input
            id="purpose"
            name="purpose"
            className="form-control"
            value={form.purpose}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="time" className="form-label">Godzina</label>
          <input
            id="time"
            name="time"
            type="time"
            className="form-control"
            value={form.time}
            onChange={handleChange}
          />
        </div>

        <button className="btn btn-primary">OK</button>
      </form>

      {summary && <p className="alert alert-info mt-3">{summary}</p>}
    </main>
  );
}

export default App;
```

Najważniejsza linia to `[name]: value`.
Oznacza: zaktualizuj pole obiektu, którego nazwa jest w zmiennej `name`.
Jeżeli input ma `name="owner"`, zmieni się `form.owner`.
Jeżeli input ma `name="purpose"`, zmieni się `form.purpose`.

### 37.3. Błędy per pole

W prostych przykładach często jest jeden komunikat.
W lepszej dokumentacji warto pokazać błędy przypisane do konkretnych pól.
To daje czytelniejszy interfejs i lepszy kod.

```jsx
const [errors, setErrors] = useState({});

function validate(form) {
  const nextErrors = {};

  if (form.fullName.trim() === "") {
    nextErrors.fullName = "Podaj imię i nazwisko";
  }

  if (!form.email.includes("@")) {
    nextErrors.email = "Adres email musi zawierać znak @";
  }

  if (form.courseNumber.trim() === "") {
    nextErrors.courseNumber = "Podaj numer kursu";
  }

  return nextErrors;
}
```

Użycie w `handleSubmit`:

```jsx
function handleSubmit(event) {
  event.preventDefault();

  const nextErrors = validate(form);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  console.log("Dane poprawne", form);
}
```

Wyświetlenie błędu przy polu:

```jsx
<input
  id="email"
  name="email"
  className={`form-control ${errors.email ? "is-invalid" : ""}`}
  value={form.email}
  onChange={handleChange}
/>
{errors.email && <div className="invalid-feedback">{errors.email}</div>}
```

Bootstrap ma klasy `is-invalid` i `invalid-feedback`.
To jest bardzo przydatne przy formularzach, które mają wyglądać profesjonalnie bez pisania dużej ilości CSS.

### 37.4. Checkboxy jako tablica

Czasem checkbox nie oznacza jednej wartości true/false, tylko wiele wybranych opcji.
Przykład: użytkownik wybiera technologie, kategorie albo składniki hasła.

```jsx
const [selectedCategories, setSelectedCategories] = useState(["kwiaty"]);

function toggleCategory(category) {
  setSelectedCategories((previousCategories) => {
    if (previousCategories.includes(category)) {
      return previousCategories.filter((item) => item !== category);
    }

    return [...previousCategories, category];
  });
}
```

JSX:

```jsx
{["kwiaty", "zwierzeta", "samochody"].map((category) => (
  <div className="form-check" key={category}>
    <input
      id={category}
      type="checkbox"
      className="form-check-input"
      checked={selectedCategories.includes(category)}
      onChange={() => toggleCategory(category)}
    />
    <label htmlFor={category} className="form-check-label">
      {category}
    </label>
  </div>
))}
```

Filtrowanie:

```jsx
const visiblePhotos = photos.filter((photo) =>
  selectedCategories.includes(photo.category)
);
```

Ten wzorzec jest bardziej elastyczny niż trzy osobne stany typu `showFlowers`, `showAnimals`, `showCars`.
Jeżeli jutro dojdzie czwarta kategoria, nie musisz dopisywać czwartego `useState`.

### 37.5. useRef i formularz niekontrolowany

Formularz kontrolowany jest podstawowym wzorcem w React.
Czasem jednak chcesz tylko odczytać wartość pola po kliknięciu, bez aktualizacji stanu po każdym znaku.
Wtedy można użyć `useRef`.

```jsx
// src/App.js
import { useRef, useState } from "react";

function App() {
  const nameRef = useRef(null);
  const [message, setMessage] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    const name = nameRef.current.value;

    if (name.trim() === "") {
      setMessage("Podaj imię i nazwisko");
      nameRef.current.focus();
      return;
    }

    setMessage(`Witaj, ${name}`);
  }

  return (
    <main className="container mt-4">
      <form onSubmit={handleSubmit}>
        <label htmlFor="name" className="form-label">Imię i nazwisko</label>
        <input id="name" ref={nameRef} className="form-control" />
        <button className="btn btn-primary mt-3">Zapisz</button>
      </form>
      {message && <p className="mt-3">{message}</p>}
    </main>
  );
}

export default App;
```

`useRef` ma tu dwa zastosowania.
Po pierwsze, pozwala odczytać wartość pola.
Po drugie, pozwala ustawić fokus przez `nameRef.current.focus()`.
W większości prostych komponentów częściej użyjesz formularzy kontrolowanych, ale `useRef` jest świetny do fokusu po błędzie.

### 37.6. FormData

`FormData` pozwala odczytać wartości formularza po jego zatwierdzeniu.
Nie trzeba tworzyć stanu dla każdego pola, jeśli dane są potrzebne tylko po kliknięciu.

```jsx
function App() {
  function handleSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const title = formData.get("title");
    const type = formData.get("type");

    console.log(`tytul: ${title}; rodzaj: ${type}`);
  }

  return (
    <main className="container mt-4">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="title" className="form-label">Tytuł filmu</label>
          <input id="title" name="title" className="form-control" />
        </div>

        <div className="mb-3">
          <label htmlFor="type" className="form-label">Rodzaj</label>
          <select id="type" name="type" className="form-select" defaultValue="Komedia">
            <option>Komedia</option>
            <option>Obyczajowy</option>
            <option>Sensacyjny</option>
            <option>Horror</option>
          </select>
        </div>

        <button className="btn btn-primary">Dodaj</button>
      </form>
    </main>
  );
}
```

To jest formularz niekontrolowany.
Nie ma `value` i `onChange`.
Dla początkujących bezpieczniejsze są formularze kontrolowane, bo stan jest widoczny w kodzie.
Ale `FormData` warto znać, bo do prostego wypisania danych w konsoli bywa bardzo wygodne.


## 38. useEffect, dane lokalne i efekty uboczne

`useEffect` jest potrzebny wtedy, gdy komponent ma zsynchronizować się z czymś poza samym renderowaniem JSX.
Może to być localStorage, pobranie pliku JSON, timer, tytuł strony albo zdarzenie przeglądarki.
Nie używaj `useEffect` do prostych obliczeń, które można wykonać podczas renderu.

### 38.1. Tablica zależności

`useEffect` ma drugi argument: tablicę zależności.
Od niej zależy, kiedy efekt się uruchamia.

```jsx
useEffect(() => {
  console.log("Uruchamia się po każdym renderze");
});

useEffect(() => {
  console.log("Uruchamia się tylko po pierwszym renderze");
}, []);

useEffect(() => {
  console.log("Uruchamia się po zmianie search");
}, [search]);
```

Przykład praktyczny: tytuł strony zależny od liczby notatek.

```jsx
useEffect(() => {
  document.title = `Notatki: ${notes.length}`;
}, [notes.length]);
```

Zależności powinny zawierać wartości używane w efekcie.
Jeżeli używasz `search`, wpisz `search`.
Jeżeli używasz `notes.length`, możesz wpisać `notes.length`.

### 38.2. Cleanup

Cleanup to funkcja sprzątająca zwracana z `useEffect`.
Jest potrzebna przy timerach, subskrypcjach i zdarzeniach.

```jsx
useEffect(() => {
  const id = setInterval(() => {
    console.log("Minęła sekunda");
  }, 1000);

  return () => {
    clearInterval(id);
  };
}, []);
```

Bez `clearInterval` timer działałby dalej nawet po usunięciu komponentu.
W prostych komponentach rzadko trzeba używać timera, ale cleanup jest ważnym pojęciem.

Przykład nasłuchiwania klawiatury:

```jsx
useEffect(() => {
  function handleKeyDown(event) {
    if (event.key === "Escape") {
      setMessage("");
    }
  }

  window.addEventListener("keydown", handleKeyDown);

  return () => {
    window.removeEventListener("keydown", handleKeyDown);
  };
}, []);
```

To może się przydać przy zamykaniu komunikatu, modalu albo resetowaniu wyboru.

### 38.3. Fetch z loading i error

Jeżeli plik `photos.json` znajduje się w `public/data/photos.json`, możesz pobrać go przez `fetch("/data/photos.json")`.
To jest dobre, gdy aplikacja ma pobrać dane z lokalnego pliku, ale nadal pozostaje aplikacją front-endową.

Przykładowy plik `public/data/photos.json`:

```json
[
  { "id": 1, "title": "Kwiat", "category": "kwiaty", "file": "/img/kwiat.jpg", "downloads": 0 },
  { "id": 2, "title": "Kot", "category": "zwierzeta", "file": "/img/kot.jpg", "downloads": 3 }
]
```

Komponent:

```jsx
// src/App.js
import { useEffect, useState } from "react";

function App() {
  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadPhotos() {
      try {
        const response = await fetch("/data/photos.json");

        if (!response.ok) {
          throw new Error("Nie udało się wczytać danych");
        }

        const data = await response.json();
        setPhotos(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadPhotos();
  }, []);

  if (loading) {
    return <p className="container mt-4">Ładowanie danych...</p>;
  }

  if (error) {
    return <p className="container mt-4 alert alert-danger">{error}</p>;
  }

  return (
    <main className="container mt-4">
      <h1>Kolekcja</h1>
      <p>Liczba zdjęć: {photos.length}</p>
    </main>
  );
}

export default App;
```

Ten wzorzec ma trzy stany:

- `photos` przechowuje dane,
- `loading` mówi, czy dane jeszcze się ładują,
- `error` przechowuje komunikat błędu.

W prostym projekcie często wystarczy tablica wpisana w kodzie.
Ale jeśli chcesz mieć dokumentację pełniejszą i praktyczną, warto znać ten wariant.

### 38.4. localStorage jako praktyczny wzorzec

`localStorage` pozwala zapisać dane w przeglądarce.
Po odświeżeniu strony dane nadal mogą być dostępne.
To może przydać się w notatkach, liczniku pobrań albo ustawieniach.

```jsx
import { useEffect, useState } from "react";

function App() {
  const [notes, setNotes] = useState(() => {
    const savedNotes = localStorage.getItem("notes");
    return savedNotes ? JSON.parse(savedNotes) : [];
  });

  useEffect(() => {
    localStorage.setItem("notes", JSON.stringify(notes));
  }, [notes]);

  function addNote(text) {
    setNotes((previousNotes) => [...previousNotes, text]);
  }
}
```

Ważne:

- `localStorage` zapisuje tekst, więc obiekty i tablice trzeba zamienić przez `JSON.stringify`.
- Przy odczycie trzeba użyć `JSON.parse`.
- Warto obsłużyć brak danych.
- Dla prostych projektów nie zapisuj wszystkiego do localStorage, jeśli funkcjonalność tego nie wymaga.


## 39. Dobre praktyki UI

React to nie tylko JavaScript.
Aplikacja musi być czytelna, dostępna i przewidywalna.
Poprawny HTML i proste dobre praktyki często zapobiegają błędom, nawet gdy aplikacja jest niewielka.

### 39.1. button type

W HTML przycisk wewnątrz formularza domyślnie działa jak `submit`.
To może być problem, jeśli masz dodatkowy przycisk, który nie ma zatwierdzać formularza.

```jsx
<form onSubmit={handleSubmit}>
  <button type="button" onClick={generatePassword}>
    Generuj hasło
  </button>

  <button type="submit">
    Zatwierdź
  </button>
</form>
```

Zasada:

- `type="submit"` dla przycisku zatwierdzającego formularz,
- `type="button"` dla zwykłej akcji wewnątrz formularza,
- `type="reset"` rzadko, zwykle lepiej zrobić reset w React przez stan.

To jest ważne w formularzu pracownika z generowaniem hasła.
Przycisk `Generuj hasło` nie powinien przypadkowo wysyłać formularza.

### 39.2. Dostępność formularzy

Każde pole powinno mieć etykietę.
`label` łączymy z polem przez `htmlFor` i `id`.

```jsx
<label htmlFor="email" className="form-label">
  Email
</label>
<input id="email" className="form-control" />
```

Obraz powinien mieć `alt`.

```jsx
<img src="/img/kot.jpg" alt="Kot leżący na kanapie" />
```

Jeżeli przycisk ma tylko ikonę albo znak, dodaj `aria-label`.

```jsx
<button
  type="button"
  className="btn btn-outline-secondary"
  aria-label="Poprzedni element"
  onClick={goPrevious}
>
  &lt;
</button>
```

Komunikat błędu powinien być blisko pola albo w widocznym alercie.

```jsx
{error && (
  <div className="alert alert-danger" role="alert">
    {error}
  </div>
)}
```

To nie jest tylko „ładny dodatek”.
Dobrze opisane pola są łatwiejsze do testowania i mniej podatne na pomyłki.

### 39.3. Semantyczny układ strony

Zamiast samych `div`, używaj elementów, które opisują znaczenie.

```jsx
<main className="container mt-4">
  <header className="mb-4">
    <h1>Kolekcja zdjęć</h1>
  </header>

  <section aria-labelledby="filters-title">
    <h2 id="filters-title" className="h4">Filtry</h2>
    {/* checkboxy */}
  </section>

  <section aria-labelledby="cards-title">
    <h2 id="cards-title" className="h4">Zdjęcia</h2>
    {/* karty */}
  </section>
</main>
```

Semantyka pomaga utrzymać porządek.
W widoku z formularzem możesz mieć `main`, `form`, `section`.
W widoku z kartami możesz mieć `article` dla pojedynczej karty.
W widoku z listą możesz mieć `ul` albo `ol`.

### 39.4. Wzorce przydatne w małych aplikacjach

Poniższe wzorce są naturalnym rozszerzeniem formularzy, list, kart i stanu.
Warto je mieć w dokumentacji, bo często pojawiają się w małych aplikacjach użytkowych.

| Wzorzec | Co trzeba umieć | Dlaczego pasuje do poziomu |
| --- | --- | --- |
| wyszukiwarka listy | `input`, `filter`, `toLowerCase` | podobne do filtrowania kategorii |
| sortowanie listy | `select`, `[...items].sort` | podobne do widoku kart i tabeli |
| dynamiczne maksimum suwaka | stan zależny od wyboru | podobne do wieku zwierzęcia |
| blokowanie elementu | boolean w obiekcie, `opacity` | podobne do kości |
| zapis ustawień | `localStorage` | podobne do notatek i ustawień |
| licznik znaków | `textarea`, `value.length` | prosty stan formularza |
| podsumowanie formularza | template string | wiele formularzy użytkowych |
| tabela danych | `table`, `map` | alternatywa dla listy/kart |
| reset widoku | ustawienie stanów początkowych | gry, formularze, RGB |

Przykład wyszukiwarki:

```jsx
const [search, setSearch] = useState("");

const visibleCourses = courses.filter((course) =>
  course.toLowerCase().includes(search.trim().toLowerCase())
);

return (
  <>
    <input
      className="form-control mb-3"
      placeholder="Szukaj kursu"
      value={search}
      onChange={(event) => setSearch(event.target.value)}
    />

    <ul className="list-group">
      {visibleCourses.map((course) => (
        <li className="list-group-item" key={course}>
          {course}
        </li>
      ))}
    </ul>
  </>
);
```

Przykład dynamicznego maksimum suwaka:

```jsx
const maxAgeByAnimal = {
  Pies: 18,
  Kot: 20,
  "Świnka morska": 9
};

const maxAge = maxAgeByAnimal[animal];

function handleAnimalChange(event) {
  const nextAnimal = event.target.value;
  setAnimal(nextAnimal);
  setAge((previousAge) => Math.min(previousAge, maxAgeByAnimal[nextAnimal]));
}
```

Ten fragment pokazuje ważny detal.
Jeżeli zmieniasz gatunek z kota na świnkę morską, wcześniejszy wiek 20 może być za duży.
Dlatego po zmianie gatunku można ograniczyć wiek przez `Math.min`.

Przykład blokowanych kości:

```jsx
function toggleLocked(id) {
  setDice((previousDice) =>
    previousDice.map((die) =>
      die.id === id ? { ...die, locked: !die.locked } : die
    )
  );
}

function rollUnlockedDice() {
  setDice((previousDice) =>
    previousDice.map((die) =>
      die.locked
        ? die
        : { ...die, value: Math.floor(Math.random() * 6) + 1 }
    )
  );
}
```

To jest wzorzec aktualizacji tablicy obiektów.
Przydaje się nie tylko w grze.
Tak samo można przełączać urządzenia, zaznaczać elementy, ukrywać zdjęcia albo zapisywać wybrane rekordy.


## 40. Rozbudowane projekty wzorcowe

Ten rozdział jest po to, żeby mieć kod, który można realnie czytać, rozbierać i przerabiać.
Każdy projekt ma kontekst, informację o pliku i komentarze.
To neutralne wzorce: formularz, walidacja, checkboxy, tablice, obrazy, liczniki i dynamiczny interfejs.

### 40.1. Generator hasła z formularzem

Ten projekt ćwiczy kilka bardzo ważnych rzeczy naraz:

- pola tekstowe,
- `select`,
- `input type="number"`,
- checkboxy,
- dwa przyciski w jednym formularzu,
- `button type="button"` i `button type="submit"`,
- generowanie losowego tekstu,
- walidację,
- komunikat podsumowujący.

Kod wklej do `src/App.js`.
Jeżeli używasz Bootstrapa globalnie w `src/index.js`, możesz usunąć import Bootstrapa z tego pliku.

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const positions = ["Programista", "Administrator", "Projektant", "Tester"];

function generatePassword(length, useUppercase, useDigits, useSpecial) {
  let characters = "abcdefghijklmnopqrstuvwxyz";

  if (useUppercase) {
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  }

  if (useDigits) {
    characters += "0123456789";
  }

  if (useSpecial) {
    characters += "!@#$%^&*";
  }

  let password = "";

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    password += characters[randomIndex];
  }

  return password;
}

function App() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [position, setPosition] = useState(positions[0]);
  const [passwordLength, setPasswordLength] = useState("8");
  const [useUppercase, setUseUppercase] = useState(true);
  const [useDigits, setUseDigits] = useState(true);
  const [useSpecial, setUseSpecial] = useState(false);
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  function handleGeneratePassword() {
    const length = Number(passwordLength);

    if (!Number.isInteger(length) || length < 1) {
      setMessage("Długość hasła musi być liczbą większą od zera.");
      return;
    }

    const generated = generatePassword(
      length,
      useUppercase,
      useDigits,
      useSpecial
    );

    setPassword(generated);
    setMessage(`Wygenerowane hasło: ${generated}`);
  }

  function handleSubmit(event) {
    event.preventDefault();

    if (firstName.trim() === "" || lastName.trim() === "") {
      setMessage("Podaj imię i nazwisko pracownika.");
      return;
    }

    if (password === "") {
      setMessage("Najpierw wygeneruj hasło.");
      return;
    }

    setMessage(
      `Dodano pracownika: ${firstName} ${lastName}, stanowisko: ${position}, hasło: ${password}`
    );
  }

  return (
    <main className="container mt-4" style={{ maxWidth: 760 }}>
      <h1>Dodaj pracownika</h1>

      <form onSubmit={handleSubmit}>
        <section className="mb-4">
          <h2 className="h4">Dane pracownika</h2>

          <div className="row g-3">
            <div className="col-md-6">
              <label htmlFor="firstName" className="form-label">Imię</label>
              <input
                id="firstName"
                className="form-control"
                value={firstName}
                onChange={(event) => setFirstName(event.target.value)}
              />
            </div>

            <div className="col-md-6">
              <label htmlFor="lastName" className="form-label">Nazwisko</label>
              <input
                id="lastName"
                className="form-control"
                value={lastName}
                onChange={(event) => setLastName(event.target.value)}
              />
            </div>

            <div className="col-12">
              <label htmlFor="position" className="form-label">Stanowisko</label>
              <select
                id="position"
                className="form-select"
                value={position}
                onChange={(event) => setPosition(event.target.value)}
              >
                {positions.map((item) => (
                  <option key={item}>{item}</option>
                ))}
              </select>
            </div>
          </div>
        </section>

        <section className="mb-4">
          <h2 className="h4">Generowanie hasła</h2>

          <div className="mb-3">
            <label htmlFor="passwordLength" className="form-label">
              Długość hasła
            </label>
            <input
              id="passwordLength"
              type="number"
              min="1"
              className="form-control"
              value={passwordLength}
              onChange={(event) => setPasswordLength(event.target.value)}
            />
          </div>

          <div className="form-check">
            <input
              id="uppercase"
              type="checkbox"
              className="form-check-input"
              checked={useUppercase}
              onChange={(event) => setUseUppercase(event.target.checked)}
            />
            <label htmlFor="uppercase" className="form-check-label">
              Wielkie litery
            </label>
          </div>

          <div className="form-check">
            <input
              id="digits"
              type="checkbox"
              className="form-check-input"
              checked={useDigits}
              onChange={(event) => setUseDigits(event.target.checked)}
            />
            <label htmlFor="digits" className="form-check-label">
              Cyfry
            </label>
          </div>

          <div className="form-check mb-3">
            <input
              id="special"
              type="checkbox"
              className="form-check-input"
              checked={useSpecial}
              onChange={(event) => setUseSpecial(event.target.checked)}
            />
            <label htmlFor="special" className="form-check-label">
              Znaki specjalne
            </label>
          </div>

          <button
            type="button"
            className="btn btn-secondary"
            onClick={handleGeneratePassword}
          >
            Generuj hasło
          </button>
        </section>

        <button type="submit" className="btn btn-primary">
          Zatwierdź
        </button>
      </form>

      {message && (
        <div className="alert alert-info mt-4" role="alert">
          {message}
        </div>
      )}
    </main>
  );
}

export default App;
```

Co jest tu najważniejsze:

- Funkcja `generatePassword` jest poza komponentem, bo nie potrzebuje stanu Reacta.
- Przycisk `Generuj hasło` ma `type="button"`, więc nie zatwierdza formularza.
- Przycisk `Zatwierdź` ma `type="submit"`, więc uruchamia `onSubmit`.
- Długość hasła jest tekstem z inputa, dlatego używamy `Number(passwordLength)`.
- Wygenerowane hasło zapisujemy w stanie, bo ma być później użyte przy zatwierdzaniu.

### 40.2. Widok kart z kategoriami, wyszukiwaniem i sortowaniem

Ten projekt rozwija prosty widok kart.
Pokazuje, jak połączyć kilka mechanik:

- tablica obiektów,
- checkboxy jako tablica wybranych kategorii,
- wyszukiwarka,
- sortowanie,
- renderowanie kart,
- aktualizacja jednego elementu w stanie.

Kod wklej do `src/App.js`.
Obrazy przykładowo umieść w `public/img`.
Jeżeli nie masz obrazów, możesz tymczasowo podmienić ścieżki na dowolne działające adresy.

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const initialPhotos = [
  {
    id: 1,
    title: "Róża",
    category: "kwiaty",
    file: "/img/roza.jpg",
    downloads: 3
  },
  {
    id: 2,
    title: "Kot",
    category: "zwierzeta",
    file: "/img/kot.jpg",
    downloads: 7
  },
  {
    id: 3,
    title: "Samochód",
    category: "samochody",
    file: "/img/samochod.jpg",
    downloads: 2
  }
];

const categories = ["kwiaty", "zwierzeta", "samochody"];

function App() {
  const [photos, setPhotos] = useState(initialPhotos);
  const [selectedCategories, setSelectedCategories] = useState(categories);
  const [search, setSearch] = useState("");
  const [sortMode, setSortMode] = useState("title");

  function toggleCategory(category) {
    setSelectedCategories((previous) => {
      if (previous.includes(category)) {
        return previous.filter((item) => item !== category);
      }

      return [...previous, category];
    });
  }

  function downloadPhoto(id) {
    setPhotos((previousPhotos) =>
      previousPhotos.map((photo) =>
        photo.id === id
          ? { ...photo, downloads: photo.downloads + 1 }
          : photo
      )
    );
  }

  const visiblePhotos = photos
    .filter((photo) => selectedCategories.includes(photo.category))
    .filter((photo) =>
      photo.title.toLowerCase().includes(search.trim().toLowerCase())
    )
    .sort((a, b) => {
      if (sortMode === "downloads") {
        return b.downloads - a.downloads;
      }

      return a.title.localeCompare(b.title);
    });

  return (
    <main className="container mt-4">
      <header className="mb-4">
        <h1>Kolekcja zdjęć</h1>
        <p className="text-muted">
          Przykład widoku kart z filtrowaniem, wyszukiwaniem i licznikiem pobrań.
        </p>
      </header>

      <section className="mb-4" aria-labelledby="filters-title">
        <h2 id="filters-title" className="h4">Filtry</h2>

        <div className="row g-3">
          <div className="col-md-5">
            <label htmlFor="search" className="form-label">Szukaj</label>
            <input
              id="search"
              className="form-control"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Wpisz tytuł zdjęcia"
            />
          </div>

          <div className="col-md-4">
            <label htmlFor="sortMode" className="form-label">Sortowanie</label>
            <select
              id="sortMode"
              className="form-select"
              value={sortMode}
              onChange={(event) => setSortMode(event.target.value)}
            >
              <option value="title">Alfabetycznie</option>
              <option value="downloads">Najwięcej pobrań</option>
            </select>
          </div>
        </div>

        <div className="d-flex flex-wrap gap-3 mt-3">
          {categories.map((category) => (
            <div className="form-check form-switch" key={category}>
              <input
                id={category}
                type="checkbox"
                role="switch"
                className="form-check-input"
                checked={selectedCategories.includes(category)}
                onChange={() => toggleCategory(category)}
              />
              <label htmlFor={category} className="form-check-label">
                {category}
              </label>
            </div>
          ))}
        </div>
      </section>

      <section aria-labelledby="cards-title">
        <h2 id="cards-title" className="h4">
          Zdjęcia: {visiblePhotos.length}
        </h2>

        {visiblePhotos.length === 0 ? (
          <div className="alert alert-warning">
            Brak zdjęć spełniających warunki.
          </div>
        ) : (
          <div className="row g-3">
            {visiblePhotos.map((photo) => (
              <div className="col-12 col-md-6 col-lg-4" key={photo.id}>
                <article className="card h-100">
                  <img
                    src={photo.file}
                    className="card-img-top"
                    alt={photo.title}
                  />
                  <div className="card-body">
                    <h3 className="h5">{photo.title}</h3>
                    <p>Kategoria: {photo.category}</p>
                    <p>Pobrania: {photo.downloads}</p>
                    <button
                      type="button"
                      className="btn btn-primary"
                      onClick={() => downloadPhoto(photo.id)}
                    >
                      Pobierz
                    </button>
                  </div>
                </article>
              </div>
            ))}
          </div>
        )}
      </section>
    </main>
  );
}

export default App;
```

Uwaga techniczna: `sort()` mutuje tablicę.
W tym przykładzie `sort()` jest wywołany po dwóch `filter()`, a `filter()` tworzy nowe tablice.
Dzięki temu oryginalny stan `photos` nie jest sortowany bezpośrednio.
Gdyby sortować samą tablicę ze stanu, użyj najpierw kopii: `[...photos].sort(...)`.

### 40.3. Kości z blokowaniem

Ten projekt ćwiczy dynamiczne obrazy, tablicę obiektów, losowanie i przełączanie stanu jednego elementu.
To jest bardzo dobry wzorzec dla aplikacji typu gra, urządzenia, kafelki albo elementy wybierane kliknięciem.

Załóżmy, że w folderze `public/img` masz pliki:

```text
public/
  img/
    dice-1.png
    dice-2.png
    dice-3.png
    dice-4.png
    dice-5.png
    dice-6.png
```

Kod:

```jsx
// src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function createInitialDice() {
  return Array.from({ length: 5 }, (_, index) => ({
    id: index + 1,
    value: 1,
    locked: false
  }));
}

function rollOneDie() {
  return Math.floor(Math.random() * 6) + 1;
}

function App() {
  const [dice, setDice] = useState(createInitialDice);

  const sum = dice.reduce((total, die) => total + die.value, 0);

  function rollDice() {
    setDice((previousDice) =>
      previousDice.map((die) =>
        die.locked ? die : { ...die, value: rollOneDie() }
      )
    );
  }

  function toggleLocked(id) {
    setDice((previousDice) =>
      previousDice.map((die) =>
        die.id === id ? { ...die, locked: !die.locked } : die
      )
    );
  }

  function resetGame() {
    setDice(createInitialDice());
  }

  return (
    <main className="container mt-4">
      <h1>Gra w kości</h1>

      <p className="lead">Suma oczek: {sum}</p>

      <div className="d-flex flex-wrap gap-3 mb-4">
        {dice.map((die) => (
          <button
            key={die.id}
            type="button"
            className="btn btn-light border"
            onClick={() => toggleLocked(die.id)}
            aria-label={
              die.locked
                ? `Kość ${die.id} zablokowana`
                : `Kość ${die.id} odblokowana`
            }
          >
            <img
              src={`/img/dice-${die.value}.png`}
              alt={`Kość z liczbą oczek ${die.value}`}
              style={{
                width: 80,
                height: 80,
                objectFit: "contain",
                opacity: die.locked ? 0.5 : 1
              }}
            />
          </button>
        ))}
      </div>

      <div className="d-flex gap-2">
        <button type="button" className="btn btn-primary" onClick={rollDice}>
          Rzut
        </button>
        <button type="button" className="btn btn-secondary" onClick={resetGame}>
          Reset
        </button>
      </div>
    </main>
  );
}

export default App;
```

Co tu się dzieje:

- `dice` jest tablicą pięciu obiektów.
- Każda kość ma `id`, `value` i `locked`.
- Kliknięcie kości przełącza `locked`.
- Rzut losuje tylko kości, które nie są zablokowane.
- Obrazek zależy od `die.value`.
- Przezroczystość zależy od `die.locked`.
- Suma jest stanem pochodnym, więc jest obliczana przez `reduce`, a nie trzymana osobno w `useState`.

Ten przykład jest szczególnie dobry do nauki, bo łączy wiele fundamentów Reacta w jednym miejscu.
Jeżeli rozumiesz ten kod, rozumiesz też dużą część typowych interfejsów ze stanem i listą obiektów.


## A. Tabela referencyjna: formularze

| Element | Stan | Zdarzenie | Wartość |
| --- | --- | --- | --- |
| `input text` | `useState('')` | `onChange` | `e.target.value` |
| `input number` | `useState('')` | `onChange` | `Number(e.target.value)` |
| `password` | `useState('')` | `onChange` | `e.target.value` |
| `select` | `useState(opcja)` | `onChange` | `e.target.value` |
| `textarea` | `useState('')` | `onChange` | `e.target.value` |
| `checkbox` | `useState(false)` | `onChange` | `e.target.checked` |
| `radio` | `useState(wartość)` | `onChange` | `e.target.value` |
| `range` | `useState(liczba)` | `onChange` | `Number(e.target.value)` |


## B. Tabela referencyjna: operacje na tablicach

| Cel | Metoda | Wzorzec |
| --- | --- | --- |
| wyświetlenie listy | `map` | `items.map(item => <li key={item.id}>...</li>)` |
| filtrowanie | `filter` | `items.filter(item => item.active)` |
| dodanie | spread | `setItems(prev => [...prev, item])` |
| usunięcie | `filter` | `setItems(prev => prev.filter(x => x.id !== id))` |
| zmiana jednego | `map` | `x.id === id ? { ...x, value } : x` |
| suma | `reduce` | `items.reduce((s, x) => s + x.count, 0)` |
| wyszukanie | `find` | `items.find(x => x.id === id)` |


## C. Tabela referencyjna: Bootstrap

| Cel | Klasy |
| --- | --- |
| kontener | `container mt-4` |
| etykieta | `form-label` |
| input | `form-control` |
| select | `form-select` |
| checkbox | `form-check`, `form-check-input`, `form-check-label` |
| switch | `form-check form-switch` |
| przycisk | `btn btn-primary` |
| siatka | `row`, `col-12`, `col-md-6`, `col-lg-4` |
| karta | `card`, `card-body`, `card-img-top` |
| alert | `alert alert-danger` |

---

## 41. Kompletny Projekt: Lista Zadań (Todo App) [Wieloplikowy]

Ten projekt pokazuje, jak w praktyce dzielić aplikację na wiele plików. Jest to kluczowe, gdy projekt rośnie, aby utrzymać czytelność i porządek.

### 41.1. Struktura plików

W folderze `src` Twojego projektu powinna pojawić się następująca struktura:
```text
src/
  components/
    TaskForm.js
    TaskList.js
  App.js
```

### 41.2. App.js (Rodzic trzymający stan)

`App.js` to mózg Twojej aplikacji. Tutaj trzymasz listę zadań i funkcje do jej modyfikacji, które przekazujesz do "dzieci" (komponentów pomocniczych).

```jsx
// src/App.js
import { useState } from "react";
import TaskForm from "./components/TaskForm"; // Importujemy nasze komponenty
import TaskList from "./components/TaskList";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Nasz główny stan - tablica obiektów z zadaniami
  const [tasks, setTasks] = useState([
    { id: 1, text: "Nauczyć się Reacta", completed: false },
    { id: 2, text: "Zrobić projekt na zaliczenie", completed: true }
  ]);

  // Funkcja dodająca nowe zadanie - zostanie przekazana do TaskForm
  function addTask(taskText) {
    const newTask = {
      id: Date.now(), // Prosty sposób na unikalne ID
      text: taskText,
      completed: false
    };
    // ZAWSZE tworzymy nową tablicę używając spread operatora [...]
    setTasks((prevTasks) => [...prevTasks, newTask]);
  }

  // Funkcja usuwająca zadanie - zostanie przekazana do TaskList
  function deleteTask(id) {
    setTasks((prevTasks) => prevTasks.filter(task => task.id !== id));
  }

  return (
    <main className="container mt-5" style={{ maxWidth: "600px" }}>
      <h1 className="text-center mb-4">Moja Lista Zadań</h1>
      
      {/* Przekazujemy funkcję addTask jako 'prop' do komponentu TaskForm */}
      <TaskForm onAddTask={addTask} />
      
      {/* Przekazujemy listę zadań oraz funkcję usuwania jako 'props' do TaskList */}
      <TaskList tasks={tasks} onDeleteTask={deleteTask} />
      
      <div className="mt-3 text-muted">
        Pozostało zadań: {tasks.filter(t => !t.completed).length}
      </div>
    </main>
  );
}

export default App;
```

### 41.3. TaskForm.js (Komponent dodawania)

Ten komponent odpowiada tylko za pole tekstowe i przycisk "Dodaj". Nie wie on o istnieniu listy zadań - po prostu zgłasza do rodzica, że użytkownik wpisał nowy tekst.

```jsx
// src/components/TaskForm.js
import { useState } from "react";

function TaskForm({ onAddTask }) {
  const [text, setText] = useState(""); // Stan lokalny tylko dla tego inputa

  function handleSubmit(e) {
    e.preventDefault(); // Blokujemy przeładowanie strony
    
    // Walidacja - nie dodajemy pustych zadań
    if (text.trim() === "") return;

    // Wywołujemy funkcję otrzymaną od rodzica (App.js)
    onAddTask(text);
    
    // Czyścimy pole tekstowe po dodaniu
    setText("");
  }

  return (
    <form onSubmit={handleSubmit} className="input-group mb-4">
      <input 
        type="text" 
        className="form-control" 
        placeholder="Co masz do zrobienia?"
        value={text} // Input kontrolowany
        onChange={(e) => setText(e.target.value)}
      />
      <button className="btn btn-success" type="submit">Dodaj</button>
    </form>
  );
}

export default TaskForm;
```

### 41.4. TaskList.js (Komponent listy)

Ten komponent odbiera listę i po prostu ją "renderuje" (wyświetla) używając funkcji `map()`.

```jsx
// src/components/TaskList.js

function TaskList({ tasks, onDeleteTask }) {
  // Jeśli nie ma zadań, wyświetlamy pomocny komunikat (Renderowanie warunkowe)
  if (tasks.length === 0) {
    return <p className="text-center text-muted">Brak zadań. Odpocznij!</p>;
  }

  return (
    <ul className="list-group">
      {tasks.map((task) => (
        // Każdy element listy generowany przez map() MUSI mieć unikalne 'key'
        <li key={task.id} className="list-group-item d-flex justify-content-between align-items-center">
          <span style={{ textDecoration: task.completed ? "line-through" : "none" }}>
            {task.text}
          </span>
          <button 
            className="btn btn-danger btn-sm"
            onClick={() => onDeleteTask(task.id)} // Zgłaszamy usunięcie do rodzica
          >
            Usuń
          </button>
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
```

### 41.5. Podsumowanie przepływu danych

1.  **Dół (Props)**: Rodzic (`App.js`) przekazuje dane (`tasks`) i funkcje do dzieci. Dzięki temu dzieci wiedzą, co wyświetlić.
2.  **Góra (Callbacks)**: Dzieci (`TaskForm`, `TaskList`) nie zmieniają stanu bezpośrednio. One "dzwonią" do rodzica wywołując funkcje (`onAddTask`, `onDeleteTask`), a rodzic wykonuje właściwą zmianę w `useState`.
3.  **Odświeżenie**: Gdy rodzic zmieni stan, React automatycznie "odmalowuje" (`re-render`) wszystkie dzieci z nowymi danymi.


## 42. Najczęstsze pułapki i jak ich unikać

### 42.1. Brak `key` w pętli map()
React używa atrybutu `key`, aby wiedzieć, który element listy się zmienił.
- **Błąd**: `{items.map(item => <li>{item.text}</li>)}`
- **Poprawnie**: `{items.map(item => <li key={item.id}>{item.text}</li>)}`
- **Uwaga**: Nie używaj indeksu (`index`) jako klucza, jeśli kolejność elementów może się zmieniać (np. przy usuwaniu).

### 42.2. Mutowanie stanu zamiast tworzenia kopii
W React stan jest "niezmienny" (`immutable`). Zawsze tworzymy nową kopię tablicy lub obiektu.
- **Błąd**: `tasks.push(newTask); setTasks(tasks);` (React nie zauważy zmiany referencji i nie odświeży strony).
- **Poprawnie**: `setTasks([...tasks, newTask]);` (Używamy operatora spread, aby stworzyć NOWĄ tablicę).

### 42.3. Próba odczytu stanu zaraz po jego ustawieniu
Funkcja `setStan` jest asynchroniczna. Zmiana nie dzieje się natychmiast w tej samej linii kodu.
```javascript
setCount(count + 1);
console.log(count); // Tu nadal będzie STARA wartość!
```
Jeśli potrzebujesz nowej wartości do obliczeń, zrób to przed ustawieniem stanu lub użyj `useEffect`.

### 42.4. Brak `event.preventDefault()` w formularzu
Domyślne zachowanie przeglądarki po wysłaniu formularza to przeładowanie strony. W React (SPA) chcemy tego uniknąć.
```javascript
function handleSubmit(e) {
  e.preventDefault(); // To jest Twoja najważniejsza linia w obsłudze formularzy!
  // ... dalsza logika
}
```

