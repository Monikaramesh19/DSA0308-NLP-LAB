from collections import defaultdict, Counter

training_data = [
    ("The", "DT"), ("dog", "NN"), ("barks", "VBZ"),
    ("A", "DT"), ("cat", "NN"), ("runs", "VBZ"),
    ("The", "DT"), ("boy", "NN"), ("plays", "VBZ")
]

word_tag_count = defaultdict(Counter)

for word, tag in training_data:
    word_tag_count[word.lower()][tag] += 1

def pos_tag(word):
    tags = word_tag_count[word.lower()]
    if tags:
        return tags.most_common(1)[0][0]
    return "NN"

sentence = "The dog runs"
words = sentence.split()

for word in words:
    print(word, pos_tag(word))