from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report

from .nlp import *
from .data import *


def class_create(texts, labels):
    # Preprocess and tokenize text data
    preprocessed_texts = [" ".join([token.lemma_ for token in nlp(text) if not token.is_stop]) for text in texts]

    # Transform text into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(preprocessed_texts)

    # Train SVM model
    svm_model = SVC(kernel='linear')  # Linear SVM
    svm_model.fit(X, labels)

    return svm_model, vectorizer


def class_predict(svm_model, vectorizer, text):
    preprocessed_test_text = " ".join([token.lemma_ for token in nlp(text) if not token.is_stop])

    x = vectorizer.transform([preprocessed_test_text])

    # Make predictions
    prediction = svm_model.predict(x)
