import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The student is studying artificial intelligence."

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Word\t\tPOS Tag")

for word, tag in pos_tags:
    print(word, "\t\t", tag)