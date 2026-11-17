import random
from collections import defaultdict

text = "natural language processing is interesting natural language processing is useful"

words = text.lower().split()

bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    bigram_model[words[i]].append(words[i + 1])

word = "natural"
generated = [word]

for i in range(10):
    next_words = bigram_model.get(word)

    if not next_words:
        break

    word = random.choice(next_words)
    generated.append(word)

print("Generated Text:")
print(" ".join(generated))