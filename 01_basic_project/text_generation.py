from transformers import Pipeline

text_generator = Pipeline(
    task="text-generation",
    model="deepseek-ai/DeepSeek-R1"
)

messages = [
    {"role": "user", "content": "What is the size of the universe?"}
]

response = text_generator(messages)

print(response)