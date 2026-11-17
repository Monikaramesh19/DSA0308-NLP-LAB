
import spacy

nlp = spacy.load("en_core_web_sm")

text = "John bought a laptop. He uses it every day."

doc = nlp(text)

for token in doc:
    if token.pos_ == "PRON":
        print("Pronoun:", token.text)

        if token.text.lower() == "he":
            print("Reference:", "John")

        elif token.text.lower() == "it":
            print("Reference:", "laptop")
