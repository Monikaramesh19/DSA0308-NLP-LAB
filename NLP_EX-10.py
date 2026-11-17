words = ["The", "students", "are", "playing"]

tags = ["DT", "NN", "NN", "NN"]

print("Initial POS Tags:")

for word, tag in zip(words, tags):
    print(word, tag)

for i in range(len(words)):
    if words[i] == "are":
        tags[i] = "VBP"

    elif words[i].endswith("ing"):
        tags[i] = "VBG"

    elif i > 0 and tags[i - 1] == "DT":
        tags[i] = "NNS"

print("\nFinal POS Tags:")

for word, tag in zip(words, tags):
    print(word, tag)