
from fastapi import FastAPI
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from fastapi.middleware.cors import CORSMiddleware
import databases
import pandas as pd

app = FastAPI()

# Use correct function name 'pd.read_csv()' instead of 'pd.read_cvs()'
sents = pd.read_csv(
    r'F:\ON DEV\csv files\daraz-code-mixed-product-reviews.csv')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


f = pd.DataFrame(data)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['Reviews'], df['Sentiments'], test_size=0.2, random_state=42)

# Create a Naive Bayes model pipeline
model = CountVectorizer()  # Convert text data to a bag-of-words representation
X_train_vectorized = model.fit_transform(X_train)

classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Predict on the test set
X_test_vectorized = model.transform(X_test)
predictions = classifier.predict(X_test_vectorized)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")


@app.get("/")
def read_root():
    return {"Hello": "World"}


