from transformers.pipelines import pipeline



text_generator = pipeline(
    task="text-generation",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    token=hftoken
)
print("text is generating...")
generated_text = text_generator("what is blackhole?")
print(f"\ngenerated text:\n{'-'*30}")
print(generated_text)