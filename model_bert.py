from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# Load pre-trained model and tokenizer from Hugging Face
model_name = "tidarat/WangchanBERTa"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, ignore_mismatched_sizes=True)
sentiment_model = pipeline(task="text-classification",
                           model=model,
                           tokenizer=tokenizer)

def predict_bert(text, decode=False):
    # input text
    result = sentiment_model(text)[0]
    label = result['label']
    score = result['score']
    
    if label == "depression":
        return("ข้อความนี้มีลักษณะไปในทางเชิงลบ")
    else:
        return("ข้อความนี้มีลักษณะไปในทางเชิงบวก")
