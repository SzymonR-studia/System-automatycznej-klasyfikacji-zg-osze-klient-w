# Automated Customer Ticket Classification

This project classifies English-language banking support messages into 35 selected intents from the public [Banking77 dataset](https://huggingface.co/datasets/PolyAI/banking77). It is intended to support the initial routing of customer tickets.

The selected intents cover card access and delivery, card payments and cash withdrawals, bank transfers, and account top-ups. The original Banking77 train/test split is preserved. The filtered data contains 5,160 training examples and 1,400 test examples, with 40 test examples per intent.

## Requirements

- Python 3.12
- Packages listed in `requirements.txt`

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the packages:

```bash
python -m pip install -r requirements.txt
```

## Prepare the data

Run:

```bash
python src/prepare_data.py
```

The script uses the full CSV files in `data/raw/` when they are present. If either source split is missing, it downloads Banking77. It filters the original train and test splits independently and writes the selected examples with readable intent names to:

- `data/processed/banking77_train.csv`
- `data/processed/banking77_test.csv`

The original files in `data/raw/` are kept unchanged.

## Train and evaluate

Run:

```bash
python src/train_model.py
```

The script trains a TF-IDF and Logistic Regression pipeline on the filtered training data. It evaluates the model and a keyword-rule baseline on the same test data, reporting accuracy and macro F1. The project target is a macro F1 score of at least 0.80.

The evaluated model is saved to `models/banking77_model.joblib`.

## Run the application

After training the model, start the Streamlit application:

```bash
streamlit run src/app.py
```

Enter a customer message in English to see its predicted intent in Polish.

## Documentation

- [Project documentation in Polish](docs/dokumentacja.md)
- [Technical summary in English](docs/technical-summary-en.md)
- [Selected Banking77 intents](docs/zakres-intencji.md)