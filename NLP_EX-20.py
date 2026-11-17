from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning is a part of artificial intelligence",
    "Python is used for machine learning",
    "Artificial intelligence is changing technology",
    "Natural language processing uses machine learning"
]

query = "machine learning"

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

ranked_indices = scores.argsort()[::-1]

print("Search Query:", query)
print("\nRanked Documents:")

for index in ranked_indices:
    print("\nDocument:", documents[index])
    print("Score:", round(scores[index], 3))
