# 🧠 News Classifier – Text Classification Web App

A simple and lightweight web application built with **FastAPI** to classify Russian news articles using a pre-trained machine learning model.

---

## 📁 Project Structure

```
ML-final/
├── main.py                  # FastAPI application
├── templates/
│   └── index.html           # HTML form
├── static/                  # CSS styles
│   └── styles.css     
├── news_classifier_ru.joblib  # Pre-trained ML model
└── requirements.txt         # Python dependencies
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/sq1der/news_classifier.git
cd ML-final
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

📍 Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📝 How to Use

1. Go to the homepage.
2. Enter a news snippet in Russian.
3. Click the **"Predict"** button.
4. The model will classify the news topic and display the result.

---

## 🧪 Example Inputs

Try any of the following examples:

```
Команда «Астана» выиграла чемпионат Казахстана по футболу.

Президент подписал закон о поддержке малого бизнеса.

Компания Apple представила новый iPhone с улучшенной камерой.
```

---

## 🛠 Tech Stack

- 🐍 Python 3.11  
- ⚡ FastAPI  
- 🧠 Scikit-learn  
- 🗣 nltk  
- 🎨 HTML + CSS  
- 💾 joblib (for model persistence)

---

## 📦 About the Model

The machine learning model was pre-trained and saved in the `news_classifier_ru.joblib` file.  
It uses TF-IDF features and a classification algorithm to predict the topic of a Russian news snippet.

---

## ⭐️ Support the Project

If you like this project, feel free to ⭐️ it on GitHub!
