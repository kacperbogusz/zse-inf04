# Dokumentacja: React

## Spis treści

- [1. Wprowadzenie](#1-wprowadzenie)
  - [1.1. Czym jest React](#11-czym-jest-react)
  - [1.2. Czym jest Single Page Application (SPA)](#12-czym-jest-single-page-application-spa)
  - [1.3. Deklaratywność vs imperatywność](#13-deklaratywność-vs-imperatywność)
  - [1.4. Virtual DOM — jak React aktualizuje stronę](#14-virtual-dom--jak-react-aktualizuje-stronę)
  - [1.5. Jak korzystać z tego poradnika](#15-jak-korzystać-z-tego-poradnika)
- [2. Środowisko pracy](#2-środowisko-pracy)
  - [2.1. Node.js, npm i npx](#21-nodejs-npm-i-npx)
  - [2.2. Instalacja Node.js](#22-instalacja-nodejs)
  - [2.3. Sprawdzanie wersji](#23-sprawdzanie-wersji)
  - [2.4. Czym jest Create React App](#24-czym-jest-create-react-app)
  - [2.5. Tworzenie nowego projektu](#25-tworzenie-nowego-projektu)
  - [2.6. Uruchamianie projektu](#26-uruchamianie-projektu)
  - [2.7. Struktura katalogów](#27-struktura-katalogów)
  - [2.8. Czyszczenie projektu startowego](#28-czyszczenie-projektu-startowego)
  - [2.9. Skrypty npm](#29-skrypty-npm)
  - [2.10. Instalacja dodatkowych bibliotek](#210-instalacja-dodatkowych-bibliotek)
- [3. Podstawy JavaScript potrzebne w React](#3-podstawy-javascript-potrzebne-w-react)
  - [3.1. Zmienne — const, let, var](#31-zmienne--const-let-var)
  - [3.2. Typy danych](#32-typy-danych)
  - [3.3. Operatory arytmetyczne](#33-operatory-arytmetyczne)
  - [3.4. Operatory porównania](#34-operatory-porównania)
  - [3.5. Operatory logiczne](#35-operatory-logiczne)
  - [3.6. Template stringi (szablony napisów)](#36-template-stringi-szablony-napisów)
  - [3.7. Instrukcja warunkowa if / else if / else](#37-instrukcja-warunkowa-if--else-if--else)
  - [3.8. Operator trójargumentowy (ternary)](#38-operator-trójargumentowy-ternary)
  - [3.9. Funkcje — deklaracja i wyrażenie](#39-funkcje--deklaracja-i-wyrażenie)
  - [3.10. Funkcje strzałkowe (arrow functions)](#310-funkcje-strzałkowe-arrow-functions)
  - [3.11. Tablice — tworzenie i podstawowe metody](#311-tablice--tworzenie-i-podstawowe-metody)
  - [3.12. Metody tablic kluczowe w React — map, filter, find, reduce](#312-metody-tablic-kluczowe-w-react--map-filter-find-reduce)
  - [3.13. Obiekty](#313-obiekty)
  - [3.14. Destrukturyzacja tablic i obiektów](#314-destrukturyzacja-tablic-i-obiektów)
  - [3.15. Operator spread (...)](#315-operator-spread-)
  - [3.16. Import i export modułów](#316-import-i-export-modułów)
  - [3.17. Konwersje typów](#317-konwersje-typów)
  - [3.18. Metody napisów](#318-metody-napisów)
  - [3.19. Truthy i falsy](#319-truthy-i-falsy)
  - [3.20. Konsola przeglądarki — console.log()](#320-konsola-przeglądarki--consolelog)
  - [3.21. Instrukcja warunkowa switch](#321-instrukcja-warunkowa-switch)
  - [3.22. Pętle (for, while, do...while) i iteracja](#322-pętle-for-while-dowhile-i-iteracja)
  - [3.23. Asynchroniczność (Promises, async/await, try/catch)](#323-asynchroniczność-promises-asyncawait-trycatch)
  - [3.24. Dodatkowe metody tablic — forEach, some, every, slice, splice, concat](#324-dodatkowe-metody-tablic--foreach-some-every-slice-splice-concat)
  - [3.25. Obiekt Math — losowanie, zaokrąglanie, min/max](#325-obiekt-math--losowanie-zaokrąglanie-minmax)
  - [3.26. Obiekt Date — data i czas](#326-obiekt-date--data-i-czas)
  - [3.27. setTimeout i setInterval — opóźnienia i interwały](#327-settimeout-i-setinterval--opóźnienia-i-interwały)
  - [3.28. Operator ?? (nullish coalescing) i ?. (optional chaining)](#328-operator--nullish-coalescing-i--optional-chaining)
  - [3.29. Obsługa błędów — try / catch / finally](#329-obsługa-błędów--try--catch--finally)
  - [3.30. Wyrażenia regularne (RegExp) — podstawy](#330-wyrażenia-regularne-regexp--podstawy)
- [4. JSX — składnia widoku](#4-jsx--składnia-widoku)
  - [4.1. Czym jest JSX](#41-czym-jest-jsx)
  - [4.2. Wstawianie wartości JavaScript w JSX](#42-wstawianie-wartości-javascript-w-jsx)
  - [4.3. Atrybuty HTML vs JSX](#43-atrybuty-html-vs-jsx)
  - [4.4. Zasada jednego elementu nadrzędnego](#44-zasada-jednego-elementu-nadrzędnego)
  - [4.5. Fragmenty — puste znaczniki](#45-fragmenty--puste-znaczniki)
  - [4.6. Komentarze w JSX](#46-komentarze-w-jsx)
  - [4.7. Atrybuty boolean](#47-atrybuty-boolean)
  - [4.8. Co można wstawiać w klamrach — podsumowanie](#48-co-można-wstawiać-w-klamrach--podsumowanie)
  - [4.9. Tagi samozamykające z HTML w JSX (Zasada zamknięcia)](#49-tagi-samozamykające-z-html-w-jsx-zasada-zamknięcia)
  - [4.10. Multimedia ze źródłem (Audio, Soundplayery i Wideo)](#410-multimedia-ze-źródłem-audio-soundplayery-i-wideo)
  - [4.11. Elementy osadzone: Iframe (Mapy, Embedy z YouTube)](#411-elementy-osadzone-iframe-mapy-embedy-z-youtube)
- [5. Komponenty](#5-komponenty)
  - [5.1. Czym jest komponent](#51-czym-jest-komponent)
  - [5.2. Pierwszy komponent funkcyjny](#52-pierwszy-komponent-funkcyjny)
  - [5.3. Komponent statyczny — bez stanu](#53-komponent-statyczny--bez-stanu)
  - [5.4. Kompozycja — komponenty w komponentach](#54-kompozycja--komponenty-w-komponentach)
  - [5.5. Podział na pliki — osobne komponenty](#55-podział-na-pliki--osobne-komponenty)
  - [5.6. Props — przekazywanie danych do komponentu](#56-props--przekazywanie-danych-do-komponentu)
  - [5.7. Props — destrukturyzacja](#57-props--destrukturyzacja)
  - [5.8. Props — wartości domyślne](#58-props--wartości-domyślne)
  - [5.9. Children — zawartość między znacznikami](#59-children--zawartość-między-znacznikami)
  - [5.10. Kiedy dzielić komponent na mniejsze](#510-kiedy-dzielić-komponent-na-mniejsze)
- [6. Stylowanie](#6-stylowanie)
  - [6.1. CSS w projekcie React (CRA)](#61-css-w-projekcie-react-cra)
  - [6.2. className zamiast class](#62-classname-zamiast-class)
  - [6.3. Style inline w JSX](#63-style-inline-w-jsx)
  - [6.4. Dynamiczne klasy CSS](#64-dynamiczne-klasy-css)
  - [6.5. Dynamiczne style inline](#65-dynamiczne-style-inline)
  - [6.6. Organizacja plików CSS](#66-organizacja-plików-css)
- [7. Zdarzenia (Events)](#7-zdarzenia-events)
  - [7.1. onClick — obsługa kliknięcia](#71-onclick--obsługa-kliknięcia)
  - [7.2. onChange — zmiana wartości pola](#72-onchange--zmiana-wartości-pola)
  - [7.3. onSubmit — wysłanie formularza](#73-onsubmit--wysłanie-formularza)
  - [7.4. onBlur — utrata fokusa](#74-onblur--utrata-fokusa)
  - [7.5. Przekazywanie argumentów do handlera](#75-przekazywanie-argumentów-do-handlera)
  - [7.6. Obiekt zdarzenia (event)](#76-obiekt-zdarzenia-event)
  - [7.7. Najczęstsze zdarzenia — tabela](#77-najczęstsze-zdarzenia--tabela)
- [8. Stan komponentu — useState](#8-stan-komponentu--usestate)
  - [8.1. Po co jest stan](#81-po-co-jest-stan)
  - [8.2. Składnia useState](#82-składnia-usestate)
  - [8.3. Stan liczbowy — licznik](#83-stan-liczbowy--licznik)
  - [8.4. Stan tekstowy](#84-stan-tekstowy)
  - [8.5. Stan boolean — przełącznik](#85-stan-boolean--przełącznik)
  - [8.6. Aktualizacja na podstawie poprzedniego stanu](#86-aktualizacja-na-podstawie-poprzedniego-stanu)
  - [8.7. Reset stanu](#87-reset-stanu)
  - [8.8. Stan nie aktualizuje się natychmiast](#88-stan-nie-aktualizuje-się-natychmiast)
  - [8.9. Lazy initial state](#89-lazy-initial-state)
  - [8.10. Zmienna lokalna vs stan — różnica](#810-zmienna-lokalna-vs-stan--różnica)
- [9. Formularze kontrolowane](#9-formularze-kontrolowane)
  - [9.1. Czym jest formularz kontrolowany](#91-czym-jest-formularz-kontrolowany)
  - [9.2. Input text](#92-input-text)
  - [9.3. Input number](#93-input-number)
  - [9.4. Input password](#94-input-password)
  - [9.5. Select — lista rozwijana](#95-select--lista-rozwijana)
  - [9.6. Textarea](#96-textarea)
  - [9.7. Checkbox](#97-checkbox)
  - [9.8. Checkbox jako switch (Bootstrap)](#98-checkbox-jako-switch-bootstrap)
  - [9.9. Radio — wybór jednej opcji](#99-radio--wybór-jednej-opcji)
  - [9.10. Range — suwak](#910-range--suwak)
  - [9.11. Formularz jako jeden obiekt stanu](#911-formularz-jako-jeden-obiekt-stanu)
  - [9.12. Walidacja formularza](#912-walidacja-formularza)
  - [9.13. Reset formularza](#913-reset-formularza)
- [10. Renderowanie warunkowe](#10-renderowanie-warunkowe)
  - [10.1. if przed return](#101-if-przed-return)
  - [10.2. Operator trójargumentowy w JSX](#102-operator-trójargumentowy-w-jsx)
  - [10.3. Operator && — warunkowe wyświetlanie](#103-operator----warunkowe-wyświetlanie)
  - [10.4. Komunikaty błędów walidacji](#104-komunikaty-błędów-walidacji)
  - [10.5. Obsługa pustej listy](#105-obsługa-pustej-listy)
- [11. Tablice i renderowanie list](#11-tablice-i-renderowanie-list)
  - [11.1. Renderowanie tablicy przez map()](#111-renderowanie-tablicy-przez-map)
  - [11.2. Atrybut key — dlaczego jest wymagany](#112-atrybut-key--dlaczego-jest-wymagany)
  - [11.3. Lista numerowana](#113-lista-numerowana)
  - [11.4. Dodawanie elementu do tablicy stanu](#114-dodawanie-elementu-do-tablicy-stanu)
  - [11.5. Usuwanie elementu z tablicy stanu](#115-usuwanie-elementu-z-tablicy-stanu)
  - [11.6. Aktualizacja jednego elementu w tablicy](#116-aktualizacja-jednego-elementu-w-tablicy)
  - [11.7. Sortowanie tablicy w stanie](#117-sortowanie-tablicy-w-stanie)
- [12. Obiekty w stanie](#12-obiekty-w-stanie)
  - [12.1. Model danych — tablica obiektów](#121-model-danych--tablica-obiektów)
  - [12.2. Kopiowanie obiektu — spread](#122-kopiowanie-obiektu--spread)
  - [12.3. Formularz jako obiekt stanu](#123-formularz-jako-obiekt-stanu)
  - [12.4. Dane z pliku przepisane do kodu](#124-dane-z-pliku-przepisane-do-kodu)
- [13. Bootstrap w React — Kompletny Przewodnik](#13-bootstrap-w-react--kompletny-przewodnik)
  - [13.1. Instalacja i konfiguracja Bootstrapa](#131-instalacja-i-konfiguracja-bootstrapa)
  - [13.2. Czysty Bootstrap (CSS) vs React-Bootstrap (Komponenty)](#132-czysty-bootstrap-css-vs-react-bootstrap-komponenty)
  - [13.3. System Grid (Siatka 12-kolumnowa) w detalach](#133-system-grid-siatka-12-kolumnowa-w-detalach)
  - [13.4. Flexbox z Bootstrapem (Klasy d-flex)](#134-flexbox-z-bootstrapem-klasy-d-flex)
  - [13.5. Typografia, kolory i tła](#135-typografia-kolory-i-tła)
  - [13.6. Wymiary, Marginesy i paddingi (Spacing)](#136-wymiary-marginesy-i-paddingi-spacing)
  - [13.7. Przyciski (Buttons) i grupy przycisków](#137-przyciski-buttons-i-grupy-przycisków)
  - [13.8. Formularze zaawansowane (Input, Select, Switch, Walidacja)](#138-formularze-zaawansowane-input-select-switch-walidacja)
  - [13.9. Karty (Cards) i bogate układy](#139-karty-cards-i-bogate-układy)
  - [13.10. Tabele i paginacja](#1310-tabele-i-paginacja)
  - [13.11. Komponenty UI: Alerty, Odznaki, Paski postępu i Spinnery](#1311-komponenty-ui-alerty-odznaki-paski-postępu-i-spinnery)
  - [13.12. Złożony przykład praktyczny: Panel Użytkownika](#1312-złożony-przykład-praktyczny-panel-użytkownika)
- [14. Obrazy i zasoby statyczne](#14-obrazy-i-zasoby-statyczne)
  - [14.1. Obrazy z folderu public](#141-obrazy-z-folderu-public)
  - [14.2. Obrazy z folderu src — import](#142-obrazy-z-folderu-src--import)
  - [14.3. Obraz zależny od stanu](#143-obraz-zależny-od-stanu)
  - [14.4. Obrazy w kolekcjach (tablicach obiektów)](#144-obrazy-w-kolekcjach-tablicach-obiektów)
  - [14.5. Atrybut alt — dostępność](#145-atrybut-alt--dostępność)
- [15. Przepływ danych — props w górę i w dół](#15-przepływ-danych--props-w-górę-i-w-dół)
  - [15.1. Dane płyną z góry na dół (top-down)](#151-dane-płyną-z-góry-na-dół-top-down)
  - [15.2. Callback — dziecko zgłasza zdarzenie rodzicowi](#152-callback--dziecko-zgłasza-zdarzenie-rodzicowi)
  - [15.3. Lifting state up — podnoszenie stanu](#153-lifting-state-up--podnoszenie-stanu)
  - [15.4. Pełny przykład wieloplikowy z przepływem danych](#154-pełny-przykład-wieloplikowy-z-przepływem-danych)
- [16. useEffect i efekty uboczne](#16-useeffect-i-efekty-uboczne)
  - [16.1. Po co jest useEffect](#161-po-co-jest-useeffect)
  - [16.2. useEffect przy starcie aplikacji](#162-useeffect-przy-starcie-aplikacji)
  - [16.3. Tablica zależności](#163-tablica-zależności)
  - [16.4. Cleanup — sprzątanie efektu](#164-cleanup--sprzątanie-efektu)
  - [16.5. localStorage — zapis i odczyt danych](#165-localstorage--zapis-i-odczyt-danych)
  - [16.6. Typowe pułapki useEffect](#166-typowe-pułapki-useeffect)
- [17. useRef — referencje do elementów DOM](#17-useref--referencje-do-elementów-dom)
  - [17.1. Czym jest useRef](#171-czym-jest-useref)
  - [17.2. Ustawianie fokusa na polu](#172-ustawianie-fokusa-na-polu)
  - [17.3. useRef vs useState](#173-useref-vs-usestate)
- [18. Dane lokalne, JSON i fetch](#18-dane-lokalne-json-i-fetch)
  - [18.1. Tablice danych w kodzie](#181-tablice-danych-w-kodzie)
  - [18.2. Import pliku JSON](#182-import-pliku-json)
  - [18.3. Fetch z folderu public](#183-fetch-z-folderu-public)
  - [18.4. Parsowanie danych tekstowych](#184-parsowanie-danych-tekstowych)
- [19. Logika aplikacji poza JSX](#19-logika-aplikacji-poza-jsx)
  - [19.1. Funkcje pomocnicze](#191-funkcje-pomocnicze)
  - [19.2. Osobne moduły z logiką](#192-osobne-moduły-z-logiką)
  - [19.3. Oddzielenie UI od obliczeń](#193-oddzielenie-ui-od-obliczeń)
- [20. Organizacja projektu](#20-organizacja-projektu)
  - [20.1. Nazewnictwo plików i komponentów](#201-nazewnictwo-plików-i-komponentów)
  - [20.2. Folder components](#202-folder-components)
  - [20.3. Folder data](#203-folder-data)
  - [20.4. Folder utils](#204-folder-utils)
  - [20.5. Przykładowa struktura projektu](#205-przykładowa-struktura-projektu)
- [21. Debugowanie](#21-debugowanie)
  - [21.1. Konsola przeglądarki](#211-konsola-przeglądarki)
  - [21.2. React DevTools](#212-react-devtools)
  - [21.3. Typowe błędy składni](#213-typowe-błędy-składni)
  - [21.4. Typowe błędy stanu](#214-typowe-błędy-stanu)
  - [21.5. Typowe błędy formularzy](#215-typowe-błędy-formularzy)
- [22. Najczęstsze pułapki i jak ich unikać](#22-najczęstsze-pułapki-i-jak-ich-unikać)
  - [22.1. Brak key w pętli map()](#221-brak-key-w-pętli-map)
  - [22.2. Mutowanie stanu zamiast tworzenia kopii](#222-mutowanie-stanu-zamiast-tworzenia-kopii)
  - [22.3. Odczyt stanu zaraz po ustawieniu](#223-odczyt-stanu-zaraz-po-ustawieniu)
  - [22.4. Brak event.preventDefault() w formularzu](#224-brak-eventpreventdefault-w-formularzu)
  - [22.5. Zapomnienie o import useState](#225-zapomnienie-o-import-usestate)
  - [22.6. Wywołanie funkcji zamiast przekazania referencji](#226-wywołanie-funkcji-zamiast-przekazania-referencji)
- [23. Build i publikacja projektu](#23-build-i-publikacja-projektu)
  - [23.1. npm run build](#231-npm-run-build)
  - [23.2. Co zawiera folder build](#232-co-zawiera-folder-build)
  - [23.3. Typowe problemy przy buildzie](#233-typowe-problemy-przy-buildzie)
- [24. Dobre praktyki UI i dostępność](#24-dobre-praktyki-ui-i-dostępność)
  - [24.1. Typ przycisku — button vs submit](#241-typ-przycisku--button-vs-submit)
  - [24.2. Label i htmlFor](#242-label-i-htmlfor)
  - [24.3. Semantyczny układ strony](#243-semantyczny-układ-strony)
- [25. Routing i Nawigacja w SPA (react-router-dom)](#25-routing-i-nawigacja-w-spa-react-router-dom)
- [26. Wzorce praktyczne](#26-wzorce-praktyczne)
  - [26.1. Formularz rejestracji](#261-formularz-rejestracji)
  - [26.2. Zapisy na kurs](#262-zapisy-na-kurs)
  - [26.3. Formularz filmu](#263-formularz-filmu)
  - [26.4. Galeria zdjęć z kategoriami](#264-galeria-zdjęć-z-kategoriami)
  - [26.5. Lista zadań (Todo App) — wieloplikowy](#265-lista-zadań-todo-app--wieloplikowy)
  - [26.6. Generator hasła](#266-generator-hasła)
  - [26.7. Kalkulator BMI](#267-kalkulator-bmi)
  - [26.8. Widok kart z filtrami i wyszukiwaniem](#268-widok-kart-z-filtrami-i-wyszukiwaniem)
  - [26.9. Mixer kolorów RGB](#269-mixer-kolorów-rgb)
  - [26.10. Kości do gry z blokowaniem](#2610-kości-do-gry-z-blokowaniem)
  - [26.11. Licznik z historią operacji](#2611-licznik-z-historią-operacji)
  - [26.12. Algorytmy — sumowanie, zliczanie, filtrowanie](#2612-algorytmy--sumowanie-zliczanie-filtrowanie)
  - [26.13. Prosta Playlista Audio (Odtwarzacz ze stanem)](#2613-prosta-playlista-audio-odtwarzacz-ze-stanem)
  - [26.14. Akordeon FAQ z widocznością (Sekcje Rozwijane)](#2614-akordeon-faq-z-widocznością-sekcje-rozwijane)
  - [26.15. Formularz zamówienia pizzy](#2615-formularz-zamówienia-pizzy)
  - [26.16. Przelicznik walut](#2616-przelicznik-walut)
  - [26.17. Galeria zdjęć z lightboxem i ulubionymi](#2617-galeria-zdjęć-z-lightboxem-i-ulubionymi)



---

> **Jak korzystać z tego poradnika:** Każdy rozdział jest samodzielny — możesz czytać je w dowolnej kolejności. Rozdziały 1–12 warto jednak czytać po kolei, ponieważ każdy z nich buduje na wiedzy z poprzedniego. Przykłady kodu są gotowe do uruchomienia — możesz je skopiować i przetestować w swoim projekcie React. Pliki, w których powinien znaleźć się kod, są zawsze oznaczone komentarzem na początku bloku kodu.

---

## 1. wprowadzenie

### 1.1. czym jest React

React to biblioteka JavaScript stworzona przez zespół Facebooka (Meta) w 2013 roku. Służy do budowania interfejsów użytkownika (UI). Nie jest pełnym frameworkiem — odpowiada wyłącznie za warstwę widoku. Oznacza to, że React nie narzuca sposobu obsługi routingu, zapytań do serwera ani zarządzania bazą danych. W podstawowych projektach te rzeczy nie są zazwyczaj potrzebne.

Najważniejsza zasada Reacta brzmi: **widok jest funkcją danych**. Jeżeli zmienią się dane (stan) w komponencie, React automatycznie odświeży odpowiedni fragment strony. Programista nie musi ręcznie wyszukiwać elementów DOM i zmieniać ich tekstu — React robi to sam.

React opiera się na **komponentach**. Komponent to funkcja JavaScript, która zwraca fragment widoku (napisany w składni JSX, która wygląda jak HTML). Cała aplikacja jest drzewem komponentów — od jednego głównego (`App`) aż po najmniejsze przyciski i etykiety.

### 1.2. czym jest single page application (SPA)

SPA, czyli Single Page Application (aplikacja jednostronicowa), to aplikacja webowa, która działa na jednej stronie HTML. Przeglądarka ładuje plik `index.html` oraz pliki JavaScript i CSS. Od tego momentu widok zmienia się bez pełnego przeładowania strony — wszystko odbywa się dynamicznie po stronie klienta (przeglądarki).

Proste aplikacje Reactowe są właśnie małymi SPA. W typowych, mniejszych projektach zwykle:

- nie ma backendu (serwera)
- nie ma bazy danych
- nie ma routingu (wielu podstron)
- dane są wpisane w kodzie lub skopiowane z pliku `dane.txt`

### 1.3. deklaratywność vs imperatywność

Przesiadka z czystego JavaScriptu na Reacta wymaga zmiany sposobu myślenia.

**Podejście imperatywne (czysty JavaScript / DOM):** Mówisz krok po kroku, *jak* coś zrobić. „Znajdź przycisk, dodaj do niego zdarzenie, znajdź akapit, zmień jego tekst na »Cześć«". Musisz ręcznie pilnować każdego elementu na stronie.

```js
// Podejście imperatywne — czysty JavaScript
const btn = document.querySelector("#btn");
const output = document.querySelector("#output");

btn.addEventListener("click", function () {
  output.textContent = "Kliknięto przycisk!";
});
```

**Podejście deklaratywne (React):** Mówisz, *co* chcesz osiągnąć. „Chcę, aby ten akapit zawsze wyświetlał to, co jest w zmiennej `komunikat`". React sam zajmie się aktualizacją DOM, gdy zmienna ulegnie zmianie.

```jsx
// Podejście deklaratywne — React
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [komunikat, setKomunikat] = useState("Czekam na kliknięcie...");

  return (
    <div>
      <button onClick={() => setKomunikat("Kliknięto przycisk!")}>
        Kliknij
      </button>
      <p>{komunikat}</p>
    </div>
  );
}

export default App;
```

To jak zamawianie pizzy: w podejściu imperatywnym wchodzisz do kuchni i instruujesz kucharza, ile mąki i wody ma dodać. W podejściu deklaratywnym (React) składasz zamówienie: „Chcę margheritę". Restauracja (React) sama dba o to, byś ją otrzymał.

### 1.4. virtual DOM — jak React aktualizuje stronę

Zrozumienie tego mechanizmu pomaga pisać lepszy kod:

1. **Komponenty** to Twoje „klocki" — funkcje zwracające widok.
2. Gdy zmienia się **stan** (`useState`), React tworzy w pamięci nową kopię widoku (tzw. **Virtual DOM**).
3. React **porównuje** tę kopię z tym, co aktualnie widzi użytkownik na ekranie.
4. React znajduje **tylko te różnice** (np. zmienił się tekst w jednym polu) i tylko je przesyła do prawdziwego DOM przeglądarki.

Dzięki temu aplikacje są szybkie, a programista nie musi martwić się o ręczne manipulowanie elementami HTML.

### 1.5. jak korzystać z tego poradnika

| Obszar | Co trzeba umieć | Po co |
|---|---|---|
| Środowisko | `node`, `npm`, `npx`, `npm start` | uruchomienie projektu |
| JavaScript | zmienne, funkcje, tablice, obiekty | pisanie logiki |
| JSX | `className`, `{zmienna}`, fragmenty | pisanie widoku |
| Komponenty | funkcje zwracające JSX | dzielenie UI |
| Props | przekazywanie danych do komponentu | ponowne użycie |
| Stan | `useState` | reakcja na akcje użytkownika |
| Zdarzenia | `onClick`, `onChange`, `onSubmit` | obsługa interakcji |
| Formularze | kontrolowane pola | odczyt danych |
| Listy | `map`, `filter`, `key` | dynamiczne dane |
| Bootstrap | klasy CSS | szybki wygląd |
| Zasoby | obrazy z `public` i `src` | karty, miniatury, ikony |

---

## 2. środowisko pracy

### 2.1. node.js, npm i npx

Zanim zaczniesz pracę z Reactem, musisz zrozumieć trzy narzędzia:

| Narzędzie | Co to jest | Do czego służy |
|---|---|---|
| **Node.js** | Środowisko uruchomieniowe JavaScript | Uruchamia JavaScript poza przeglądarką, obsługuje narzędzia deweloperskie |
| **npm** | Menedżer pakietów (Node Package Manager) | Instaluje biblioteki (np. React, Bootstrap), zarządza zależnościami |
| **npx** | Narzędzie do uruchamiania pakietów | Uruchamia paczkę bez globalnej instalacji (np. Create React App) |

Dodatkowo ważne pojęcia:

| Pojęcie | Opis |
|---|---|
| `package.json` | Plik opisujący projekt — nazwa, wersja, zależności, skrypty |
| `node_modules` | Folder z pobranymi bibliotekami — nie edytujemy go ręcznie |
| `package-lock.json` | Dokładne wersje zainstalowanych pakietów — nie edytujemy ręcznie |

### 2.2. instalacja node.js

Node.js pobieramy ze strony [https://nodejs.org](https://nodejs.org). Wybieramy wersję **LTS** (Long Term Support), która jest stabilna i sprawdzona. Instalator automatycznie instaluje także `npm` i `npx`.

**Windows / macOS:** Pobierz instalator ze strony, uruchom go i postępuj zgodnie z instrukcjami.

**Sprawdzenie po instalacji:** Po zainstalowaniu otwórz terminal (wiersz poleceń) i wpisz:

```bash
node -v
# Wynik np.: v20.11.0

npm -v
# Wynik np.: 10.2.4

npx --version
# Wynik np.: 10.2.4
```

Jeżeli polecenia zwracają numery wersji, instalacja się powiodła.

### 2.3. sprawdzanie wersji

Przed tworzeniem nowego projektu warto upewnić się, że narzędzia są zainstalowane:

```bash
# Sprawdzenie wersji node.js
node -v

# Sprawdzenie wersji npm
npm -v

# Sprawdzenie wersji npx
npx --version
```

Minimalne wymagania dla Create React App:
- Node.js w wersji 14 lub nowszej (zalecana 18+)
- npm w wersji 6 lub nowszej

### 2.4. czym jest create React app

Create React App (skrót: CRA) to narzędzie, które tworzy gotowy projekt Reactowy z pełną konfiguracją. Nie trzeba ręcznie konfigurować bundlera (Webpack), transpilera (Babel) ani serwera deweloperskiego — CRA robi to za nas.

CRA tworzy projekt z:
- Reactem i ReactDOM
- Babelem (kompiluje nowoczesny JavaScript i JSX do kodu zrozumiałego dla przeglądarek)
- Webpackiem (łączy pliki w jeden bundle)
- Serwerem deweloperskim z automatycznym odświeżaniem
- Środowiskiem do testów (`jest`)
- Gotowymi skryptami npm (`start`, `build`, `test`)

> **Uwaga:** Create React App jest obecnie narzędziem, które nie jest już aktywnie rozwijane przez zespół Reacta. Dla nowych projektów profesjonalnych rekomendowane są narzędzia jak Vite. Jednak CRA nadal doskonale sprawdza się do nauki i podstawowych środowisk projektowych, dlatego w tej dokumentacji używamy go świadomie.

### 2.5. tworzenie nowego projektu

Projekt tworzysz w folderze, w którym chcesz mieć katalog aplikacji. Nazwa projektu powinna być:
- pisana małymi literami
- bez spacji
- bez polskich znaków
- słowa oddzielone myślnikami

```bash
# Tworzenie nowego projektu o nazwie "moja-aplikacja"
npx create-react-app moja-aplikacja

# Wejście do folderu projektu
cd moja-aplikacja

# Uruchomienie serwera deweloperskiego
npm start
```

Po uruchomieniu `npm start` przeglądarka powinna automatycznie otworzyć adres `http://localhost:3000` z domyślną stroną startową Reacta.

Jeżeli port 3000 jest zajęty, terminal zapyta, czy użyć innego portu. Potwierdź klawiszem `Y`.

### 2.6. uruchamianie projektu

Po utworzeniu projektu najczęściej używasz dwóch poleceń:

```bash
# Uruchomienie serwera deweloperskiego — używasz codziennie przy pisaniu kodu
npm start

# Zatrzymanie serwera — ctrl + C w terminalu
```

Serwer deweloperski:
- Obserwuje zmiany w plikach źródłowych
- Po zapisaniu pliku automatycznie odświeża stronę w przeglądarce
- Wyświetla błędy kompilacji w terminalu i w przeglądarce
- Działa pod adresem `http://localhost:3000`

### 2.7. struktura katalogów

Po utworzeniu projektu przez CRA otrzymujesz następującą strukturę:

```
moja-aplikacja/
├── node_modules/          # Pobrane biblioteki (nie edytujemy)
├── public/                # Pliki statyczne
│   ├── index.html         # Główny plik HTML aplikacji
│   ├── favicon.ico        # Ikona zakładki przeglądarki
│   └── manifest.json      # Manifest aplikacji webowej
├── src/                   # Kod źródłowy aplikacji
│   ├── App.js             # Główny komponent aplikacji
│   ├── App.css            # Style głównego komponentu
│   ├── App.test.js        # Testy głównego komponentu
│   ├── index.js           # Punkt wejścia — montuje React do HTML
│   ├── index.css          # Style globalne
│   ├── logo.svg           # Logo Reacta (do usunięcia)
│   └── reportWebVitals.js # Metryki wydajności (do usunięcia)
├── package.json           # Konfiguracja projektu i zależności
├── package-lock.json      # Zablokowane wersje pakietów
└── README.md              # Opis projektu
```

**Najważniejsze pliki:**

| Plik | Rola |
|---|---|
| `public/index.html` | Główny plik HTML — zawiera `<div id="root">`, do którego React montuje aplikację |
| `src/index.js` | Punkt wejścia — montuje komponent `App` do elementu `#root` w HTML |
| `src/App.js` | Główny komponent aplikacji — tutaj zaczynasz pracę |
| `src/App.css` | Style dla komponentu App |
| `src/index.css` | Style globalne aplikacji |
| `package.json` | Lista zależności i skrypty npm |

**Jak to działa — przepływ od HTML do komponentu:**

```html
<!-- public/index.html — uproszczony widok -->
<!DOCTYPE html>
<html lang="pl">
  <head>
    <meta charset="utf-8" />
    <title>Moja Aplikacja React</title>
  </head>
  <body>
    <!-- React montuje całą aplikację do tego elementu -->
    <div id="root"></div>
  </body>
</html>
```

```jsx
// src/index.js — punkt wejścia aplikacji
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

// React znajduje element o id="root" w HTML
// i montuje do niego komponent App
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```jsx
// src/App.js — główny komponent
import "./App.css";

function App() {
  return (
    <div>
      <h1>Witaj w React!</h1>
    </div>
  );
}

export default App;
```

`React.StrictMode` to komponent, który w trybie deweloperskim pomaga wykryć potencjalne problemy. Renderuje komponenty dwukrotnie, aby sprawdzić, czy nie mają efektów ubocznych. W trybie produkcyjnym (`npm run build`) StrictMode jest ignorowany.

### 2.8. czyszczenie projektu startowego

Po utworzeniu projektu warto usunąć niepotrzebne pliki startowe i zacząć od czystego szablonu. Oto minimalny zestaw plików po wyczyszczeniu:

```jsx
// src/App.js — wyczyszczony komponent główny
import "./App.css";

function App() {
  return (
    <main>
      <h1>Moja aplikacja React</h1>
      <p>Projekt działa poprawnie.</p>
    </main>
  );
}

export default App;
```

```css
/* src/App.css — wyczyszczony plik stylów */
/* Na razie pusty — dodamy style później */
```

```jsx
// src/index.js — bez zmian, zostaje jak jest
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

Pliki, które można usunąć:
- `src/logo.svg`
- `src/App.test.js`
- `src/reportWebVitals.js`
- `src/setupTests.js`

### 2.9. skrypty npm

Skrypty są zdefiniowane w pliku `package.json`. Dzięki nim nie trzeba pamiętać pełnych poleceń:

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

| Polecenie | Kiedy używać | Efekt |
|---|---|---|
| `npm start` | Podczas pisania kodu | Uruchamia serwer deweloperski |
| `npm run build` | Przed publikacją / oddaniem projektu | Tworzy zoptymalizowany folder `build` |
| `npm test` | Przy testowaniu | Uruchamia testy |
| `npm install nazwa` | Gdy dodajesz bibliotekę | Pobiera pakiet i aktualizuje `package.json` |

Polecenia `eject` prawie nigdy nie używaj. Wyciąga ukrytą konfigurację Webpacka i Babela, co komplikuje projekt.

### 2.10. instalacja dodatkowych bibliotek

Aby zainstalować bibliotekę (np. Bootstrap), używasz polecenia `npm install`:

```bash
# Instalacja bootstrapa
npm install bootstrap

# Instalacja wielu bibliotek naraz
npm install bootstrap react-icons
```

Po instalacji biblioteka pojawia się w `node_modules` i w sekcji `dependencies` w `package.json`. Od tego momentu możesz ją importować w swoich plikach.

---

## 3. podstawy JavaScript potrzebne w React

React jest biblioteką JavaScript, więc znajomość podstaw tego języka jest niezbędna. Ten rozdział prezentuje elementy JavaScriptu, które pojawiają się najczęściej w kodzie Reactowym.

### 3.1. zmienne — const, let, var

Zmienna to "pudełko", w którym przechowujesz dane (tekst, liczby, tablice), by móc ich później użyć w programie. W nowoczesnym JavaScripcie zmienne deklarujemy za pomocą dwóch głównych słów kluczowych: `const` i `let`. Słowo `var` to przeżytek, którego w React już się nie używa.

```js
// 1. const — STAŁA REFERENCJA (Domyślny wybór w React!)
// Używamy go, gdy wiemy, że wartość przypisana do zmiennej nie ulegnie zmianie
// poprzez przypisanie znakiem równości '='.
const nazwaAplikacji = "Mój React App";
const maxUzytkownikow = 100;
// nazwaAplikacji = "Inna aplikacja"; // BŁĄD! Nie można przypisać ponownie do const

// 2. let — ZMIENNA (Używaj tylko tam, gdzie to konieczne)
// Używamy go, gdy wartość z założenia będzie się zmieniać (np. w pętlach).
let licznik = 0;
licznik = licznik + 1; // OK! Zwiększamy wartość o 1
licznik = 10;          // OK! Nadpisujemy nową wartością

// 3. var — STARY STYL (Unikaj)
// Działa podobnie do let, ale ma przestarzały sposób działania tzw. zasięgu (scope),
// co prowadzi do błędów. W React udajemy, że 'var' nie istnieje.
var staryStyl = "nie używaj w React";
```

**Zakres widoczności (Scope):**
Zmienne `let` i `const` "żyją" tylko w obrębie bloku kodu `{ ... }`, w którym zostały utworzone.
```js
if (true) {
  const tajneHaslo = "12345";
  console.log(tajneHaslo); // OK, działa
}
// console.log(tajneHaslo); // BŁĄD! tajneHaslo nie istnieje poza klamrami if-a
```

| Słowo kluczowe | Czy można przypisać ponownie | Zasięg | Typowe użycie |
|---|---|---|---|
| `const` | Nie | Blokowy `{}` | Tablice, obiekty, funkcje, stałe teksty |
| `let` | Tak | Blokowy `{}` | Licznik w pętli, zmienna pomocnicza |
| `var` | Tak | Funkcyjny | Stary kod — niezalecane |

**Ważne:** `const` nie oznacza, że wartość jest niemodyfikowalna. Oznacza, że nie można **przypisać ponownie** zmiennej. Jeżeli `const` wskazuje na tablicę lub obiekt, można modyfikować ich zawartość:

```js
const lista = [1, 2, 3];
lista.push(4);           // OK — modyfikujemy zawartość tablicy
// lista = [5, 6, 7];    // błąd — nie można przypisać ponownie

const osoba = { imie: "Jan" };
osoba.imie = "Anna";     // OK — modyfikujemy pole obiektu
// osoba = {};            // błąd — nie można przypisać ponownie
```

### 3.2. typy danych

JavaScript ma kilka podstawowych typów danych:

| Typ | Opis | Przykłady |
|---|---|---|
| `string` | Tekst (napis) | `"Ala"`, `'React'`, `` `szablon` `` |
| `number` | Liczba (całkowita lub zmiennoprzecinkowa) | `5`, `3.14`, `-10` |
| `boolean` | Wartość logiczna | `true`, `false` |
| `undefined` | Brak przypisanej wartości | `let x;` → `x` jest `undefined` |
| `null` | Celowy brak wartości | `let wynik = null;` |
| `object` | Obiekt (kolekcja par klucz-wartość) | `{ imie: "Jan", wiek: 25 }` |
| `array` | Tablica (technicznie obiekt) | `[1, 2, 3]`, `["a", "b"]` |

```js
// Przykłady każdego typu
const tytul = "Lista kursów";       // string
const liczba = 42;                   // number
const cena = 19.99;                  // number (zmiennoprzecinkowa)
const aktywny = true;                // boolean
let wybrany = undefined;             // undefined
let wynik = null;                    // null
const kurs = { nazwa: "React" };     // object
const oceny = [5, 4, 3, 5, 4];      // array
```

**Sprawdzanie typu:**

```js
console.log(typeof "tekst");     // "string"
console.log(typeof 42);          // "number"
console.log(typeof true);        // "boolean"
console.log(typeof undefined);   // "undefined"
console.log(typeof null);        // "object" (historyczny błąd JS)
console.log(typeof [1, 2]);      // "object" (tablice to obiekty)
console.log(Array.isArray([1])); // true (prawidłowy sposób sprawdzenia tablicy)
```

**Typy prymitywne vs referencyjne:**

To rozróżnienie jest kluczowe dla zrozumienia, dlaczego w React tworzymy kopie obiektów/tablic zamiast je modyfikować.

```js
// PRYMITYWNE (string, number, boolean, null, undefined)
// Kopiowanie tworzy NIEZALEŻNĄ kopię wartości
let a = 5;
let b = a;  // b = 5 (kopia wartości)
b = 10;     // a nadal = 5 (zmiana b nie wpływa na a)

// REFERENCYJNE (object, array, function)
// Kopiowanie kopiuje REFERENCJĘ (wskaźnik), nie wartość!
const arr1 = [1, 2, 3];
const arr2 = arr1;      // arr2 wskazuje na TĘ SAMĄ tablicę!
arr2.push(4);           // arr1 też ma teraz [1, 2, 3, 4]!

// Dlatego w React robimy KOPIĘ:
const arr3 = [...arr1]; // Nowa, niezależna tablica
```

### 3.3. operatory arytmetyczne

| Operator | Nazwa | Przykład | Wynik |
|---|---|---|---|
| `+` | Dodawanie | `10 + 5` | `15` |
| `-` | Odejmowanie | `10 - 5` | `5` |
| `*` | Mnożenie | `10 * 5` | `50` |
| `/` | Dzielenie | `10 / 3` | `3.3333...` |
| `%` | Reszta z dzielenia (modulo) | `10 % 3` | `1` |
| `**` | Potęgowanie | `2 ** 3` | `8` |
| `++` | Inkrementacja | `x++` | Zwiększa o 1 |
| `--` | Dekrementacja | `x--` | Zmniejsza o 1 |

```js
const a = 17;
const b = 5;

console.log(a + b);   // 22
console.log(a - b);   // 12
console.log(a * b);   // 85
console.log(a / b);   // 3.4
console.log(a % b);   // 2 (reszta z dzielenia 17 przez 5)
console.log(a ** b);  // 1419857 (17 do potęgi 5)
```

**Operatory przypisania skróconego:**

```js
let x = 10;
x += 5;   // x = 15 (x = x + 5)
x -= 3;   // x = 12
x *= 2;   // x = 24
x /= 4;   // x = 6
x %= 4;   // x = 2
```

**Operator `+` z tekstem — konkatenacja (łączenie stringów):**

```js
// Gdy jeden z operandów jest stringiem, + łączy teksty
"Cześć" + " " + "świecie"  // "Cześć świecie"
"Wiek: " + 25              // "Wiek: 25" (liczba zamieniona na string)
5 + "3"                    // "53" (nie 8! — string wygrywa)
5 + 3 + " zł"             // "8 zł" (najpierw 5+3=8, potem 8+" zł")
"Cena: " + 5 + 3           // "Cena: 53" (od lewej: string+5="Cena: 5", potem +"3")

// Dlatego w React preferujemy template stringi:
const wynik = `Cena: ${5 + 3} zł`; // "Cena: 8 zł" — jednoznaczne
```

### 3.4. operatory porównania

| Operator | Znaczenie | Przykład | Wynik |
|---|---|---|---|
| `===` | Równe (ścisłe, bez konwersji typów) | `5 === 5` | `true` |
| `!==` | Różne (ścisłe) | `5 !== "5"` | `true` |
| `==` | Równe (z konwersją typów) | `5 == "5"` | `true` |
| `!=` | Różne (z konwersją typów) | `5 != "5"` | `false` |
| `<` | Mniejsze | `3 < 5` | `true` |
| `>` | Większe | `5 > 3` | `true` |
| `<=` | Mniejsze lub równe | `5 <= 5` | `true` |
| `>=` | Większe lub równe | `3 >= 5` | `false` |

**Ważna zasada:** W React (i nowoczesnym JavaScripcie) **zawsze używaj `===` i `!==`** (ścisłe porównanie). Operator `==` dokonuje automatycznej konwersji typów, co prowadzi do nieoczywistych wyników:

```js
// Ścisłe porównanie (rekomendowane)
console.log(5 === 5);     // true
console.log(5 === "5");   // false (różne typy: number vs string)

// Luźne porównanie (unikaj)
console.log(5 == "5");    // true (JavaScript konwertuje string na number)
console.log(0 == false);  // true (nieintuicyjne)
console.log("" == false); // true (nieintuicyjne)
```

### 3.5. operatory logiczne

| Operator | Nazwa | Prawda gdy... |
|---|---|---|
| `&&` | AND (i) | Oba warunki są `true` |
| `\|\|` | OR (lub) | Przynajmniej jeden warunek jest `true` |
| `!` | NOT (negacja) | Warunek jest `false` |

```js
const wiek = 20;
const maBilet = true;

// AND — oba warunki muszą być prawdziwe
if (wiek >= 18 && maBilet) {
  console.log("Możesz wejść");
}

// OR — wystarczy jeden prawdziwy warunek
const x = 5;
if (x < 0 || x > 100) {
  console.log("Poza zakresem");
}

// NOT — odwrócenie wartości logicznej
const zamkniety = false;
if (!zamkniety) {
  console.log("Sklep jest otwarty");
}
```

**Short-circuit evaluation (skrócone obliczanie):**

Operatory `&&` i `||` nie zawsze zwracają `true`/`false` — zwracają jedną z wartości:

```js
// && zwraca PIERWSZĄ wartość falsy LUB ostatnią wartość
"Jan" && "Kowalski"  // "Kowalski" (obie truthy → zwraca ostatnią)
"" && "Kowalski"     // "" (pierwsza falsy → zwraca ją)
null && "cokolwiek"  // null

// || zwraca PIERWSZĄ wartość truthy LUB ostatnią wartość
"" || "domyślny"     // "domyślny" (pierwsza falsy → szuka dalej)
"Jan" || "domyślny"  // "Jan" (pierwsza truthy → zwraca ją)
null || undefined || "ostatni" // "ostatni"

// Praktyczne użycie — wartość domyślna
const imieUsera = pobraneImie || "Anonim";
```

### 3.6. template stringi (szablony napisów)

Template stringi to sposób wstawiania zmiennych i wyrażeń do tekstu. Używają **odwrotnych apostrofów** (backtick) `` ` `` zamiast cudzysłowów. Zmienne wstawiamy w `${}`:

```js
const imie = "Jan";
const wiek = 25;

// Template string — wstawianie zmiennych
const powitanie = `Cześć, ${imie}! Masz ${wiek} lat.`;
console.log(powitanie); // "Cześć, Jan! Masz 25 lat."

// Wyrażenia w ${}
console.log(`Za 5 lat będziesz mieć ${wiek + 5} lat.`);
// "Za 5 lat będziesz mieć 30 lat."

// Wieloliniowy tekst
const tekst = `Linia pierwsza
Linia druga
Linia trzecia`;

// Wywołanie funkcji i metod w ${}
const imieInput = "  jan  ";
const msg = `Witaj, ${imieInput.trim().toUpperCase()}!`; // "Witaj, JAN!"

// Warunek (ternary) w template stringu
const status = `Użytkownik jest ${wiek >= 18 ? "pełnoletni" : "niepełnoletni"}`;

// Dynamiczne klasy CSS w React (bardzo częste!)
const klasa = `btn btn-${aktywny ? "success" : "danger"} ${duzy ? "btn-lg" : ""}`;
```

### 3.7. instrukcja warunkowa if / else if / else

Instrukcja `if` pozwala programowi podejmować decyzje. Działa jak "rozwidlenie dróg" – kod pójdzie w jedną stronę, jeśli warunek jest spełniony (`true`), a w drugą, jeśli nie jest (`false`).

```js
const wiek = 17;

if (wiek >= 18) {
  // Ten kod wykona się TYLKO, jeśli wiek jest większy lub równy 18
  console.log("Jesteś pełnoletni, możesz wejść.");
} else if (wiek >= 13) {
  // Jeśli pierwszy warunek (wiek >= 18) zawiódł, sprawdzany jest ten
  console.log("Jesteś nastolatkiem, dostęp ograniczony.");
} else {
  // Jeśli żaden z powyższych warunków nie jest prawdziwy, wykona się 'else'
  console.log("Jesteś dzieckiem.");
}
```

**Kluczowa zasada dotycząca `if` w JSX:**
W Reakcie funkcja komponentu musi w bloku `return (...)` zwrócić kod JSX (przypominający HTML). **Nie można wstawiać klasycznego bloku `if() { ... }` wewnątrz `return`!** 
Jeśli chcesz użyć tradycyjnego `if`, musisz to zrobić **przed** słowem kluczowym `return`.

```jsx
// POPRAWNIE: użycie if przed return
function MojaStrona({ czyZalogowany }) {
  if (czyZalogowany === true) {
    return <h1>Witaj w systemie!</h1>;
  } else {
    return <h1>Zaloguj się, by zobaczyć treść.</h1>;
  }
}
```

### 3.8. operator trójargumentowy (ternary)

Operator trójargumentowy to skrócona forma `if/else`. Składa się z trzech części: `warunek ? wartość_dlaTrue : wartość_dlaFalse`.

```js
const wiek = 20;
const status = wiek >= 18 ? "Pełnoletni" : "Niepełnoletni";
console.log(status); // "Pełnoletni"
```

Jest niezwykle często używany w JSX do warunkowego wyświetlania:

```jsx
<p>{czyZalogowany ? "Witaj ponownie!" : "Zaloguj się"}</p>
```

### 3.9. funkcje — deklaracja i wyrażenie

Funkcja to nazwany fragment kodu, który "wykonuje jakąś pracę" i może być wywoływany wielokrotnie. Możesz o niej myśleć jak o maszynce – wrzucasz do niej jakieś składniki (parametry), ona robi coś z nimi w środku, a następnie "wypluwa" wynik (przy pomocy `return`). W React każdy komponent jest właśnie taką funkcją!

W JavaScripcie funkcje można definiować na dwa sposoby:

```js
// 1. Deklaracja funkcji (function declaration)
function dodaj(a, b) {
  return a + b;
}

// 2. Wyrażenie funkcyjne (function expression)
const pomnoz = function (a, b) {
  return a * b;
};

// Wywołanie
console.log(dodaj(3, 5));   // 8
console.log(pomnoz(3, 5));  // 15
```

**Parametry domyślne:**

```js
function powitaj(imie = "Gościu") {
  return `Cześć, ${imie}!`;
}

console.log(powitaj("Anna")); // "Cześć, Anna!"
console.log(powitaj());       // "Cześć, Gościu!"
```

**Funkcja bez `return` — zwraca `undefined`:**

```js
function wyswietl(tekst) {
  console.log(tekst);
  // Brak return — funkcja zwraca undefined
}

const wynik = wyswietl("Cześć"); // wynik = undefined
```

**Wiele wartości — zwracanie obiektu lub tablicy:**

```js
function obliczStatystyki(liczby) {
  const suma = liczby.reduce((a, b) => a + b, 0);
  const srednia = suma / liczby.length;
  return { suma, srednia }; // Zwracamy obiekt z wieloma wartościami
}

const { suma, srednia } = obliczStatystyki([10, 20, 30]);
```

### 3.10. funkcje strzałkowe (arrow functions)

Funkcje strzałkowe to krótsza składnia funkcji, bardzo popularna w React:

```js
// Pełna forma funkcji strzałkowej
const dodaj = (a, b) => {
  return a + b;
};

// Skrócona forma — jeśli ciało to jedno wyrażenie, nie trzeba {} i return
const podwoj = (x) => x * 2;

// Dla jednego parametru nawiasy () są opcjonalne
const kwadrat = x => x * x;

// Bez parametrów — puste nawiasy obowiązkowe
const losuj = () => Math.random();
```

**Dlaczego strzałki są ważne w React:**

```jsx
// Obsługa zdarzenia — funkcja strzałkowa inline
<button onClick={() => setLicznik(licznik + 1)}>Dodaj</button>

// Renderowanie listy — strzałka w map
{kursy.map((kurs) => <li key={kurs}>{kurs}</li>)}

// Filtrowanie — strzałka w filter
{produkty.filter((p) => p.cena < 100).map((p) => <p key={p.id}>{p.nazwa}</p>)}
```

**Parametr rest (`...`) — zbieranie wielu argumentów w tablicę:**

```js
// Rest parameter zbiera "resztę" argumentów do tablicy
function suma(...liczby) {
  return liczby.reduce((acc, n) => acc + n, 0);
}
suma(1, 2, 3)       // 6
suma(10, 20, 30, 40) // 100

// Połączenie zwykłych parametrów z rest
function log(poziom, ...wiadomosci) {
  wiadomosci.forEach(msg => console.log(`[${poziom}] ${msg}`));
}
log("INFO", "Start", "Połączono", "Gotowe");
```

### 3.11. tablice — tworzenie i podstawowe metody

Tablice (arrays) to uporządkowane kolekcje elementów. W React są fundamentalne — listy, karty, formularze wieloelementowe — wszystko opiera się na tablicach.

```js
// Tworzenie tablicy
const kursy = ["HTML", "CSS", "JavaScript", "React"];

// Dostęp do elementów (indeksowanie od 0)
console.log(kursy[0]);       // "HTML"
console.log(kursy[3]);       // "React"
console.log(kursy.length);   // 4

// Dodawanie elementu na koniec
kursy.push("Node.js");

// Usuwanie ostatniego elementu
kursy.pop();

// Dodawanie elementu na początek
kursy.unshift("Wstęp do IT");

// Usuwanie pierwszego elementu
kursy.shift();

// Sprawdzenie, czy element istnieje
console.log(kursy.includes("React")); // true
console.log(kursy.indexOf("CSS"));    // 1

// Iteracja przez tablicę
for (let i = 0; i < kursy.length; i++) {
  console.log(`${i + 1}. ${kursy[i]}`);
}

// Iteracja przez for...of
for (const kurs of kursy) {
  console.log(kurs);
}
```

### 3.12. metody tablic kluczowe w React — map, filter, find, reduce

W React niemal wszystkie operacje na listach elementów opierają się na czterech podstawowych metodach wbudowanych w JavaScript. Co kluczowe, w przypadku Reacta zależy nam na "niemutowalności" (immutability), dlatego każda z wymienionych metod **nie modyfikuje oryginalnej tablicy, ale zwraca zupełnie nową**. 

Dzięki temu React jest w stanie poprawnie zauważyć zmianę w danych i odświeżyć widok. Unikać należy używania metod klasycznych, jak `push()` czy `splice()`, które ukradkiem zmieniają tablicę bez powiadamiania Reacta.

#### 1. `map()` — transformacja elementów i generowanie list HTML
Metoda `map()` pozwala "przejść" przez każdy element tablicy wejściowej i przekształcić go, jednocześnie tworząc nową tablicę o dokładnie tej samej długości. Jej najczęstszym, kluczowym zadaniem jest generowanie zestawu znaczników (np. `<li>` lub niestandardowych komponentów) na podstawie danych.

```js
const liczby = [1, 2, 3, 4, 5];

// Starszy zapis z klasyczną definicją funkcji
const podwojone = liczby.map(function(liczba) {
  return liczba * 2; 
}); // Wynik: [2, 4, 6, 8, 10]

// Nowoczesny i preferowany w React zapis strzałkowy:
const potrojone = liczby.map(liczba => liczba * 3);

// WYKORZYSTANIE PRAKTYCZNE: Pobieranie atrybutu (np. nazwy) z każdego obiektu
const produkty = [
  { id: 1, nazwa: "Klawiatura", cena: 200 },
  { id: 2, nazwa: "Myszka", cena: 100 }
];

const zmapowaneNazwy = produkty.map(produkt => produkt.nazwa);
console.log(zmapowaneNazwy); // ["Klawiatura", "Myszka"]
```

Gdy w komponencie React wykorzystujesz funkcję `map()` do generowania znaczników z użyciem kodu JSX/HTML, **masz absolutny obowiązek przypisać do powielanego wrappera atrybut nazwany `key`**. To jedyny sposób, w jaki mechanizmy optymalizacji Reacta potrafią śledzić powtarzalność.

```jsx
function ListaZadan() {
    const listaZadan = ["Zrobić zakupy", "Odebrać paczkę", "Umyć auto"];
    
    return (
        <ul>
            {listaZadan.map(zadanie => (
                // Zawsze ustawiamy unikalny key! Najlepiej identyfikator (id) lub ciąg znaków, jeśli jest unikalny.
                <li key={zadanie} className="zadanie">
                     {zadanie}
                </li>
            ))}
        </ul>
    );
};
```

#### 2. `filter()` — odsiewanie obiektów z kolekcji
Metoda `filter()` wyciąga z elementu wszystkie wpisy, które spełnią Twój dany warunek i umieszcza je w nowo zwracanej powłoce tablicowej. W instrukcji strzałkowej `filter()` określasz logiczny test do sprawdzenia (gdzie wynik prawdziwy `true` zostawia element).

```js
const uzytkownicy = [
  { id: 1, imie: "Anna", wiek: 22 },
  { id: 2, imie: "Marek", wiek: 35 },
  { id: 3, imie: "Piotr", wiek: 15 }
];

// Zostawienie pełnoletnich:
const dorosli = uzytkownicy.filter(osoba => osoba.wiek >= 18);
// Zostaną Anna i Marek.

// KLUCZOWY WZORZEC DLA REACT: "Usuwanie" rzczy używając filter() w Stanie.
// Chcąc np. usunąć usera o id = 2, nie stosujemy splice().
// Pozostawiamy po prostu wszystkich tych, którzy takiego id NIE MAJĄ:
const idDoUsuniecia = 2;
const aktywniUzytkownicy = uzytkownicy.filter(osoba => osoba.id !== idDoUsuniecia);
```

#### 3. `find()` — zwrócenie pierwszego pasującego wyniku
`find()` operuje podobnie jak `filter()`, jednak zamiast sprawdzać do końca i zwracać wyselekcjonowaną tablicę wyników – `find()` zwraca wprost **jeden obiekt**. W momencie, w którym pierwszy obiekt spotka się z wynikiem `true`, cała operacja jest przerywana z celowo odnalezioną pozycją.

```js
const powiadomienia = [
  { pId: 101, typ: "Info", tresc: "Witaj" },
  { pId: 105, typ: "Ostrzezenie", tresc: "Blad serwera" }
];

// Odszukujemy pojedynczy element:
const pierwszyBlad = powiadomienia.find(element => element.typ === "Ostrzezenie");

console.log(pierwszyBlad); 
// Zawiera tylko sam odzyskany obiekt: { pId: 105, typ: "Ostrzezenie", tresc: "Blad serwera" }
```

#### 4. `reduce()` — analiza całej tablicy w jeden zwarty wynik
Metoda `reduce` jest kluczowa tam, gdzie np. z wieloelementowego koszyka w e-commerce musisz wyciągnąć jedną ostateczną cyfrę: "Suma do Zapłaty". Agreguje ona kolejne wiersze przekształcając je za pomocą pętli. Pętla wymusza zdefiniowanie minimum dwóch parametrów. Np. "Akumulatora" (oznaczającego ułamek sumy przechodzący rosnąco dalej z pętli do pętli) oraz reprezentanta "Bieżącej Pozycji" (odczytywanej przez krok w tablicy).

W argumencie numer dwa (dodawanym zawsze po deklaracji skomplikowanej funkcji liczącej) ustalamy stan startowy licznika: zazwyczaj `0`.

```js
const koszykKosmetykow = [
    { nazwa: "Krem", cena: 45, ilosc: 2 }, 
    { nazwa: "Balsam", cena: 15, ilosc: 1 }, 
    { nazwa: "Szampon", cena: 20, ilosc: 3 } 
];

// Sprawny kalkulator:
const sumaCalkowita = koszykKosmetykow.reduce((akumulatorKosztow, aktualnyProdukt) => {
    
    // Obliczamy cenę cząstkową danej sekcji koszyka wejściowej:
    const cenaJednostkowaRazySztuki = aktualnyProdukt.cena * aktualnyProdukt.ilosc;

    // Podwajamy i zwracamy "narośnięte saldo" przekazując kolejnemu obiegowi nową wagę 
    return akumulatorKosztow + cenaJednostkowaRazySztuki;
    
}, 0); // Kasa przed zakupami z zerowym stanem wyniosła ZERO zł.

console.log(sumaCalkowita); // Ujrzysz całkowitą wyciągniętą pojedynczą liczbę finalną: 165.
```


### 3.13. obiekty

Obiekty to kolekcje par klucz-wartość. Są podstawą modelowania danych w React:

```js
// Tworzenie obiektu
const zdjecie = {
  id: 1,
  nazwa: "kwiat.jpg",
  kategoria: "kwiaty",
  pobrania: 0,
};

// Dostęp do pól — notacja kropkowa
console.log(zdjecie.nazwa);       // "kwiat.jpg"
console.log(zdjecie.kategoria);   // "kwiaty"

// Dostęp do pól — notacja nawiasowa (przydatna z dynamicznym kluczem)
const pole = "kategoria";
console.log(zdjecie[pole]);       // "kwiaty"

// Modyfikacja pola
zdjecie.pobrania = 5;

// Dodanie nowego pola
zdjecie.autor = "Jan Kowalski";

// Sprawdzenie, czy pole istnieje
console.log("nazwa" in zdjecie);  // true
```

**Metody obiektu — Object.keys, Object.values, Object.entries:**

```js
const osoba = { imie: "Jan", wiek: 25, miasto: "Kraków" };

// Tablica kluczy
Object.keys(osoba)    // ["imie", "wiek", "miasto"]

// Tablica wartości
Object.values(osoba)  // ["Jan", 25, "Kraków"]

// Tablica par [klucz, wartość]
Object.entries(osoba) // [["imie", "Jan"], ["wiek", 25], ["miasto", "Kraków"]]

// Liczba pól w obiekcie
Object.keys(osoba).length // 3

// Iteracja po obiekcie
Object.entries(osoba).forEach(([klucz, wartosc]) => {
  console.log(`${klucz}: ${wartosc}`);
});

// Sprawdzenie czy obiekt jest pusty
const pusty = {};
Object.keys(pusty).length === 0 // true
```

**Tablica obiektów — najczęstsza struktura danych w React:**

```js
const filmy = [
  { id: 1, tytul: "Matrix", rodzaj: "Sci-Fi", rok: 1999 },
  { id: 2, tytul: "Incepcja", rodzaj: "Sci-Fi", rok: 2010 },
  { id: 3, tytul: "Titanic", rodzaj: "Dramat", rok: 1997 },
];

// Filtrowanie po rodzaju
const scifi = filmy.filter((f) => f.rodzaj === "Sci-Fi");

// Mapowanie do listy tytułów
const tytuly = filmy.map((f) => f.tytul);
// ["Matrix", "Incepcja", "Titanic"]
```

### 3.14. destrukturyzacja tablic i obiektów

Destrukturyzacja to sposób na „wyciągnięcie" wartości z tablicy lub obiektu do osobnych zmiennych. Jest niezwykle często używana w React.

**Destrukturyzacja obiektów:**

```js
const film = { tytul: "Incepcja", rodzaj: "Sci-Fi", rok: 2010 };

// Zamiast:
// const tytul = film.tytul;
// const rodzaj = film.rodzaj;

// Destrukturyzacja:
const { tytul, rodzaj, rok } = film;
console.log(tytul);  // "Incepcja"
console.log(rodzaj); // "Sci-Fi"
console.log(rok);    // 2010
```

**Destrukturyzacja tablic:**

```js
const kolory = [120, 80, 200];
const [r, g, b] = kolory;
console.log(r); // 120
console.log(g); // 80
console.log(b); // 200
```

**Destrukturyzacja w React — useState:**

```jsx
// useState zwraca tablicę [wartość, funkcjaZmieniająca]
// Destrukturyzacja wyciąga oba elementy
const [licznik, setLicznik] = useState(0);
const [imie, setImie] = useState("");
const [aktywny, setAktywny] = useState(false);
```

**Destrukturyzacja props:**

```jsx
// Zamiast function Karta(props) { ... props.tytul ... }
function Karta({ tytul, opis, cena }) {
  return (
    <div>
      <h3>{tytul}</h3>
      <p>{opis}</p>
      <p>Cena: {cena} zł</p>
    </div>
  );
}
```

**Alias (zmiana nazwy) przy destrukturyzacji:**

```js
const osoba = { imie: "Jan", wiek: 25 };
const { imie: firstName, wiek: age } = osoba;
console.log(firstName); // "Jan"
console.log(age);       // 25
```

**Wartości domyślne w destrukturyzacji:**

```js
const { imie, miasto = "Nieznane" } = { imie: "Jan" };
console.log(miasto); // "Nieznane" (bo nie było w obiekcie)

const [a = 0, b = 0, c = 0] = [10, 20];
console.log(c); // 0 (bo tablica miała tylko 2 elementy)
```

**Zagnieżdżona destrukturyzacja:**

```js
const user = {
  imie: "Jan",
  adres: { miasto: "Kraków", kod: "30-001" }
};

const { imie, adres: { miasto, kod } } = user;
console.log(miasto); // "Kraków"
console.log(kod);    // "30-001"
```

**Pomijanie elementów tablicy:**

```js
const [, drugi, , czwarty] = [10, 20, 30, 40];
console.log(drugi);   // 20
console.log(czwarty); // 40
```

### 3.15. operator spread (...)

Operator spread (`...`) „rozkłada" tablicę lub obiekt na poszczególne elementy. Jest kluczowy w React do **niemutowalnej aktualizacji stanu**:

**Spread tablicy:**

```js
const stare = [1, 2, 3];

// Kopia tablicy
const kopia = [...stare];

// Dodanie elementu na koniec (zamiast push)
const nowa = [...stare, 4];
// [1, 2, 3, 4]

// Dodanie elementu na początek
const nowa2 = [0, ...stare];
// [0, 1, 2, 3]

// Łączenie tablic
const a = [1, 2];
const b = [3, 4];
const polaczone = [...a, ...b];
// [1, 2, 3, 4]
```

**Spread obiektu:**

```js
const stary = { imie: "Jan", wiek: 25 };

// Kopia obiektu
const kopia = { ...stary };

// Kopia z modyfikacją jednego pola
const zaktualizowany = { ...stary, wiek: 26 };
// { imie: "Jan", wiek: 26 }

// Kopia z dodaniem nowego pola
const rozszerzony = { ...stary, miasto: "Kraków" };
// { imie: "Jan", wiek: 25, miasto: "Kraków" }
```

**W React — niemutowalna aktualizacja stanu:**

```jsx
// Dodanie elementu do tablicy stanu
setZadania((prev) => [...prev, noweZadanie]);

// Usunięcie elementu z tablicy stanu
setZadania((prev) => prev.filter((z) => z.id !== idDoUsuniecia));

// Aktualizacja jednego pola obiektu w stanie
setFormularz((prev) => ({ ...prev, imie: "Anna" }));
```

**Uwaga — spread tworzy PŁYTKĄ kopię (shallow copy):**

Spread kopiuje tylko pierwszy poziom. Zagnieżdżone obiekty nadal są współdzielone:

```js
const original = { imie: "Jan", adres: { miasto: "Kraków", kod: "30-001" } };
const kopia = { ...original };

kopia.imie = "Anna";           // OK — nie zmienia oryginału
kopia.adres.miasto = "Warszawa"; // UWAGA — zmienia też oryginał!

// Głęboka kopia zagnieżdżonego obiektu:
const gleboka = { ...original, adres: { ...original.adres } };
gleboka.adres.miasto = "Gdańsk"; // Teraz oryginał jest bezpieczny

// Alternatywa — structuredClone (nowoczesne przeglądarki)
const pelnaKopia = structuredClone(original);
```

### 3.16. import i export modułów (Szczegółowo)

Podział kodu na mniejsze pliki (moduły) to fundament pracy z Reactem. Zamiast pisać tysiące linijek w jednym pliku `App.js`, wyodrębniamy komponenty, dane i funkcje do osobnych plików, a następnie używamy mechanizmów `export` i `import`, by je ze sobą łączyć.

**1. Export domyślny (Default Export)**
Używany najczęściej do eksportowania głównego komponentu z pliku. W jednym pliku może być tylko jeden export domyślny.

```js
// Plik: src/components/Header.js
function Header() {
  return <header>Witaj na stronie</header>;
}

// Zazwyczaj na samym dole pliku
export default Header;
```
Importowanie tego pliku:
```js
// Plik: src/App.js
// Ważne: Możesz nadać dowolną nazwę podczas importu z funkcji default!
import Header from "./components/Header";
import MojNaglowek from "./components/Header"; // zadziała tak samo!
```

**2. Export nazwany (Named Export)**
Używany, gdy z jednego pliku chcemy wyeksportować wiele rzeczy (np. paczka różnych funkcji matematycznych, stałych wartości lub mini-komponentów).

```js
// Plik: src/utils/matematyka.js
export function dodaj(a, b) { return a + b; }
export function odejmij(a, b) { return a - b; }
export const WERSJA_API = "1.0.0";
```
Importowanie:
```js
// Plik: src/App.js
// Ważne: Przy exporcie nazwanym musisz użyć dokładnie tych samych nazw wewnątrz nawiasów klamrowych {}.
import { dodaj, odejmij, WERSJA_API } from "./utils/matematyka";

// Możesz jednak nałożyć alias (zmianę nazwy), jeśli nazwa koliduje w obecnym pliku:
import { dodaj as dodajLiczby } from "./utils/matematyka";
```

**3. Co jeszcze można importować w React?**
W ekosystemie React za pomocą instrukcji `import` możemy wciągać nie tylko JavaScript! Narzędzia takie jak Webpack czy Vite pozwalają na:
- **Import CSS:** `import "./styles.css";` (aby podłączyć style globalnie dla komponentu)
- **Import Obrazów:** `import logoImg from "./logo.png";` (daje nową powiastkę ze ścieżką do grafiki, co uodparnia na błędy ścieżek względem foleru public!)
- **Import bibliotek:** `import "bootstrap/dist/css/bootstrap.css";`

### 3.17. konwersje typów

W JavaScript ważne jest rozumienie konwersji typów, szczególnie przy formularzach:

```js
// String → Number
const tekst = "42";
const liczba = Number(tekst);         // 42
const liczba2 = parseInt(tekst);      // 42 (tylko całkowite)
const liczba3 = parseFloat("3.14");   // 3.14
const liczba4 = +"42";               // 42 (skrócona konwersja)

// Number → String
const num = 42;
const str = String(num);              // "42"
const str2 = num.toString();          // "42"

// Uwaga na NaN — Not a Number
console.log(Number("abc"));           // NaN
console.log(isNaN(Number("abc")));    // true

// Konwersja na Boolean
Boolean(0)          // false
Boolean("")         // false
Boolean(null)       // false
Boolean(undefined)  // false
Boolean("tekst")    // true
Boolean(42)         // true
Boolean([])         // true (pusta tablica to truthy!)
!!""                // false (podwójna negacja — skrócona konwersja na boolean)

// Zaokrąglanie
console.log(Math.round(3.7));   // 4
console.log(Math.floor(3.7));   // 3 (zaokrąglenie w dół)
console.log(Math.ceil(3.2));    // 4 (zaokrąglenie w górę)
console.log(3.14159.toFixed(2)); // "3.14" (zwraca string!)
```

**Ważne w formularzu React:** `input` zawsze zwraca wartość jako `string`. Jeżeli potrzebujesz `number`, musisz go jawnie skonwertować:

```jsx
// e.target.value to ZAWSZE string, nawet dla input type="number"
const handleChange = (e) => {
  setWiek(Number(e.target.value)); // Konwersja na liczbę
};
```

### 3.18. metody napisów

Metody napisów (stringów) są często potrzebne przy walidacji formularzy i przetwarzaniu tekstu:

```js
const tekst = "  Witaj w React!  ";

// Usunięcie białych znaków z początku i końca
console.log(tekst.trim());           // "Witaj w React!"

// Zamiana na wielkie/małe litery
console.log(tekst.trim().toUpperCase()); // "WITAJ W REACT!"
console.log(tekst.trim().toLowerCase()); // "witaj w react!"

// Sprawdzenie zawartości
console.log("email@example.com".includes("@"));   // true
console.log("abc123".startsWith("abc"));           // true
console.log("plik.pdf".endsWith(".pdf"));          // true

// Wycinanie fragmentu
const imie = "Jan Kowalski";
console.log(imie.slice(0, 3));       // "Jan"
console.log(imie.slice(4));          // "Kowalski"

// Podział tekstu na tablicę
const csv = "Jan,Kowalski,25";
const czesci = csv.split(",");
// ["Jan", "Kowalski", "25"]

// Zamiana fragmentu
const nowy = "Cześć świecie".replace("świecie", "React");
// "Cześć React"

// Zamiana WSZYSTKICH wystąpień
"la la la".replaceAll("la", "da"); // "da da da"

// Długość napisu
console.log("React".length); // 5

// Powtórzenie napisu
"ha".repeat(3) // "hahaha"

// Dopełnienie do określonej długości
"5".padStart(3, "0")   // "005"
"42".padStart(5, " ")  // "   42"
"hi".padEnd(5, ".")    // "hi..."

// Dostęp do znaku
"React".charAt(0)      // "R"
"React".at(-1)         // "t" (od końca)

// Kod znaku (przydatne w szyfrach, np. Cezara)
"A".charCodeAt(0)      // 65
String.fromCharCode(65) // "A"
```

### 3.19. truthy i falsy

W JavaScripcie każda wartość może być potraktowana jako `true` (truthy) lub `false` (falsy) w kontekście logicznym. To kluczowe przy renderowaniu warunkowym w React.

**Wartości falsy (traktowane jako `false`):**

| Wartość | Typ |
|---|---|
| `false` | boolean |
| `0` | number |
| `-0` | number |
| `0n` | BigInt |
| `""` (pusty string) | string |
| `null` | null |
| `undefined` | undefined |
| `NaN` | number |

**Wszystko inne jest truthy** — w tym `" "` (spacja), `[]` (pusta tablica), `{}` (pusty obiekt).

```js
// Przykłady
if ("React") {
  console.log("Prawda — niepusty string");
}

if (0) {
  console.log("Ten kod się NIE wykona — 0 jest falsy");
}

// W React — operator && do warunkowego renderowania
// {blad && <p className="text-danger">{blad}</p>}
// Jeśli blad jest "" (falsy), <p> się nie wyświetli
// Jeśli blad jest "Pole wymagane" (truthy), <p> się wyświetli
```

**Uwaga na pułapkę z `0`:**

```jsx
// BŁĘDNE — jeśli items.length === 0, React wyświetli "0" na stronie
{items.length && <ul>...</ul>}

// POPRAWNE — jawna konwersja na boolean
{items.length > 0 && <ul>...</ul>}
```

### 3.20. konsola przeglądarki i profesjonalne debugowanie (console.log)

Zanim zaczniesz budować skomplikowane UI, musisz wiedzieć, w jaki sposób komunikować się z przepływem danych w aplikacji. Konsola przeglądarki (klawisz `F12` lub `Prawy przycisk -> Zbadaj -> zakładka Console`) to podstawowe narzędzie diagnostyczne. Pozwala Ci ona "zajrzeć pod maskę" każdego komponentu React.

**Główne stopnie powiadomień (Severity):**
```js
console.log("Cześć, to podstawowa wiadomość informacyjna"); 
console.warn("Hej, uważaj – niegroźne, ale ważne ostrzeżenie! (wyświetla się na żółto)");
console.error("Błąd! Backend zawiódł! (wyświetla się na czerwono ze ścieżką błędów)");
console.info("Informacja o działaniu procesu");
```

**Złota zasada wstawiania logów w React:**
Jeśli komponent ci nie działa i nie odświeża poprawnie danych... powinieneś wstawić `console.log()` zaraz **PO** zadeklarowaniu stanów i **PRZED** blokiem `return ()`. Odpali on zmienne wirtualnie zaraz przed nowym wyrenderowaniem ekranu!

```jsx
import { useState } from "react";

function Koszyk() {
  const [ilosc, setIlosc] = useState(0);
  
  // GENIALNE do weryfikacji. Za każdym kliknięciem przycisku, zobaczysz nową wartość 
  // bez odświeżania całej wielkiej i powolnej aplikacji.
  console.log("-- Koszyk renderuje się! Aktualna Ilość:", ilosc);

  return (
    <div>
       <button onClick={() => setIlosc(ilosc + 1)}>Dodaj Winylową Płytę</button>
    </div>
  );
}
```

**Bardziej czytelne API: console.table()**
Zwykły `console.log()` bywa trudny w obsłudze dla długich tablic lub obiektów. Używaj tablic:
```js
const userzy = [
    { id: 10, nazwa: "Janek", rola: "Admin" },
    { id: 11, nazwa: "Krystyna", rola: "User" }
];

console.table(userzy); 
// W terminalu F12 wytworzy to przepiękną, sortowalną tabelę ułatwiającą wgląd w atrybuty!
```

### 3.21. instrukcja warunkowa switch

Instrukcja `switch` to alternatywa dla wielu warunków `if / else if`. Jest często używana w reducerach (`useReducer`) lub gdy mamy wiele precyzyjnych wartości do sprawdzenia.

```js
const rola = "ADMIN";

switch (rola) {
  case "ADMIN":
    console.log("Pełen dostęp");
    break; // Pamiętaj o break, inaczej wykona się też kolejny case!
  case "MODERATOR":
    console.log("Dostęp ograniczony");
    break;
  case "USER":
    console.log("Tylko odczyt");
    break;
  default:
    console.log("Rola nieznana");
}
```

**Użycie switch w React — renderowanie warunkowe:**

```jsx
function StatusIkona({ status }) {
  switch (status) {
    case "sukces":
      return <span className="text-success">✓ Gotowe</span>;
    case "blad":
      return <span className="text-danger">✗ Błąd</span>;
    case "ladowanie":
      return <span className="text-warning">⏳ Ładowanie...</span>;
    default:
      return <span className="text-muted">— Brak statusu</span>;
  }
}

// Użycie:
<StatusIkona status="sukces" />
```

**Switch z wieloma case'ami dla tej samej akcji (fall-through):**

```js
const dzien = new Date().getDay(); // 0 = niedziela, 6 = sobota

switch (dzien) {
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
    console.log("Dzień roboczy");
    break;
  case 0:
  case 6:
    console.log("Weekend!");
    break;
}
```

### 3.22. pętle (for, while, do...while) i iteracja

Chociaż w React zazwyczaj używamy metody `.map()` do renderowania list, klasyczne pętle wciąż są ważne w logice i algorytmach.

**1. Pętla `for`** - Używana gdy wiemy dokładnie, ile razy chcemy powtórzyć operację.
```js
for (let i = 0; i < 5; i++) {
  console.log(`Wykonanie numer ${i}`);
}
```

**2. Pętla `while`** - Używana, gdy nie wiemy ile razy pętla się wykona, zależy to od jakiegoś warunku, który jest sprawdzany na początku.
```js
let licznik = 0;
while (licznik < 3) {
  console.log("Licznik w while:", licznik);
  licznik++;
}
```

**3. Pętla `do...while`** - Wykona się ZAWSZE przynajmniej raz, ponieważ warunek sprawdzany jest na końcu.
```js
let x = 10;
do {
  console.log("Zawsze wykona się przynajmniej raz");
} while (x < 5); // Warunek nie jest spełniony, pętla się kończy
```

**4. Pętle `for...of` oraz `for...in`**
- `for...of` - Najlepsze do iterowania po tablicach i stringach.
- `for...in` - Używane do iterowania po kluczach obiektów (choć w React częściej używa się `Object.keys()`).
```js
const kolory = ["czerwony", "zielony", "niebieski"];
for (const kolor of kolory) {
  console.log(kolor);
}

const osoba = { imie: "Anna", wiek: 22 };
for (const klucz in osoba) {
  console.log(`${klucz}: ${osoba[klucz]}`);
}
```

**5. `break` i `continue` — sterowanie pętlą**

```js
// break — natychmiast przerywa pętlę
for (let i = 0; i < 10; i++) {
  if (i === 5) break; // Pętla kończy się przy i = 5
  console.log(i); // 0, 1, 2, 3, 4
}

// continue — pomija bieżącą iterację i przechodzi do następnej
for (let i = 0; i < 6; i++) {
  if (i === 3) continue; // Pomija 3
  console.log(i); // 0, 1, 2, 4, 5
}
```

**6. Praktyczne użycie pętli w React (poza JSX):**

W JSX do renderowania list używamy `map()`, ale pętle klasyczne przydają się w logice:

```jsx
// Generowanie hasła — pętla for w funkcji
function generujHaslo(dlugosc) {
  const znaki = "abcdefghijklmnopqrstuvwxyz0123456789";
  let haslo = "";
  for (let i = 0; i < dlugosc; i++) {
    haslo += znaki[Math.floor(Math.random() * znaki.length)];
  }
  return haslo;
}

// Tworzenie tablicy N elementów
function stworzKosci(ile) {
  const kosci = [];
  for (let i = 0; i < ile; i++) {
    kosci.push({ id: i + 1, wartosc: Math.floor(Math.random() * 6) + 1 });
  }
  return kosci;
}

// Walidacja — while do szukania błędu
function znajdzPierwszyBlad(pola) {
  let i = 0;
  while (i < pola.length) {
    if (pola[i].trim() === "") return `Pole ${i + 1} jest puste`;
    i++;
  }
  return null; // Brak błędów
}
```

### 3.23. asynchroniczność (promises, async/await, try/catch)

W dzisiejszym web developmentcie komunikacja z API jest oparta o asynchroniczność. Oznacza to, że Twój kod nie czeka w miejscu na pobranie danych z serwera, ale idzie dalej i wraca do obsługi danych, kiedy są one gotowe.

**Podejście klasyczne: Promises (.then / .catch)**
```js
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then(response => response.json()) // Przekształcamy na obiekt JS
  .then(data => console.log(data))   // Otrzymujemy dane
  .catch(error => console.error("Błąd pobierania:", error));
```

**Podejście nowoczesne: async / await + try / catch**
To jest rekomendowany sposób pobierania danych w React. Składnia przypomina kod synchroniczny, dzięki czemu jest bardzo czytelna.
```js
// Słowo 'async' przed funkcją pozwala używać 'await' w jej środku
async function pobierzDane() {
  try {
    // await zatrzymuje wykonanie TYLKO w obrębie tej funkcji, do czasu odpowiedzi
    const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log("Pobrane dane:", data);
  } catch (error) {
    console.error("Coś poszło nie tak:", error.message);
  } finally {
    console.log("Wykonuje się zawsze, niezależnie od sukcesu czy błędu");
  }
}

pobierzDane();
```

**Użycie async/await w React (z useEffect):**

```jsx
import { useState, useEffect } from "react";

function ListaUzytkownikow() {
  const [uzytkownicy, setUzytkownicy] = useState([]);
  const [ladowanie, setLadowanie] = useState(true);
  const [blad, setBlad] = useState(null);

  useEffect(() => {
    // Definiujemy async funkcję WEWNĄTRZ useEffect
    async function pobierz() {
      try {
        const res = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!res.ok) throw new Error("Błąd sieci");
        const data = await res.json();
        setUzytkownicy(data);
      } catch (err) {
        setBlad(err.message);
      } finally {
        setLadowanie(false);
      }
    }

    pobierz(); // Wywołujemy ją
  }, []); // Pusta tablica = tylko raz przy montowaniu

  if (ladowanie) return <p>Ładowanie...</p>;
  if (blad) return <p className="text-danger">Błąd: {blad}</p>;

  return (
    <ul>
      {uzytkownicy.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

**Ważne:** Nie można przekazać async funkcji bezpośrednio do useEffect (`useEffect(async () => {...})`). Trzeba zdefiniować async funkcję wewnątrz i ją wywołać.

### 3.24. dodatkowe metody tablic — forEach, some, every, slice, splice, concat

Oprócz `map`, `filter`, `find` i `reduce` istnieje wiele innych przydatnych metod tablicowych.

#### `forEach()` — wykonanie operacji na każdym elemencie (bez zwracania nowej tablicy)

```js
const owoce = ["jabłko", "banan", "gruszka"];

owoce.forEach((owoc, index) => {
  console.log(`${index + 1}. ${owoc}`);
});
// 1. jabłko
// 2. banan
// 3. gruszka
```

**Różnica `forEach` vs `map`:** `forEach` nic nie zwraca (undefined), `map` zwraca nową tablicę. W React do renderowania list używamy `map`, nie `forEach`.

#### `some()` — czy JAKIKOLWIEK element spełnia warunek

```js
const oceny = [3, 4, 2, 5, 3];
const maOceneCelujaca = oceny.some(o => o === 6);  // false
const maNiedostateczna = oceny.some(o => o === 1); // false
const maDwojke = oceny.some(o => o === 2);         // true
```

#### `every()` — czy WSZYSTKIE elementy spełniają warunek

```js
const oceny = [4, 5, 4, 5, 5];
const wszystkieZaliczone = oceny.every(o => o >= 3); // true
const wszystkieCelujace = oceny.every(o => o === 6); // false
```

Przydatne w React np. do walidacji:

```jsx
const pola = [imie, email, haslo];
const formularzWypelniony = pola.every(pole => pole.trim() !== "");
```

#### `slice()` — wycięcie fragmentu tablicy (BEZ mutacji)

```js
const liczby = [10, 20, 30, 40, 50];

liczby.slice(1, 3)  // [20, 30] — od indeksu 1 do 3 (bez 3)
liczby.slice(2)     // [30, 40, 50] — od indeksu 2 do końca
liczby.slice(-2)    // [40, 50] — ostatnie 2 elementy
```

#### `splice()` — modyfikacja tablicy w miejscu (MUTUJE!)

```js
const kolory = ["czerwony", "zielony", "niebieski"];

// Usunięcie 1 elementu od indeksu 1
kolory.splice(1, 1); // kolory = ["czerwony", "niebieski"]

// Wstawienie elementu na pozycji 1
kolory.splice(1, 0, "żółty"); // kolory = ["czerwony", "żółty", "niebieski"]

// Zamiana elementu na pozycji 0
kolory.splice(0, 1, "pomarańczowy"); // kolory = ["pomarańczowy", "żółty", "niebieski"]
```

**Uwaga:** W React NIE używamy `splice` na stanie — mutuje tablicę. Zamiast tego używamy `filter` (usuwanie) lub `map` (zamiana).

#### `concat()` — łączenie tablic (BEZ mutacji)

```js
const a = [1, 2];
const b = [3, 4];
const c = a.concat(b); // [1, 2, 3, 4]

// Alternatywa ze spread (częściej używana w React):
const d = [...a, ...b]; // [1, 2, 3, 4]
```

#### `flat()` — spłaszczanie zagnieżdżonych tablic

```js
const zagniezdzona = [[1, 2], [3, 4], [5]];
const plaska = zagniezdzona.flat(); // [1, 2, 3, 4, 5]
```

#### `indexOf()` i `findIndex()`

```js
const kursy = ["HTML", "CSS", "React"];
kursy.indexOf("CSS");     // 1
kursy.indexOf("Angular"); // -1 (nie znaleziono)

const produkty = [{ id: 1, nazwa: "A" }, { id: 2, nazwa: "B" }];
produkty.findIndex(p => p.id === 2); // 1
```

#### `join()` — łączenie elementów w string

```js
const slowa = ["Cześć", "świecie"];
slowa.join(" ");  // "Cześć świecie"
slowa.join(", "); // "Cześć, świecie"
slowa.join("");   // "Cześćświecie"
```

#### `reverse()` — odwrócenie kolejności (MUTUJE!)

```js
const liczby = [1, 2, 3, 4, 5];
const odwrocone = [...liczby].reverse(); // [5, 4, 3, 2, 1] — kopia, by nie mutować
```

#### `Set` — usuwanie duplikatów z tablicy

`Set` to struktura danych przechowująca tylko unikalne wartości:

```js
const zDuplikatami = ["jabłko", "banan", "jabłko", "gruszka", "banan"];

// Usunięcie duplikatów — najczęstszy wzorzec
const unikalne = [...new Set(zDuplikatami)];
// ["jabłko", "banan", "gruszka"]

// Wyciągnięcie unikalnych kategorii z tablicy obiektów (częste w React!)
const produkty = [
  { id: 1, kategoria: "Elektronika" },
  { id: 2, kategoria: "Odzież" },
  { id: 3, kategoria: "Elektronika" },
];
const kategorie = [...new Set(produkty.map(p => p.kategoria))];
// ["Elektronika", "Odzież"]
```

#### `Array.from` — tworzenie tablicy z czegoś iterowalnego

```js
// Tablica N elementów
Array.from({ length: 5 }, (_, i) => i + 1) // [1, 2, 3, 4, 5]

// Tablica 10 zer
Array.from({ length: 10 }, () => 0) // [0, 0, 0, ..., 0]

// String na tablicę znaków
Array.from("React") // ["R", "e", "a", "c", "t"]
```

### 3.25. obiekt Math — losowanie, zaokrąglanie, min/max

Obiekt `Math` zawiera stałe i metody matematyczne. Nie trzeba go importować.

```js
// Zaokrąglanie
Math.round(3.5)   // 4 — do najbliższej całkowitej
Math.round(3.4)   // 3
Math.floor(3.9)   // 3 — zawsze w dół
Math.ceil(3.1)    // 4 — zawsze w górę
Math.trunc(3.9)   // 3 — obcięcie części dziesiętnej

// Wartość bezwzględna
Math.abs(-7)      // 7

// Potęgowanie i pierwiastek
Math.pow(2, 3)    // 8 (to samo co 2 ** 3)
Math.sqrt(16)     // 4

// Minimum i maksimum
Math.min(3, 1, 7, 2)  // 1
Math.max(3, 1, 7, 2)  // 7

// Min/max z tablicy — użyj spread
const oceny = [3, 5, 2, 4];
Math.min(...oceny) // 2
Math.max(...oceny) // 5

// Stała PI
Math.PI // 3.141592653589793
```

#### Losowanie liczb — Math.random()

`Math.random()` zwraca losową liczbę z zakresu [0, 1) — od 0 (włącznie) do 1 (wyłącznie).

```js
// Losowa liczba 0-1
Math.random() // np. 0.7234...

// Losowa liczba całkowita od 0 do 9
Math.floor(Math.random() * 10)

// Losowa liczba całkowita od 1 do 6 (kość do gry)
Math.floor(Math.random() * 6) + 1

// Losowa liczba całkowita z zakresu [min, max]
function losujZZakresu(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
losujZZakresu(10, 20) // np. 14

// Losowy element z tablicy
const kolory = ["red", "green", "blue", "yellow"];
const losowy = kolory[Math.floor(Math.random() * kolory.length)];
```

### 3.26. obiekt Date — data i czas

```js
// Aktualna data i czas
const teraz = new Date();
console.log(teraz); // np. "2025-06-15T10:30:00.000Z"

// Pobieranie składowych
teraz.getFullYear()  // 2025
teraz.getMonth()     // 5 (miesiące od 0! Styczeń = 0, Czerwiec = 5)
teraz.getDate()      // 15 (dzień miesiąca)
teraz.getDay()       // 0 (dzień tygodnia: 0 = niedziela, 1 = poniedziałek)
teraz.getHours()     // 10
teraz.getMinutes()   // 30
teraz.getSeconds()   // 0

// Tworzenie konkretnej daty
const sylwester = new Date(2025, 11, 31); // Grudzień 31 (miesiąc od 0!)
const zStringa = new Date("2025-06-15");

// Timestamp — milisekundy od 1 stycznia 1970
Date.now() // np. 1718451000000 — przydatne jako unikalne ID

// Formatowanie daty
teraz.toLocaleDateString("pl-PL") // "15.06.2025"
teraz.toLocaleTimeString("pl-PL") // "10:30:00"
teraz.toLocaleString("pl-PL")     // "15.06.2025, 10:30:00"

// Porównywanie dat
const data1 = new Date("2025-01-01");
const data2 = new Date("2025-06-01");
console.log(data1 < data2); // true
```

Typowe użycie w React:

```jsx
function Stopka() {
  const rok = new Date().getFullYear();
  return <footer>&copy; {rok} Moja Aplikacja</footer>;
}
```

### 3.27. setTimeout i setInterval — opóźnienia i interwały

#### `setTimeout` — jednorazowe opóźnienie

```js
// Wykonaj funkcję PO 2 sekundach (2000 ms)
setTimeout(() => {
  console.log("Minęły 2 sekundy!");
}, 2000);

// Anulowanie timera
const timer = setTimeout(() => {
  console.log("To się nie wykona");
}, 5000);
clearTimeout(timer); // Anulujemy przed wykonaniem
```

#### `setInterval` — powtarzanie co X milisekund

```js
// Wykonuj co 1 sekundę
const interwał = setInterval(() => {
  console.log("Tik...");
}, 1000);

// Zatrzymanie interwału
clearInterval(interwał);
```

#### Użycie w React (z useEffect):

```jsx
import { useState, useEffect } from "react";

function Stoper() {
  const [sekundy, setSekundy] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setSekundy(prev => prev + 1);
    }, 1000);

    // Cleanup — zatrzymanie przy odmontowaniu komponentu
    return () => clearInterval(id);
  }, []);

  return <p>Czas: {sekundy}s</p>;
}
```

### 3.28. operator ?? (nullish coalescing) i ?. (optional chaining)

#### `??` — wartość domyślna dla null/undefined

Operator `??` zwraca prawą stronę TYLKO gdy lewa jest `null` lub `undefined`. Różni się od `||`, który reaguje na wszystkie wartości falsy (0, "", false).

```js
const imie = null;
const wyswietlane = imie ?? "Anonim"; // "Anonim"

const liczba = 0;
const a = liczba || 10;  // 10 — bo 0 jest falsy!
const b = liczba ?? 10;  // 0  — bo 0 nie jest null/undefined

const tekst = "";
const c = tekst || "domyślny";  // "domyślny" — bo "" jest falsy
const d = tekst ?? "domyślny";  // "" — bo "" nie jest null/undefined
```

#### `?.` — bezpieczny dostęp do zagnieżdżonych pól

Operator `?.` sprawdza, czy wartość po lewej nie jest `null`/`undefined` zanim spróbuje odczytać pole. Jeśli jest — zwraca `undefined` zamiast rzucać błąd.

```js
const user = { imie: "Jan", adres: { miasto: "Kraków" } };

// Bez optional chaining — błąd jeśli adres nie istnieje
// user.adres.ulica → undefined
// user.kontakt.email → TypeError: Cannot read property 'email' of undefined

// Z optional chaining — bezpieczne
user.adres?.miasto    // "Kraków"
user.adres?.ulica     // undefined (bez błędu)
user.kontakt?.email   // undefined (bez błędu)

// Łączenie z ??
const miasto = user.adres?.miasto ?? "Nieznane"; // "Kraków"
const email = user.kontakt?.email ?? "brak";     // "brak"
```

Przydatne w React przy danych z API:

```jsx
function ProfilUsera({ user }) {
  return (
    <div>
      <p>Imię: {user?.imie ?? "Ładowanie..."}</p>
      <p>Miasto: {user?.adres?.miasto ?? "Nie podano"}</p>
    </div>
  );
}
```

### 3.29. obsługa błędów — try / catch / finally

Blok `try/catch` pozwala przechwycić błędy bez zatrzymywania całej aplikacji.

```js
// Podstawowa składnia
try {
  // Kod, który może rzucić błąd
  const dane = JSON.parse("to nie jest JSON");
} catch (error) {
  // Obsługa błędu
  console.error("Błąd parsowania:", error.message);
} finally {
  // Opcjonalnie — wykona się ZAWSZE (niezależnie od błędu)
  console.log("Koniec operacji");
}
```

#### Rzucanie własnych błędów — `throw`

```js
function podziel(a, b) {
  if (b === 0) {
    throw new Error("Nie można dzielić przez zero!");
  }
  return a / b;
}

try {
  const wynik = podziel(10, 0);
} catch (error) {
  console.error(error.message); // "Nie można dzielić przez zero!"
}
```

#### Typowe użycie w React — walidacja i fetch:

```jsx
function handleSubmit(e) {
  e.preventDefault();
  try {
    if (wiek < 0 || wiek > 150) {
      throw new Error("Nieprawidłowy wiek");
    }
    console.log("Formularz OK");
  } catch (error) {
    setBlad(error.message);
  }
}
```

### 3.30. wyrażenia regularne (RegExp) — podstawy

Wyrażenia regularne (regex) służą do wyszukiwania wzorców w tekście. Przydatne przy walidacji formularzy.

```js
// Tworzenie wyrażenia regularnego
const wzorzec = /abc/;           // Literał
const wzorzec2 = new RegExp("abc"); // Konstruktor

// Testowanie — czy string pasuje do wzorca
/abc/.test("abcdef")  // true
/xyz/.test("abcdef")  // false

// Flagi
/abc/i  // i = case-insensitive (ignoruje wielkość liter)
/abc/g  // g = global (znajdź wszystkie wystąpienia)
```

#### Najczęstsze wzorce do walidacji:

```js
// Email (uproszczony)
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
emailRegex.test("jan@mail.pl")  // true
emailRegex.test("niepoprawny")  // false

// Tylko cyfry
/^\d+$/.test("12345")   // true
/^\d+$/.test("123abc")  // false

// Tylko litery (polskie też)
/^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+$/.test("Kraków") // true

// Minimum 8 znaków, przynajmniej 1 cyfra i 1 duża litera
/^(?=.*[A-Z])(?=.*\d).{8,}$/.test("Haslo123") // true

// Kod pocztowy (XX-XXX)
/^\d{2}-\d{3}$/.test("30-001") // true

// Numer telefonu (9 cyfr)
/^\d{9}$/.test("123456789") // true
```

#### Metody stringów z regex:

```js
const tekst = "Mam 3 koty i 2 psy";

// match — znajdź pasujące fragmenty
tekst.match(/\d+/g)  // ["3", "2"]

// replace z regex
tekst.replace(/\d+/g, "X")  // "Mam X koty i X psy"

// split z regex
"jabłko, banan;  gruszka".split(/[,;]\s*/) // ["jabłko", "banan", "gruszka"]
```

#### Użycie w React — walidacja formularza:

```jsx
function walidujEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(email)) {
    return "Nieprawidłowy format email";
  }
  return "";
}

function walidujHaslo(haslo) {
  if (haslo.length < 8) return "Minimum 8 znaków";
  if (!/[A-Z]/.test(haslo)) return "Wymagana duża litera";
  if (!/\d/.test(haslo)) return "Wymagana cyfra";
  return "";
}
```

---

## 4. jsx — składnia widoku

### 4.1. czym jest jsx

JSX (JavaScript XML) to rozszerzenie składni JavaScript, które pozwala pisać kod wyglądający jak HTML bezpośrednio w plikach JavaScript. JSX nie jest HTML-em — jest tylko **składnią**, która jest kompilowana do wywołań `React.createElement()`.

```jsx
// To co piszesz (JSX):
const element = <h1>Witaj, React!</h1>;

// To na co JSX jest kompilowany (pod spodem):
const element = React.createElement("h1", null, "Witaj, React!");
```

Nie musisz znać formy skompilowanej — wystarczy, że piszesz w JSX. Babel (kompilator w CRA) dokonuje tej transformacji automatycznie.

### 4.2. wstawianie wartości JavaScript w jsx

Wartości JavaScript wstawiamy w JSX za pomocą **nawiasów klamrowych** `{}`:

```jsx
// Plik: src/App.js
function App() {
  const tytul = "Lista kursów";
  const liczba = 4;
  const imie = "Jan";

  return (
    <section>
      {/* Zmienna tekstowa */}
      <h2>{tytul}</h2>

      {/* Zmienna liczbowa */}
      <p>Liczba kursów: {liczba}</p>

      {/* Wyrażenie matematyczne */}
      <p>Następny numer: {liczba + 1}</p>

      {/* Wywołanie metody */}
      <p>Imię wielkimi literami: {imie.toUpperCase()}</p>

      {/* Operator trójargumentowy */}
      <p>{liczba > 3 ? "Dużo kursów" : "Mało kursów"}</p>
    </section>
  );
}

export default App;
```

### 4.3. atrybuty HTML vs jsx

W JSX kilka atrybutów HTML ma inne nazwy, ponieważ oryginalne nazwy kolidują ze słowami kluczowymi JavaScript:

| HTML | JSX | Powód |
|---|---|---|
| `class` | `className` | `class` to słowo zarezerwowane w JS |
| `for` | `htmlFor` | `for` to słowo zarezerwowane w JS |
| `onclick` | `onClick` | React używa camelCase |
| `onchange` | `onChange` | camelCase |
| `onsubmit` | `onSubmit` | camelCase |
| `tabindex` | `tabIndex` | camelCase |
| `readonly` | `readOnly` | camelCase |
| `maxlength` | `maxLength` | camelCase |

```jsx
{/* Poprawny JSX */}
<label htmlFor="email" className="form-label">
  Email
</label>
<input
  id="email"
  className="form-control"
  type="text"
  readOnly
  tabIndex={1}
/>
```

### 4.4. zasada jednego elementu nadrzędnego

Komponent musi zwrócić **jeden główny element**. Nie można zwrócić dwóch sąsiednich elementów bez wspólnego rodzica:

```jsx
// błąd — dwa elementy obok siebie bez wspólnego rodzica
function App() {
  return (
    <h1>Tytuł</h1>
    <p>Opis</p>
  );
}

// POPRAWNIE — owinięte w jeden element
function App() {
  return (
    <div>
      <h1>Tytuł</h1>
      <p>Opis</p>
    </div>
  );
}

// POPRAWNIE — element semantyczny
function App() {
  return (
    <main>
      <h1>Tytuł</h1>
      <p>Opis</p>
    </main>
  );
}
```

### 4.5. fragmenty — puste znaczniki

Jeśli nie chcesz dodawać dodatkowego elementu HTML (np. `div`), możesz użyć **Fragmentu**. Fragment to pusty znacznik `<>...</>`, który nie dodaje żadnego elementu do DOM:

```jsx
// Fragment — nie dodaje żadnego elementu HTML
function App() {
  return (
    <>
      <h1>Tytuł</h1>
      <p>Opis</p>
    </>
  );
}

// Alternatywna pełna forma
import { Fragment } from "react";

function App() {
  return (
    <Fragment>
      <h1>Tytuł</h1>
      <p>Opis</p>
    </Fragment>
  );
}
```

### 4.6. komentarze w jsx

Komentarze w JSX muszą być w nawiasach klamrowych i mieć składnię JavaScriptu:

```jsx
function App() {
  return (
    <div>
      {/* To jest komentarz w JSX */}
      <h1>Tytuł</h1>

      {/* Komentarz wieloliniowy
          w JSX */}
      <p>Opis</p>
    </div>
  );
}
```

### 4.7. atrybuty boolean

Atrybuty logiczne (boolean) w JSX mogą być podawane bez wartości — wtedy oznaczają `true`:

```jsx
{/* disabled bez wartości = disabled={true} */}
<button disabled>Nieaktywny</button>

{/* Dynamiczny atrybut boolean */}
<button disabled={czyWyslane}>Wyślij</button>

{/* Checkbox zaznaczony */}
<input type="checkbox" checked={zaznaczony} onChange={handleChange} />

{/* Pole tylko do odczytu */}
<input type="text" readOnly value="Nie można edytować" />
```

### 4.8. co można wstawiać w klamrach — podsumowanie

| Można wstawić | Przykład | Uwagi |
|---|---|---|
| Zmienną | `{imie}` | Najprostszy przypadek |
| Liczbę | `{wiek}` | React zamieni ją na tekst |
| Wyrażenie | `{cena * ilosc}` | Krótkie obliczenia |
| Wynik funkcji | `{formatuj(cena)}` | Funkcja nie powinna zmieniać stanu |
| Operator warunkowy | `{x > 5 ? "Tak" : "Nie"}` | Do komunikatów |
| Operator `&&` | `{blad && <p>{blad}</p>}` | Warunkowe wyświetlanie |

**Czego NIE można wstawić:**

- Instrukcji `if/else` (to nie jest wyrażenie)
- Obiektów (React nie wie, jak je wyświetlić)
- Pętli `for` (użyj `map()`)

```jsx
// błąd — if nie jest wyrażeniem
{if (x > 5) { return "Tak" }}

// POPRAWNIE — operator trójargumentowy
{x > 5 ? "Tak" : "Nie"}
```

---


### 4.9. tagi samozamykające z HTML w jsx (Zasada zamknięcia)

Gdy przychodzi praca z tagami `HTML`, bardzo często zapomina się o podstawowej regule JSX: **Każdy znacznik musi być zamknięty**. W klasycznym wczesnym HTML pisaliśmy np. `<br>`, `<img>` lub `<input>`. W React (dzięki rygorowi składni XML) coś takiego wywoła od razu potężny błąd kompilacji na czerwono.

Musisz **natychmiast** postawić zamykający ukośnik przez ostatecznym plusem tagu:
```jsx
// Błędny kod w React (nie skompiluje się środowisko, wyrzuci syntax error):
// <img src="plik.jpg" alt="zdjęcie"> 
// <input type="text">
// <br>
// <hr>

// Prawidłowy działający kod w React:
<img src="plik.jpg" alt="zdjęcie" /> 
<input type="text" />
<br />
<hr />
```

### 4.10. multimedia ze źródłem (Audio, soundplayery i wideo)

Praca z plikami multimedialnymi to klasyk i genialny krok do pierwszych wielkich sukcesów małych interaktywnych apek (np. tworzenie prostej playlisty czy domowego centrum filmowego). Tagi `<audio>` oraz `<video>` wprawdzie są klasycznymi znacznikami HTML, to jednak perfekcyjnie dają się wprawiać w ruch przez mechanizm stanu w JSX i ścieżki (src).

**Podstawowy Odtwarzacz Audio:**
Przeglądarki budują pod niego swój własny (nie do podrobienia za lekko) panel playera z głośnością, przesuwakiem time i prędkoscią - jeżeli tylko nakarmisz tag dopiskiem `controls`.

```jsx
// Aby plik audio zadziałał poprawnie bez problematycznego weebpacka "importu pliku", przenieś swoje pliki mp3
// bezpośrednio do twojego głównego folderu `public/dzwieki/muzyka.mp3`
function PodstawowyAudioPlayer() {
  return (
    <div>
      <h2>Rozdział Odtwarzacza</h2>
      {/* 
        controls - absolutnie najważniejszy parametr! To on wyświetla panel odtwarzania z osią czasu, play'em i głosem.
        autoPlay - wymusza autostart (najczęściej blokowany przez przeglądarki Chrome do czasu jak użytkownik sam nie kliknie czegokolwiek).
        loop - decyduje by muzyka odtwarzała się w nieskończoność.
      */}
      <audio controls loop>
        <source src="/dzwieki/muzyka.mp3" type="audio/mpeg" />
        Twoja przeglądarka nie obsługuje nowoczesnego tagu audio w HTML5 :(.
      </audio>
    </div>
  );
}
```

**Podstawowe Wideo:**
Tag `video` daje tak samo olbrzymią fantazję z mediami co audio. Jeżeli chcesz utworzyć popularny dzisiaj efekt - odtwarzał z tła wyciszony film loopujacy w niekoćzność (jak w portfolio agencji czy netflixie), użyj `muted`, `autoPlay` i `loop`:
```jsx
function WideoWyjasnienia() {
  return (
    <div style={{ maxWidth: "600px", margin: "auto" }}>
    
      <h3>Kino - Film z plakatem startowym</h3>
      {/* video jest bardzo czułe, polecam zawsze zapiąć szerokości / max width żeby player się nie wymsknął bokiem na monitorze */}
      <video controls width="100%" poster="/grafika/placeholder.jpg">
        <source src="/filmy/zapowiedz.mp4" type="video/mp4" />
      </video>
      <hr />

      <h3>Film w Tle (nie reagujący, leci jak zwariowany animowany GIF)</h3>
      {/* Autostartujący, całkowicie cichy film do bycia interaktywnym żywym tłem - muted! */}
      <video autoPlay loop muted width="100%">
        <source src="/filmy/animacja.mp4" type="video/mp4" />
      </video>
      
    </div>
  );
}
```
*Złota Rada: W dodanym atrybucie `poster=""` wklepujesz po prostu lokacje do jpega z miniaturką przed wcisnięciu PLAY przez konsumenta.*

### 4.11. elementy osadzone: iframe (Mapy, embedy z YouTube)

Na stronach "kontaktowych" i w rozbudowanych projektach - niesamowicie cenne jest osadzić aplikacje od zewnętrznych dostawców. Iframe to dosłownie okno w Twojej stronie wyświetlające zasoby z innych serwerów (np. Google).

```jsx
// Zwykle kopiując kod z google maps dostaniesz z internetu kod z czerwonymi ostrzeżeniami jak "frameborder". 
// To wina braku zgodności z restrykcyjnym strictmode JSX (pisalismy o tym u góry), trzeba je lekko przespelować:
function LokalizacjaFirmaWidok() {
  return (
    <iframe 
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d111... itd i tak dalej" 
      width="100%" 
      height="450" 
      style={{ border: 0, borderRadius: "10px" }} // Zamiast np. frameborder="0"
      allowFullScreen={true} // W JSX booleanowe true powinno lecieć dla tych właściwości!
      loading="lazy" 
      referrerPolicy="no-referrer-when-downgrade"
      title="Mapa Firmy Google" // Bezwzględny w React, inaczej dostajesz błąd.
    />
  );
}
```
*Zawsze pilnuj czy atrybuty CSS skopiowane z Google / YT - np. puste stringi `style="border: 0"` nie sa przypisywane do Twoich obiektow style.*

---


## 5. komponenty

### 5.1. czym jest komponent

Komponent to absolutny fundament Reacta. Wyobraź sobie stronę internetową nie jako jeden wielki plik HTML, ale jako budowlę z **klocków LEGO**. Każdy klocek to osobny "komponent". Masz klocek-Nawigację, klocek-Przycisk, klocek-Stopkę.

Z technicznego punktu widzenia komponent to zwykła **funkcja JavaScript**, która różni się od innych funkcji tylko dwiema rzeczami:
1. **Zawsze zaczyna się wielką literą** (np. `Nawigacja`, `Przycisk`, a nie `nawigacja`). React używa wielkiej litery, żeby odróżnić własne komponenty od zwykłych tagów HTML (jak `<div>` czy `<span>`).
2. **Zwraca kod JSX** (czyli wyglądający jak HTML kod definiujący, co zobaczy użytkownik).

Dzięki podzieleniu aplikacji na komponenty, możesz:
- Użyć tego samego przycisku w 10 różnych miejscach w kodzie.
- Edytować wygląd Przycisku tylko w jednym pliku, a zmieni się on wszędzie.
- Znacznie łatwiej czytać kod i nim zarządzać.

### 5.2. pierwszy komponent funkcyjny

```jsx
// Plik: src/App.js
function App() {
  return (
    <main>
      <h1>Moja pierwsza aplikacja React</h1>
      <p>Projekt działa poprawnie.</p>
    </main>
  );
}

export default App;
```

Każdy komponent:
1. Jest **funkcją** (nazwa z wielkiej litery).
2. **Zwraca** JSX (widok).
3. Jest **eksportowany** (`export default`) — aby inne pliki mogły go użyć.

### 5.3. komponent statyczny — bez stanu

Komponent nie musi mieć stanu. Może po prostu wyświetlać statyczny widok:

```jsx
// Plik: src/components/Footer.js
function Footer() {
  const rok = new Date().getFullYear();

  return (
    <footer style={{ textAlign: "center", marginTop: "2rem", color: "gray" }}>
      <p>&copy; {rok} Moja Aplikacja. Wszelkie prawa zastrzeżone.</p>
    </footer>
  );
}

export default Footer;
```

```jsx
// Plik: src/components/InfoBox.js
function InfoBox() {
  return (
    <div className="alert alert-info">
      <h4>Informacja</h4>
      <p>To jest statyczny komponent informacyjny.</p>
    </div>
  );
}

export default InfoBox;
```

### 5.4. kompozycja — komponenty w komponentach

Siła Reacta polega na składaniu komponentów jak klocków. Jeden komponent może zawierać inne:

```jsx
// Plik: src/components/Header.js
function Header() {
  return (
    <header>
      <h1>Aplikacja Kursów</h1>
      <p>Znajdź idealny kurs dla siebie</p>
    </header>
  );
}

export default Header;
```

```jsx
// Plik: src/components/Footer.js
function Footer() {
  return (
    <footer>
      <p>&copy; 2025 Aplikacja Kursów</p>
    </footer>
  );
}

export default Footer;
```

```jsx
// Plik: src/App.js — składanie komponentów
import Header from "./components/Header";
import Footer from "./components/Footer";

function App() {
  return (
    <div>
      <Header />
      <main className="container mt-4">
        <p>Treść główna aplikacji</p>
      </main>
      <Footer />
    </div>
  );
}

export default App;
```

### 5.5. podział na pliki — osobne komponenty

Każdy komponent zazwyczaj ma własny plik. Konwencja nazewnictwa:
- Nazwa pliku = nazwa komponentu
- PascalCase (każde słowo z wielkiej litery)
- Rozszerzenie `.js` (lub `.jsx`)

```
src/
├── App.js
├── App.css
├── index.js
├── index.css
└── components/
    ├── Header.js
    ├── Footer.js
    ├── KursLista.js
    └── KursKarta.js
```

### 5.6. props — przekazywanie danych do komponentu

Props (skrót od "properties", czyli właściwości) to dane przekazywane z komponentu rodzica do komponentu dziecka. Działają dokładnie tak samo jak **parametry funkcji**. 

Wróćmy do analogii z klockami LEGO: masz gotowy klocek "Przycisk", ale chcesz, by na jednej stronie był czerwony z napisem "Usuń", a na innej zielony z napisem "Zapisz". Nie budujesz dwóch osobnych komponentów! Zamiast tego do jednego, uniwersalnego komponentu Przycisk przekazujesz odpowiednie `propsy` (np. kolor i tekst).

```jsx
// Plik: src/components/Powitanie.js
// Komponent odbiera obiekt 'props' jako swój pierwszy parametr
function Powitanie(props) {
  return <h2>Cześć, {props.imie}! Masz {props.wiek} lat.</h2>;
}

export default Powitanie;
```

```jsx
// Plik: src/App.js — użycie komponentu z propsami
import Powitanie from "./components/Powitanie";

function App() {
  return (
    <main>
      <Powitanie imie="Jan" wiek={25} />
      <Powitanie imie="Anna" wiek={30} />
      <Powitanie imie="Piotr" wiek={22} />
    </main>
  );
}

export default App;
```

**Zasady propsów:**
- Props są **tylko do odczytu** — dziecko NIE może ich modyfikować.
- Tekst (`string`) podajemy w cudzysłowach: `imie="Jan"`.
- Liczby, zmienne i wyrażenia podajemy w klamrach: `wiek={25}`.
- Boolean `true` — wystarczy sam atrybut: `aktywny` = `aktywny={true}`.

### 5.7. props — destrukturyzacja

Zamiast odwoływać się do `props.imie`, `props.wiek` itd., można użyć destrukturyzacji:

```jsx
// Plik: src/components/KursKarta.js
// Destrukturyzacja propsów bezpośrednio w parametrze
function KursKarta({ nazwa, opis, cena }) {
  return (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">{nazwa}</h5>
        <p className="card-text">{opis}</p>
        <p className="card-text"><strong>Cena: {cena} zł</strong></p>
      </div>
    </div>
  );
}

export default KursKarta;
```

### 5.8. props — wartości domyślne

```jsx
// Plik: src/components/Przycisk.js
function Przycisk({ tekst = "Kliknij", kolor = "primary" }) {
  return (
    <button className={`btn btn-${kolor}`}>
      {tekst}
    </button>
  );
}

export default Przycisk;
```

```jsx
// Użycie
<Przycisk />                             {/* tekst="Kliknij", kolor="primary" */}
<Przycisk tekst="Zapisz" />              {/* kolor nadal "primary" */}
<Przycisk tekst="Usuń" kolor="danger" /> {/* wszystkie nadpisane */}
```

### 5.9. children — zawartość między znacznikami

Specjalny prop `children` zawiera to, co zostanie umieszczone między otwierającym a zamykającym znacznikiem komponentu:

```jsx
// Plik: src/components/Panel.js
function Panel({ tytul, children }) {
  return (
    <div className="card mb-3">
      <div className="card-header">
        <h5>{tytul}</h5>
      </div>
      <div className="card-body">
        {children}
      </div>
    </div>
  );
}

export default Panel;
```

```jsx
// Plik: src/App.js — użycie komponentu Panel
import Panel from "./components/Panel";

function App() {
  return (
    <main className="container mt-4">
      <Panel tytul="O aplikacji">
        <p>To jest moja aplikacja React.</p>
        <p>Używam komponentu Panel jako kontenera.</p>
      </Panel>

      <Panel tytul="Kontakt">
        <p>Email: jan@example.com</p>
      </Panel>
    </main>
  );
}

export default App;
```

### 5.10. kiedy dzielić komponent na mniejsze

Komponent warto podzielić, gdy:
- Ma więcej niż ~100 linii JSX.
- Powtarza się w wielu miejscach (np. karta produktu).
- Ma wyraźnie oddzielne odpowiedzialności (np. formularz + lista wyników).
- Chcesz przekazywać mu różne dane przez props.

W prostych aplikacjach często wystarczy jeden komponent `App`. Nie musisz na siłę dzielić interfejsu, jeśli widok jest mały.

---

## 6. stylowanie

### 6.1. CSS w projekcie React (CRA)

W CRA pliki CSS importujesz bezpośrednio w plikach JavaScript:

```jsx
// Plik: src/App.js
import "./App.css"; // Import pliku CSS

function App() {
  return <h1 className="tytul-glowny">Witaj!</h1>;
}

export default App;
```

```css
/* Plik: src/App.css */
.tytul-glowny {
  color: #333;
  font-size: 2rem;
  text-align: center;
  margin-top: 2rem;
}
```

### 6.2. className zamiast class

W JSX atrybut HTML `class` zamieniony jest na `className`:

```jsx
{/* BŁĘDNIE — class to słowo zarezerwowane w JS */}
<div class="container">

{/* POPRAWNIE — className */}
<div className="container">
```

### 6.3. style inline w jsx

Style inline w JSX zapisywane są jako **obiekt JavaScript** (nie string jak w HTML):

```jsx
// W HTML: style="color: red; font-size: 20px;"
// W JSX:
<p style={{ color: "red", fontSize: "20px" }}>
  Tekst czerwony
</p>

// Podwójne klamry:
// Zewnętrzne {} — wstawiamy JavaScript do JSX
// Wewnętrzne {} — definiujemy obiekt JavaScript
```

**Różnice między CSS a stylem inline w JSX:**

| CSS | JSX inline |
|---|---|
| `font-size: 20px;` | `fontSize: "20px"` |
| `background-color: red;` | `backgroundColor: "red"` |
| `margin-top: 10px;` | `marginTop: "10px"` |
| `border-radius: 5px;` | `borderRadius: "5px"` |
| `text-align: center;` | `textAlign: "center"` |

Zasada: nazwy CSS z myślnikami zamieniamy na **camelCase**.

### 6.4. dynamiczne klasy CSS

Klasy CSS można ustawiać dynamicznie na podstawie stanu:

```jsx
// Plik: src/App.js
import { useState } from "react";
import "./App.css";

function App() {
  const [aktywny, setAktywny] = useState(false);

  return (
    <div>
      {/* Dynamiczna klasa za pomocą operatora trójargumentowego */}
      <p className={aktywny ? "tekst-zielony" : "tekst-czerwony"}>
        Status: {aktywny ? "Aktywny" : "Nieaktywny"}
      </p>

      {/* Łączenie stałej klasy z dynamiczną */}
      <button
        className={`btn ${aktywny ? "btn-success" : "btn-danger"}`}
        onClick={() => setAktywny(!aktywny)}
      >
        Przełącz
      </button>
    </div>
  );
}

export default App;
```

```css
/* Plik: src/App.css */
.tekst-zielony {
  color: green;
  font-weight: bold;
}

.tekst-czerwony {
  color: red;
  font-weight: bold;
}
```

### 6.5. dynamiczne style inline

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [rozmiar, setRozmiar] = useState(16);
  const [kolor, setKolor] = useState("#333333");

  return (
    <div className="container mt-4">
      <p style={{ fontSize: `${rozmiar}px`, color: kolor }}>
        Tekst z dynamicznym stylem
      </p>

      <label>
        Rozmiar: {rozmiar}px
        <input
          type="range"
          min="10"
          max="50"
          value={rozmiar}
          onChange={(e) => setRozmiar(Number(e.target.value))}
        />
      </label>
    </div>
  );
}

export default App;
```

### 6.6. organizacja plików CSS

W prostych projektach wystarczy:
- `src/index.css` — style globalne
- `src/App.css` — style komponentu App

W większych projektach:
- Każdy komponent może mieć własny plik CSS: `Header.css`, `Footer.css`
- Import CSS w pliku komponentu: `import "./Header.css";`

```
src/
├── components/
│   ├── Header.js
│   ├── Header.css
│   ├── KursKarta.js
│   └── KursKarta.css
├── App.js
├── App.css
├── index.js
└── index.css
```

---

## 7. zdarzenia (Events)

### 7.1. onClick — obsługa kliknięcia

Zdarzenie `onClick` reaguje na kliknięcie elementu (najczęściej przycisku):

```jsx
// Plik: src/App.js
function App() {
  // Sposób 1: Osobna funkcja obsługi (handler)
  function handleKliknij() {
    console.log("Przycisk został kliknięty!");
  }

  // Sposób 2: Handler z parametrem
  function handlePowitaj(imie) {
    console.log(`Cześć, ${imie}!`);
  }

  return (
    <div className="container mt-4">
      {/* Przekazanie referencji do funkcji (BEZ nawiasów) */}
      <button onClick={handleKliknij}>Kliknij mnie</button>

      {/* Funkcja strzałkowa inline */}
      <button onClick={() => console.log("Kliknięto!")}>
        Kliknij
      </button>

      {/* Przekazanie argumentu — wymaga strzałki */}
      <button onClick={() => handlePowitaj("Jan")}>
        Powitaj Jana
      </button>
    </div>
  );
}

export default App;
```

**Ważne — częsty błąd:**

```jsx
{/* błąd — funkcja WYKONA SIĘ od razu przy renderze */}
<button onClick={handlePowitaj("Jan")}>Kliknij</button>

{/* POPRAWNIE — funkcja wykona się dopiero po kliknięciu */}
<button onClick={() => handlePowitaj("Jan")}>Kliknij</button>
```

### 7.2. onChange — zmiana wartości pola

Zdarzenie `onChange` reaguje na zmianę wartości pola formularza. Jest kluczowe w formularzach kontrolowanych:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [imie, setImie] = useState("");

  function handleZmiana(event) {
    // event.target.value zawiera aktualną wartość pola
    setImie(event.target.value);
  }

  return (
    <div className="container mt-4">
      <input
        type="text"
        value={imie}
        onChange={handleZmiana}
        placeholder="Wpisz imię"
      />
      <p>Wpisałeś: {imie}</p>
    </div>
  );
}

export default App;
```

### 7.3. onSubmit — wysłanie formularza

Zdarzenie `onSubmit` reaguje na wysłanie formularza. **Zawsze** należy wywołać `event.preventDefault()`, aby zapobiec przeładowaniu strony:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [imie, setImie] = useState("");
  const [wiadomosc, setWiadomosc] = useState("");

  function handleSubmit(event) {
    event.preventDefault(); // Zapobiegamy przeładowaniu strony!
    console.log("Wysłano formularz:", imie);
    setWiadomosc(`Cześć, ${imie}!`);
    setImie(""); // Czyszczenie pola po wysłaniu
  }

  return (
    <div className="container mt-4">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={imie}
          onChange={(e) => setImie(e.target.value)}
          placeholder="Wpisz imię"
          className="form-control mb-2"
        />
        <button type="submit" className="btn btn-primary">
          Wyślij
        </button>
      </form>

      {wiadomosc && <p className="mt-3">{wiadomosc}</p>}
    </div>
  );
}

export default App;
```

### 7.4. onBlur — utrata fokusa

Zdarzenie `onBlur` reaguje, gdy pole traci fokus (kursor go opuści). Przydatne do walidacji:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [blad, setBlad] = useState("");

  function walidujEmail() {
    if (!email.includes("@")) {
      setBlad("Email musi zawierać znak @");
    } else {
      setBlad("");
    }
  }

  return (
    <div className="container mt-4">
      <input
        type="text"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        onBlur={walidujEmail}
        placeholder="Wpisz email"
        className="form-control"
      />
      {blad && <p style={{ color: "red" }}>{blad}</p>}
    </div>
  );
}

export default App;
```

### 7.5. przekazywanie argumentów do handlera

Gdy chcesz przekazać argument do funkcji obsługi zdarzenia, musisz użyć funkcji strzałkowej:

```jsx
// Plik: src/App.js
function App() {
  function handleUsun(id) {
    console.log("Usuwam element o id:", id);
  }

  const elementy = [
    { id: 1, nazwa: "Element A" },
    { id: 2, nazwa: "Element B" },
    { id: 3, nazwa: "Element C" },
  ];

  return (
    <ul>
      {elementy.map((el) => (
        <li key={el.id}>
          {el.nazwa}
          {/* Strzałka opakowuje wywołanie z argumentem */}
          <button onClick={() => handleUsun(el.id)}>Usuń</button>
        </li>
      ))}
    </ul>
  );
}

export default App;
```

### 7.6. obiekt zdarzenia (event)

Każdy handler otrzymuje obiekt zdarzenia (event) jako pierwszy argument:

```jsx
function App() {
  function handleKliknij(event) {
    console.log("Typ zdarzenia:", event.type);       // "click"
    console.log("Element docelowy:", event.target);   // <button>...</button>
    console.log("Tekst elementu:", event.target.textContent);
  }

  function handleZmiana(event) {
    console.log("Wartość pola:", event.target.value);
    console.log("Nazwa pola:", event.target.name);
  }

  return (
    <div>
      <button onClick={handleKliknij}>Kliknij</button>
      <input name="imie" onChange={handleZmiana} />
    </div>
  );
}
```

### 7.7. najczęstsze zdarzenia — tabela

| Zdarzenie | Element | Kiedy się uruchamia |
|---|---|---|
| `onClick` | Przycisk, link, dowolny element | Po kliknięciu |
| `onChange` | Input, select, textarea, checkbox | Gdy zmieni się wartość |
| `onSubmit` | Form | Gdy formularz jest wysyłany |
| `onBlur` | Input, select, textarea | Gdy pole traci fokus |
| `onFocus` | Input, select, textarea | Gdy pole uzyskuje fokus |
| `onKeyDown` | Input | Gdy klawisz jest wciśnięty |
| `onKeyUp` | Input | Gdy klawisz jest puszczony |
| `onMouseEnter` | Dowolny element | Gdy kursor wjeżdża na element |
| `onMouseLeave` | Dowolny element | Gdy kursor opuszcza element |

---

## 8. stan komponentu — useState

### 8.1. po co jest stan (React hook `useState`)

W podstawowym JavaScripcie, gdy chcemy przechować rosnącą liczbę kliknięć posłużylibyśmy się słówkiem `let`, a następnie zmienili tę wartość poprzez standardowe przypisanie (np. `naszaZmienna = 5`). W React, budując aplikacje Single Page Application wymagamy, by w reakcji na zaistniałą operację nasz ekran natychmiast odświeżał bloki odpowiedzialne w HTML i JSX za dany zmienny widok.

Zwykłe zadeklarowanie `let` nie wystarcza – o ile system zaktualizowałby wpis matematycznie w obrębie pamięci wewnętrznej uśpionego układu – ekran HTML w przeglądarce internauty powtarzałby uparcie cyfrę wyświetloną jednorazowo wejścia przy renderze. Stan, czyli `state`, i z dedykowana do powoływania go instrukcja tj: `useState`, wymusza aktualizowanie od zera wskazanego wyrenderowanego komponentu zawsze, gdy tylko przypiszemy z wykorzystaniem go jakiekolwiek pożądane, ewoluujące dane.

```jsx
// BŁĘDNIE - Dlaczego 'let' na ekranie nam w UI nie zadziała
function KomponentOpartyOLetBledny() {
  let zepsutyLicznik = 0;

  function przyspieszLiczenie() {
    zepsutyLicznik = zepsutyLicznik + 1; 
    console.log("Ten licznik zmienia wartość, ale HTML o tym nie wie", zepsutyLicznik);  
  }

  return (
    <div>
      <p>Licznik zatrzymany i na wpust martwy wizualnie: {zepsutyLicznik}</p>
      <button onClick={przyspieszLiczenie}>Wykonaj. Żadna graficzna animacja DOM HTML na podstronie nie wystąpi.</button>
    </div>
  );
}
```

```jsx
// POPRAWNIE - W oparciu o naturalne środowisko i Hook z React -> State
import { useState } from "react"; 

function DzialajacyReakcyjnyNaszZliczajacyWidok() {
  // useState wyrównuje dwu-częściową Tablicę po dekonstrukcji: 
  // Pierwszy wpis [liczbaWPolu] to zwykły uchwyt pozwalający ODCZYTYWAĆ wartość z systemu dla HTML.
  // Drugi wpis [setLiczbaWPolu], zwany w żargonie profesjonalnym `setterem`, służy systemowi TYLKO i WYŁĄCZNIE do modyfikowania owej liczby. Po wpisaniu tam danych "w locie" po wciśnięciu guzika, set... zarządzi błyskawicznie "re-render" byś od razu po spacji zobaczył efekty na oknie HTML. W argumencie do (..) useState - daliśmy 0 odpowiada za domyślny status startu do wglądu.
  
  const [liczbaWPolu, setLiczbaWPolu] = useState(0); 

  function wezwijRozkazReRenderuZPodbiciemPrawa() {
    setLiczbaWPolu(liczbaWPolu + 1); 
  }

  return (
    <div>
      <p>Licznik powiązany ze sprawnie działającym aktualizatorem State w oknie render: {liczbaWPolu}</p>
      <button onClick={wezwijRozkazReRenderuZPodbiciemPrawa}>Naciśnij guzik! Skrypt uaktualni i odmaluje re-renderowane ramy na nowe wyniki.</button>
    </div>
  );
}

export default DzialajacyReakcyjnyNaszZliczajacyWidok;
```


### 8.2. składnia useState

```jsx
import { useState } from "react";

// Składnia:
const [wartość, setWartość] = useState(wartośćPoczątkowa);
```

| Element | Znaczenie |
|---|---|
| `wartość` | Aktualna wartość stanu |
| `setWartość` | Funkcja do zmiany stanu (konwencja: `set` + nazwa) |
| `wartośćPoczątkowa` | Wartość przy pierwszym renderze |

```jsx
// Przykłady typów stanu
const [licznik, setLicznik] = useState(0);         // number
const [imie, setImie] = useState("");               // string
const [aktywny, setAktywny] = useState(false);      // boolean
const [lista, setLista] = useState([]);              // tablica
const [formularz, setFormularz] = useState({         // obiekt
  imie: "",
  email: "",
});
```

### 8.3. stan liczbowy — licznik

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [licznik, setLicznik] = useState(0);

  return (
    <div className="container mt-4 text-center">
      <h1>Licznik: {licznik}</h1>
      <button className="btn btn-success me-2" onClick={() => setLicznik(licznik + 1)}>
        +1
      </button>
      <button className="btn btn-danger me-2" onClick={() => setLicznik(licznik - 1)}>
        -1
      </button>
      <button className="btn btn-secondary" onClick={() => setLicznik(0)}>
        Reset
      </button>
    </div>
  );
}

export default App;
```

### 8.4. stan tekstowy

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [imie, setImie] = useState("");

  return (
    <div className="container mt-4">
      <label htmlFor="imie" className="form-label">Twoje imię:</label>
      <input
        id="imie"
        type="text"
        className="form-control"
        value={imie}
        onChange={(e) => setImie(e.target.value)}
        placeholder="Wpisz imię"
      />
      <p className="mt-2">Wpisałeś: <strong>{imie || "(nic)"}</strong></p>
      <p>Liczba znaków: {imie.length}</p>
    </div>
  );
}

export default App;
```

### 8.5. stan boolean — przełącznik

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [widoczny, setWidoczny] = useState(true);

  return (
    <div className="container mt-4">
      <button
        className="btn btn-primary"
        onClick={() => setWidoczny(!widoczny)}
      >
        {widoczny ? "Ukryj" : "Pokaż"} treść
      </button>

      {widoczny && (
        <div className="alert alert-info mt-3">
          <p>To jest treść, którą można pokazać lub ukryć.</p>
        </div>
      )}
    </div>
  );
}

export default App;
```

### 8.6. aktualizacja na podstawie poprzedniego stanu

Jeśli nowa wartość stanu zależy od poprzedniej, używaj **formy funkcyjnej**:

```jsx
// Forma zwykła — OK w prostych przypadkach
setLicznik(licznik + 1);

// Forma funkcyjna — ZALECANA gdy nowa wartość zależy od poprzedniej
setLicznik((prev) => prev + 1);
```

Forma funkcyjna jest ważna, gdy wiele aktualizacji może nastąpić szybko po sobie:

```jsx
function dodajTrzy() {
  // błąd — wszystkie trzy odczytają ten sam „stary" licznik
  setLicznik(licznik + 1);
  setLicznik(licznik + 1);
  setLicznik(licznik + 1);
  // Wynik: licznik wzrośnie tylko o 1!

  // POPRAWNIE — każda aktualizacja bazuje na aktualnej wartości
  setLicznik((prev) => prev + 1);
  setLicznik((prev) => prev + 1);
  setLicznik((prev) => prev + 1);
  // Wynik: licznik wzrośnie o 3
}
```

### 8.7. reset stanu

Reset stanu polega na ustawieniu wartości początkowej:

```jsx
const [imie, setImie] = useState("");
const [wiek, setWiek] = useState(0);

function handleReset() {
  setImie("");
  setWiek(0);
}
```

### 8.8. stan nie aktualizuje się natychmiast

Funkcja `setState` jest asynchroniczna — nowa wartość nie jest dostępna od razu w tej samej linii kodu:

```jsx
function handleKliknij() {
  setLicznik(licznik + 1);
  console.log(licznik); // Nadal STARA wartość!
}
```

Jeśli potrzebujesz nowej wartości do obliczeń w tym samym handlerze, oblicz ją przed ustawieniem stanu:

```jsx
function handleKliknij() {
  const nowaWartosc = licznik + 1;
  setLicznik(nowaWartosc);
  console.log(nowaWartosc); // Teraz masz nową wartość
}
```

### 8.9. lazy initial state

Jeśli obliczenie wartości początkowej jest kosztowne, przekaż **funkcję** do `useState`:

```jsx
// Funkcja zostanie wywołana TYLKO przy pierwszym renderze
const [dane, setDane] = useState(() => {
  const zapisane = localStorage.getItem("dane");
  return zapisane ? JSON.parse(zapisane) : [];
});
```

### 8.10. zmienna lokalna vs stan — różnica

| Cecha | Zmienna lokalna (`let`) | Stan (`useState`) |
|---|---|---|
| Zmiana wartości | Odbywa się po cichu | Powoduje re-render komponentu |
| Widok (JSX) | Nie aktualizuje się | Aktualizuje się automatycznie |
| Przetrwa re-render? | Nie — resetuje się | Tak — React zapamiętuje wartość |
| Użycie w React | Zmienne pomocnicze, obliczenia | Dane interaktywne (formularze, listy) |

---

## 9. formularze kontrolowane

### 9.1. czym jest formularz kontrolowany i dlaczego go musisz pisać?

Zrozumienie **formularza kontrolowanego (controlled forms)** jest jedną z absolutnie najważniejszych umiejętności react-developera. Jeżeli przychodzisz z czystego HTML'a lub PHP, pamiętasz że kliknięcie przycisku "Submit" (<form>) domyślnie powodowało odświeżenie całej strony (i np. wysłanie żądania do serwera dopisując parametry do paska adresu URL typu `?name=adam`).

**W aplikacjach Single Page Application (React) takie zdarzenie (przeładowanie karty) to gigantyczny błąd! Aplikacja nigdy nie powinna mrugać odświeżając okno przeglądarki!** Właśnie dlatego całkowicie "przejmujesz kontrolę" nad zachowaniem formularza z wykorzystaniem **stanu (useState)**.

Wprowadzamy mechanizm z 3 fundamentalnymi filarami:
1. **Pamięć Aplikacji (Stan):** Deklarujemy zmienną `useState` np. `[haslo, setHaslo] = useState("")`.
2. **Kierunek w dół (value):** Nakazujemy inputowi (pole wpisywania), aby zawsze pokazywał to co kryje się w the w stanie: `value={haslo}`. Oznacza to, że input bez zgłoszenia przez React sam z siebie absolutnie nie pokaże tekstu jeśli klikniemy klawisz! W tym momencie jest uwięziony ("kontrolowany" przez stary stan).
3. **Kierunek w górę (onChange):** Reagujemy na fizyczne wstukiwanie klawiszy we wpisie przez event: `onChange={(event) => setHaslo(event.target.value)}`. Event ten powołuje nowy stan z nową literką - a punkt drugi każe inputowi to przerysować.

```jsx
// Złoty, najważniejszy wzorzec formularza basic:
import { useState } from "react";

function FormularzPodstawowy() {
  const [szukanaFraza, setSzukanaFraza] = useState("");

  // Funkcja blokująca odświeżenie strony po wciśnięciu Enter!
  const obslugaWyslania = (event) => {
    event.preventDefault(); // <-- KRÓL REAGOWANIA W REACT (Zatrzymanie domyślnego zachowania)
    console.log("Znaleziono wpisaną przez użytkownika frazę: ", szukanaFraza);
    
    // Na przykład tutaj wysyłałoby się zapytanie do serwera...
  };

  return (
    <form onSubmit={obslugaWyslania}>
      <label>Szukaj u nas:</label>
      <input 
        type="text"
        value={szukanaFraza} // 2. Połączenie 1 stronne (blokada tekstu z zewnątrz)
        onChange={(e) => setSzukanaFraza(e.target.value)} // 3. Uwolnienie tekstów i reakcja
      />
      <button type="submit">Szukaj teraz</button>
    </form>
  );
}
```
Zastosowanie `e.preventDefault()` jest krytyczne podczas budowy aplikacji wykorzystujących klasyczne formularze webowe!

### 9.2. input text

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [imie, setImie] = useState("");

  return (
    <div className="container mt-4">
      <div className="mb-3">
        <label htmlFor="imie" className="form-label">Imię:</label>
        <input
          id="imie"
          type="text"
          className="form-control"
          value={imie}
          onChange={(e) => setImie(e.target.value)}
          placeholder="Wpisz swoje imię"
        />
      </div>
      <p>Wartość: {imie}</p>
    </div>
  );
}

export default App;
```

### 9.3. input number

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [wiek, setWiek] = useState(0);

  return (
    <div className="container mt-4">
      <div className="mb-3">
        <label htmlFor="wiek" className="form-label">Wiek:</label>
        <input
          id="wiek"
          type="number"
          className="form-control"
          value={wiek}
          onChange={(e) => setWiek(Number(e.target.value))}
          min="0"
          max="150"
        />
      </div>
      <p>Wiek: {wiek} lat</p>
      <p>{wiek >= 18 ? "Pełnoletni" : "Niepełnoletni"}</p>
    </div>
  );
}

export default App;
```

**Uwaga:** `e.target.value` zawsze zwraca `string`, nawet dla `type="number"`. Musisz skonwertować na liczbę za pomocą `Number()`.

### 9.4. input password

```jsx
<div className="mb-3">
  <label htmlFor="haslo" className="form-label">Hasło:</label>
  <input
    id="haslo"
    type="password"
    className="form-control"
    value={haslo}
    onChange={(e) => setHaslo(e.target.value)}
    placeholder="Wpisz hasło"
  />
</div>
```

### 9.5. select — lista rozwijana

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [rodzaj, setRodzaj] = useState("");

  const rodzaje = ["Sensacyjny", "Komedia", "Horror", "Dramat", "Sci-Fi"];

  return (
    <div className="container mt-4">
      <div className="mb-3">
        <label htmlFor="rodzaj" className="form-label">Rodzaj filmu:</label>
        <select
          id="rodzaj"
          className="form-select"
          value={rodzaj}
          onChange={(e) => setRodzaj(e.target.value)}
        >
          <option value="">-- Wybierz rodzaj --</option>
          {rodzaje.map((r) => (
            <option key={r} value={r}>{r}</option>
          ))}
        </select>
      </div>
      {rodzaj && <p>Wybrany rodzaj: {rodzaj}</p>}
    </div>
  );
}

export default App;
```

### 9.6. textarea

Textarea w React działa tak samo jak input — przez `value` i `onChange`:

```jsx
<div className="mb-3">
  <label htmlFor="opis" className="form-label">Opis:</label>
  <textarea
    id="opis"
    className="form-control"
    rows="4"
    value={opis}
    onChange={(e) => setOpis(e.target.value)}
    placeholder="Wpisz opis..."
  />
</div>
```

### 9.7. checkbox

Checkbox używa `checked` zamiast `value` i `onChange` z `e.target.checked`:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [zgoda, setZgoda] = useState(false);

  return (
    <div className="container mt-4">
      <div className="form-check mb-3">
        <input
          id="zgoda"
          type="checkbox"
          className="form-check-input"
          checked={zgoda}
          onChange={(e) => setZgoda(e.target.checked)}
        />
        <label htmlFor="zgoda" className="form-check-label">
          Akceptuję regulamin
        </label>
      </div>
      <p>Zgoda: {zgoda ? "Tak" : "Nie"}</p>
    </div>
  );
}

export default App;
```

### 9.8. checkbox jako switch (Bootstrap)

```jsx
<div className="form-check form-switch mb-3">
  <input
    id="tryb"
    type="checkbox"
    className="form-check-input"
    checked={trybCiemny}
    onChange={(e) => setTrybCiemny(e.target.checked)}
  />
  <label htmlFor="tryb" className="form-check-label">
    Tryb ciemny
  </label>
</div>
```

### 9.9. radio — wybór jednej opcji

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [plec, setPlec] = useState("");

  return (
    <div className="container mt-4">
      <p>Płeć:</p>
      <div className="form-check">
        <input
          id="kobieta"
          type="radio"
          className="form-check-input"
          name="plec"
          value="kobieta"
          checked={plec === "kobieta"}
          onChange={(e) => setPlec(e.target.value)}
        />
        <label htmlFor="kobieta" className="form-check-label">Kobieta</label>
      </div>
      <div className="form-check">
        <input
          id="mezczyzna"
          type="radio"
          className="form-check-input"
          name="plec"
          value="mezczyzna"
          checked={plec === "mezczyzna"}
          onChange={(e) => setPlec(e.target.value)}
        />
        <label htmlFor="mezczyzna" className="form-check-label">Mężczyzna</label>
      </div>
      {plec && <p className="mt-2">Wybrano: {plec}</p>}
    </div>
  );
}

export default App;
```

### 9.10. range — suwak

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [glosnosc, setGlosnosc] = useState(50);

  return (
    <div className="container mt-4">
      <label htmlFor="glosnosc" className="form-label">
        Głośność: {glosnosc}%
      </label>
      <input
        id="glosnosc"
        type="range"
        className="form-range"
        min="0"
        max="100"
        value={glosnosc}
        onChange={(e) => setGlosnosc(Number(e.target.value))}
      />
    </div>
  );
}

export default App;
```

### 9.11. formularz jako jeden obiekt stanu

Zamiast tworzyć osobny `useState` dla każdego pola, możesz trzymać cały formularz w jednym obiekcie:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [formularz, setFormularz] = useState({
    imie: "",
    email: "",
    wiek: 0,
  });

  // Uniwersalna funkcja obsługi zmiany — działa dla każdego pola
  function handleChange(e) {
    const { name, value, type } = e.target;
    setFormularz((prev) => ({
      ...prev,
      // Jeśli pole jest liczbowe, konwertuj na Number
      [name]: type === "number" ? Number(value) : value,
    }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Dane formularza:", formularz);
  }

  return (
    <div className="container mt-4">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="imie" className="form-label">Imię:</label>
          <input
            id="imie"
            name="imie"
            type="text"
            className="form-control"
            value={formularz.imie}
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email:</label>
          <input
            id="email"
            name="email"
            type="text"
            className="form-control"
            value={formularz.email}
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="wiek" className="form-label">Wiek:</label>
          <input
            id="wiek"
            name="wiek"
            type="number"
            className="form-control"
            value={formularz.wiek}
            onChange={handleChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">Wyślij</button>
      </form>
    </div>
  );
}

export default App;
```

**Kluczowy mechanizm:** `[name]: value` — dynamiczny klucz obiektu. Jeśli `name="imie"`, to `[name]` staje się polem `imie` w obiekcie. Dzięki temu **jedna funkcja** `handleChange` obsługuje **wszystkie pola**.

### 9.12. walidacja formularza

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [imie, setImie] = useState("");
  const [email, setEmail] = useState("");
  const [bledy, setBledy] = useState({});

  function waliduj() {
    const noweBledy = {};

    if (imie.trim() === "") {
      noweBledy.imie = "Imię jest wymagane";
    } else if (imie.trim().length < 2) {
      noweBledy.imie = "Imię musi mieć co najmniej 2 znaki";
    }

    if (email.trim() === "") {
      noweBledy.email = "Email jest wymagany";
    } else if (!email.includes("@")) {
      noweBledy.email = "Email musi zawierać @";
    }

    return noweBledy;
  }

  function handleSubmit(e) {
    e.preventDefault();
    const noweBledy = waliduj();

    if (Object.keys(noweBledy).length > 0) {
      setBledy(noweBledy);
      return; // Przerywamy — formularz jest niepoprawny
    }

    setBledy({}); // Czyścimy błędy
    console.log("Wysłano:", { imie, email });
  }

  return (
    <div className="container mt-4">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="imie" className="form-label">Imię:</label>
          <input
            id="imie"
            type="text"
            className={`form-control ${bledy.imie ? "is-invalid" : ""}`}
            value={imie}
            onChange={(e) => setImie(e.target.value)}
          />
          {bledy.imie && <div className="invalid-feedback">{bledy.imie}</div>}
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email:</label>
          <input
            id="email"
            type="text"
            className={`form-control ${bledy.email ? "is-invalid" : ""}`}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          {bledy.email && <div className="invalid-feedback">{bledy.email}</div>}
        </div>
        <button type="submit" className="btn btn-primary">Wyślij</button>
      </form>
    </div>
  );
}

export default App;
```

### 9.13. reset formularza

```jsx
function handleReset() {
  setImie("");
  setEmail("");
  setWiek(0);
  setBledy({});
}

// Dla formularza obiektowego:
function handleReset() {
  setFormularz({ imie: "", email: "", wiek: 0 });
}
```

```jsx
<button type="button" className="btn btn-secondary" onClick={handleReset}>
  Wyczyść
</button>
```

---

## 10. renderowanie warunkowe

### 10.1. if przed return

Najprostszy sposób — warunkowe zwrócenie innego widoku:

```jsx
function App() {
  const [zalogowany, setZalogowany] = useState(false);

  if (!zalogowany) {
    return (
      <div className="container mt-4">
        <p>Musisz się zalogować.</p>
        <button className="btn btn-primary" onClick={() => setZalogowany(true)}>
          Zaloguj
        </button>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <p>Witaj! Jesteś zalogowany.</p>
      <button className="btn btn-danger" onClick={() => setZalogowany(false)}>
        Wyloguj
      </button>
    </div>
  );
}
```

### 10.2. operator trójargumentowy w jsx

Do krótkich warunków w JSX:

```jsx
<p>{aktywny ? "Status: Aktywny" : "Status: Nieaktywny"}</p>
<button className={`btn ${aktywny ? "btn-success" : "btn-danger"}`}>
  {aktywny ? "Wyłącz" : "Włącz"}
</button>
```

### 10.3. operator && — warunkowe wyświetlanie

Wyświetla element **tylko gdy** warunek jest prawdziwy:

```jsx
{blad && <p className="text-danger">{blad}</p>}
{lista.length > 0 && <ul>{lista.map(el => <li key={el}>{el}</li>)}</ul>}
{zalogowany && <button className="btn btn-danger">Wyloguj</button>}
```

### 10.4. komunikaty błędów walidacji

```jsx
{bledy.imie && (
  <div className="text-danger small mt-1">{bledy.imie}</div>
)}
```

### 10.5. obsługa pustej listy

```jsx
function ListaKursow({ kursy }) {
  if (kursy.length === 0) {
    return <p className="text-muted">Brak kursów do wyświetlenia.</p>;
  }

  return (
    <ul className="list-group">
      {kursy.map((kurs) => (
        <li key={kurs.id} className="list-group-item">{kurs.nazwa}</li>
      ))}
    </ul>
  );
}
```

---

## 11. tablice i renderowanie list

### 11.1. renderowanie tablicy przez map()

`map()` to główny sposób wyświetlania list w React:

```jsx
// Plik: src/App.js
function App() {
  const kursy = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "React od podstaw",
    "Bazy danych SQL",
  ];

  return (
    <div className="container mt-4">
      <h2>Dostępne kursy ({kursy.length})</h2>
      <ol>
        {kursy.map((kurs, index) => (
          <li key={index}>{kurs}</li>
        ))}
      </ol>
    </div>
  );
}

export default App;
```

### 11.2. atrybut key — dlaczego jest wymagany

Każdy element generowany przez `map()` **musi mieć** atrybut `key` — unikalny identyfikator, który pozwala Reactowi śledzić, który element się zmienił:

```jsx
// błąd — brak key (ostrzeżenie w konsoli)
{elementy.map((el) => <li>{el.nazwa}</li>)}

// POPRAWNIE — key z unikalnego id
{elementy.map((el) => <li key={el.id}>{el.nazwa}</li>)}

// DOPUSZCZALNE — index jako key (tylko gdy lista się nie zmienia)
{elementy.map((el, index) => <li key={index}>{el.nazwa}</li>)}
```

**Zasady key:**
- Key musi być **unikalny** wśród rodzeństwa.
- Najlepszy key to **id** z danych (np. z bazy danych, `Date.now()`).
- **Nie używaj indeksu** (`index`) jako key, jeśli kolejność elementów może się zmieniać (przy usuwaniu, sortowaniu).

### 11.3. lista numerowana

```jsx
function App() {
  const kursy = ["HTML", "CSS", "JavaScript", "React"];

  return (
    <div className="container mt-4">
      <h2>Dostępnych kursów: {kursy.length}</h2>
      <ol>
        {kursy.map((kurs, index) => (
          <li key={index}>{kurs}</li>
        ))}
      </ol>
    </div>
  );
}
```

### 11.4. dodawanie elementu do tablicy stanu

W React **nigdy nie mutujemy** stanu. Zamiast `push()` tworzymy nową tablicę za pomocą spread:

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [zadania, setZadania] = useState([]);
  const [tekst, setTekst] = useState("");

  function handleDodaj(e) {
    e.preventDefault();
    if (tekst.trim() === "") return;

    // POPRAWNIE — tworzenie nowej tablicy z dodanym elementem
    const noweZadanie = { id: Date.now(), tekst: tekst };
    setZadania((prev) => [...prev, noweZadanie]);
    setTekst(""); // Czyszczenie pola
  }

  return (
    <div className="container mt-4">
      <form onSubmit={handleDodaj}>
        <input
          type="text"
          className="form-control mb-2"
          value={tekst}
          onChange={(e) => setTekst(e.target.value)}
          placeholder="Nowe zadanie"
        />
        <button type="submit" className="btn btn-success">Dodaj</button>
      </form>
      <ul className="list-group mt-3">
        {zadania.map((z) => (
          <li key={z.id} className="list-group-item">{z.tekst}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

### 11.5. usuwanie elementu z tablicy stanu

Usuwanie odbywa się przez `filter()` — tworzymy nową tablicę bez elementu o podanym id:

```jsx
function handleUsun(id) {
  setZadania((prev) => prev.filter((z) => z.id !== id));
}

// W JSX:
{zadania.map((z) => (
  <li key={z.id} className="list-group-item d-flex justify-content-between">
    {z.tekst}
    <button className="btn btn-danger btn-sm" onClick={() => handleUsun(z.id)}>
      Usuń
    </button>
  </li>
))}
```

### 11.6. aktualizacja jednego elementu w tablicy

Aktualizacja jednego elementu odbywa się przez `map()` — tworzymy nową tablicę, a element o podanym id zastępujemy zmodyfikowaną kopią:

```jsx
function zwiekszPobrania(id) {
  setZdjecia((prev) =>
    prev.map((zdjecie) =>
      zdjecie.id === id
        ? { ...zdjecie, pobrania: zdjecie.pobrania + 1 }
        : zdjecie
    )
  );
}
```

Wyjaśnienie krok po kroku:
1. `map()` przechodzi przez każdy element tablicy.
2. Jeśli `id` elementu pasuje — tworzymy **kopię** z zmienionym polem (`{ ...zdjecie, pobrania: zdjecie.pobrania + 1 }`).
3. Jeśli `id` nie pasuje — zwracamy element bez zmian.
4. `map()` zwraca **nową tablicę** — stara nie jest mutowana.

### 11.7. sortowanie tablicy w stanie

```jsx
function handleSortuj() {
  setElementy((prev) =>
    [...prev].sort((a, b) => a.nazwa.localeCompare(b.nazwa))
  );
}

// Sortowanie liczbowe
function handleSortujPoCenie() {
  setProdukty((prev) =>
    [...prev].sort((a, b) => a.cena - b.cena)
  );
}
```

**Ważne:** `sort()` mutuje tablicę, dlatego najpierw tworzymy kopię `[...prev]`, a dopiero na niej wywołujemy `sort()`.

---

## 12. obiekty w stanie

### 12.1. model danych — tablica obiektów

W React dane najczęściej modelujemy jako tablicę obiektów:

```jsx
const zdjecia = [
  { id: 1, nazwa: "kwiat.jpg", kategoria: "kwiaty", pobrania: 12 },
  { id: 2, nazwa: "gora.jpg", kategoria: "krajobrazy", pobrania: 34 },
  { id: 3, nazwa: "roza.jpg", kategoria: "kwiaty", pobrania: 7 },
  { id: 4, nazwa: "miasto.jpg", kategoria: "miasto", pobrania: 21 },
];
```

### 12.2. kopiowanie obiektu — spread

W React stan jest niezmienny (immutable). Przy aktualizacji obiektu **nigdy nie modyfikujemy** go bezpośrednio — tworzymy kopię:

```jsx
const [osoba, setOsoba] = useState({ imie: "Jan", wiek: 25, miasto: "Kraków" });

// błąd — mutacja
osoba.wiek = 26;
setOsoba(osoba); // React NIE widzi zmiany (ta sama referencja)

// POPRAWNIE — kopia ze zmienioną wartością
setOsoba({ ...osoba, wiek: 26 });

// Z formą funkcyjną (zalecane)
setOsoba((prev) => ({ ...prev, wiek: 26 }));
```

### 12.3. formularz jako obiekt stanu

Patrz sekcja [9.11](#911-formularz-jako-jeden-obiekt-stanu).

### 12.4. dane z pliku przepisane do kodu

Często surowe dane, pochodzące np. z pliku `dane.txt`, możemy przenieść bezpośrednio do kodu jako tablicę obiektów:

```jsx
// Plik: src/App.js
// dane.txt zawierał:
// kwiat.jpg;kwiaty;12
// gora.jpg;krajobrazy;34
// roza.jpg;kwiaty;7

function App() {
  const [zdjecia, setZdjecia] = useState([
    { id: 1, nazwa: "kwiat.jpg", kategoria: "kwiaty", pobrania: 12 },
    { id: 2, nazwa: "gora.jpg", kategoria: "krajobrazy", pobrania: 34 },
    { id: 3, nazwa: "roza.jpg", kategoria: "kwiaty", pobrania: 7 },
  ]);

  // ... reszta komponentu
}
```

---

## 13. Bootstrap w React — kompletny przewodnik

Bootstrap to najpopularniejszy na świecie framework CSS służący do szybkiego tworzenia nowoczesnych i responsywnych interfejsów użytkownika. React i Bootstrap doskonale się przenikają, pozwalając na niesamowite przyspieszenie pracy nad front-endem, szczególnie w aplikacjach panelowych czy e-commerce.

### 13.1. instalacja i konfiguracja bootstrapa

Do projektu Reactowego instalujemy Bootstrapa jako paczkę NPM. Nie używamy linków CDN (tagów `<link />` w plikach HTML), ponieważ podejście oparte na pakietach npm, dzięki procesom budowania (Webpack/Vite), ładuje i optymalizuje naszą aplikację poprawnie.

```bash
# Szybka rejestracja pakietu bootstrapa w projekcie
npm install bootstrap
```

Po zakończeniu instalacji, należy zaimportować główne style CSS Bootstrapa w pliku głównym — najczęściej w **`src/index.js`** (lub czasami w `src/App.js`).

```jsx
// Plik: src/index.js
import React from "react";
import ReactDOM from "react-dom/client";

// Importuj zawsze przed twoimi własnymi stylami.
import "bootstrap/dist/css/bootstrap.css"; 
// Jeśli chcesz korzystać również z ikon: npm install bootstrap-icons
// import "bootstrap-icons/font/bootstrap-icons.css";

import "./index.css"; // Twój plik z nadpisanymi stylami (ważne by był po Bootstrapie!)
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### 13.2. czysty Bootstrap (CSS) vs React-Bootstrap (Komponenty)

Są dwie główne szkoły używania Bootstrapa z Reactem:

1. **Stylowanie przy pomocy klas (`className`)** — Opisywane w tej dokumentacji. Zwykła i najbardziej popularna metoda polegająca na budowaniu HTML przy pomocy JSX i przypisywaniu predefiniowanych klas Bootstrapa (np. `<div className="col-md-6 mb-3">`). Jest to najprostsze, nie wymaga nauki nowej biblioteki komponentów, a cała wiedza z "czystego HTML'a" od razu tutaj wystarczy.
2. **Użycie `react-bootstrap`** — Zastępuje tradycyjnego Bootstrapa paczką oddzielnych komponentów JSX (np. `<Button variant="primary">`). Może być nieco bardziej zawiłe w nauczaniu i polecane raczej dla skomplikowanych projektów korporacyjnych. Wymaga wywołania `npm install react-bootstrap bootstrap`.

**W tej dokumentacji skupiamy się w 100% na klasach CSS z podstawowego Bootstrapa**, czyli najlepszym, najszybszym i uniwersalnym podejściu, doskonale sprawdzającym się zarówno w małych jak i potężnych projektach!

### 13.3. system Grid (Siatka 12-kolumnowa) w detalach

System sieci Bootstrap zbudowany jest w oparciu o *flexbox* i umożliwia utworzenie od 1 do 12 kolumn na stronie internetowej, które automatycznie skalują się zależąc od rozmiaru urządzenia.

Zasada: masz **pojemnik nadrzędny**, w nim dodajesz **wiersz** (`row`), a w nim tworzysz **kolumny** (`col`).

**Lista breakpointów (odcięć dla urządzeń):**
- `xs` (Extra small) — telefony (<576px) — używane przez bazową klasę, np. `.col-`
- `sm` (Small) — większe telefony (≥576px) — `.col-sm-`
- `md` (Medium) — tablety (≥768px) — `.col-md-`
- `lg` (Large) — małe laptopy / komputery (≥992px) — `.col-lg-`
- `xl` (Extra large) — normalne ekrany (≥1200px) — `.col-xl-`
- `xxl` (Extra extra large) — wielkie ekrany TV (≥1400px) — `.col-xxl-`

Przykłady precyzyjnego pozycjonowania (Responsywny Grid):

```jsx
<div className="container">
  {/* Wiersz z 3 równymi kolumnami na komputerze (col-md-4), 
      ale jedna nad drugą na małych telefonach (col-12) */}
  <div className="row">
    <div className="col-12 col-md-4 bg-primary text-white p-3">Kolumna 1</div>
    <div className="col-12 col-md-4 bg-success text-white p-3">Kolumna 2</div>
    <div className="col-12 col-md-4 bg-danger text-white p-3">Kolumna 3</div>
  </div>

  {/* Układ bocznego paska i zawartości głównej */}
  <div className="row mt-4">
    <div className="col-12 col-lg-3">Boczny Pasek Nawigacji (25% szerokości)</div>
    <div className="col-12 col-lg-9">Zawartość Główna (75% szerokości)</div>
  </div>
</div>
```

### 13.4. flexbox z bootstrapem (Klasy d-flex)

Bootstrap ułatwia pracę z flexboxem, dostarczając potężne klasy sterujące. Uruchamiasz je stosując klasę `d-flex` (zamiast `row`).

```jsx
<div className="container mt-4">
  <div className="d-flex justify-content-between align-items-center bg-light p-3">
    <div>Logo Lewa Strona</div>
    <div className="d-flex gap-3"> {/* gap-3 robi równe odstępy miedzy dziećmi */}
      <button className="btn btn-outline-secondary">Zaloguj</button>
      <button className="btn btn-primary">Zarejestruj się</button>
    </div>
  </div>

  {/* Praca w pionie */}
  <div className="d-flex flex-column align-items-center mt-5">
    <h2>Zapisz się do newslettera</h2>
    <input type="email" className="form-control w-50 mt-2" placeholder="Twój e-mail" />
  </div>
</div>
```

- **justify-content-center** - Wyśrodkowanie w poziomie
- **justify-content-between** - Pchanie do krawędzi (wolna przestrzeń w środku)
- **align-items-center** - Wyrównanie w pionie
- **gap-1, gap-2, gap-3, gap-4** - Genialne klasy na luki i odstępy pomiędzy elementami w środku kontenera.

### 13.5. typografia, kolory i tła

Kolor w Bootstrap stosuje się poprzez wywoływanie słów-kluczy dla palety (primary, secondary, success, danger, warning, info, light, dark).

- Kolor tekstu: `text-primary`, `text-danger`, `text-muted` (szary zgaszony kolor), `text-white`.
- Kolor tła: `bg-primary`, `bg-dark`, `bg-light`, `bg-success`.
- Ułożenie tekstu: `text-start` (lewo), `text-center` (środek), `text-end` (prawo).
- Estetyka tekstu: `fst-italic` (kursywa), `fw-bold` (pogrubienie), `fs-1`... `fs-6` (rozmiary czcionek jak znaczniki h1-h6).

```jsx
<div className="bg-dark text-white p-5 text-center">
  <h1 className="fw-bold">Nagle nagłówek z efektem!</h1>
  <p className="fs-4 text-muted">To jest podtytuł dla tekstu...</p>
</div>
```

### 13.6. wymiary, marginesy i paddingi (Spacing)

Aby użyć przerw (spacingów) używasz prefiksu do klasy na wzór `[właściwość][strona]-[rozmiar]`.
- **m** (Margin) i **p** (Padding)
- **Strona:** `t` (Top / góra), `b` (Bottom / dół), `s` (Start / lewo), `e` (End / prawo), `x` (oś X - lewo/prawo), `y` (oś Y - góra/dół), albo brak strony = "z każdej strony".
- **Rozmiary:** `0` (brak), `1` do `5` (narastający rozmiar), `auto` (automatycznie).

Z kolei rozmiar sztywnego elementu:
- **Szerokość:** `w-25`, `w-50`, `w-75`, `w-100`, `w-auto`.
- **Wysokość:** `h-25`, `h-50`, `h-75`, `h-100`.

```jsx
<div className="w-100 mx-auto mt-5 p-4 bg-light">
  {/* mx-auto idealnie wyśrodkowuje box na ekranie o ile jest w kontenerze */}
  <p className="mb-0">Zero marginesu od dołu (bottom).</p>
  <p className="my-3 px-5">Margines w pionie równy 3, padding poziomy (w lewo/prawo) to 5.</p>
</div>
```

### 13.7. przyciski (Buttons) i grupy przycisków

Klasa bazowa to zawsze `.btn`. Doklejasz do nich warianty:

```jsx
<div>
  {/* Zwykłe (wypełnienie) */}
  <button className="btn btn-primary m-1">Podstawowy</button>
  <button className="btn btn-success m-1">Zakończ</button>
  <button className="btn btn-danger m-1">Usuń</button>
  
  {/* Zarysowane (Outline) — transparentne tło z obwolutą i kolorem przy najechaniu */}
  <button className="btn btn-outline-info m-1">Przeczytaj więcej</button>
  <button className="btn btn-outline-dark m-1">Ciemny zarys</button>

  {/* Różne Rozmiary */}
  <button className="btn btn-primary btn-sm m-1">Mały knopik</button>
  <button className="btn btn-primary btn-lg m-1">Wielki Przycisk</button>

  {/* Stan wyłączony przy spełnionych warunkach React! */}
  <button className="btn btn-secondary w-100 mt-2" disabled={true}>
    Nieaktywny
  </button>
</div>
```

Możesz też zamknąć przyciski w `btn-group`, by scalić je ze sobą (nie będzie między nimi przerw i zaokrągleń u granic).
```jsx
<div className="btn-group" role="group">
  <button type="button" className="btn btn-outline-primary">Lewy</button>
  <button type="button" className="btn btn-outline-primary">Środkowy</button>
  <button type="button" className="btn btn-outline-primary">Prawy</button>
</div>
```

### 13.8. formularze zaawansowane (Input, select, switch, walidacja)

Znakomita dokumentacja Bootstrapa jest idealna jeśli połączymy to ze statusem (Stanem) formularza w React. Pola wejściowe używają klasy `form-control`, rozwijane zniżki `form-select`. Klasa `form-label` do opisów. `is-valid` lub `is-invalid` idealnie kolorują błędy.

```jsx
import { useState } from "react";

function SkomplikowanyFormularz() {
  const [imie, setImie] = useState("");
  const [przedmiot, setPrzedmiot] = useState("");
  
  // Zwróci logikę z poprawnością w klasie CSS
  const getValidationClass = () => {
    if (imie.length === 0) return ""; 
    return imie.length >= 3 ? "is-valid" : "is-invalid"; // Zmienia na czerwień lub zieleń
  };

  return (
    <form className="p-4 border rounded bg-light">
      <h3 className="mb-4">Zgłoszenie Użytkownika</h3>
      
      <div className="mb-3">
        <label htmlFor="imieUsera" className="form-label">Imię przypisane</label>
        <input 
          id="imieUsera" 
          type="text" 
          className={`form-control ${getValidationClass()}`} // Dynamika Bootstrap!
          value={imie} 
          onChange={(e) => setImie(e.target.value)} 
          placeholder="Wpisz imię..." 
        />
        <div className="invalid-feedback">Imię musi mieć minimum 3 znaki!</div>
      </div>

      <div className="mb-3">
        <label className="form-label">Wybór Przedmiotu</label>
        <select className="form-select text-primary shadow-sm" value={przedmiot} onChange={(e) => setPrzedmiot(e.target.value)}>
          <option value="">-- wybierz --</option>
          <option value="matma">Matematyka</option>
          <option value="fizyka">Fizyka</option>
        </select>
      </div>

      <div className="mb-3 form-check form-switch">
        <input className="form-check-input" type="checkbox" role="switch" id="regulamin" />
        <label className="form-check-label" htmlFor="regulamin">Zgadzam się na regulamin</label>
      </div>

      <button className="btn btn-success w-100" type="submit">Zapisz ustawienia</button>
    </form>
  );
}
```

### 13.9. karty (Cards) i bogate układy

Karty (Card) to fundamentalny składnik dla nowoczesnych dashboardów, produktów w sklepie do kliknięcia itp.

Budowa: Kontener `.card`, opcjonalnie z `.card-header` oraz `.card-footer`, oraz obowiązkowo serce karty `.card-body`, gdzie wrzucszamy detale i ewentualnie nagłówek karty z klasą `.card-title`. Opcjonalny obraz na samej górze lub u dołu za pomocą `.card-img-top`.

```jsx
<div className="row">
  {listaProduktow.map(prod => (
    <div key={prod.id} className="col-12 col-md-6 col-lg-4 mb-4">
      <div className="card h-100 shadow-sm border-0">
        <img src={prod.img} className="card-img-top" alt={prod.nazwa} style={{ height: "200px", objectFit: "cover" }} />
        <div className="card-body d-flex flex-column">
          <h5 className="card-title text-truncate">{prod.nazwa}</h5>
          <p className="card-text text-muted">{prod.opis}</p>
          <div className="mt-auto d-flex justify-content-between align-items-center">
            <span className="fw-bold fs-4 text-primary">{prod.cena} PLN</span>
            <button className="btn btn-outline-primary btn-sm">Do koszyka</button>
          </div>
        </div>
      </div>
    </div>
  ))}
</div>
```
*(Uwaga ekspercka) Zwróć uwagę na sprytne użycie klas `h-100`, w `card` oraz `d-flex flex-column` z `mt-auto` (powyżej button). Pozwala to na zrównanie wszystkich kart (każda będzie taka sama wysokość) a przyciski dociśnięte do ich podstawy dla doskonałej estetyki.*

### 13.10. tabele i paginacja

```jsx
<div className="table-responsive">
  {/* Dodaj klasę table-responsive do wrappera, by długa tabela pozwalała się scrollować na komórce. */}
  <table className="table table-bordered table-striped table-hover mt-3 shadow-sm rounded">
    <thead className="table-dark">
      <tr>
        <th>ID</th>
        <th>Imię</th>
        <th>Etykieta</th>
        <th className="text-end">Akcje</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>#102</td>
        <td>Janina Kowalska</td>
        <td><span className="badge bg-info">Premium</span></td>
        <td className="text-end">
          <button className="btn btn-sm btn-danger">Usuń</button>
        </td>
      </tr>
      <tr>
        <td>#103</td>
        <td>Marek Nowak</td>
        <td><span className="badge bg-secondary">Zwykły</span></td>
        <td className="text-end">
          <button className="btn btn-sm btn-danger">Usuń</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

### 13.11. komponenty UI: alerty, odznaki, paski postępu i spinnery

React kocha wykorzystać warunkowe renderowanie, by chować lub odsłaniać takie powiadomienia! W połączeniu z Bootstrapem to bardzo proste zadanie.

```jsx
{/* Alert / Powiadomienie */}
{czySukces && (
  <div className="alert alert-success mt-3" role="alert">
    <strong>Gratulacje!</strong> Twoje konto zostało poprawinie aktywowane.
  </div>
)}

{/* Odznaki */}
<h3>Powiadomienia <span className="badge bg-danger rounded-pill">12</span></h3>
Oto najnowszy komunikat <span className="badge bg-primary px-3 shadow">NOWOŚĆ</span>

{/* Spinner kręcący w dół na czas odświeżania API! */}
{isLoading && (
  <div className="d-flex justify-content-center mt-5">
    <div className="spinner-border text-primary" role="status">
      <span className="visually-hidden">Ładowanie danych...</span>
    </div>
  </div>
)}

{/* Pasek postępu */}
<div className="progress mt-4" style={{ height: "30px" }}>
  <div 
    className="progress-bar progress-bar-striped progress-bar-animated bg-success" 
    role="progressbar" 
    style={{ width: "75%" }}>
    75% Pobrano
  </div>
</div>
```

### 13.12. złożony przykład praktyczny: panel użytkownika

Poniżej całościowy kod demonstrujący profesjonalne i eleganckie wykonanie interfejsu (Dashboard/Panel) stosując w pełni zasady Bootstrapa, które właśnie przyswoiłeś.

```jsx
import React, { useState } from "react";

function UserDashboard() {
  const [trywCiemny, setTrybCiemny] = useState(false);

  return (
    <div className={trywCiemny ? "bg-dark text-white min-vh-100" : "bg-light min-vh-100"}>
      {/* Pasek Nawigacyjny na Samej Górze - Navbar z kontenerem */}
      <nav className={`navbar px-4 shadow-sm ${trywCiemny ? "navbar-dark bg-secondary" : "navbar-light bg-white"}`}>
        <div className="container-fluid">
          <span className="navbar-brand mb-0 h1 fw-bold">🚀 MójPanel PRO</span>
          <div className="form-check form-switch ms-auto">
            <input 
              className="form-check-input" 
              type="checkbox" 
              id="ciemnyTryb"
              checked={trywCiemny}
              onChange={() => setTrybCiemny(!trywCiemny)}
            />
            <label className="form-check-label" htmlFor="ciemnyTryb">
              {trywCiemny ? "Jasny motyw" : "Ciemny motyw"}
            </label>
          </div>
        </div>
      </nav>

      {/* Kontener główny aplikacji */}
      <div className="container mt-5">
        <div className="row">
          
          {/* Kolumna Profilowa (z boku dla dużych urządzeń, na samej górze dla małych) */}
          <div className="col-12 col-lg-3 mb-4">
            <div className={`card shadow-sm border-0 ${trywCiemny ? "bg-secondary text-white" : ""}`}>
              <div className="card-body text-center p-4">
                <div className="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center mx-auto mb-3" style={{ width: "80px", height: "80px", fontSize: "2rem" }}>
                  JK
                </div>
                <h5 className="card-title fw-bold">Jan Kowalski</h5>
                <p className="card-text text-muted mb-4">Frontend Developer</p>
                <div className="d-grid gap-2">
                  <button className="btn btn-primary btn-sm">Edytuj Profil</button>
                  <button className="btn btn-outline-danger btn-sm">Wyloguj</button>
                </div>
              </div>
            </div>
          </div>

          {/* Kolumna Ze Statystykami (Główny content strony obok zdjęcia) */}
          <div className="col-12 col-lg-9">
            <div className="row">
              <div className="col-12 col-md-6 mb-3">
                 <div className={`card border-success border-2 placeholder-glow shadow-sm ${trywCiemny ? "bg-secondary" : ""}`}>
                    <div className="card-body d-flex justify-content-between align-items-center">
                      <div>
                        <h6 className="mb-0 text-muted">Zarabiane W Coins</h6>
                        <h2 className="text-success mb-0 fw-bold">+ 12 450</h2>
                      </div>
                      <span className="fs-1">💰</span>
                    </div>
                 </div>
              </div>

              <div className="col-12 col-md-6 mb-3">
                 <div className={`card border-warning border-2 shadow-sm ${trywCiemny ? "bg-secondary" : ""}`}>
                    <div className="card-body d-flex justify-content-between align-items-center">
                      <div>
                        <h6 className="mb-0 text-muted">Twoje Zadania</h6>
                        <h2 className="text-warning mb-0 fw-bold">4 Zostały</h2>
                      </div>
                      <span className="fs-1">⚡</span>
                    </div>
                 </div>
              </div>
            </div>
            
            {/* Ostatnie akcje - tabela dla informacji */}
            <div className={`card mt-3 shadow-sm border-0 ${trywCiemny ? "bg-secondary text-white" : ""}`}>
              <div className="card-header bg-transparent border-0 d-flex justify-content-between align-items-center p-4">
                <h5 className="mb-0 fw-bold">Ostatnie aktywności systemu</h5>
                <button className="btn btn-sm btn-outline-primary">Załaduj więcej</button>
              </div>
              <div className="card-body p-0">
                <div className="table-responsive">
                  <table className={`table mb-0 ${trywCiemny ? "table-dark" : "table-hover"}`}>
                     <thead className="table-light">
                        <tr>
                          <th className="px-4">Użytkownik</th>
                          <th>Status</th>
                          <th className="text-end px-4">Czas Aktywności</th>
                        </tr>
                     </thead>
                     <tbody>
                        <tr>
                          <td className="px-4 fw-bold">Marek_1993</td>
                          <td><span className="badge bg-success">Online</span></td>
                          <td className="text-end px-4 text-muted">2 minuty temu</td>
                        </tr>
                        <tr>
                          <td className="px-4 fw-bold">AniaW</td>
                          <td><span className="badge bg-danger">Wylogowana</span></td>
                          <td className="text-end px-4 text-muted">Pół godziny temu</td>
                        </tr>
                     </tbody>
                  </table>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}

export default UserDashboard;
```
To jest niesamowicie rozszerzone kompendium Bootstrapa, które da ci 100% pewności w radzeniu sobie ze wszystkimi stylami i układami w Twoich projektach!

---

## 14. obrazy i zasoby statyczne

### 14.1. obrazy z folderu public

Obrazy umieszczone w folderze `public/` są dostępne bezpośrednio po ścieżce:

```jsx
{/* Obraz: public/zdjecia/kwiat.jpg */}
<img src="/zdjecia/kwiat.jpg" alt="Kwiat" />

{/* Obraz: public/logo.png */}
<img src="/logo.png" alt="Logo" />
```

Zalety: prostota, brak importu.
Wady: brak optymalizacji przez Webpack.

### 14.2. obrazy z folderu src — import

```jsx
// Plik: src/App.js
import kwiatImg from "./zdjecia/kwiat.jpg";

function App() {
  return <img src={kwiatImg} alt="Kwiat" />;
}
```

Zalety: Webpack optymalizuje obraz, ostrzeże, jeśli plik nie istnieje.

### 14.3. obraz zależny od stanu

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [kategoria, setKategoria] = useState("kwiaty");

  // Obraz z folderu public
  const sciezka = `/zdjecia/${kategoria}.jpg`;

  return (
    <div className="container mt-4">
      <img src={sciezka} alt={kategoria} style={{ maxWidth: "300px" }} />
      <div className="mt-2">
        <button className="btn btn-primary me-2" onClick={() => setKategoria("kwiaty")}>Kwiaty</button>
        <button className="btn btn-primary me-2" onClick={() => setKategoria("krajobrazy")}>Krajobrazy</button>
        <button className="btn btn-primary" onClick={() => setKategoria("miasto")}>Miasto</button>
      </div>
    </div>
  );
}

export default App;
```

### 14.4. obrazy w kolekcjach (tablicach obiektów)

```jsx
const zdjecia = [
  { id: 1, plik: "kwiat.jpg", opis: "Kwiat" },
  { id: 2, plik: "gora.jpg", opis: "Góra" },
  { id: 3, plik: "morze.jpg", opis: "Morze" },
];

// Renderowanie — obrazy z folderu public/zdjecia/
{zdjecia.map((z) => (
  <div key={z.id} className="card" style={{ width: "200px" }}>
    <img src={`/zdjecia/${z.plik}`} className="card-img-top" alt={z.opis} />
    <div className="card-body">
      <p className="card-text">{z.opis}</p>
    </div>
  </div>
))}
```

### 14.5. atrybut alt — dostępność

Atrybut `alt` jest wymagany na obrazkach. Opisuje zawartość obrazu dla czytników ekranu i wyświetla się, gdy obraz nie może być załadowany:

```jsx
{/* Poprawnie */}
<img src="/kwiat.jpg" alt="Czerwony kwiat na łące" />

{/* Dla obrazów dekoracyjnych — pusty alt */}
<img src="/dekoracja.png" alt="" />
```

---

## 15. przepływ danych — props w górę i w dół

### 15.1. dane płyną z góry na dół (top-down)

W React dane (props) płyną **zawsze z rodzica do dziecka** — nigdy odwrotnie. Rodzic przekazuje dane jako props, a dziecko je odbiera i wyświetla:

```jsx
// Plik: src/App.js (rodzic)
import KursKarta from "./components/KursKarta";

function App() {
  const kursy = [
    { id: 1, nazwa: "React", cena: 199 },
    { id: 2, nazwa: "JavaScript", cena: 149 },
  ];

  return (
    <div className="container mt-4">
      {kursy.map((kurs) => (
        <KursKarta key={kurs.id} nazwa={kurs.nazwa} cena={kurs.cena} />
      ))}
    </div>
  );
}

export default App;
```

```jsx
// Plik: src/components/KursKarta.js (dziecko)
function KursKarta({ nazwa, cena }) {
  return (
    <div className="card mb-2">
      <div className="card-body">
        <h5>{nazwa}</h5>
        <p>Cena: {cena} zł</p>
      </div>
    </div>
  );
}

export default KursKarta;
```

### 15.2. callback — dziecko zgłasza zdarzenie rodzicowi

Dziecko nie może bezpośrednio zmienić stanu rodzica. Zamiast tego rodzic **przekazuje funkcję** (callback) jako prop, a dziecko ją wywołuje:

```jsx
// Plik: src/App.js (rodzic)
import { useState } from "react";
import DodajKurs from "./components/DodajKurs";

function App() {
  const [kursy, setKursy] = useState(["React", "JavaScript"]);

  // Ta funkcja jest przekazywana jako prop do dziecka
  function handleDodaj(nowyKurs) {
    setKursy((prev) => [...prev, nowyKurs]);
  }

  return (
    <div className="container mt-4">
      <DodajKurs onDodaj={handleDodaj} />
      <ul className="list-group mt-3">
        {kursy.map((kurs, i) => (
          <li key={i} className="list-group-item">{kurs}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

```jsx
// Plik: src/components/DodajKurs.js (dziecko)
import { useState } from "react";

function DodajKurs({ onDodaj }) {
  const [tekst, setTekst] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (tekst.trim() === "") return;
    onDodaj(tekst);     // Wywołanie callbacka z rodzica
    setTekst("");        // Czyszczenie pola
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="input-group">
        <input
          type="text"
          className="form-control"
          value={tekst}
          onChange={(e) => setTekst(e.target.value)}
          placeholder="Nazwa kursu"
        />
        <button type="submit" className="btn btn-success">Dodaj</button>
      </div>
    </form>
  );
}

export default DodajKurs;
```

### 15.3. lifting state up — podnoszenie stanu

Gdy dwa komponenty muszą dzielić ten sam stan, stan przenosi się do ich **wspólnego rodzica**. Rodzic trzyma stan i przekazuje go do obu dzieci:

```jsx
// Plik: src/App.js — rodzic trzyma stan
import { useState } from "react";
import Formularz from "./components/Formularz";
import Podglad from "./components/Podglad";

function App() {
  // Stan jest w rodzicu — oba dzieci mają do niego dostęp
  const [imie, setImie] = useState("");

  return (
    <div className="container mt-4">
      <Formularz imie={imie} onZmiana={setImie} />
      <Podglad imie={imie} />
    </div>
  );
}

export default App;
```

```jsx
// Plik: src/components/Formularz.js — dziecko edytujące
function Formularz({ imie, onZmiana }) {
  return (
    <input
      type="text"
      className="form-control mb-3"
      value={imie}
      onChange={(e) => onZmiana(e.target.value)}
      placeholder="Wpisz imię"
    />
  );
}

export default Formularz;
```

```jsx
// Plik: src/components/Podglad.js — dziecko wyświetlające
function Podglad({ imie }) {
  return <p>Podgląd: <strong>{imie || "(puste)"}</strong></p>;
}

export default Podglad;
```

### 15.4. pełny przykład wieloplikowy z przepływem danych

Diagram przepływu danych:

```
App (stan: zadania)
├── ZadanieFormularz (callback: onDodaj)
└── ZadanieLista (props: zadania, callback: onUsun)
    └── ZadanieElement (props: zadanie, callback: onUsun)
```

- **Dół (Props):** App → ZadanieLista → ZadanieElement (dane płyną w dół).
- **Góra (Callbacks):** ZadanieFormularz → App (dziecko zgłasza zdarzenie do rodzica).
- **Odświeżenie:** Gdy rodzic zmieni stan, React automatycznie re-renderuje wszystkie dzieci z nowymi danymi.

---

## 16. useEffect i efekty uboczne

### 16.1. po co jest useEffect

`useEffect` to hook do wykonywania **efektów ubocznych** — operacji, które nie dotyczą bezpośrednio wyniku renderowania. Przykłady:
- Pobranie danych z API lub localStorage
- Ustawienie tytułu strony
- Ustawienie timera

```jsx
import { useEffect } from "react";
```

### 16.2. useEffect przy starcie aplikacji

```jsx
// Plik: src/App.js
import { useState, useEffect } from "react";

function App() {
  const [dane, setDane] = useState([]);

  // useEffect z pustą tablicą zależności [] — wykona się RAZ po pierwszym renderze
  useEffect(() => {
    console.log("Komponent się zamontował!");
    document.title = "Moja Aplikacja";
  }, []);

  return (
    <div className="container mt-4">
      <h1>Aplikacja</h1>
    </div>
  );
}

export default App;
```

### 16.3. tablica zależności

Tablica zależności `[]` kontroluje, **kiedy** efekt się uruchomi:

```jsx
// Wykonuje się po KAŻDYM renderze (brak tablicy zależności)
useEffect(() => {
  console.log("Render!");
});

// Wykonuje się TYLKO RAZ — po pierwszym renderze (pusta tablica)
useEffect(() => {
  console.log("Montowanie!");
}, []);

// Wykonuje się gdy zmieni się wartość 'szukaj'
useEffect(() => {
  console.log("Wyszukiwanie:", szukaj);
}, [szukaj]);
```

| Tablica zależności | Kiedy się uruchomi |
|---|---|
| Brak | Po każdym renderze |
| `[]` | Tylko raz — po pierwszym renderze |
| `[a, b]` | Gdy zmieni się `a` lub `b` |

### 16.4. cleanup — sprzątanie efektu

Efekt może zwrócić funkcję czyszczącą (cleanup), która wykona się przed następnym uruchomieniem efektu lub gdy komponent się odmontowuje:

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    console.log("Tykanie...");
  }, 1000);

  // Cleanup — sprzątanie przy odmontowywaniu
  return () => {
    clearInterval(timer);
  };
}, []);
```

### 16.5. localStorage — zapis i odczyt danych

`localStorage` pozwala zapisywać dane w przeglądarce, które przetrwają odświeżenie strony:

```jsx
// Plik: src/App.js
import { useState, useEffect } from "react";

function App() {
  // Odczyt z localStorage przy starcie
  const [zadania, setZadania] = useState(() => {
    const zapisane = localStorage.getItem("zadania");
    return zapisane ? JSON.parse(zapisane) : [];
  });

  // Zapis do localStorage przy każdej zmianie zadań
  useEffect(() => {
    localStorage.setItem("zadania", JSON.stringify(zadania));
  }, [zadania]);

  // ... reszta komponentu
  return (
    <div className="container mt-4">
      <p>Liczba zadań: {zadania.length}</p>
    </div>
  );
}

export default App;
```

**Kluczowe funkcje localStorage:**

| Metoda | Opis |
|---|---|
| `localStorage.setItem("klucz", "wartość")` | Zapisuje dane (string) |
| `localStorage.getItem("klucz")` | Odczytuje dane (string lub null) |
| `localStorage.removeItem("klucz")` | Usuwa dane |
| `JSON.stringify(obiekt)` | Zamienia obiekt/tablicę na string JSON |
| `JSON.parse(tekst)` | Zamienia string JSON na obiekt/tablicę |

### 16.6. typowe pułapki useEffect

```jsx
// PUŁAPKA 1: Brak tablicy zależności — nieskończona pętla!
useEffect(() => {
  setLicznik(licznik + 1); // Zmiana stanu → re-render → efekt → zmiana stanu → ...
}); // ← brak [] to powtarzanie w nieskończoność

// PUŁAPKA 2: Zapomnienie o zależności
useEffect(() => {
  console.log("Szukaj:", szukaj); // Używasz szukaj, ale nie masz go w []
}, []); // ← efekt uruchomi się tylko raz, nie reagując na zmiany szukaj

// POPRAWNIE:
useEffect(() => {
  console.log("Szukaj:", szukaj);
}, [szukaj]); // ← efekt uruchomi się gdy zmieni się szukaj
```

---

## 17. useRef — referencje do elementów DOM

### 17.1. czym jest useRef

`useRef` to hook, który tworzy „pojemnik" na wartość, która **nie powoduje re-renderu** przy zmianie. Najczęściej używany do uzyskania referencji do elementu DOM:

```jsx
import { useRef } from "react";
```

### 17.2. ustawianie fokusa na polu

```jsx
// Plik: src/App.js
import { useState, useRef } from "react";

function App() {
  const [imie, setImie] = useState("");
  const inputRef = useRef(null); // Tworzymy referencję

  function handleReset() {
    setImie("");
    inputRef.current.focus(); // Ustawiamy fokus na polu
  }

  return (
    <div className="container mt-4">
      <input
        ref={inputRef} // Przypisujemy referencję do elementu
        type="text"
        className="form-control mb-2"
        value={imie}
        onChange={(e) => setImie(e.target.value)}
        placeholder="Wpisz imię"
      />
      <button className="btn btn-secondary" onClick={handleReset}>
        Wyczyść i ustaw fokus
      </button>
    </div>
  );
}

export default App;
```

### 17.3. useRef vs useState

| Cecha | `useState` | `useRef` |
|---|---|---|
| Zmiana wartości powoduje re-render | Tak | Nie |
| Typowe użycie | Dane wyświetlane w widoku | Referencje do DOM, timery |
| Dostęp do wartości | `zmienna` | `ref.current` |

---

## 18. dane lokalne, JSON i fetch

### 18.1. tablice danych w kodzie

Najprostszy sposób — dane wpisane bezpośrednio w pliku:

```jsx
// Plik: src/data/kursy.js
const kursy = [
  { id: 1, nazwa: "HTML i CSS", cena: 99 },
  { id: 2, nazwa: "JavaScript", cena: 149 },
  { id: 3, nazwa: "React", cena: 199 },
];

export default kursy;
```

```jsx
// Plik: src/App.js
import kursy from "./data/kursy";

function App() {
  return (
    <ul>
      {kursy.map((k) => (
        <li key={k.id}>{k.nazwa} — {k.cena} zł</li>
      ))}
    </ul>
  );
}
```

### 18.2. import pliku JSON

Można bezpośrednio importować plik JSON:

```json
// Plik: src/data/filmy.json
[
  { "id": 1, "tytul": "Matrix", "rok": 1999 },
  { "id": 2, "tytul": "Incepcja", "rok": 2010 },
  { "id": 3, "tytul": "Titanic", "rok": 1997 }
]
```

```jsx
// Plik: src/App.js
import filmy from "./data/filmy.json";

function App() {
  return (
    <ul>
      {filmy.map((f) => (
        <li key={f.id}>{f.tytul} ({f.rok})</li>
      ))}
    </ul>
  );
}
```

### 18.3. fetch z folderu public

Pliki JSON umieszczone w `public/` można pobrać za pomocą `fetch`:

```jsx
// Plik: src/App.js
import { useState, useEffect } from "react";

function App() {
  const [dane, setDane] = useState([]);
  const [ladowanie, setLadowanie] = useState(true);

  useEffect(() => {
    fetch("/dane.json") // Plik w public/dane.json
      .then((response) => response.json())
      .then((data) => {
        setDane(data);
        setLadowanie(false);
      })
      .catch((error) => {
        console.error("Błąd pobierania:", error);
        setLadowanie(false);
      });
  }, []);

  if (ladowanie) {
    return <p>Ładowanie...</p>;
  }

  return (
    <ul>
      {dane.map((el) => (
        <li key={el.id}>{el.nazwa}</li>
      ))}
    </ul>
  );
}

export default App;
```

### 18.4. parsowanie danych tekstowych

Gdy dane z pliku `dane.txt` trzeba przetworzyć:

```jsx
// Dane w formacie: "nazwa;kategoria;liczba"
const daneRaw = `kwiat.jpg;kwiaty;12
gora.jpg;krajobrazy;34
roza.jpg;kwiaty;7`;

const zdjecia = daneRaw.split("\n").map((linia, index) => {
  const [nazwa, kategoria, pobrania] = linia.split(";");
  return {
    id: index + 1,
    nazwa: nazwa,
    kategoria: kategoria,
    pobrania: Number(pobrania),
  };
});

console.log(zdjecia);
// [
//   { id: 1, nazwa: "kwiat.jpg", kategoria: "kwiaty", pobrania: 12 },
//   { id: 2, nazwa: "gora.jpg", kategoria: "krajobrazy", pobrania: 34 },
//   { id: 3, nazwa: "roza.jpg", kategoria: "kwiaty", pobrania: 7 },
// ]
```

---

## 19. logika aplikacji poza jsx

### 19.1. funkcje pomocnicze

Funkcje, które nie potrzebują stanu, można definiować **poza komponentem** lub w osobnych plikach:

```jsx
// Plik: src/App.js

// Funkcja pomocnicza — poza komponentem
function formatujCene(cena) {
  return `${cena.toFixed(2)} zł`;
}

function czyPoprawnyEmail(email) {
  return email.includes("@") && email.includes(".");
}

function App() {
  return (
    <div>
      <p>Cena: {formatujCene(29.9)}</p>
      <p>Email: {czyPoprawnyEmail("jan@mail.pl") ? "OK" : "Błąd"}</p>
    </div>
  );
}

export default App;
```

### 19.2. osobne moduły z logiką

```js
// Plik: src/utils/walidacja.js
export function czyPuste(wartosc) {
  return wartosc.trim() === "";
}

export function czyWZakresie(liczba, min, max) {
  return liczba >= min && liczba <= max;
}

export function czyPoprawnyEmail(email) {
  return email.includes("@") && email.includes(".");
}
```

```jsx
// Plik: src/App.js
import { czyPuste, czyPoprawnyEmail } from "./utils/walidacja";

function App() {
  // ... użycie funkcji walidacyjnych
}
```

### 19.3. oddzielenie UI od obliczeń

Dobra praktyka: logika obliczeniowa **poza komponentem**, widok **w komponencie**:

```jsx
// Plik: src/utils/koszyk.js
export function obliczSume(produkty) {
  return produkty.reduce((suma, p) => suma + p.cena * p.ilosc, 0);
}

export function obliczRabat(suma, procentRabatu) {
  return suma * (procentRabatu / 100);
}
```

```jsx
// Plik: src/App.js
import { obliczSume, obliczRabat } from "./utils/koszyk";

function App() {
  const produkty = [
    { id: 1, nazwa: "Kurs React", cena: 199, ilosc: 1 },
    { id: 2, nazwa: "Kurs JS", cena: 149, ilosc: 2 },
  ];

  const suma = obliczSume(produkty);
  const rabat = obliczRabat(suma, 10);

  return (
    <div className="container mt-4">
      <p>Suma: {suma.toFixed(2)} zł</p>
      <p>Rabat 10%: -{rabat.toFixed(2)} zł</p>
      <p><strong>Do zapłaty: {(suma - rabat).toFixed(2)} zł</strong></p>
    </div>
  );
}
```

---

## 20. organizacja projektu

### 20.1. nazewnictwo plików i komponentów

| Konwencja | Przykład | Dotyczy |
|---|---|---|
| PascalCase | `KursKarta.js`, `ZadanieFormularz.js` | Pliki komponentów |
| camelCase | `walidacja.js`, `formatowanie.js` | Pliki z logiką/narzędziami |
| camelCase | `handleSubmit`, `setImie` | Funkcje i zmienne |

**Zasada:** Nazwa pliku komponentu = nazwa komponentu:
- Plik: `KursKarta.js` → Komponent: `function KursKarta() { ... }`

### 20.2. folder components

```
src/
└── components/
    ├── Header.js
    ├── Footer.js
    ├── KursKarta.js
    ├── KursLista.js
    └── ZadanieFormularz.js
```

### 20.3. folder data

```
src/
└── data/
    ├── kursy.js       # Tablica obiektów
    └── filmy.json     # Dane JSON
```

### 20.4. folder utils

```
src/
└── utils/
    ├── walidacja.js   # Funkcje walidacyjne
    ├── formatowanie.js # Formatowanie tekstu, cen
    └── algorytmy.js   # Funkcje algorytmiczne
```

### 20.5. przykładowa struktura projektu

```
src/
├── components/
│   ├── Header.js
│   ├── Footer.js
│   ├── KursFormularz.js
│   └── KursLista.js
├── data/
│   └── kursy.js
├── utils/
│   └── walidacja.js
├── App.js
├── App.css
├── index.js
└── index.css
```

---

## 21. debugowanie

### 21.1. konsola przeglądarki

```jsx
function handleSubmit(e) {
  e.preventDefault();
  console.log("Wartości formularza:", { imie, email, wiek });
  console.log("Typ imie:", typeof imie);
  console.log("Długość listy:", lista.length);
}
```

### 21.2. React DevTools

React DevTools to rozszerzenie przeglądarki (Chrome / Firefox), które pozwala:
- Przeglądać drzewo komponentów
- Podglądać props i stan (state) każdego komponentu
- Śledzić re-rendery

Instalacja: wyszukaj „React Developer Tools" w sklepie rozszerzeń przeglądarki.

### 21.3. typowe błędy składni

| Błąd | Przyczyna | Rozwiązanie |
|---|---|---|
| `Adjacent JSX elements must be wrapped` | Dwa elementy bez wspólnego rodzica | Owinąć w `<div>` lub `<>` |
| `'class' is not a valid attribute` | Użycie `class` zamiast `className` | Zamień na `className` |
| `'for' is not a valid attribute` | Użycie `for` zamiast `htmlFor` | Zamień na `htmlFor` |
| `Expected a ')' to match '('` | Brakujący nawias | Sprawdź nawiasy w JSX |

### 21.4. typowe błędy stanu

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Widok nie aktualizuje się | Użycie `let` zamiast `useState` | Zamień na `useState` |
| Widok nie aktualizuje się | Mutowanie stanu (push, bezpośrednia zmiana) | Tworzenie kopii (spread) |
| Stara wartość w console.log | Stan jest asynchroniczny | Loguj przed `setState` lub użyj `useEffect` |

### 21.5. typowe błędy formularzy

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Strona się przeładowuje | Brak `e.preventDefault()` | Dodaj na początku `handleSubmit` |
| Pole nie reaguje na pisanie | Brak `onChange` | Dodaj `onChange` z `setState` |
| Pole wyświetla `undefined` | Brak wartości początkowej stanu | `useState("")` zamiast `useState()` |
| `NaN` w polu liczbowym | Brak konwersji `Number()` | `setWiek(Number(e.target.value))` |

---

## 22. najczęstsze pułapki i jak ich unikać

### 22.1. brak key w pętli map()

```jsx
// BŁĄD (ostrzeżenie w konsoli)
{items.map((item) => <li>{item.text}</li>)}

// POPRAWNIE
{items.map((item) => <li key={item.id}>{item.text}</li>)}
```

### 22.2. mutowanie stanu zamiast tworzenia kopii

```jsx
// błąd — React nie widzi zmiany referencji
tasks.push(newTask);
setTasks(tasks);

// POPRAWNIE — nowa tablica
setTasks([...tasks, newTask]);

// błąd — mutacja obiektu
osoba.wiek = 26;
setOsoba(osoba);

// POPRAWNIE — nowy obiekt
setOsoba({ ...osoba, wiek: 26 });
```

### 22.3. odczyt stanu zaraz po ustawieniu

```jsx
// błąd — stara wartość
setCount(count + 1);
console.log(count); // Nadal stara!

// ROZWIĄZANIE — oblicz przed
const nowy = count + 1;
setCount(nowy);
console.log(nowy); // Nowa wartość
```

### 22.4. brak event.preventDefault() w formularzu

```jsx
// błąd — strona się przeładowuje
function handleSubmit(e) {
  console.log("Dane:", imie);
}

// POPRAWNIE
function handleSubmit(e) {
  e.preventDefault(); // Najważniejsza linia!
  console.log("Dane:", imie);
}
```

### 22.5. zapomnienie o import useState

```jsx
// błąd — useState is not defined
function App() {
  const [x, setX] = useState(0);
}

// POPRAWNIE
import { useState } from "react";
function App() {
  const [x, setX] = useState(0);
}
```

### 22.6. wywołanie funkcji zamiast przekazania referencji

```jsx
// błąd — funkcja WYKONA SIĘ natychmiast przy renderze
<button onClick={handleKliknij()}>Kliknij</button>

// POPRAWNIE — przekazanie referencji (bez nawiasów)
<button onClick={handleKliknij}>Kliknij</button>

// POPRAWNIE — z argumentem (strzałka)
<button onClick={() => handleUsun(id)}>Usuń</button>
```

---

## 23. build i publikacja projektu

### 23.1. npm run build

```bash
npm run build
```

To polecenie tworzy zoptymalizowaną wersję produkcyjną w folderze `build/`. Pliki są minifikowane (skompresowane), co zapewnia szybsze ładowanie.

### 23.2. co zawiera folder build

```
build/
├── index.html          # Główny plik HTML
├── static/
│   ├── css/            # Skompresowane pliki CSS
│   │   └── main.abc123.css
│   ├── js/             # Skompresowane pliki JavaScript
│   │   └── main.xyz789.js
│   └── media/          # Obrazy importowane z src/
└── favicon.ico
```

### 23.3. typowe problemy przy buildzie

| Problem | Przyczyna | Rozwiązanie |
|---|---|---|
| Ostrzeżenia o nieużywanych zmiennych | Zadeklarowane, ale nieużywane zmienne | Usuń nieużywane zmienne i importy |
| Białe plamy zamiast obrazów | Zła ścieżka do obrazu | Użyj `import` dla obrazów z `src/` lub `/` dla `public/` |
| Błąd kompilacji | Błąd składni w kodzie | Napraw błąd wskazany w terminalu |

---

## 24. dobre praktyki UI i dostępność

### 24.1. typ przycisku — button vs submit

```jsx
{/* Przycisk wysyłający formularz */}
<button type="submit">Wyślij</button>

{/* Przycisk NIE wysyłający formularza — np. reset, anuluj */}
<button type="button" onClick={handleAnuluj}>Anuluj</button>
```

Jeśli nie podasz `type`, przycisk wewnątrz `<form>` domyślnie jest `type="submit"` i może spowodować niechciane wysłanie formularza.

### 24.2. label i htmlFor

Każde pole formularza powinno mieć etykietę `<label>` powiązaną z polem przez `htmlFor`:

```jsx
<label htmlFor="email" className="form-label">Email:</label>
<input id="email" type="text" className="form-control" />
```

Kliknięcie etykiety automatycznie przenosi fokus na powiązane pole — to ułatwia obsługę, szczególnie na urządzeniach mobilnych.

### 24.3. semantyczny układ strony

```jsx
function App() {
  return (
    <div>
      <header>
        <h1>Moja Aplikacja</h1>
      </header>
      <main className="container mt-4">
        {/* Główna treść */}
      </main>
      <footer className="text-center mt-4">
        <p>&copy; 2025</p>
      </footer>
    </div>
  );
}
```

---

## 25. routing i nawigacja w SPA (react-router-dom)

### 25.1. czym jest Client-Side Routing?

Tak jak wspomnieliśmy w rozdziale wprowadzającym do SPA, aplikacje Reactowe z reguły ładują tylko jeden plik `index.html`. Aby zasymulować przechodzenie między podstronami (np. z `/` na `/profil` czy `/logowanie`) bez odświeżania całej przeglądarki, używamy tzw. "Client-Side Routingu". W ekosystemie React najpopularniejszym do tego narzędziem jest biblioteka **React Router**.

Zanim zaczniesz, musisz ją zainstalować:

```bash
npm install react-router-dom
```

### 25.2. BrowserRouter, Routes i Route

Aby routing zadziałał, musimy obudować naszą aplikację (zwykle w pliku `src/index.js` lub `src/App.js`) odpowiednimi komponentami dostarczanymi przez bibliotekę `react-router-dom`.

*   `BrowserRouter` - Główny "wrapper" (owijka), który włącza nasłuchiwanie na zmiany adresu URL w przeglądarce.
*   `Routes` - Kontener na nasze ścieżki. Sprawdza obecny URL i wybiera *tylko jeden*, najlepiej pasujący `Route`.
*   `Route` - Definiuje konkretną ścieżkę. Przyjmuje atrybut `path` (ścieżka w URL) oraz `element` (komponent JSX, który ma zostać wyświetlony).

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom"; 

import EkranDomowy from "./pages/EkranDomowy";
import LogowanieForm from "./pages/LogowanieForm";
import Blad404 from "./pages/Blad404";

function App() {
  return (
    <BrowserRouter>
        {/* Elementy umieszczone poza <Routes> (np. nawigacja, stopka) będą widoczne na KAZDEJ podstronie */}
        <nav>Menu Główne dla Sklepu - Stały widżet Nav</nav> 
        
        <Routes>
            {/* Strona główna */}
            <Route path="/" element={<EkranDomowy />} />
            
            {/* Podstrona logowania */}
            <Route path="/login" element={<LogowanieForm />} />
            
            {/* Specjalna ścieżka "*" wyłapuje wszystkie nieznane adresy (Błąd 404) */}
            <Route path="*" element={<Blad404 />} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### 25.3. linkowanie pomiędzy podstronami używając `<Link>`

Gdybyśmy do nawigacji użyli standardowego znacznika HTML `<a href="/login">`, przeglądarka pobrałaby stronę na nowo z serwera, co spowodowałoby reset całego stanu Reacta. Aby temu zapobiec, używamy komponentu `<Link>`.

```jsx
import { Link } from "react-router-dom"; 

function TopNavigation() {
    return (
        <nav>
            {/* Zamiast <a href="/"> używamy <Link to="/"> */}
            <Link to="/">Strona Główna</Link>
            <Link to="/login">Zaloguj się</Link>
        </nav>
    );
}
```

Dzięki `<Link>`, React zmienia zawartość ekranu "w locie", co jest błyskawiczne i zachowuje stan aplikacji.

### 25.4. nawigacja z poziomu kodu (useNavigate)

Często musimy przenieść użytkownika na inną stronę w wyniku jakiejś akcji (np. po udanym zalogowaniu lub po wysłaniu formularza). Nie używamy do tego kliknięcia w `<Link>`, lecz hooka `useNavigate`.

```jsx
import { useNavigate } from "react-router-dom";
import { useState } from "react";

function LogowanieForm() {
    const [login, setLogin] = useState("");
    const navigate = useNavigate(); // Inicjalizacja hooka
    
    function handleSubmit(e) {
        e.preventDefault();
        
        // Tutaj np. wysyłamy zapytanie do serwera. Jeśli sukces:
        if (login === "admin") {
           // Przenieś programatycznie na stronę panelu
           navigate("/panel"); 
        } else {
           alert("Błędny login!");
        }
    }

    return (
       <form onSubmit={handleSubmit}>
          <input value={login} onChange={e => setLogin(e.target.value)} />
          <button type="submit">Zaloguj</button>
       </form>
    );
}
```

### 25.5. parametry w ścieżkach (useParams)

Często ścieżki są dynamiczne, np. profil konkretnego użytkownika `/user/123` lub strona produktu `/produkt/5`. W React Router definiujemy to przy pomocy dwukropka `:id`. Następnie w komponencie możemy ten parametr odczytać używając hooka `useParams`.

**Definicja w App.js:**
```jsx
<Route path="/produkt/:id" element={<ProduktSzczegoly />} />
```

**Odczyt w komponencie:**
```jsx
import { useParams } from "react-router-dom";

function ProduktSzczegoly() {
  // useParams zwraca obiekt z parametrami z paska adresu
  const { id } = useParams();

  return (
    <div>
      <h1>Szczegóły produktu numer: {id}</h1>
      {/* Tutaj możemy użyć id np. do pobrania danych o tym konkretnym produkcie z API */}
    </div>
  );
}
```


## 26. wzorce praktyczne

### 26.1. formularz rejestracji

Prosty formularz z walidacją — jeden z najczęstszych wzorców w aplikacjach webowych.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Stan dla każdego pola formularza
  const [imie, setImie] = useState("");
  const [email, setEmail] = useState("");
  const [haslo, setHaslo] = useState("");
  const [regulamin, setRegulamin] = useState(false);

  // Stan dla błędów walidacji
  const [bledy, setBledy] = useState({});

  // Stan dla komunikatu sukcesu
  const [sukces, setSukces] = useState("");

  // Funkcja walidacyjna — sprawdza dane i zwraca obiekt z błędami
  function waliduj() {
    const noweBledy = {};

    // Walidacja imienia
    if (imie.trim() === "") {
      noweBledy.imie = "Imię jest wymagane";
    } else if (imie.trim().length < 2) {
      noweBledy.imie = "Imię musi mieć co najmniej 2 znaki";
    }

    // Walidacja emaila
    if (email.trim() === "") {
      noweBledy.email = "Email jest wymagany";
    } else if (!email.includes("@") || !email.includes(".")) {
      noweBledy.email = "Email musi zawierać @ i .";
    }

    // Walidacja hasła
    if (haslo === "") {
      noweBledy.haslo = "Hasło jest wymagane";
    } else if (haslo.length < 6) {
      noweBledy.haslo = "Hasło musi mieć co najmniej 6 znaków";
    }

    // Walidacja regulaminu
    if (!regulamin) {
      noweBledy.regulamin = "Musisz zaakceptować regulamin";
    }

    return noweBledy;
  }

  // Obsługa wysłania formularza
  function handleSubmit(e) {
    e.preventDefault(); // Zapobiegamy przeładowaniu strony

    const noweBledy = waliduj();

    // Jeśli są błędy — wyświetlamy je i przerywamy
    if (Object.keys(noweBledy).length > 0) {
      setBledy(noweBledy);
      setSukces("");
      return;
    }

    // Brak błędów — wyświetlamy sukces
    setBledy({});
    setSukces(`Zarejestrowano: ${imie} (${email})`);
    console.log("Dane rejestracji:", { imie, email, haslo });

    // Reset formularza
    setImie("");
    setEmail("");
    setHaslo("");
    setRegulamin(false);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "500px" }}>
      <h1 className="mb-4">Rejestracja</h1>

      {/* Komunikat sukcesu */}
      {sukces && <div className="alert alert-success">{sukces}</div>}

      <form onSubmit={handleSubmit}>
        {/* Pole: Imię */}
        <div className="mb-3">
          <label htmlFor="imie" className="form-label">Imię:</label>
          <input
            id="imie"
            type="text"
            className={`form-control ${bledy.imie ? "is-invalid" : ""}`}
            value={imie}
            onChange={(e) => setImie(e.target.value)}
            placeholder="Wpisz imię"
          />
          {bledy.imie && <div className="invalid-feedback">{bledy.imie}</div>}
        </div>

        {/* Pole: Email */}
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email:</label>
          <input
            id="email"
            type="text"
            className={`form-control ${bledy.email ? "is-invalid" : ""}`}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="jan@example.com"
          />
          {bledy.email && <div className="invalid-feedback">{bledy.email}</div>}
        </div>

        {/* Pole: Hasło */}
        <div className="mb-3">
          <label htmlFor="haslo" className="form-label">Hasło:</label>
          <input
            id="haslo"
            type="password"
            className={`form-control ${bledy.haslo ? "is-invalid" : ""}`}
            value={haslo}
            onChange={(e) => setHaslo(e.target.value)}
            placeholder="Minimum 6 znaków"
          />
          {bledy.haslo && <div className="invalid-feedback">{bledy.haslo}</div>}
        </div>

        {/* Checkbox: Regulamin */}
        <div className="form-check mb-3">
          <input
            id="regulamin"
            type="checkbox"
            className={`form-check-input ${bledy.regulamin ? "is-invalid" : ""}`}
            checked={regulamin}
            onChange={(e) => setRegulamin(e.target.checked)}
          />
          <label htmlFor="regulamin" className="form-check-label">
            Akceptuję regulamin
          </label>
          {bledy.regulamin && <div className="invalid-feedback">{bledy.regulamin}</div>}
        </div>

        <button type="submit" className="btn btn-primary w-100">
          Zarejestruj się
        </button>
      </form>
    </main>
  );
}

export default App;
```

---

### 26.2. zapisy na kurs

Przykład połączenia prostego formularza z widokiem powiązanym z tablicą danych.

**Wymagania:**
- Tablica nazw kursów
- Wyświetlenie liczby kursów
- Lista numerowana kursów
- Formularz z imieniem, nazwiskiem i numerem kursu
- Wyświetlenie w konsoli imienia, nazwiska i nazwy kursu lub komunikatu „Nieprawidłowy numer kursu"

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Tablica kursów — dane stałe
  const kursy = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "Sieci komputerowe",
    "Bazy danych SQL",
  ];

  // Stan formularza
  const [imie, setImie] = useState("");
  const [nazwisko, setNazwisko] = useState("");
  const [numerKursu, setNumerKursu] = useState("");

  // Obsługa przycisku "Zapisz do kursu"
  function handleZapisz() {
    const numer = Number(numerKursu);

    // Walidacja — czy numer mieści się w zakresie tablicy
    if (numer >= 1 && numer <= kursy.length) {
      // Numer jest poprawny — wyświetlamy dane w konsoli
      console.log(`${imie} ${nazwisko}`);
      console.log(`Kurs: ${kursy[numer - 1]}`);
    } else {
      // Numer jest niepoprawny
      console.log(`${imie} ${nazwisko}`);
      console.log("Nieprawidłowy numer kursu");
    }
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "600px" }}>
      <h1>Zapisy na kursy</h1>

      {/* Wyświetlenie liczby kursów */}
      <p>Dostępnych kursów: <strong>{kursy.length}</strong></p>

      {/* Lista numerowana kursów — renderowana dynamicznie */}
      <ol>
        {kursy.map((kurs, index) => (
          <li key={index}>{kurs}</li>
        ))}
      </ol>

      <hr />

      {/* Formularz zapisu */}
      <div className="mb-3">
        <label htmlFor="imie" className="form-label">Imię:</label>
        <input
          id="imie"
          type="text"
          className="form-control"
          value={imie}
          onChange={(e) => setImie(e.target.value)}
        />
      </div>

      <div className="mb-3">
        <label htmlFor="nazwisko" className="form-label">Nazwisko:</label>
        <input
          id="nazwisko"
          type="text"
          className="form-control"
          value={nazwisko}
          onChange={(e) => setNazwisko(e.target.value)}
        />
      </div>

      <div className="mb-3">
        <label htmlFor="numer" className="form-label">Numer kursu:</label>
        <input
          id="numer"
          type="number"
          className="form-control"
          value={numerKursu}
          onChange={(e) => setNumerKursu(e.target.value)}
        />
      </div>

      <button className="btn btn-primary" onClick={handleZapisz}>
        Zapisz do kursu
      </button>
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki:**
- Tablica danych stałych (`const kursy = [...]`)
- Renderowanie listy numerowanej przez `map()`
- Odczyt wartości pól formularza ze stanu
- Mapowanie numeru na element tablicy (`kursy[numer - 1]`)
- Prosty warunek walidacyjny
- Wynik trafia do `console.log()`, nie na stronę

---

### 26.3. formularz filmu

Kolejny przykład wprowadzania kontrolowanych struktur danych – tym razem na liście rozwijanej.

**Wymagania:**
- Formularz z polem „Tytuł filmu"
- Lista rozwijana (select) z rodzajem filmu
- Przycisk „Dodaj"
- Startowo puste pola
- Wypisanie danych formularza do konsoli po kliknięciu

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Stan formularza — startowo puste
  const [tytul, setTytul] = useState("");
  const [rodzaj, setRodzaj] = useState("");

  // Lista rodzajów filmów do selecta
  const rodzaje = ["Sensacyjny", "Komedia", "Horror", "Dramat", "Sci-Fi"];

  // Obsługa kliknięcia "Dodaj"
  function handleDodaj(e) {
    e.preventDefault(); // Zapobiegamy przeładowaniu

    // Wypisanie danych do konsoli
    console.log(`Tytuł: ${tytul}`);
    console.log(`Rodzaj: ${rodzaj}`);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "500px" }}>
      <h1>Dodaj film</h1>

      <form onSubmit={handleDodaj}>
        {/* Pole: Tytuł filmu */}
        <div className="mb-3">
          <label htmlFor="tytul" className="form-label">Tytuł filmu:</label>
          <input
            id="tytul"
            type="text"
            className="form-control"
            value={tytul}
            onChange={(e) => setTytul(e.target.value)}
            placeholder="Wpisz tytuł filmu"
          />
        </div>

        {/* Pole: Rodzaj filmu (select) */}
        <div className="mb-3">
          <label htmlFor="rodzaj" className="form-label">Rodzaj:</label>
          <select
            id="rodzaj"
            className="form-select"
            value={rodzaj}
            onChange={(e) => setRodzaj(e.target.value)}
          >
            <option value="">-- Wybierz rodzaj --</option>
            {rodzaje.map((r) => (
              <option key={r} value={r}>{r}</option>
            ))}
          </select>
        </div>

        <button type="submit" className="btn btn-primary">
          Dodaj
        </button>
      </form>
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki:**
- Kontrolowane pole tekstowe (`input text`)
- Kontrolowany `select` z dynamicznie generowanymi opcjami
- Obsługa `onSubmit` z `preventDefault()`
- Składanie danych do jednego wyniku w konsoli

---

### 26.4. galeria zdjęć z kategoriami

Interaktywna galeria kafelkowa opierająca się o filtry stanów (checkboxy / switche).

**Wymagania:**
- Tablica obiektów zdjęć z `dane.txt`
- Trzy pola switch/checkbox do filtrowania kategorii
- Filtrowanie zdjęć po zaznaczonych kategoriach
- Wyświetlanie bloków zdjęć obok siebie
- Pokazanie liczby pobrań
- Przycisk „Pobierz" zwiększający liczbę pobrań dla klikniętego zdjęcia

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Dane zdjęć — przepisane z dane.txt
  const [zdjecia, setZdjecia] = useState([
    { id: 1, nazwa: "kwiat.jpg", kategoria: "kwiaty", pobrania: 12 },
    { id: 2, nazwa: "gora.jpg", kategoria: "krajobrazy", pobrania: 34 },
    { id: 3, nazwa: "roza.jpg", kategoria: "kwiaty", pobrania: 7 },
    { id: 4, nazwa: "miasto.jpg", kategoria: "miasto", pobrania: 21 },
    { id: 5, nazwa: "jezioro.jpg", kategoria: "krajobrazy", pobrania: 15 },
    { id: 6, nazwa: "tulipan.jpg", kategoria: "kwiaty", pobrania: 3 },
    { id: 7, nazwa: "ulica.jpg", kategoria: "miasto", pobrania: 9 },
  ]);

  // Stan checkboxów/switchów — które kategorie są zaznaczone
  const [filtry, setFiltry] = useState({
    kwiaty: true,
    krajobrazy: true,
    miasto: true,
  });

  // Obsługa zmiany switcha — aktualizacja jednego pola w obiekcie filtrów
  function handleFiltr(kategoria) {
    setFiltry((prev) => ({
      ...prev,
      [kategoria]: !prev[kategoria],
    }));
  }

  // Obsługa kliknięcia "Pobierz" — zwiększenie pobrań dla jednego zdjęcia
  function handlePobierz(id) {
    setZdjecia((prev) =>
      prev.map((z) =>
        z.id === id ? { ...z, pobrania: z.pobrania + 1 } : z
      )
    );
  }

  // Filtrowanie zdjęć — pokazujemy tylko te z zaznaczonych kategorii
  const przefiltrowane = zdjecia.filter((z) => filtry[z.kategoria]);

  return (
    <main className="container mt-4">
      <h1>Galeria zdjęć</h1>

      {/* Switche do filtrowania kategorii */}
      <div className="mb-4">
        {Object.keys(filtry).map((kategoria) => (
          <div key={kategoria} className="form-check form-switch form-check-inline">
            <input
              id={`filtr-${kategoria}`}
              type="checkbox"
              className="form-check-input"
              checked={filtry[kategoria]}
              onChange={() => handleFiltr(kategoria)}
            />
            <label htmlFor={`filtr-${kategoria}`} className="form-check-label">
              {kategoria}
            </label>
          </div>
        ))}
      </div>

      {/* Siatka kart ze zdjęciami */}
      <div className="row">
        {przefiltrowane.map((zdjecie) => (
          <div key={zdjecie.id} className="col-md-4 mb-3">
            <div className="card">
              {/* Miejsce na obraz — w prawdziwym projekcie byłby tu <img> */}
              <div
                className="card-img-top bg-secondary d-flex align-items-center justify-content-center"
                style={{ height: "150px", color: "white" }}
              >
                {zdjecie.nazwa}
              </div>
              <div className="card-body">
                <p className="card-text">
                  Kategoria: <strong>{zdjecie.kategoria}</strong>
                </p>
                <p className="card-text">
                  Pobrania: <strong>{zdjecie.pobrania}</strong>
                </p>
                <button
                  className="btn btn-success btn-sm"
                  onClick={() => handlePobierz(zdjecie.id)}
                >
                  Pobierz
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Komunikat gdy brak zdjęć */}
      {przefiltrowane.length === 0 && (
        <p className="text-muted text-center">Brak zdjęć do wyświetlenia.</p>
      )}
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki:**
- Tablica obiektów w stanie (`useState`)
- Switche/checkboxy kontrolujące filtrowanie
- `filter()` do wyświetlania tylko wybranych kategorii
- `map()` do aktualizacji jednego elementu (zwiększenie licznika pobrań)
- Spread operator (`...`) do niemutowalnej aktualizacji
- Grid Bootstrap (`row` / `col-md-4`) do układania kart obok siebie
- Warunkowe renderowanie pustej listy

---

### 26.5. lista zadań (Todo app) — wieloplikowy

Kompletny przykład aplikacji z podziałem na pliki — wzorzec przepływu danych parent-child.

```
src/
├── App.js                    # Rodzic — trzyma stan
├── components/
│   ├── TaskForm.js           # Formularz dodawania
│   └── TaskList.js           # Lista zadań
└── index.js                  # Punkt wejścia
```

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

function App() {
  // Stan globalny — lista zadań trzymana w rodzicu
  const [tasks, setTasks] = useState([]);

  // Funkcja dodająca zadanie — przekazywana do TaskForm
  function addTask(taskText) {
    const newTask = {
      id: Date.now(),         // Prosty sposób na unikalne ID
      text: taskText,
      completed: false,
    };
    setTasks((prev) => [...prev, newTask]);
  }

  // Funkcja usuwająca zadanie — przekazywana do TaskList
  function deleteTask(id) {
    setTasks((prev) => prev.filter((task) => task.id !== id));
  }

  // Funkcja przełączająca ukończenie — przekazywana do TaskList
  function toggleTask(id) {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  }

  return (
    <main className="container mt-5" style={{ maxWidth: "600px" }}>
      <h1 className="text-center mb-4">Lista Zadań</h1>

      {/* Komponent formularza — otrzymuje callback onAddTask */}
      <TaskForm onAddTask={addTask} />

      {/* Komponent listy — otrzymuje dane i callbacki */}
      <TaskList
        tasks={tasks}
        onDeleteTask={deleteTask}
        onToggleTask={toggleTask}
      />

      {/* Podsumowanie */}
      <div className="mt-3 text-muted text-center">
        Pozostało zadań: {tasks.filter((t) => !t.completed).length} / {tasks.length}
      </div>
    </main>
  );
}

export default App;
```

```jsx
// Plik: src/components/TaskForm.js
import { useState } from "react";

function TaskForm({ onAddTask }) {
  const [text, setText] = useState(""); // Stan lokalny — tylko dla tego inputa

  function handleSubmit(e) {
    e.preventDefault();

    // Walidacja — nie dodajemy pustych zadań
    if (text.trim() === "") return;

    // Wywołujemy callback od rodzica
    onAddTask(text);

    // Czyścimy pole
    setText("");
  }

  return (
    <form onSubmit={handleSubmit} className="input-group mb-4">
      <input
        type="text"
        className="form-control"
        placeholder="Co masz do zrobienia?"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button className="btn btn-success" type="submit">
        Dodaj
      </button>
    </form>
  );
}

export default TaskForm;
```

```jsx
// Plik: src/components/TaskList.js
function TaskList({ tasks, onDeleteTask, onToggleTask }) {
  // Obsługa pustej listy
  if (tasks.length === 0) {
    return <p className="text-center text-muted">Brak zadań. Odpocznij!</p>;
  }

  return (
    <ul className="list-group">
      {tasks.map((task) => (
        <li
          key={task.id}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          {/* Tekst zadania — przekreślony, jeśli ukończone */}
          <span
            style={{
              textDecoration: task.completed ? "line-through" : "none",
              cursor: "pointer",
            }}
            onClick={() => onToggleTask(task.id)}
          >
            {task.text}
          </span>

          {/* Przycisk usuwania */}
          <button
            className="btn btn-danger btn-sm"
            onClick={() => onDeleteTask(task.id)}
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

**Podsumowanie przepływu danych:**

1. **Dół (Props):** `App` → `TaskList` (przekazuje `tasks`, `onDeleteTask`, `onToggleTask`)
2. **Góra (Callbacks):** `TaskForm` → `App` (dziecko wywołuje `onAddTask`)
3. **Odświeżenie:** Gdy `App` zmieni stan, React odmalowuje `TaskForm` i `TaskList` z nowymi danymi

---

### 26.6. generator hasła

Aplikacja generująca losowe hasło na podstawie ustawień użytkownika.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  const [dlugosc, setDlugosc] = useState(12);
  const [duzeLinetry, setDuzeLitery] = useState(true);
  const [cyfry, setCyfry] = useState(true);
  const [specjalne, setSpecjalne] = useState(false);
  const [haslo, setHaslo] = useState("");

  function generujHaslo() {
    let znaki = "abcdefghijklmnopqrstuvwxyz";
    if (duzeLinetry) znaki += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (cyfry) znaki += "0123456789";
    if (specjalne) znaki += "!@#$%^&*()_+-=[]{}|;:,.<>?";

    let wynik = "";
    for (let i = 0; i < dlugosc; i++) {
      const losowy = Math.floor(Math.random() * znaki.length);
      wynik += znaki[losowy];
    }

    setHaslo(wynik);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "500px" }}>
      <h1>Generator hasła</h1>

      {/* Suwak długości */}
      <div className="mb-3">
        <label className="form-label">Długość: {dlugosc}</label>
        <input
          type="range"
          className="form-range"
          min="4"
          max="32"
          value={dlugosc}
          onChange={(e) => setDlugosc(Number(e.target.value))}
        />
      </div>

      {/* Checkboxy opcji */}
      <div className="form-check mb-2">
        <input
          id="duze"
          type="checkbox"
          className="form-check-input"
          checked={duzeLinetry}
          onChange={(e) => setDuzeLitery(e.target.checked)}
        />
        <label htmlFor="duze" className="form-check-label">Duże litery (A-Z)</label>
      </div>

      <div className="form-check mb-2">
        <input
          id="cyfry"
          type="checkbox"
          className="form-check-input"
          checked={cyfry}
          onChange={(e) => setCyfry(e.target.checked)}
        />
        <label htmlFor="cyfry" className="form-check-label">Cyfry (0-9)</label>
      </div>

      <div className="form-check mb-3">
        <input
          id="specjalne"
          type="checkbox"
          className="form-check-input"
          checked={specjalne}
          onChange={(e) => setSpecjalne(e.target.checked)}
        />
        <label htmlFor="specjalne" className="form-check-label">Znaki specjalne (!@#$)</label>
      </div>

      <button className="btn btn-primary mb-3" onClick={generujHaslo}>
        Generuj hasło
      </button>

      {/* Wynik */}
      {haslo && (
        <div className="alert alert-success">
          <strong>Wygenerowane hasło:</strong>
          <code className="d-block mt-1" style={{ fontSize: "1.2rem" }}>
            {haslo}
          </code>
        </div>
      )}
    </main>
  );
}

export default App;
```

---

### 26.7. kalkulator BMI

Formularz z obliczeniem BMI i interpretacją wyniku.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

// Funkcja pomocnicza — interpretacja BMI (poza komponentem)
function interpretujBMI(bmi) {
  if (bmi < 18.5) return { tekst: "Niedowaga", kolor: "warning" };
  if (bmi < 25) return { tekst: "Waga prawidłowa", kolor: "success" };
  if (bmi < 30) return { tekst: "Nadwaga", kolor: "warning" };
  return { tekst: "Otyłość", kolor: "danger" };
}

function App() {
  const [waga, setWaga] = useState("");
  const [wzrost, setWzrost] = useState("");
  const [wynik, setWynik] = useState(null);
  const [blad, setBlad] = useState("");

  function handleOblicz(e) {
    e.preventDefault();

    // Walidacja
    const wagaNum = Number(waga);
    const wzrostNum = Number(wzrost);

    if (wagaNum <= 0 || wzrostNum <= 0) {
      setBlad("Podaj poprawne wartości wagi i wzrostu");
      setWynik(null);
      return;
    }

    // Obliczenie BMI: waga(kg) / wzrost(m)^2
    const wzrostM = wzrostNum / 100; // cm → m
    const bmi = wagaNum / (wzrostM * wzrostM);

    setWynik(bmi);
    setBlad("");
    console.log(`Waga: ${wagaNum}kg, Wzrost: ${wzrostNum}cm, BMI: ${bmi.toFixed(2)}`);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "400px" }}>
      <h1>Kalkulator BMI</h1>

      <form onSubmit={handleOblicz}>
        <div className="mb-3">
          <label htmlFor="waga" className="form-label">Waga (kg):</label>
          <input
            id="waga"
            type="number"
            className="form-control"
            value={waga}
            onChange={(e) => setWaga(e.target.value)}
            placeholder="np. 70"
          />
        </div>

        <div className="mb-3">
          <label htmlFor="wzrost" className="form-label">Wzrost (cm):</label>
          <input
            id="wzrost"
            type="number"
            className="form-control"
            value={wzrost}
            onChange={(e) => setWzrost(e.target.value)}
            placeholder="np. 175"
          />
        </div>

        <button type="submit" className="btn btn-primary w-100">
          Oblicz BMI
        </button>
      </form>

      {/* Błąd walidacji */}
      {blad && <div className="alert alert-danger mt-3">{blad}</div>}

      {/* Wynik BMI */}
      {wynik !== null && (
        <div className={`alert alert-${interpretujBMI(wynik).kolor} mt-3`}>
          <h4>BMI: {wynik.toFixed(2)}</h4>
          <p>{interpretujBMI(wynik).tekst}</p>
        </div>
      )}
    </main>
  );
}

export default App;
```

---

### 26.8. widok kart z filtrami i wyszukiwaniem

Rozbudowany widok kart z wyszukiwarką tekstową i filtrami kategorii.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  // Dane stałe — produkty
  const produkty = [
    { id: 1, nazwa: "Laptop Pro", kategoria: "Elektronika", cena: 4500 },
    { id: 2, nazwa: "Mysz bezprzewodowa", kategoria: "Elektronika", cena: 120 },
    { id: 3, nazwa: "Koszulka bawełniana", kategoria: "Odzież", cena: 49 },
    { id: 4, nazwa: "Spodnie jeansowe", kategoria: "Odzież", cena: 180 },
    { id: 5, nazwa: "Rower górski", kategoria: "Sport", cena: 2200 },
    { id: 6, nazwa: "Piłka nożna", kategoria: "Sport", cena: 80 },
    { id: 7, nazwa: "Monitor 27\"", kategoria: "Elektronika", cena: 1500 },
    { id: 8, nazwa: "Buty biegowe", kategoria: "Sport", cena: 350 },
  ];

  // Wyciągnięcie unikalnych kategorii
  const kategorie = [...new Set(produkty.map((p) => p.kategoria))];

  // Stan filtrów
  const [szukaj, setSzukaj] = useState("");
  const [wybranaKategoria, setWybranaKategoria] = useState("Wszystkie");
  const [sortowanie, setSortowanie] = useState("nazwa");

  // Filtrowanie
  let przefiltrowane = produkty;

  // Filtr tekstowy
  if (szukaj.trim() !== "") {
    przefiltrowane = przefiltrowane.filter((p) =>
      p.nazwa.toLowerCase().includes(szukaj.toLowerCase())
    );
  }

  // Filtr kategorii
  if (wybranaKategoria !== "Wszystkie") {
    przefiltrowane = przefiltrowane.filter(
      (p) => p.kategoria === wybranaKategoria
    );
  }

  // Sortowanie
  przefiltrowane = [...przefiltrowane].sort((a, b) => {
    if (sortowanie === "nazwa") return a.nazwa.localeCompare(b.nazwa);
    if (sortowanie === "cena-rosnaco") return a.cena - b.cena;
    if (sortowanie === "cena-malejaco") return b.cena - a.cena;
    return 0;
  });

  return (
    <main className="container mt-4">
      <h1>Katalog produktów</h1>

      {/* Panel filtrów */}
      <div className="row mb-4">
        {/* Wyszukiwarka */}
        <div className="col-md-4 mb-2">
          <input
            type="text"
            className="form-control"
            placeholder="Szukaj produktu..."
            value={szukaj}
            onChange={(e) => setSzukaj(e.target.value)}
          />
        </div>

        {/* Filtr kategorii */}
        <div className="col-md-4 mb-2">
          <select
            className="form-select"
            value={wybranaKategoria}
            onChange={(e) => setWybranaKategoria(e.target.value)}
          >
            <option value="Wszystkie">Wszystkie kategorie</option>
            {kategorie.map((k) => (
              <option key={k} value={k}>{k}</option>
            ))}
          </select>
        </div>

        {/* Sortowanie */}
        <div className="col-md-4 mb-2">
          <select
            className="form-select"
            value={sortowanie}
            onChange={(e) => setSortowanie(e.target.value)}
          >
            <option value="nazwa">Sortuj: Nazwa A-Z</option>
            <option value="cena-rosnaco">Sortuj: Cena rosnąco</option>
            <option value="cena-malejaco">Sortuj: Cena malejąco</option>
          </select>
        </div>
      </div>

      {/* Licznik wyników */}
      <p className="text-muted">Znaleziono: {przefiltrowane.length} produktów</p>

      {/* Siatka kart */}
      <div className="row">
        {przefiltrowane.map((produkt) => (
          <div key={produkt.id} className="col-md-4 mb-3">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{produkt.nazwa}</h5>
                <p className="card-text">
                  <span className="badge bg-secondary">{produkt.kategoria}</span>
                </p>
                <p className="card-text">
                  <strong>{produkt.cena} zł</strong>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Obsługa braku wyników */}
      {przefiltrowane.length === 0 && (
        <p className="text-center text-muted">
          Brak produktów spełniających kryteria wyszukiwania.
        </p>
      )}
    </main>
  );
}

export default App;
```

---

### 26.9. mixer kolorów RGB

Trzy suwaki sterujące kolorem tła w czasie rzeczywistym.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  const [r, setR] = useState(100);
  const [g, setG] = useState(150);
  const [b, setB] = useState(200);

  // Kolor w formacie CSS
  const kolor = `rgb(${r}, ${g}, ${b})`;

  // Kolor w formacie HEX
  const hex =
    "#" +
    r.toString(16).padStart(2, "0") +
    g.toString(16).padStart(2, "0") +
    b.toString(16).padStart(2, "0");

  return (
    <main className="container mt-4" style={{ maxWidth: "500px" }}>
      <h1>Mixer kolorów RGB</h1>

      {/* Podgląd koloru */}
      <div
        style={{
          width: "100%",
          height: "150px",
          backgroundColor: kolor,
          borderRadius: "10px",
          marginBottom: "1rem",
          border: "1px solid #ccc",
        }}
      />

      {/* Wartości koloru */}
      <p className="text-center">
        <strong>RGB:</strong> {kolor} | <strong>HEX:</strong> {hex.toUpperCase()}
      </p>

      {/* Suwak R (czerwony) */}
      <div className="mb-3">
        <label className="form-label" style={{ color: "red" }}>
          R (czerwony): {r}
        </label>
        <input
          type="range"
          className="form-range"
          min="0"
          max="255"
          value={r}
          onChange={(e) => setR(Number(e.target.value))}
        />
      </div>

      {/* Suwak G (zielony) */}
      <div className="mb-3">
        <label className="form-label" style={{ color: "green" }}>
          G (zielony): {g}
        </label>
        <input
          type="range"
          className="form-range"
          min="0"
          max="255"
          value={g}
          onChange={(e) => setG(Number(e.target.value))}
        />
      </div>

      {/* Suwak B (niebieski) */}
      <div className="mb-3">
        <label className="form-label" style={{ color: "blue" }}>
          B (niebieski): {b}
        </label>
        <input
          type="range"
          className="form-range"
          min="0"
          max="255"
          value={b}
          onChange={(e) => setB(Number(e.target.value))}
        />
      </div>

      {/* Reset */}
      <button
        className="btn btn-secondary w-100"
        onClick={() => { setR(0); setG(0); setB(0); }}
      >
        Reset (czarny)
      </button>
    </main>
  );
}

export default App;
```

---

### 26.10. kości do gry z blokowaniem

Gra w kości — rzut 5 kośćmi, możliwość blokowania wybranych kości przy ponownym rzucie.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

// Funkcja losująca wartość kości (1-6)
function losujKosc() {
  return Math.floor(Math.random() * 6) + 1;
}

function App() {
  // Stan kości — tablica 5 obiektów z wartością i stanem blokady
  const [kosci, setKosci] = useState([
    { id: 1, wartosc: losujKosc(), zablokowana: false },
    { id: 2, wartosc: losujKosc(), zablokowana: false },
    { id: 3, wartosc: losujKosc(), zablokowana: false },
    { id: 4, wartosc: losujKosc(), zablokowana: false },
    { id: 5, wartosc: losujKosc(), zablokowana: false },
  ]);

  const [liczbaRzutow, setLiczbaRzutow] = useState(1);

  // Rzut kośćmi — tylko niezablokowane
  function handleRzut() {
    setKosci((prev) =>
      prev.map((k) =>
        k.zablokowana ? k : { ...k, wartosc: losujKosc() }
      )
    );
    setLiczbaRzutow((prev) => prev + 1);
  }

  // Blokowanie/odblokowanie kości
  function handleBlokuj(id) {
    setKosci((prev) =>
      prev.map((k) =>
        k.id === id ? { ...k, zablokowana: !k.zablokowana } : k
      )
    );
  }

  // Nowa gra — reset
  function handleNowaGra() {
    setKosci(
      kosci.map((k) => ({ ...k, wartosc: losujKosc(), zablokowana: false }))
    );
    setLiczbaRzutow(1);
  }

  // Suma kości
  const suma = kosci.reduce((acc, k) => acc + k.wartosc, 0);

  return (
    <main className="container mt-4 text-center" style={{ maxWidth: "500px" }}>
      <h1>Kości do gry</h1>
      <p>Rzut numer: {liczbaRzutow} | Suma: {suma}</p>

      {/* Wyświetlanie kości */}
      <div className="d-flex justify-content-center gap-2 mb-4">
        {kosci.map((k) => (
          <button
            key={k.id}
            className={`btn btn-lg ${
              k.zablokowana ? "btn-danger" : "btn-outline-dark"
            }`}
            style={{ width: "60px", height: "60px", fontSize: "1.5rem" }}
            onClick={() => handleBlokuj(k.id)}
          >
            {k.wartosc}
          </button>
        ))}
      </div>

      <p className="text-muted small">
        Kliknij kość, aby ją zablokować (czerwona = zablokowana)
      </p>

      <div className="d-flex gap-2 justify-content-center">
        <button className="btn btn-primary" onClick={handleRzut}>
          Rzuć kośćmi
        </button>
        <button className="btn btn-secondary" onClick={handleNowaGra}>
          Nowa gra
        </button>
      </div>
    </main>
  );
}

export default App;
```

---

### 26.11. licznik z historią operacji

Licznik, który zapisuje historię wszystkich wykonanych operacji.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  const [licznik, setLicznik] = useState(0);
  const [historia, setHistoria] = useState([]);

  function wykonajOperacje(operacja, wartosc) {
    let nowaWartosc;

    switch (operacja) {
      case "dodaj":
        nowaWartosc = licznik + wartosc;
        break;
      case "odejmij":
        nowaWartosc = licznik - wartosc;
        break;
      case "pomnoz":
        nowaWartosc = licznik * wartosc;
        break;
      case "reset":
        nowaWartosc = 0;
        break;
      default:
        return;
    }

    // Zapis do historii
    const wpis = {
      id: Date.now(),
      operacja: operacja,
      wartosc: wartosc,
      wynik: nowaWartosc,
      czas: new Date().toLocaleTimeString(),
    };

    setHistoria((prev) => [wpis, ...prev]); // Najnowsze na górze
    setLicznik(nowaWartosc);
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "500px" }}>
      <h1 className="text-center">Licznik: {licznik}</h1>

      {/* Przyciski operacji */}
      <div className="d-flex gap-2 justify-content-center mb-4">
        <button className="btn btn-success" onClick={() => wykonajOperacje("dodaj", 1)}>+1</button>
        <button className="btn btn-success" onClick={() => wykonajOperacje("dodaj", 5)}>+5</button>
        <button className="btn btn-danger" onClick={() => wykonajOperacje("odejmij", 1)}>-1</button>
        <button className="btn btn-danger" onClick={() => wykonajOperacje("odejmij", 5)}>-5</button>
        <button className="btn btn-info" onClick={() => wykonajOperacje("pomnoz", 2)}>×2</button>
        <button className="btn btn-secondary" onClick={() => wykonajOperacje("reset", 0)}>Reset</button>
      </div>

      {/* Historia operacji */}
      <h5>Historia operacji ({historia.length})</h5>
      {historia.length === 0 ? (
        <p className="text-muted">Brak operacji</p>
      ) : (
        <table className="table table-sm table-striped">
          <thead>
            <tr>
              <th>Czas</th>
              <th>Operacja</th>
              <th>Wynik</th>
            </tr>
          </thead>
          <tbody>
            {historia.map((w) => (
              <tr key={w.id}>
                <td>{w.czas}</td>
                <td>{w.operacja} {w.wartosc !== 0 ? w.wartosc : ""}</td>
                <td>{w.wynik}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Czyszczenie historii */}
      {historia.length > 0 && (
        <button
          className="btn btn-outline-danger btn-sm"
          onClick={() => setHistoria([])}
        >
          Wyczyść historię
        </button>
      )}
    </main>
  );
}

export default App;
```

---

### 26.12. algorytmy w React — sumowanie, zliczanie, filtrowanie

Przykłady typowych operacji algorytmicznych osadzonych w React.

#### 26.12.1. suma i średnia z tablicy

```jsx
// Plik: src/App.js
import { useState } from "react";

function App() {
  const [oceny, setOceny] = useState([5, 4, 3, 5, 4, 2, 5, 3]);
  const [nowaOcena, setNowaOcena] = useState("");

  // Obliczenia — robione przed return, nie w stanie
  const suma = oceny.reduce((acc, o) => acc + o, 0);
  const srednia = oceny.length > 0 ? suma / oceny.length : 0;
  const najwyzsza = oceny.length > 0 ? Math.max(...oceny) : 0;
  const najnizsza = oceny.length > 0 ? Math.min(...oceny) : 0;

  function handleDodaj() {
    const ocena = Number(nowaOcena);
    if (ocena >= 1 && ocena <= 6) {
      setOceny((prev) => [...prev, ocena]);
      setNowaOcena("");
    }
  }

  return (
    <div className="container mt-4" style={{ maxWidth: "400px" }}>
      <h2>Statystyki ocen</h2>
      <p>Oceny: {oceny.join(", ")}</p>
      <p>Suma: {suma}</p>
      <p>Średnia: {srednia.toFixed(2)}</p>
      <p>Najwyższa: {najwyzsza}</p>
      <p>Najniższa: {najnizsza}</p>
      <p>Liczba ocen: {oceny.length}</p>

      <div className="input-group mt-3">
        <input
          type="number"
          className="form-control"
          value={nowaOcena}
          onChange={(e) => setNowaOcena(e.target.value)}
          placeholder="1-6"
          min="1"
          max="6"
        />
        <button className="btn btn-primary" onClick={handleDodaj}>Dodaj ocenę</button>
      </div>
    </div>
  );
}

export default App;
```

#### 26.12.2. zliczanie wystąpień

```jsx
function App() {
  const dane = ["kot", "pies", "kot", "ryba", "pies", "kot", "papuga"];

  // Zliczanie za pomocą reduce
  const zliczenie = dane.reduce((acc, el) => {
    acc[el] = (acc[el] || 0) + 1;
    return acc;
  }, {});

  return (
    <div className="container mt-4">
      <h2>Zliczanie wystąpień</h2>
      <table className="table" style={{ maxWidth: "300px" }}>
        <thead>
          <tr><th>Element</th><th>Ilość</th></tr>
        </thead>
        <tbody>
          {Object.entries(zliczenie).map(([klucz, wartosc]) => (
            <tr key={klucz}>
              <td>{klucz}</td>
              <td>{wartosc}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

#### 26.12.3. filtrowanie po wielu kryteriach

```jsx
function App() {
  const [minCena, setMinCena] = useState(0);
  const [maxCena, setMaxCena] = useState(1000);
  const [szukaj, setSzukaj] = useState("");

  const produkty = [
    { id: 1, nazwa: "Laptop", cena: 3000 },
    { id: 2, nazwa: "Mysz", cena: 50 },
    { id: 3, nazwa: "Klawiatura", cena: 200 },
    { id: 4, nazwa: "Monitor", cena: 1500 },
    { id: 5, nazwa: "Słuchawki", cena: 350 },
  ];

  // Filtrowanie z wieloma warunkami jednocześnie
  const wyniki = produkty
    .filter((p) => p.cena >= minCena && p.cena <= maxCena)
    .filter((p) => p.nazwa.toLowerCase().includes(szukaj.toLowerCase()));

  return (
    <div className="container mt-4">
      <h2>Filtrowanie produktów</h2>

      <div className="row mb-3">
        <div className="col">
          <input type="text" className="form-control" placeholder="Szukaj..."
            value={szukaj} onChange={(e) => setSzukaj(e.target.value)} />
        </div>
        <div className="col">
          <input type="number" className="form-control" placeholder="Min cena"
            value={minCena} onChange={(e) => setMinCena(Number(e.target.value))} />
        </div>
        <div className="col">
          <input type="number" className="form-control" placeholder="Max cena"
            value={maxCena} onChange={(e) => setMaxCena(Number(e.target.value))} />
        </div>
      </div>

      <p>Znaleziono: {wyniki.length}</p>
      <ul className="list-group">
        {wyniki.map((p) => (
          <li key={p.id} className="list-group-item d-flex justify-content-between">
            <span>{p.nazwa}</span>
            <span>{p.cena} zł</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

#### 26.12.4. szyfr cezara

```jsx
import { useState } from "react";

function App() {
  const [tekst, setTekst] = useState("");
  const [przesuniecie, setPrzesuniecie] = useState(3);
  const [wynik, setWynik] = useState("");

  function szyfrujCezar(tekst, przesuniecie) {
    return tekst
      .split("")
      .map((znak) => {
        // Małe litery
        if (znak >= "a" && znak <= "z") {
          const kod = ((znak.charCodeAt(0) - 97 + przesuniecie) % 26 + 26) % 26 + 97;
          return String.fromCharCode(kod);
        }
        // Duże litery
        if (znak >= "A" && znak <= "Z") {
          const kod = ((znak.charCodeAt(0) - 65 + przesuniecie) % 26 + 26) % 26 + 65;
          return String.fromCharCode(kod);
        }
        // Inne znaki bez zmian
        return znak;
      })
      .join("");
  }

  function handleSzyfruj() {
    setWynik(szyfrujCezar(tekst, przesuniecie));
  }

  function handleDeszyfruj() {
    setWynik(szyfrujCezar(tekst, -przesuniecie));
  }

  return (
    <div className="container mt-4" style={{ maxWidth: "500px" }}>
      <h2>Szyfr Cezara</h2>

      <div className="mb-3">
        <label className="form-label">Tekst:</label>
        <input type="text" className="form-control" value={tekst}
          onChange={(e) => setTekst(e.target.value)} placeholder="Wpisz tekst" />
      </div>

      <div className="mb-3">
        <label className="form-label">Przesunięcie: {przesuniecie}</label>
        <input type="range" className="form-range" min="1" max="25"
          value={przesuniecie} onChange={(e) => setPrzesuniecie(Number(e.target.value))} />
      </div>

      <div className="d-flex gap-2 mb-3">
        <button className="btn btn-primary" onClick={handleSzyfruj}>Szyfruj</button>
        <button className="btn btn-secondary" onClick={handleDeszyfruj}>Deszyfruj</button>
      </div>

      {wynik && (
        <div className="alert alert-info">
          <strong>Wynik:</strong> {wynik}
        </div>
      )}
    </div>
  );
}

export default App;
```

---

---

### 26.13. prosta playlista audio (Odtwarzacz ze stanem)

Ten wzorzec jest genialnym rozwiązaniem skomplikowanego zadania polegającego na zbudowaniu „Player’a” i manipulowaniu ścieżkami podawanych plików typu `mp3`. 
Z reguły polega to na wrzuceniu utworów do tablicy (bazy), a po kliknięciu klawisza `<li>` zmienieniu całego odtwarzanego źródła na nową muzykę w hooku (stanie).

```jsx
// Główny lub opcjonalny plik: src/App.js
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css"; // Polegamy mocno na gridach / kartkach bootstrapa stąd.

// Ważne: Baza musi wskazywać na folder publiczny dla ładowarki! Pliki muszą tam siedzieć (public/dzwieki/..._
const LISTA_UTWOROW = [
  { id: 1, tytul: "Zimowy wiatr", wokalista: "Marek_Pytlas", src: "/dzwieki/wiatr.mp3" },
  { id: 2, tytul: "Nocne gwieździste niebo", wokalista: "Dj GROM", src: "/dzwieki/niebo.mp3" },
  { id: 3, tytul: "Energetyczny Pop 2026", wokalista: "Sygmund", src: "/dzwieki/pop.mp3" }
];

function OdtwarzaczZPlayLista() {
  // Trzymamy w całości obiekt w którym jest i autor i jego mp3!
  const [obecnyUtwor, setObecnyUtwor] = useState(LISTA_UTWOROW[0]);

  return (
    <div className="container mt-5">
      <div className="card shadow border-dark" style={{ maxWidth: "550px", margin: "auto" }}>
        
        {/* ======== Widok playera (górny ekran odtwarzania) ======== */}
        <div className="card-header bg-dark text-white text-center rounded-top">
          <h5 className="mb-0">🎵 Twoja Cyfrowa Playlista</h5>
        </div>
        <div className="card-body text-center bg-light">
          <h6 className="text-secondary text-uppercase ls-1">Aktualnie gra</h6>
          <h2 className="text-primary fw-bold">{obecnyUtwor.tytul}</h2>
          <p className="text-muted fs-5">Artysta: {obecnyUtwor.wokalista}</p>
          
          {/* Tag Audio ma atrybut kluczowy -> key={}. 
             Zmusza to silnik React'a do "zniszczenia i zrestartowania Playera" kiedy podepniemy mu nowy key'u 
             w zapiętym źródle (mp3). Bez tego podmienimy src ale utwór nie zadziała.
          */}
          <audio controls autoPlay key={obecnyUtwor.src} className="w-100 mt-4 px-2">
             <source src={obecnyUtwor.src} type="audio/mpeg" />
          </audio>
        </div>

        {/* ======== Sekcja listy utworów do klikania ======== */}
        <ul className="list-group list-group-flush rounded-bottom">
          {LISTA_UTWOROW.map((utwor) => {
             // Wzmienie dynamiczne klasy jeżeli piosenka w pętli zgadza się ze stanem obecnym w pamięci
             const aktywnyClass = utwor.id === obecnyUtwor.id ? "active bg-primary border-primary fw-bold" : "";
             
             return (
               <li 
                 key={utwor.id} 
                 className={`list-group-item list-group-item-action ${aktywnyClass}`}
                 onClick={() => setObecnyUtwor(utwor)}
                 style={{ cursor: "pointer", transition: "0.2s" }}
               >
                 <div className="d-flex justify-content-between align-items-center">
                    <span>{utwor.id}. {utwor.tytul} </span>
                    <span className="badge rounded-pill bg-dark">
                      {utwor.id === obecnyUtwor.id ? "Odtwarza się" : "Graj"}
                    </span>
                 </div>
               </li>
             );
          })}
        </ul>

      </div>
    </div>
  );
}

export default OdtwarzaczZPlayLista;
```

---

### 26.14. akordeon FAQ z widocznością (Sekcje rozwijane)

Typowe zadanie architektoniczne - "Mam listę elementów, ale po kliknięciu konkretnego w dół rościąga mi się tekst/odpowiedź, gasząc resztę na biało!". Jest to idealne pole dla **Renderowania warunkowego**.

```jsx
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const BAZA_FAQ = [
  { id: 1, pyta: "Jak długo czekam na dostawę?", opowiada: "Zasze w 24 godziny od kupienia zlecenia po zaksięgowaniu P24 na naszym koncie firmowym." },
  { id: 2, pyta: "Czy dostawa jest darmowa dla paczek?", opowiada: "Dla zamówień przekraczających trefny pułap 199.99 PLN wysyłamy na nasz pełny, gigantyczny paczkowy koszt całkowicie za free." },
  { id: 3, pyta: "Co z procedurą zgłaszanych zwrotów 12 dniowych", opowiada: "Towar ze wgzlędów higienicznych i certyfikatów z rąk Reacta nie może zostać o dziwo wysłany w drogę powrotnę a zaledwie w proces reklamacji wewnątrz chatu." }
];

function ModulPytanUzytkownikaFAQ() {
  // Stan "otwarteId" trzyma ID rozwiniętego segmentu. Wartość startowa to puste -> 'null', czyli wszystkie ukryte.
  const [otwarteId, setOtwarteId] = useState(null);

  // Funkcja odbierająca kliknięcie:
  const nacisnietyPrzycisk = (idMiejsca) => {
    // Jeżeli kliknięto id tego samego, co jest już otwarte... ZAMKNIJ wszystkich (przypisać tu null).
    if (otwarteId === idMiejsca) {
      setOtwarteId(null);
    } else {
      setOtwarteId(idMiejsca); // Jak wciśnie inny guzik - po prostu OTWÓRZ go! A przy okazji reszta zgasi flagi.
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-5 fw-bold text-dark">Baza Częstych Przyszłoch Pytań</h2>
      
      <div className="list-group shadow-lg overflow-hidden border-0 rounded" style={{ maxWidth: "600px", margin: "auto" }}>
        {BAZA_FAQ.map((rekord) => {
          
          // Boolean (flaga bool) decydująca wewnątrz metody - jeżeli w koszcie się zgadza to True
          const panelWidoczny = otwarteId === rekord.id; 
          
          return (
            <div key={rekord.id}>
              
              {/* Sekcja Clickable (Nagłówek Modułu z Zapytaniem) */}
              <button 
                onClick={() => nacisnietyPrzycisk(rekord.id)}
                className={`list-group-item list-group-item-action d-flex justify-content-between align-items-center py-3 border-0 border-bottom
                 ${panelWidoczny ? "bg-primary text-white" : ""}`}
                style={{ fontSize: "1.1rem" }}
              >
                <div className="fw-bold">
                  <span className="me-3 fs-4 text-warning">?</span>
                  Question. {rekord.pyta}
                </div>
                {/* Genialny feedback do strzałeczek kierunkowych! */}
                <span className="fs-5">{panelWidoczny ? "⮝ Zwiń" : "⮟ Rozwiń"}</span>
              </button>

              {/* Renderowanie warunkowe (wyświetl / zmiel). Gdyby zmienna pod bool'a u góry wynosiła fałsz, po prostu przeskoczy tę sekcję. */}
              {panelWidoczny && (
                <div className="p-4 bg-light text-muted border-start border-5 border-warning opacity-75">
                  <strong className="text-dark">Odpowiedź Eksperta:</strong> <br/>
                  <p className="mt-2 mb-0 lh-lg">{rekord.opowiada}</p>
                </div>
              )}
              
            </div>
          )
        })}
      </div>
    </div>
  );
}

export default ModulPytanUzytkownikaFAQ;
```


---

### 26.15. formularz zamówienia pizzy

Rozbudowany formularz łączący wiele typów pól: radio (rozmiar), checkboxy (składniki z cenami), select (sos), range (ostrość), textarea (uwagi), dynamiczne obliczanie ceny, walidację i podsumowanie zamówienia w formie paragonu.

**Smaczki:** dynamiczna cena aktualizowana w czasie rzeczywistym, limit składników (max 5), wizualny wskaźnik ostrości z emoji, animowany paragon po złożeniu zamówienia, przycisk "Zamów ponownie" przywracający ostatnie zamówienie z localStorage.

```jsx
// Plik: src/App.js
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";

// Dane cennika — poza komponentem (stałe)
const ROZMIARY = [
  { id: "mala", nazwa: "Mała (25cm)", cena: 22 },
  { id: "srednia", nazwa: "Średnia (32cm)", cena: 28 },
  { id: "duza", nazwa: "Duża (40cm)", cena: 35 },
];

const SKLADNIKI = [
  { id: "ser", nazwa: "Podwójny ser", cena: 4 },
  { id: "szynka", nazwa: "Szynka", cena: 5 },
  { id: "pieczarki", nazwa: "Pieczarki", cena: 3 },
  { id: "oliwki", nazwa: "Oliwki", cena: 4 },
  { id: "papryka", nazwa: "Papryka", cena: 3 },
  { id: "salami", nazwa: "Salami pikantne", cena: 6 },
  { id: "rukola", nazwa: "Rukola", cena: 3 },
  { id: "ananas", nazwa: "Ananas", cena: 4 },
];

const SOSY = ["Bez sosu", "Czosnkowy", "Pomidorowy", "Ostry", "Barbecue"];

const MAX_SKLADNIKOW = 5;

// Funkcja pomocnicza — emoji ostrości
function emotikonOstrosci(poziom) {
  if (poziom === 0) return "🧊 Łagodna";
  if (poziom <= 2) return "🌶️ Lekko pikantna";
  if (poziom <= 4) return "🌶️🌶️ Pikantna";
  return "🌶️🌶️🌶️ Piekielna!";
}

function App() {
  // Stan formularza
  const [rozmiar, setRozmiar] = useState("srednia");
  const [wybraneSkladniki, setWybraneSkladniki] = useState([]);
  const [sos, setSos] = useState("Bez sosu");
  const [ostrosc, setOstrosc] = useState(0);
  const [uwagi, setUwagi] = useState("");
  const [imie, setImie] = useState("");

  // Stan UI
  const [zamowienie, setZamowienie] = useState(null); // Złożone zamówienie (paragon)
  const [bledy, setBledy] = useState({});

  // Odczyt ostatniego zamówienia z localStorage
  const [ostatnie, setOstatnie] = useState(() => {
    const zapis = localStorage.getItem("ostatniePizza");
    return zapis ? JSON.parse(zapis) : null;
  });

  // Obliczanie ceny — dynamicznie przy każdym renderze
  const cenaRozmiaru = ROZMIARY.find((r) => r.id === rozmiar)?.cena || 0;
  const cenaSkladnikow = wybraneSkladniki.reduce((suma, id) => {
    const skladnik = SKLADNIKI.find((s) => s.id === id);
    return suma + (skladnik?.cena || 0);
  }, 0);
  const cenaCalkowita = cenaRozmiaru + cenaSkladnikow;

  // Obsługa checkboxów składników
  function handleSkladnik(id) {
    setWybraneSkladniki((prev) => {
      if (prev.includes(id)) {
        // Odznaczenie — usuwamy
        return prev.filter((s) => s !== id);
      }
      // Zaznaczenie — dodajemy (z limitem)
      if (prev.length >= MAX_SKLADNIKOW) return prev;
      return [...prev, id];
    });
  }

  // Walidacja
  function waliduj() {
    const noweBledy = {};
    if (imie.trim().length < 2) noweBledy.imie = "Podaj imię (min. 2 znaki)";
    if (wybraneSkladniki.length === 0) noweBledy.skladniki = "Wybierz przynajmniej 1 składnik";
    return noweBledy;
  }

  // Złożenie zamówienia
  function handleSubmit(e) {
    e.preventDefault();
    const noweBledy = waliduj();
    if (Object.keys(noweBledy).length > 0) {
      setBledy(noweBledy);
      return;
    }
    setBledy({});

    const dane = {
      imie,
      rozmiar: ROZMIARY.find((r) => r.id === rozmiar).nazwa,
      skladniki: wybraneSkladniki.map(
        (id) => SKLADNIKI.find((s) => s.id === id).nazwa
      ),
      sos,
      ostrosc,
      uwagi,
      cena: cenaCalkowita,
      czas: new Date().toLocaleTimeString("pl-PL"),
    };

    setZamowienie(dane);

    // Zapis do localStorage
    localStorage.setItem("ostatniePizza", JSON.stringify({ rozmiar, wybraneSkladniki, sos, ostrosc }));
    setOstatnie({ rozmiar, wybraneSkladniki, sos, ostrosc });
  }

  // Przywrócenie ostatniego zamówienia
  function handlePrzywroc() {
    if (!ostatnie) return;
    setRozmiar(ostatnie.rozmiar);
    setWybraneSkladniki(ostatnie.wybraneSkladniki);
    setSos(ostatnie.sos);
    setOstrosc(ostatnie.ostrosc);
    setZamowienie(null);
  }

  // Nowe zamówienie — reset
  function handleReset() {
    setRozmiar("srednia");
    setWybraneSkladniki([]);
    setSos("Bez sosu");
    setOstrosc(0);
    setUwagi("");
    setImie("");
    setZamowienie(null);
    setBledy({});
  }

  // Widok paragonu po złożeniu zamówienia
  if (zamowienie) {
    return (
      <main className="container mt-4" style={{ maxWidth: "500px" }}>
        <div className="card border-success shadow">
          <div className="card-header bg-success text-white text-center">
            <h4 className="mb-0">🍕 Zamówienie złożone!</h4>
          </div>
          <div className="card-body" style={{ fontFamily: "monospace" }}>
            <p className="text-muted text-center mb-3">--- PARAGON ---</p>
            <p><strong>Klient:</strong> {zamowienie.imie}</p>
            <p><strong>Rozmiar:</strong> {zamowienie.rozmiar}</p>
            <p><strong>Składniki:</strong></p>
            <ul className="mb-2">
              {zamowienie.skladniki.map((s) => (
                <li key={s}>{s}</li>
              ))}
            </ul>
            <p><strong>Sos:</strong> {zamowienie.sos}</p>
            <p><strong>Ostrość:</strong> {emotikonOstrosci(zamowienie.ostrosc)}</p>
            {zamowienie.uwagi && <p><strong>Uwagi:</strong> {zamowienie.uwagi}</p>}
            <hr />
            <p className="fs-4 text-center fw-bold text-success">
              Do zapłaty: {zamowienie.cena.toFixed(2)} zł
            </p>
            <p className="text-muted text-center small">Godzina: {zamowienie.czas}</p>
          </div>
          <div className="card-footer d-flex gap-2">
            <button className="btn btn-primary flex-grow-1" onClick={handleReset}>
              Nowe zamówienie
            </button>
            <button className="btn btn-outline-secondary flex-grow-1" onClick={handlePrzywroc}>
              Zamów to samo
            </button>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "600px" }}>
      <h1 className="text-center mb-4">🍕 Zamów Pizzę</h1>

      {/* Pasek ceny — przyklejony na górze */}
      <div className="alert alert-warning d-flex justify-content-between align-items-center sticky-top">
        <span>Twoja pizza:</span>
        <span className="fs-4 fw-bold">{cenaCalkowita.toFixed(2)} zł</span>
      </div>

      <form onSubmit={handleSubmit}>
        {/* Imię */}
        <div className="mb-3">
          <label htmlFor="imie" className="form-label">Twoje imię:</label>
          <input
            id="imie"
            type="text"
            className={`form-control ${bledy.imie ? "is-invalid" : ""}`}
            value={imie}
            onChange={(e) => setImie(e.target.value)}
            placeholder="Na kogo zamówienie?"
          />
          {bledy.imie && <div className="invalid-feedback">{bledy.imie}</div>}
        </div>

        {/* Rozmiar — radio */}
        <fieldset className="mb-3">
          <legend className="fs-6 fw-bold">Rozmiar:</legend>
          {ROZMIARY.map((r) => (
            <div key={r.id} className="form-check">
              <input
                id={`rozmiar-${r.id}`}
                type="radio"
                className="form-check-input"
                name="rozmiar"
                value={r.id}
                checked={rozmiar === r.id}
                onChange={(e) => setRozmiar(e.target.value)}
              />
              <label htmlFor={`rozmiar-${r.id}`} className="form-check-label">
                {r.nazwa} — <strong>{r.cena} zł</strong>
              </label>
            </div>
          ))}
        </fieldset>

        {/* Składniki — checkboxy z limitem */}
        <fieldset className="mb-3">
          <legend className="fs-6 fw-bold">
            Składniki ({wybraneSkladniki.length}/{MAX_SKLADNIKOW}):
            {bledy.skladniki && (
              <span className="text-danger small ms-2">{bledy.skladniki}</span>
            )}
          </legend>
          <div className="row">
            {SKLADNIKI.map((s) => {
              const zaznaczony = wybraneSkladniki.includes(s.id);
              const zablokowany = !zaznaczony && wybraneSkladniki.length >= MAX_SKLADNIKOW;
              return (
                <div key={s.id} className="col-6">
                  <div className="form-check">
                    <input
                      id={`skladnik-${s.id}`}
                      type="checkbox"
                      className="form-check-input"
                      checked={zaznaczony}
                      disabled={zablokowany}
                      onChange={() => handleSkladnik(s.id)}
                    />
                    <label
                      htmlFor={`skladnik-${s.id}`}
                      className={`form-check-label ${zablokowany ? "text-muted" : ""}`}
                    >
                      {s.nazwa} (+{s.cena} zł)
                    </label>
                  </div>
                </div>
              );
            })}
          </div>
        </fieldset>

        {/* Sos — select */}
        <div className="mb-3">
          <label htmlFor="sos" className="form-label fw-bold">Sos do pizzy:</label>
          <select
            id="sos"
            className="form-select"
            value={sos}
            onChange={(e) => setSos(e.target.value)}
          >
            {SOSY.map((s) => (
              <option key={s} value={s}>{s}</option>
            ))}
          </select>
        </div>

        {/* Ostrość — range z emoji */}
        <div className="mb-3">
          <label htmlFor="ostrosc" className="form-label fw-bold">
            Ostrość: {emotikonOstrosci(ostrosc)}
          </label>
          <input
            id="ostrosc"
            type="range"
            className="form-range"
            min="0"
            max="5"
            value={ostrosc}
            onChange={(e) => setOstrosc(Number(e.target.value))}
          />
          <div className="d-flex justify-content-between text-muted small">
            <span>Łagodna</span>
            <span>Piekielna</span>
          </div>
        </div>

        {/* Uwagi — textarea */}
        <div className="mb-4">
          <label htmlFor="uwagi" className="form-label fw-bold">
            Uwagi do zamówienia:
          </label>
          <textarea
            id="uwagi"
            className="form-control"
            rows="2"
            value={uwagi}
            onChange={(e) => setUwagi(e.target.value)}
            placeholder="Np. bez cebuli, pokrojona na 8 kawałków..."
            maxLength={200}
          />
          <small className="text-muted">{uwagi.length}/200 znaków</small>
        </div>

        {/* Przyciski */}
        <div className="d-flex gap-2">
          <button type="submit" className="btn btn-success flex-grow-1 btn-lg">
            🛒 Zamów ({cenaCalkowita.toFixed(2)} zł)
          </button>
          {ostatnie && (
            <button type="button" className="btn btn-outline-primary" onClick={handlePrzywroc}>
              ↺ Ostatnie
            </button>
          )}
        </div>
      </form>
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki w tym wzorcu:**
- **Radio** — wybór jednej opcji (rozmiar) z dynamiczną ceną
- **Checkboxy z limitem** — `disabled` gdy osiągnięto max, wizualne wygaszenie
- **Select** — lista rozwijana (sos)
- **Range z wizualizacją** — suwak ostrości + emoji zależne od wartości
- **Textarea z licznikiem znaków** — `maxLength` + wyświetlanie `uwagi.length`
- **Dynamiczna cena** — obliczana przy każdym renderze (nie w stanie!)
- **localStorage** — zapamiętywanie ostatniego zamówienia
- **Warunkowy render całego widoku** — `if (zamowienie)` zwraca paragon zamiast formularza
- **fieldset + legend** — semantyczne grupowanie pól formularza
- **Sticky element** — pasek ceny przyklejony na górze (`sticky-top`)

---

### 26.16. przelicznik walut

Dwukierunkowy przelicznik walut z dynamiczną tabelą kursów, historią przeliczeń, zamianą walut jednym kliknięciem i wizualnym wskaźnikiem siły waluty.

**Smaczki:** przeliczanie w obie strony (zmiana jednego inputa aktualizuje drugi), przycisk zamiany walut (⇄), historia ostatnich 5 przeliczeń, flagi krajów przy walutach, formatowanie liczb z separatorami tysięcy, podświetlenie waluty mocniejszej/słabszej.

```jsx
// Plik: src/App.js
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

// Kursy walut względem PLN (mockowane — w prawdziwej apce z API)
const WALUTY = [
  { kod: "PLN", nazwa: "Polski złoty", flaga: "🇵🇱", kursDoPlN: 1 },
  { kod: "EUR", nazwa: "Euro", flaga: "🇪🇺", kursDoPlN: 4.32 },
  { kod: "USD", nazwa: "Dolar amerykański", flaga: "🇺🇸", kursDoPlN: 3.95 },
  { kod: "GBP", nazwa: "Funt brytyjski", flaga: "🇬🇧", kursDoPlN: 5.05 },
  { kod: "CHF", nazwa: "Frank szwajcarski", flaga: "🇨🇭", kursDoPlN: 4.48 },
  { kod: "JPY", nazwa: "Jen japoński", flaga: "🇯🇵", kursDoPlN: 0.026 },
  { kod: "CZK", nazwa: "Korona czeska", flaga: "🇨🇿", kursDoPlN: 0.17 },
  { kod: "UAH", nazwa: "Hrywna ukraińska", flaga: "🇺🇦", kursDoPlN: 0.096 },
];

// Funkcja przeliczająca
function przelicz(kwota, walutaZ, walutaDo) {
  if (!kwota || isNaN(kwota)) return "";
  // Najpierw na PLN, potem na walutę docelową
  const wPLN = kwota * walutaZ.kursDoPlN;
  const wynik = wPLN / walutaDo.kursDoPlN;
  return wynik;
}

// Formatowanie kwoty z separatorami
function formatujKwote(liczba, kod) {
  if (liczba === "" || isNaN(liczba)) return "—";
  return new Intl.NumberFormat("pl-PL", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(liczba) + " " + kod;
}

function App() {
  const [kwotaZ, setKwotaZ] = useState("100");
  const [kwotaDo, setKwotaDo] = useState("");
  const [walutaZId, setWalutaZId] = useState("PLN");
  const [walutaDoId, setWalutaDoId] = useState("EUR");
  const [historia, setHistoria] = useState([]);
  const [ostatniaEdycja, setOstatniaEdycja] = useState("z"); // "z" lub "do"

  const walutaZ = WALUTY.find((w) => w.kod === walutaZId);
  const walutaDo = WALUTY.find((w) => w.kod === walutaDoId);

  // Kurs wymiany między wybranymi walutami
  const kursWymiany = walutaZ.kursDoPlN / walutaDo.kursDoPlN;
  const kursOdwrotny = walutaDo.kursDoPlN / walutaZ.kursDoPlN;

  // Przeliczenie przy zmianie kwoty "z"
  function handleKwotaZ(e) {
    const val = e.target.value;
    setKwotaZ(val);
    setOstatniaEdycja("z");
    if (val === "" || isNaN(val)) {
      setKwotaDo("");
    } else {
      setKwotaDo(przelicz(Number(val), walutaZ, walutaDo).toFixed(2));
    }
  }

  // Przeliczenie przy zmianie kwoty "do" (dwukierunkowe!)
  function handleKwotaDo(e) {
    const val = e.target.value;
    setKwotaDo(val);
    setOstatniaEdycja("do");
    if (val === "" || isNaN(val)) {
      setKwotaZ("");
    } else {
      setKwotaZ(przelicz(Number(val), walutaDo, walutaZ).toFixed(2));
    }
  }

  // Zmiana waluty źródłowej — przelicz ponownie
  function handleZmianaWalutyZ(e) {
    const nowaWaluta = WALUTY.find((w) => w.kod === e.target.value);
    setWalutaZId(e.target.value);
    if (kwotaZ && !isNaN(kwotaZ)) {
      setKwotaDo(przelicz(Number(kwotaZ), nowaWaluta, walutaDo).toFixed(2));
    }
  }

  // Zmiana waluty docelowej — przelicz ponownie
  function handleZmianaWalutyDo(e) {
    const nowaWaluta = WALUTY.find((w) => w.kod === e.target.value);
    setWalutaDoId(e.target.value);
    if (kwotaZ && !isNaN(kwotaZ)) {
      setKwotaDo(przelicz(Number(kwotaZ), walutaZ, nowaWaluta).toFixed(2));
    }
  }

  // Zamiana walut (⇄)
  function handleZamien() {
    setWalutaZId(walutaDoId);
    setWalutaDoId(walutaZId);
    setKwotaZ(kwotaDo);
    setKwotaDo(kwotaZ);
  }

  // Zapisanie do historii
  function handleZapisz() {
    if (!kwotaZ || isNaN(kwotaZ) || Number(kwotaZ) === 0) return;
    const wpis = {
      id: Date.now(),
      z: `${formatujKwote(Number(kwotaZ), walutaZId)}`,
      do: `${formatujKwote(Number(kwotaDo), walutaDoId)}`,
      kurs: kursWymiany.toFixed(4),
      czas: new Date().toLocaleTimeString("pl-PL"),
    };
    setHistoria((prev) => [wpis, ...prev].slice(0, 5)); // Max 5 wpisów
  }

  return (
    <main className="container mt-4" style={{ maxWidth: "600px" }}>
      <h1 className="text-center mb-4">💱 Przelicznik Walut</h1>

      {/* Kurs wymiany */}
      <div className="alert alert-info text-center py-2">
        <span>{walutaZ.flaga} 1 {walutaZId}</span>
        <strong className="mx-2">=</strong>
        <span>{walutaDo.flaga} {kursWymiany.toFixed(4)} {walutaDoId}</span>
      </div>

      {/* Formularz przeliczania */}
      <div className="card shadow-sm mb-4">
        <div className="card-body">

          {/* Waluta źródłowa */}
          <div className="row align-items-end mb-3">
            <div className="col-7">
              <label htmlFor="kwotaZ" className="form-label small text-muted">Mam:</label>
              <input
                id="kwotaZ"
                type="number"
                className="form-control form-control-lg"
                value={kwotaZ}
                onChange={handleKwotaZ}
                placeholder="0.00"
                min="0"
                step="0.01"
              />
            </div>
            <div className="col-5">
              <select
                className="form-select form-select-lg"
                value={walutaZId}
                onChange={handleZmianaWalutyZ}
              >
                {WALUTY.map((w) => (
                  <option key={w.kod} value={w.kod}>
                    {w.flaga} {w.kod}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Przycisk zamiany */}
          <div className="text-center mb-3">
            <button
              type="button"
              className="btn btn-outline-secondary btn-sm rounded-circle"
              onClick={handleZamien}
              title="Zamień waluty"
              style={{ width: "40px", height: "40px", fontSize: "1.2rem" }}
            >
              ⇄
            </button>
          </div>

          {/* Waluta docelowa */}
          <div className="row align-items-end mb-3">
            <div className="col-7">
              <label htmlFor="kwotaDo" className="form-label small text-muted">Otrzymam:</label>
              <input
                id="kwotaDo"
                type="number"
                className="form-control form-control-lg"
                value={kwotaDo}
                onChange={handleKwotaDo}
                placeholder="0.00"
                min="0"
                step="0.01"
              />
            </div>
            <div className="col-5">
              <select
                className="form-select form-select-lg"
                value={walutaDoId}
                onChange={handleZmianaWalutyDo}
              >
                {WALUTY.map((w) => (
                  <option key={w.kod} value={w.kod}>
                    {w.flaga} {w.kod}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Przycisk zapisu */}
          <button
            type="button"
            className="btn btn-primary w-100"
            onClick={handleZapisz}
            disabled={!kwotaZ || isNaN(kwotaZ) || Number(kwotaZ) === 0}
          >
            📋 Zapisz przeliczenie
          </button>
        </div>
      </div>

      {/* Tabela kursów */}
      <details className="mb-4">
        <summary className="fw-bold mb-2" style={{ cursor: "pointer" }}>
          📊 Tabela kursów (względem PLN)
        </summary>
        <table className="table table-sm table-striped">
          <thead className="table-dark">
            <tr>
              <th>Waluta</th>
              <th className="text-end">Kurs (1 = X PLN)</th>
              <th className="text-end">Siła</th>
            </tr>
          </thead>
          <tbody>
            {WALUTY.filter((w) => w.kod !== "PLN")
              .sort((a, b) => b.kursDoPlN - a.kursDoPlN)
              .map((w) => (
                <tr key={w.kod}>
                  <td>{w.flaga} {w.kod} — {w.nazwa}</td>
                  <td className="text-end">{w.kursDoPlN.toFixed(3)}</td>
                  <td className="text-end">
                    {w.kursDoPlN > 4 ? (
                      <span className="badge bg-success">Mocna</span>
                    ) : w.kursDoPlN > 1 ? (
                      <span className="badge bg-warning text-dark">Średnia</span>
                    ) : (
                      <span className="badge bg-secondary">Słaba</span>
                    )}
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </details>

      {/* Historia przeliczeń */}
      {historia.length > 0 && (
        <div className="card">
          <div className="card-header d-flex justify-content-between align-items-center">
            <span className="fw-bold">📜 Historia ({historia.length}/5)</span>
            <button
              className="btn btn-sm btn-outline-danger"
              onClick={() => setHistoria([])}
            >
              Wyczyść
            </button>
          </div>
          <ul className="list-group list-group-flush">
            {historia.map((h) => (
              <li key={h.id} className="list-group-item d-flex justify-content-between">
                <span>{h.z} → {h.do}</span>
                <small className="text-muted">{h.czas}</small>
              </li>
            ))}
          </ul>
        </div>
      )}
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki w tym wzorcu:**
- **Dwukierunkowe przeliczanie** — zmiana jednego inputa aktualizuje drugi (i odwrotnie)
- **Dynamiczny przelicznik** — zmiana waluty w select natychmiast przelicza kwotę
- **Zamiana walut (⇄)** — jednym kliknięciem zamienia źródło z celem
- **Historia z limitem** — `slice(0, 5)` ogranicza do 5 ostatnich wpisów
- **Intl.NumberFormat** — profesjonalne formatowanie liczb z separatorami
- **`<details>` / `<summary>`** — natywny HTML do rozwijania tabeli kursów (bez stanu!)
- **Warunkowe badge** — zagnieżdżony ternary do wyświetlania siły waluty
- **Disabled button** — przycisk nieaktywny gdy brak danych
- **Obliczenia poza stanem** — `kursWymiany` obliczany przy renderze, nie trzymany w useState

---

### 26.17. galeria zdjęć z lightboxem i ulubionymi

Interaktywna galeria zdjęć z filtrowaniem po kategoriach, powiększaniem w lightboxie (modal), nawigacją strzałkami ←/→, oznaczaniem ulubionych (serduszko), licznikiem wyświetleń i trybem siatki/listy.

**Smaczki:** lightbox z nawigacją klawiaturą (← → Esc), animowane serduszko ulubionych, przełącznik widoku siatka/lista, sortowanie po wyświetleniach/nazwie, licznik wyświetleń zwiększany przy otwarciu lightboxa, filtr "Tylko ulubione".

```jsx
// Plik: src/App.js
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";

// Dane galerii — w prawdziwej apce z API lub JSON
// Obrazy z folderu public/galeria/
const ZDJECIA_POCZATKOWE = [
  { id: 1, plik: "krajobraz1.jpg", tytul: "Górski poranek", kategoria: "Krajobrazy", wyswietlenia: 0, ulubione: false },
  { id: 2, plik: "miasto1.jpg", tytul: "Nocne miasto", kategoria: "Miasto", wyswietlenia: 0, ulubione: false },
  { id: 3, plik: "krajobraz2.jpg", tytul: "Jezioro o świcie", kategoria: "Krajobrazy", wyswietlenia: 0, ulubione: false },
  { id: 4, plik: "zwierze1.jpg", tytul: "Lis w lesie", kategoria: "Zwierzęta", wyswietlenia: 0, ulubione: false },
  { id: 5, plik: "miasto2.jpg", tytul: "Most o zachodzie", kategoria: "Miasto", wyswietlenia: 0, ulubione: false },
  { id: 6, plik: "zwierze2.jpg", tytul: "Sowa na gałęzi", kategoria: "Zwierzęta", wyswietlenia: 0, ulubione: false },
  { id: 7, plik: "krajobraz3.jpg", tytul: "Polna droga", kategoria: "Krajobrazy", wyswietlenia: 0, ulubione: false },
  { id: 8, plik: "miasto3.jpg", tytul: "Stare kamienice", kategoria: "Miasto", wyswietlenia: 0, ulubione: false },
  { id: 9, plik: "zwierze3.jpg", tytul: "Motyl na kwiatku", kategoria: "Zwierzęta", wyswietlenia: 0, ulubione: false },
];

function App() {
  const [zdjecia, setZdjecia] = useState(ZDJECIA_POCZATKOWE);
  const [filtrKategoria, setFiltrKategoria] = useState("Wszystkie");
  const [tylkoUlubione, setTylkoUlubione] = useState(false);
  const [sortowanie, setSortowanie] = useState("nazwa");
  const [widok, setWidok] = useState("siatka"); // "siatka" lub "lista"
  const [lightboxId, setLightboxId] = useState(null); // ID otwartego zdjęcia (null = zamknięty)

  // Wyciągnięcie unikalnych kategorii
  const kategorie = ["Wszystkie", ...new Set(zdjecia.map((z) => z.kategoria))];

  // Filtrowanie i sortowanie
  let przefiltrowane = zdjecia;

  if (filtrKategoria !== "Wszystkie") {
    przefiltrowane = przefiltrowane.filter((z) => z.kategoria === filtrKategoria);
  }
  if (tylkoUlubione) {
    przefiltrowane = przefiltrowane.filter((z) => z.ulubione);
  }

  // Sortowanie
  przefiltrowane = [...przefiltrowane].sort((a, b) => {
    if (sortowanie === "nazwa") return a.tytul.localeCompare(b.tytul);
    if (sortowanie === "wyswietlenia") return b.wyswietlenia - a.wyswietlenia;
    return 0;
  });

  // Lightbox — aktualne zdjęcie
  const lightboxZdjecie = zdjecia.find((z) => z.id === lightboxId);
  // Indeks w przefiltrowanej liście (do nawigacji ←/→)
  const lightboxIndex = przefiltrowane.findIndex((z) => z.id === lightboxId);

  // Otwarcie lightboxa — zwiększa wyświetlenia
  function otworzLightbox(id) {
    setLightboxId(id);
    setZdjecia((prev) =>
      prev.map((z) => (z.id === id ? { ...z, wyswietlenia: z.wyswietlenia + 1 } : z))
    );
  }

  // Nawigacja w lightboxie
  function nastepne() {
    if (lightboxIndex < przefiltrowane.length - 1) {
      const noweId = przefiltrowane[lightboxIndex + 1].id;
      otworzLightbox(noweId);
    }
  }

  function poprzednie() {
    if (lightboxIndex > 0) {
      const noweId = przefiltrowane[lightboxIndex - 1].id;
      otworzLightbox(noweId);
    }
  }

  function zamknijLightbox() {
    setLightboxId(null);
  }

  // Obsługa klawiatury w lightboxie
  useEffect(() => {
    if (lightboxId === null) return;

    function handleKey(e) {
      if (e.key === "Escape") zamknijLightbox();
      if (e.key === "ArrowRight") nastepne();
      if (e.key === "ArrowLeft") poprzednie();
    }

    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  });

  // Toggle ulubione
  function toggleUlubione(id, e) {
    e.stopPropagation(); // Nie otwieraj lightboxa przy kliknięciu serduszka
    setZdjecia((prev) =>
      prev.map((z) => (z.id === id ? { ...z, ulubione: !z.ulubione } : z))
    );
  }

  // Liczba ulubionych
  const liczbaUlubionych = zdjecia.filter((z) => z.ulubione).length;

  return (
    <main className="container mt-4">
      <h1 className="text-center mb-4">📸 Galeria Zdjęć</h1>

      {/* Panel filtrów */}
      <div className="row mb-4 g-2 align-items-center">
        {/* Kategoria */}
        <div className="col-md-3">
          <select
            className="form-select"
            value={filtrKategoria}
            onChange={(e) => setFiltrKategoria(e.target.value)}
          >
            {kategorie.map((k) => (
              <option key={k} value={k}>{k}</option>
            ))}
          </select>
        </div>

        {/* Sortowanie */}
        <div className="col-md-3">
          <select
            className="form-select"
            value={sortowanie}
            onChange={(e) => setSortowanie(e.target.value)}
          >
            <option value="nazwa">Sortuj: A-Z</option>
            <option value="wyswietlenia">Sortuj: Popularne</option>
          </select>
        </div>

        {/* Tylko ulubione */}
        <div className="col-md-3">
          <div className="form-check form-switch">
            <input
              id="ulubione-filtr"
              type="checkbox"
              className="form-check-input"
              checked={tylkoUlubione}
              onChange={(e) => setTylkoUlubione(e.target.checked)}
            />
            <label htmlFor="ulubione-filtr" className="form-check-label">
              ❤️ Ulubione ({liczbaUlubionych})
            </label>
          </div>
        </div>

        {/* Przełącznik widoku */}
        <div className="col-md-3 text-end">
          <div className="btn-group" role="group">
            <button
              className={`btn btn-sm ${widok === "siatka" ? "btn-primary" : "btn-outline-primary"}`}
              onClick={() => setWidok("siatka")}
            >
              ▦ Siatka
            </button>
            <button
              className={`btn btn-sm ${widok === "lista" ? "btn-primary" : "btn-outline-primary"}`}
              onClick={() => setWidok("lista")}
            >
              ☰ Lista
            </button>
          </div>
        </div>
      </div>

      {/* Licznik wyników */}
      <p className="text-muted small">
        Wyświetlanie: {przefiltrowane.length} z {zdjecia.length} zdjęć
      </p>

      {/* Widok SIATKA */}
      {widok === "siatka" && (
        <div className="row">
          {przefiltrowane.map((z) => (
            <div key={z.id} className="col-6 col-md-4 mb-4">
              <div
                className="card h-100 shadow-sm"
                style={{ cursor: "pointer" }}
                onClick={() => otworzLightbox(z.id)}
              >
                {/* Obraz — w prawdziwej apce: src={`/galeria/${z.plik}`} */}
                <div
                  className="card-img-top bg-secondary d-flex align-items-center justify-content-center text-white"
                  style={{ height: "180px", fontSize: "0.8rem" }}
                >
                  📷 {z.plik}
                </div>
                <div className="card-body p-2">
                  <div className="d-flex justify-content-between align-items-start">
                    <div>
                      <h6 className="card-title mb-1">{z.tytul}</h6>
                      <small className="text-muted">
                        <span className="badge bg-light text-dark me-1">{z.kategoria}</span>
                        👁 {z.wyswietlenia}
                      </small>
                    </div>
                    {/* Przycisk ulubione */}
                    <button
                      className="btn btn-sm p-0 border-0"
                      onClick={(e) => toggleUlubione(z.id, e)}
                      style={{ fontSize: "1.3rem" }}
                    >
                      {z.ulubione ? "❤️" : "🤍"}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Widok LISTA */}
      {widok === "lista" && (
        <div className="list-group">
          {przefiltrowane.map((z) => (
            <div
              key={z.id}
              className="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
              onClick={() => otworzLightbox(z.id)}
              style={{ cursor: "pointer" }}
            >
              <div className="d-flex align-items-center gap-3">
                <div
                  className="bg-secondary rounded d-flex align-items-center justify-content-center text-white"
                  style={{ width: "60px", height: "60px", fontSize: "0.6rem" }}
                >
                  📷
                </div>
                <div>
                  <h6 className="mb-0">{z.tytul}</h6>
                  <small className="text-muted">{z.kategoria} • 👁 {z.wyswietlenia}</small>
                </div>
              </div>
              <button
                className="btn btn-sm p-0 border-0"
                onClick={(e) => toggleUlubione(z.id, e)}
                style={{ fontSize: "1.3rem" }}
              >
                {z.ulubione ? "❤️" : "🤍"}
              </button>
            </div>
          ))}
        </div>
      )}

      {/* Brak wyników */}
      {przefiltrowane.length === 0 && (
        <div className="text-center text-muted py-5">
          <p className="fs-1">🔍</p>
          <p>Brak zdjęć spełniających kryteria.</p>
        </div>
      )}

      {/* LIGHTBOX (Modal) */}
      {lightboxId !== null && lightboxZdjecie && (
        <div
          className="position-fixed top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center"
          style={{ backgroundColor: "rgba(0,0,0,0.9)", zIndex: 9999 }}
          onClick={zamknijLightbox}
        >
          {/* Zawartość lightboxa — kliknięcie nie zamyka */}
          <div
            className="text-center text-white p-4"
            style={{ maxWidth: "90vw", maxHeight: "90vh" }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Przycisk zamknięcia */}
            <button
              className="btn btn-outline-light position-absolute top-0 end-0 m-3"
              onClick={zamknijLightbox}
            >
              ✕
            </button>

            {/* Obraz powiększony */}
            <div
              className="bg-dark border border-secondary rounded d-flex align-items-center justify-content-center mx-auto mb-3"
              style={{ width: "70vw", height: "60vh", fontSize: "1.5rem" }}
            >
              📷 {lightboxZdjecie.plik}
              {/* W prawdziwej apce: <img src={`/galeria/${lightboxZdjecie.plik}`} ... /> */}
            </div>

            {/* Info */}
            <h4>{lightboxZdjecie.tytul}</h4>
            <p className="text-muted">
              {lightboxZdjecie.kategoria} • 👁 {lightboxZdjecie.wyswietlenia} wyświetleń
              <button
                className="btn btn-sm border-0 ms-2"
                onClick={() => toggleUlubione(lightboxZdjecie.id, { stopPropagation: () => {} })}
                style={{ fontSize: "1.3rem" }}
              >
                {lightboxZdjecie.ulubione ? "❤️" : "🤍"}
              </button>
            </p>

            {/* Nawigacja ←/→ */}
            <div className="d-flex justify-content-between mt-3" style={{ width: "70vw", margin: "0 auto" }}>
              <button
                className="btn btn-outline-light btn-lg"
                onClick={poprzednie}
                disabled={lightboxIndex <= 0}
              >
                ← Poprzednie
              </button>
              <span className="align-self-center">
                {lightboxIndex + 1} / {przefiltrowane.length}
              </span>
              <button
                className="btn btn-outline-light btn-lg"
                onClick={nastepne}
                disabled={lightboxIndex >= przefiltrowane.length - 1}
              >
                Następne →
              </button>
            </div>

            <p className="text-muted small mt-3">
              Nawigacja: ← → strzałki | Esc = zamknij
            </p>
          </div>
        </div>
      )}
    </main>
  );
}

export default App;
```

**Kluczowe mechaniki w tym wzorcu:**
- **Lightbox (modal)** — pełnoekranowy overlay z `position: fixed`, zamykany kliknięciem tła lub Esc
- **Nawigacja klawiaturą** — `useEffect` z `addEventListener("keydown")` + cleanup
- **`e.stopPropagation()`** — kliknięcie serduszka nie otwiera lightboxa, kliknięcie zdjęcia w modalu nie zamyka go
- **Przełącznik widoku** — `widok === "siatka"` vs `widok === "lista"` renderuje zupełnie inny layout
- **Filtrowanie + sortowanie + ulubione** — trzy niezależne filtry działające razem
- **Licznik wyświetleń** — zwiększany przy otwarciu lightboxa (`otworzLightbox`)
- **Toggle ulubione** — `map` z odwróceniem booleana dla jednego elementu
- **`new Set`** — wyciąganie unikalnych kategorii z danych
- **Nawigacja w lightboxie** — `findIndex` w przefiltrowanej liście do ←/→
- **Disabled buttons** — strzałki nieaktywne na krańcach listy
- **Responsywna siatka** — `col-6 col-md-4` (2 kolumny na telefonie, 3 na desktopie)
- **Placeholder zamiast obrazów** — div z emoji symulujący obraz (w prawdziwej apce zamień na `<img>`)
