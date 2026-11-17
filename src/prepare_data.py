import csv
from pathlib import Path

from selected_intents import SELECTED_INTENTS


def download_raw_data(raw_dir: Path) -> None:
    """Download Banking77 only when the original split files are missing."""
    split_names = ("train", "test")
    raw_paths = [raw_dir / f"banking77_{name}.csv" for name in split_names]
    if all(path.exists() for path in raw_paths):
        return

    from datasets import load_dataset

    print("Pobieranie zbioru Banking77...", flush=True)
    dataset = load_dataset("PolyAI/banking77")
    raw_dir.mkdir(parents=True, exist_ok=True)

    for split_name in split_names:
        split = dataset[split_name]
        output_path = raw_dir / f"banking77_{split_name}.csv"
        with output_path.open("w", newline="", encoding="utf-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=("text", "label"))
            writer.writeheader()
            writer.writerows(
                {"text": row["text"], "label": row["label"]} for row in split
            )
        print(
            f"{split_name}: zapisano {len(split)} oryginalnych zgłoszeń do {output_path}",
            flush=True,
        )


def filter_split(source_path: Path, output_path: Path, split_name: str) -> int:
    selected_counts = {intent: 0 for intent in SELECTED_INTENTS.values()}

    with source_path.open("r", newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)
        if not reader.fieldnames or not {"text", "label"}.issubset(reader.fieldnames):
            raise ValueError(
                f"Plik {source_path} musi zawierać kolumny 'text' i 'label'."
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=("text", "label"))
            writer.writeheader()

            for row in reader:
                try:
                    label_id = int(row["label"])
                except (TypeError, ValueError) as exc:
                    raise ValueError(
                        f"Nieprawidłowa etykieta w pliku {source_path}: {row['label']!r}"
                    ) from exc

                intent = SELECTED_INTENTS.get(label_id)
                if intent is None:
                    continue

                writer.writerow({"text": row["text"], "label": intent})
                selected_counts[intent] += 1

    missing_intents = [intent for intent, count in selected_counts.items() if count == 0]
    if missing_intents:
        output_path.unlink(missing_ok=True)
        raise ValueError(
            f"W zbiorze {split_name} brakuje wybranych intencji: "
            f"{', '.join(missing_intents)}"
        )

    return sum(selected_counts.values())


def main():
    project_dir = Path(__file__).resolve().parent.parent
    raw_dir = project_dir / "data" / "raw"
    processed_dir = project_dir / "data" / "processed"

    download_raw_data(raw_dir)
    processed_dir.mkdir(parents=True, exist_ok=True)

    for split_name in ("train", "test"):
        source_path = raw_dir / f"banking77_{split_name}.csv"
        processed_path = processed_dir / f"banking77_{split_name}.csv"

        row_count = filter_split(source_path, processed_path, split_name)

        print(
            f"{split_name}: zapisano {row_count} zgłoszeń "
            f"z {len(SELECTED_INTENTS)} intencjami do {processed_path}",
            flush=True,
        )

    print("Gotowe! Oryginalne podziały train/test zostały zachowane.", flush=True)


if __name__ == "__main__":
    main()
