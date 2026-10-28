from pathlib import Path
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def main():
    project_dir = Path(__file__).resolve().parent.parent
    data_dir = project_dir / "data" / "raw"
    models_dir = project_dir / "models"

    train_df = pd.read_csv(data_dir / "banking77_train.csv")

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    print("Trenowanie modelu...", flush=True)
    model.fit(train_df["text"], train_df["label"])

    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "banking77_model.joblib"

    joblib.dump(model, model_path)

    print(f"Model zapisano w: {model_path}", flush=True)


if __name__ == "__main__":
    main()
