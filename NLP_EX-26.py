
from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "Hello, how are you? Welcome to the world of artificial intelligence."

result = translator(text)

print("English Text:")
print(text)

print("\nFrench Translation:")
print(result[0]['translation_text'])
