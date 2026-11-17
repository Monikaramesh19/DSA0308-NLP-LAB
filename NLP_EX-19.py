import nltk
from nltk.wsd import lesk

nltk.download('wordnet')
nltk.download('omw-1.4')

sentence = "I went to the bank to deposit money"

words = sentence.split()

sense = lesk(words, 'bank')

print("Sentence:", sentence)
print("Target Word: bank")

if sense:
    print("Meaning:", sense.definition())
    print("Synset:", sense.name())
else:
    print("No meaning found")
