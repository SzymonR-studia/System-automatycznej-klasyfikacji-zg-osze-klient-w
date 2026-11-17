from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, f1_score


def main():
    # Ścieżki do danych
    project_dir = Path(__file__).resolve().parent.parent
    data_dir = project_dir / "data" / "processed"

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
    macro_f1 = f1_score(y_test, predictions, average="macro")
    target_macro_f1 = 0.80

    print(f"\nAccuracy: {accuracy:.4f}", flush=True)
    print(
        f"Macro F1: {macro_f1:.4f} "
        f"(cel: co najmniej {target_macro_f1:.2f})",
        flush=True,
    )
    if macro_f1 >= target_macro_f1:
        print("Osiągnięto założony próg macro F1.", flush=True)
    else:
        print("Nie osiągnięto założonego progu macro F1.", flush=True)

    print("\nRaport klasyfikacji:", flush=True)
    print(classification_report(y_test, predictions), flush=True)

    # Zapisujemy dokładnie ten model, który został oceniony powyżej.
    models_dir = project_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "banking77_model.joblib"
    joblib.dump(model, model_path)
    print(f"\nModel zapisano w: {model_path}", flush=True)


if __name__ == "__main__":
    main()