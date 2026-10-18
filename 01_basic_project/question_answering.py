from transformers import pipeline

text = """Dear Amazon, last week I ordered an Optimus Prime action figure grom your online store in Germany. Unfortunately, when I opened the package, I discovered to my horror that I had been sent an action figure of Megatron  instead! As a lifelong enemy of the Decepticons, I hope you can understand my dilemma. To resolve the issue, I demand an exchange of Megatron for the Optimus Prime figure I ordered. Enclosed are copies of my records concerning this purchase. I expect to hear from you soon. sincrely, Bumblebee."""

#  FIXED: Removed the leading hyphen from the task name
qa_pipeline = pipeline(task='question-answering')

question = "what does the user want?"

# Run the pipeline with your question and context
outputs = qa_pipeline(question=question, context=text)
print(outputs)
