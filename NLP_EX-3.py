import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

words = ["playing", "studies", "connected", "happiness", "cars"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Morphological Analysis")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("Word:", word)
    print("Stem:", stem)
    print("Lemma:", lemma)
    print()