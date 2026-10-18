from transformers.pipelines import pipeline

answering_question = pipeline(task="question-answering")


context = """
Today is Monday, October 5, 2026. As of today, there are exactly 87 days left 
until the year 2026 concludes. The remaining time in the year consists of 
26 days left in October, 30 days in November, and 31 days in December. 
The final day of the year will be Thursday, December 31, 2026, making way 
for the arrival of the New Year on Friday, January 1, 2027.
"""

question = "how many days left in 2026?"

#  Get the answer
result = answering_question(question=question, context=context)

# 4. Print the output
print(f"Question: {question}")
print(f"Answer: {result['answer']}")
print(f"Confidence Score: {round(result['score'], 4)}")