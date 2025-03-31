from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import preprocess_data

# Load and preprocess data
X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer = preprocess_data("spam.csv")

# Train the model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print evaluation results
print("Model Accuracy:", accuracy)
print("Classification Report:\n", report)
