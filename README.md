# 📩 Spam SMS Detection

## 🚀 Project Overview
This project is an **SMS Spam Detector** that classifies messages as **Spam** or **Ham (Not Spam)** using a Machine Learning model. The dataset consists of labeled messages categorized accordingly. The project includes **data preprocessing, model training, evaluation, and prediction**.

## 📂 Project Structure
```
Spam_Detection_Project/
│── spam.csv                  # Dataset file
│── main.py                    # Main script to run the project
│── data_preprocessing.py      # Data cleaning & TF-IDF conversion
│── train_model.py             # Model training & evaluation
│── predict.py                 # Predict function for new SMS
│── requirements.txt           # Dependencies (optional)
│── README.md                  # Project Documentation
```

## 📌 Features
✅ **Train a Spam Detection Model** using Machine Learning  
✅ **Text Preprocessing & Feature Extraction** (TF-IDF)  
✅ **Evaluate Model Performance** using Accuracy, Precision, Recall, and F1-score  
✅ **Real-time SMS Classification** for new user input  
✅ **Scalable Code Structure** for easy expansion  

## 📂 Dataset
The project uses a **spam.csv** dataset containing labeled SMS messages categorized as:
- `ham` (Non-Spam)
- `spam` (Unwanted messages)

## 🔧 Installation & Setup
### 1️⃣ Install Dependencies
```bash
pip install pandas scikit-learn
```

### 2️⃣ Train the Model
```bash
python train_model.py
```

### 3️⃣ Run the Prediction System
```bash
python main.py
```

## 🔍 How It Works
1️⃣ **Train the Model** – `train_model.py` preprocesses data, trains the model, and evaluates performance.  
2️⃣ **Make Predictions** – `predict.py` loads the trained model and classifies messages as spam or ham.  
3️⃣ **Use Preprocessed Data** – `data_preprocessing.py` cleans and transforms raw SMS text for model training.  

## 📊 Model Performance
| Metric              | Value  |
|---------------------|--------|
| Accuracy           | ~97%   |
| Precision          | ~96%   |
| Recall             | ~95%   |
| F1-Score          | ~95%   |

## 📌 Future Enhancements
🔹 **Add More Models** for comparison (Naive Bayes, SVM, Logistic Regression)  
🔹 **Develop a Web UI** using Flask or Streamlit  
🔹 **Deploy the Model** on a cloud platform (e.g., Heroku)  

## 🤝 Contributing
Feel free to fork this repository, make improvements, and submit pull requests!

## 📜 License
This project is open-source and available for learning purposes. Feel free to enhance it!

---
Made with ❤️ by **Yash Phulbagkar** 🚀

