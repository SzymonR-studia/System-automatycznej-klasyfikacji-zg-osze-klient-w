from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def main():
    texts = [
        "I cannot log into my banking app",
        "My card was stolen",
        "I want to transfer money",
        "I forgot my password",
        "My card payment was declined",
        "How can I check my account balance?",
    ]

    labels = [
        "login_problem",
        "card_stolen",
        "cash_transfer",
        "login_problem",
        "cash_withdrawal",
        "cash_withdrawal",
    ]

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    model.fit(texts, labels)

    message = "I cannot access my account"
    prediction = model.predict([message])[0]

    print("Zgłoszenie:", message)
    print("Przewidywana kategoria:", prediction)


if __name__ == "__main__":
    main()
