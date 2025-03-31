from data_preprocessing import clean_text
from train_model import model, vectorizer

def predict_sms(message):
    """Classify a given SMS as Spam or Ham."""
    message_cleaned = clean_text(message)  # Clean text
    message_tfidf = vectorizer.transform([message_cleaned])  # Convert to TF-IDF
    prediction = model.predict(message_tfidf)[0]  # Predict using model
    return "Spam" if prediction == 1 else "Ham"

# Test cases
if __name__ == "__main__":
    test_messages = [
        "Congratulations! You have won a free iPhone. Click the link to claim your prize.",
        "Hey, are we still meeting for lunch today?",
    ]
    
    for msg in test_messages:
        print(f"Message: {msg}\nPrediction: {predict_sms(msg)}\n")
