import pandas as pd
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to preprocess dataset
def preprocess_data(file_path):
    df = pd.read_csv(file_path, encoding='latin-1')

    # Rename & keep necessary columns
    df = df.rename(columns={"v1": "label", "v2": "message"})
    df = df[["label", "message"]]
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Convert labels

    # Clean messages
    df['message'] = df['message'].apply(clean_text)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

    # Convert text to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer

