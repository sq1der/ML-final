from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import nltk
from nltk.tokenize import word_tokenize
from pymorphy3 import MorphAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.corpus import stopwords

app = FastAPI()

# Статика и шаблоны
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Загрузка модели
model_data = joblib.load("news_classifier_ru.joblib")
model = model_data['model']
stop_words = model_data['stop_words']
punctuation_marks = model_data['punctuation_marks']
morph = MorphAnalyzer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return " ".join([
        morph.parse(token)[0].normal_form
        for token in tokens
        if token not in punctuation_marks and morph.parse(token)[0].normal_form not in stop_words
    ])

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, user_text: str = Form(...)):
    preprocessed_text = preprocess(user_text)
    prediction = model.predict([preprocessed_text])[0]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": prediction,
        "original": user_text
    })
