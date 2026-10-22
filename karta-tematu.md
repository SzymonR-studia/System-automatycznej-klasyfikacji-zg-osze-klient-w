# Karta zgłoszenia tematu projektu

**Grupa:** L2 · **Zespół:** Z7 · **Data:** 2026-10-17
Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027
Oddajecie mailem do **22.10, 16:45**, temat `SI L2 · Z<nr zespołu> · karta`.

## 1\. Skład zespołu

> Rola jest wstępna — można ją zmienić w trakcie projektu bez uzgadniania.

|Imię i nazwisko|Nr albumu|Rola (wstępna)|
|-|-|-|
|Weronika Brandkiewicz|31062|implementacja i trenowanie modelu SI|
|Szymon Ratajczak|31081|przygotowanie danych i rozwój modelu SI|
|Milena Mazurek|31837|testowanie i ocena skuteczności modelu SI|

## 2\. Roboczy tytuł (PL)

System automatycznej klasyfikacji zgłoszeń klientów

## 3\. Tytuł (EN)

Automated customer ticket classification system

## 4\. Problem — co system ma robić i dla kogo (3–5 zdań)

Firmy otrzymują dużą liczbę wiadomości od klientów dotyczących problemów z płatnościami, dostawami, kontami i produktami. Ręczne przypisywanie wiadomości do odpowiednich kategorii jest czasochłonne i może prowadzić do błędów. Celem projektu jest stworzenie aplikacji, która automatycznie przypisuje zgłoszenie do odpowiedniej kategorii na podstawie jego treści. System będzie przeznaczony dla pracowników obsługi klienta i ma ułatwić wstępną segregację zgłoszeń. Użytkownik będzie mógł wpisać treść wiadomości i otrzymać przewidywaną kategorię.

## 5\. Dlaczego SI i dlaczego ta technologia

**a) Dlaczego zwykły algorytm nie wystarczy.** Zaznaczcie jeden powód:

* \[ ] nie umiemy zapisać reguły krok po kroku
* \[ ] przepis istnieje, ale jest obliczeniowo za drogi
* \[x] reguł jest za dużo i zmieniają się w czasie

Uzasadnienie (2–3 zdania):

Wiadomości od klientów mogą być formułowane na wiele różnych sposobów, nawet jeśli dotyczą tego samego problemu. Ręczne tworzenie i aktualizowanie reguł opartych na słowach kluczowych byłoby czasochłonne i nie zawsze skuteczne.



**b) Technologia SI:**

* \[ ] sieć neuronowa
* \[ ] system ekspertowy / wnioskowanie regułowe
* \[ ] algorytm genetyczny
* \[x] klasyczne uczenie maszynowe



Dlaczego ta technologia pasuje do tego problemu (2–3 zdania):

Klasyczne uczenie maszynowe umożliwia automatyczną klasyfikację tekstu na podstawie przykładów oznaczonych odpowiednimi kategoriami. W projekcie wykorzystamy reprezentację tekstu TF-IDF oraz algorytm Logistic Regression. W przeciwieństwie do prostego wyszukiwania słów kluczowych model będzie uczył się zależności między treścią wiadomości a jej kategorią.



## 6\. Dane

* Źródło: publiczny zbiór Banking77 dostępny na platformie Hugging Face, zawierający anglojęzyczne zapytania klientów dotyczące usług bankowych.
* Rozmiar / format: zbiór zawiera 13 083 przykłady tekstowe z etykietami intencji; dane są dostępne w formacie możliwym do przetwarzania w Pythonie.
* Czy dane są już dostępne? tak / nie — plan pozyskania: Tak. Plan zakłada pobranie zbioru, wybranie ograniczonej liczby kategorii, przygotowanie danych i podział ich na zbiór treningowy oraz testowy.

## 7\. Stos technologiczny

* Python
* pandas — przetwarzanie danych
* scikit-learn — TF-IDF, Logistic Regression i ocena modelu
* Streamlit — prosty interfejs aplikacji
* Git i GitHub — kontrola wersji i współpraca zespołowa

## 8\. Kryterium sukcesu

* Metryka i próg: osiągnięcie macro F1-score na poziomie co najmniej 0,80 na niezależnym zbiorze testowym.
* Punkt odniesienia (prosta metoda, z którą porównacie wynik): porównanie wyniku modelu z prostą metodą klasyfikacji opartą na regułach i słowach kluczowych.

## 9\. Zakres minimalny (co powstanie na pewno)

* Przygotowanie i analiza zbioru danych.
* Implementacja klasyfikatora tekstu z wykorzystaniem TF-IDF i Logistic Regression.
* Podział danych na zbiór treningowy i testowy.
* Ocena jakości modelu przy użyciu macro F1-score i accuracy.
* Prosta aplikacja umożliwiająca wpisanie wiadomości i wyświetlenie przewidywanej kategorii.
* Dokumentacja w języku polskim oraz README i streszczenie techniczne w języku angielskim.

## 10\. Zakres opcjonalny (co dorobimy, jeśli starczy czasu)

* Porównanie kilku algorytmów klasyfikacji, np. Logistic Regression i Naive Bayes.
* Wyświetlanie prawdopodobieństwa przynależności do poszczególnych kategorii.
* Dodanie kolejnych kategorii zgłoszeń.
* Pomiar czasu klasyfikacji pojedynczej wiadomości.

## 11\. Repozytorium

[https://github.com/SzymonR-studia/System-automatycznej-klasyfikacji-zg-osze-klient-w](https://github.com/SzymonR-studia/System-automatycznej-klasyfikacji-zg-osze-klient-w)

## 12\. Główne ryzyko i plan awaryjny

**Ryzyko**: model może nie osiągnąć zakładanego wyniku jakości lub przygotowanie danych może zająć więcej czasu, niż przewidziano.

**Plan awaryjny**: ograniczymy liczbę kategorii do kilku najczęstszych, uprościmy przetwarzanie tekstu i porównamy różne klasyczne algorytmy uczenia maszynowego.

\---

*Decyzja prowadzącego:* \[ ] zatwierdzony  \[ ] do poprawy · *Uwagi:*

