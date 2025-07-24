import os
import pickle

MODEL_PATH = os.path.join(os.path.dirname(__file__), "spam_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict(text: str):
    prediction = model.predict([text])[0]
    prob = model.predict_proba([text])[0]
    return {
        "prediction": "spam" if prediction == 1 else "ham",
        "probability": {"spam: %": float(prob[1]*100), "ham: %": float(prob[0]*100)},
        "label": int(prediction)
    }
