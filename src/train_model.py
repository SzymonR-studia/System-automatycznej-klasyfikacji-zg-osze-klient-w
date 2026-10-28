from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


def main():
    # Ścieżki do danych
    project_dir = Path(__file__).resolve().parent.parent
    data_dir = project_dir / "data" / "raw"

    train_path = data_dir / "banking77_train.csv"
    test_path = data_dir / "banking77_test.csv"

    # Wczytanie danych
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    print("Liczba danych treningowych:", len(train_df), flush=True)
    print("Liczba danych testowych:", len(test_df), flush=True)

    # Przygotowanie tekstów i etykiet
    X_train = train_df["text"]
    y_train = train_df["label"]

    X_test = test_df["text"]
    y_test = test_df["label"]

    # Utworzenie modelu
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    # Trenowanie
    print("Trenowanie modelu...", flush=True)
    model.fit(X_train, y_train)

    # Ocena na danych testowych
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"\nAccuracy: {accuracy:.4f}", flush=True)
    print("\nRaport klasyfikacji:", flush=True)
    print(classification_report(y_test, predictions), flush=True)


if __name__ == "__main__":
    main()
