# Technical Summary

## Project

This project classifies English-language customer service messages for a bank. It is intended to help support staff route incoming tickets to an appropriate intent category.

## Dataset and scope

The project uses the public [Banking77 dataset](https://huggingface.co/datasets/PolyAI/banking77) and selects 35 intents covering card access and delivery, card payments and cash withdrawals, transfers, and account top-ups. The original train/test split is preserved. The filtered training set contains 5,160 examples; the test set contains 1,400 examples, with 40 examples per intent. The complete selected-intent list is documented in [Polish project documentation](zakres-intencji.md).

## Method

The main classifier is a scikit-learn pipeline combining `TfidfVectorizer` with `LogisticRegression(max_iter=1000)`. It is trained on the filtered training split and evaluated on the filtered test split.

A simple keyword-rule baseline is evaluated on the same test examples. It scores phrase matches for each intent and falls back to the most frequent training label when no rule matches.

## Evaluation

The project reports accuracy and macro F1. The target set in the project brief is a macro F1 score of at least 0.80 on the independent test set.

| Method | Accuracy | Macro F1 |
|---|---:|---:|
| TF-IDF + Logistic Regression | 0.8886 | 0.8897 |
| Keyword-rule baseline | 0.1129 | 0.1372 |

The classifier exceeds the target macro F1 score of 0.80 on the test set. The keyword-rule baseline scores substantially lower on the same test examples.

## Application

The Streamlit interface accepts a customer message and displays the predicted intent in Polish. The trained pipeline is stored at `models/banking77_model.joblib`.
