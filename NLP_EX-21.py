
import spacy

nlp = spacy.load("en_core_web_sm")

text = "The intelligent student developed a machine learning project."

doc = nlp(text)

print("Sentence:", text)
print("\nNoun Phrases and Their Meanings:")

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root Word:", chunk.root.text)
    print("Meaning:", chunk.root.lemma_)
