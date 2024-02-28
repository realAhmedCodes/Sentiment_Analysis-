
from fastapi import FastAPI
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from fastapi.middleware.cors import CORSMiddleware
import databases
from pydantic import BaseModel
import pandas as pd

app = FastAPI()


sents = pd.read_csv(
    r'F:\ON DEV\csv files\daraz-code-mixed-product-reviews.csv')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


X_train, X_test, y_train, y_test = train_test_split(
    sents['Reviews'], sents['Sentiments'], test_size=0.2, random_state=42)


model = CountVectorizer() 
X_train_vectorized = model.fit_transform(X_train)

classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: str


@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):

    text = [request.text]
    text_vectorized = model.transform(text)
    result = classifier.predict(text_vectorized)[0]
    return {"sentiment": result}


@app.get("/")
def read_root():
    return {"Hello": "World"}
