from transformers import BertTokenizer, BertForSequenceClassification

def load_model_and_tokenizer():
    """Function to load and return the saved model and tokenizer"""
    model = BertForSequenceClassification.from_pretrained('SentimentAnalysisModel')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    return model, tokenizer