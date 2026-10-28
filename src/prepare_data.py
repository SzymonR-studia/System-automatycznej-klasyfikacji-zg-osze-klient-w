from datasets import load_dataset
from pathlib import Path
import pandas as pd


def main():
    print("Pobieranie zbioru Banking77...", flush=True)

    dataset = load_dataset("PolyAI/banking77")

    output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    for split_name in ("train", "test"):
        df = dataset[split_name].to_pandas()
        output_path = output_dir / f"banking77_{split_name}.csv"
        df.to_csv(output_path, index=False)
        print(
            f"{split_name}: zapisano {len(df)} zgłoszeń do {output_path}",
            flush=True,
        )

    print("Gotowe!", flush=True)


if __name__ == "__main__":
    main()
