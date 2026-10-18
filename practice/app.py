from transformers import pipeline

text_classifier = pipeline(
    task="text-classification"
)


print(text_classifier("AI is dangerous"))