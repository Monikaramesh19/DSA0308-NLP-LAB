import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

word = "computer"

synsets = wordnet.synsets(word)

print("Word:", word)
print("\nSynsets and Meanings:")

for syn in synsets[:5]:
    print("\nSynset:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())
