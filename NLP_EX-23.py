from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "Machine learning is a branch of artificial intelligence.",
    "It helps computers learn from data.",
    "Machine learning is used in many applications."
]

vectorizer = TfidfVectorizer()

matrix = vectorizer.fit_transform(text)

similarity = cosine_similarity(matrix)

scores = []

for i in range(len(text) - 1):
    score = similarity[i][i + 1]
    scores.append(score)
    print("Similarity between sentence", i + 1, "and", i + 2,
          ":", round(score, 3))

average = sum(scores) / len(scores)

print("\nCoherence Score:", round(average, 3))

if average >= 0.2:
    print("Text is Coherent")
else:
    print("Text is Less Coherent")
