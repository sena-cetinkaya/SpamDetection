import os
import pandas as pd
import pickle
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from app.db.crud import bulk_insert_emails, get_training_data

load_dotenv()

MODEL_PATH = "app/models/spam_model.pkl"

def prepare_data_from_csv():
    df = pd.read_csv("data/tr_email_spam.csv")
    df = df.dropna()
    df = df[df["Classification"].isin(["spam", "ham"])]  # spam ve ham olan sınıflar filtrelenir. içteki df true-false döner, dıştaki df trueları alır
    df = df[["Text", "Classification"]].copy()
    df["label"] = df["Classification"].map({"spam": 1, "ham": 0})
    #df.rename(columns={"Text": "content", "Classification": "classification"}, inplace=True)
    df.rename(columns={"Text": "content"}, inplace=True)
    return df.to_dict(orient="records")

if not os.path.exists(MODEL_PATH):
    emails = prepare_data_from_csv()
    bulk_insert_emails(emails)

    records = get_training_data()
    df = pd.DataFrame([{"Text": r.content, "Label": r.label } for r in records])
    X = df["Text"]
    y = df["Label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)

    models = {
        "RandomForest": RandomForestClassifier(),
        "NaiveBayes": MultinomialNB()
    }

    best_model = None
    best_score = 0

    for name, model in models.items():
        pipe = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("clf", model)
        ])
        pipe.fit(X_train, y_train)
        score = accuracy_score(y_test, pipe.predict(X_test))
        print(f"{name} Accuracy: {score:.4f}")
        if score > best_score:
            best_model = pipe
            best_score = score

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(best_model, f)

    print(f"Model saved: {MODEL_PATH}, Accuracy: {best_score:.4f}")
else:
    print("Model already exists.")
