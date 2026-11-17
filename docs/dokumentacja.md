# Dokumentacja projektu

## Cel

Projekt klasyfikuje anglojęzyczne zgłoszenia klientów banku do jednej z 35 wybranych intencji Banking77. Ma wspierać wstępną segregację wiadomości przez pracowników obsługi klienta.

## Dane

Źródłem danych jest publiczny zbiór [Banking77](https://huggingface.co/datasets/PolyAI/banking77), zawierający zgłoszenia klientów i etykiety intencji. Projekt obejmuje kategorie związane z kartami, płatnościami i wypłatami, przelewami oraz doładowaniami. Pełna lista wybranych intencji znajduje się w [zakresie intencji](zakres-intencji.md).

Oryginalny podział na train i test jest zachowany. Pełne pliki źródłowe znajdują się w `data/raw/`, a przefiltrowane zbiory z czytelnymi nazwami etykiet w `data/processed/`:

- treningowy: 5 160 przykładów,
- testowy: 1 400 przykładów, po 40 na każdą intencję.

## Przygotowanie danych

Skrypt `src/prepare_data.py` korzysta z istniejących plików źródłowych, a gdy ich brakuje, pobiera Banking77. Następnie osobno filtruje oryginalne zbiory treningowy i testowy według listy w `src/selected_intents.py`. W kolumnie `label` zapisuje nazwę intencji zamiast liczbowego identyfikatora. Dane nie są ponownie losowo dzielone.

Uruchomienie:

```bash
python src/prepare_data.py
```

## Model i ocena

Klasyfikator jest pipeline'em scikit-learn z `TfidfVectorizer` oraz `LogisticRegression(max_iter=1000)`. Trening odbywa się na `data/processed/banking77_train.csv`; jako niezależny zbiór testowy służy `data/processed/banking77_test.csv`.

Skrypt `src/train_model.py` wypisuje accuracy, macro F1 i raport klasyfikacji. Porównuje także model z prostym baseline'em regułowym, który dopasowuje frazy do intencji, a przy braku dopasowania wybiera najczęstszą etykietę ze zbioru treningowego.

Kryterium sukcesu z karty tematu to macro F1 co najmniej 0,80. Wyniki modelu i baseline'u należy uzupełnić po uruchomieniu oceny; nie zostały jeszcze zmierzone.

```bash
python src/train_model.py
```

Ten skrypt zapisuje oceniony pipeline do `models/banking77_model.joblib`. Aplikacja Streamlit używa zapisanego modelu.

## Aplikacja

Uruchom interfejs poleceniem:

```bash
streamlit run src/app.py
```

Użytkownik wpisuje treść zgłoszenia po angielsku. Aplikacja wyświetla przewidywaną kategorię po polsku. Jeśli zapisany model nie zwraca etykiet z aktualnego zestawu 35 intencji, aplikacja prosi o ponowny trening.

## Wyniki

| Metoda | Accuracy | Macro F1 |
|---|---:|---:|
| TF-IDF + Logistic Regression | do uzupełnienia po ocenie | do uzupełnienia po ocenie |
| Baseline słów kluczowych | do uzupełnienia po ocenie | do uzupełnienia po ocenie |