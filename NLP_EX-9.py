import nltk

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*ness$', 'NN'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger(patterns)

text = "The beautiful girl is happily dancing"

words = nltk.word_tokenize(text)

tags = tagger.tag(words)

for word, tag in tags:
    print(word, tag)