
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = "Write a short paragraph about Artificial Intelligence."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

print("Generated Text:")
print(response.choices[0].message.content)
