from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "running", "runner",
         "happiness", "studies", "connected", "connection"]

print("Original Word\tStemmed Word")

for word in words:
    print(word, "\t\t", ps.stem(word))