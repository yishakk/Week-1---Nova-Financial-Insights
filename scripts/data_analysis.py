import pandas as pd
import textblob as TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity