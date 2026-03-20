import re

def extract_concepts(text):

    keywords = [
        "machine learning",
        "deep learning",
        "cnn",
        "tensorflow",
        "overfitting",
        "neural network",
        "api",
        "backend",
        "database"
    ]

    found = []

    for k in keywords:
        if k.lower() in text.lower():
            found.append(k)

    return found