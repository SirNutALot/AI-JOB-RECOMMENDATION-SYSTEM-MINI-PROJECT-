import re
import spacy

nlp = spacy.load("en_core_web_sm")
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_text(text):

    text = clean_text(text)

    doc = nlp(text)

    processed_words = []

    for token in doc:

        if not token.is_stop and not token.is_punct:

            processed_words.append(token.lemma_)

    return " ".join(processed_words)