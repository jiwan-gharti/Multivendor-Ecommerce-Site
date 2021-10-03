import re
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd 

dataset = pd.read_csv("mainapp/trained_model/amazon.csv")
train_texts = dataset.iloc[:, 0]
train_labels = dataset.iloc[:, 1]
cv = CountVectorizer(binary=True)



NON_ALPHANUM = re.compile(r"[\W]")
NON_ASCII = re.compile(r"[^a-z0-9\s]")

def normalize_text(texts):
    normalized_text = []
    for text in texts:
        lower = text.lower()
        no_punctuation = NON_ALPHANUM.sub(r" ", lower)
        no_non_ascii = NON_ASCII.sub(r'',no_punctuation)
        normalized_text.append(no_non_ascii)
    return normalized_text

normalized_train_text = normalize_text(train_texts)
cv.fit(normalized_train_text)

def normalize_model(normalized_train_text):
    x = cv.transform(normalized_train_text)
    return x

def model_prdict(x):
    model = pickle.load(open("mainapp/trained_model/sentimental_analysis_model",'rb'))
    result = model.predict(x)
    return result
