from transformers import pipeline

## Use defalut model for sentiment analysis
def sentiment_classifier():
    classifier = pipeline(task="sentiment-analysis")
    result = classifier("I am absolutely loving this Hugging Face tutorial!")
    print(result)

## Note: go to hugging face, then search for any task 
## By defaults it loads distilbert-base-uncased-finetuned-sst-2-english model



## Use a specific model
## Browse the Hugging Face Models Hub and copy the exact name/ID of the custom model you prefer (e.g., "finiteautomata/bertweet-base-sentiment-analysis").
def specific_sentiment_classifier(text):
    classifier = pipeline(task="text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")
    result = classifier(text)
    print(result)
# specific_sentiment_classifier("Meh, the event was okay. Nothing groundbreaking")


## Explicit Nidek abd Tijebuzer Loading (Production Environments grade)
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
def explicit_sentiment_analyzer(text):
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    classifier = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
        truncation=True
    )

    print(classifier(text))

explicit_sentiment_analyzer("Hugging Face makes deployment seamless!")