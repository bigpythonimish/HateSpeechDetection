import json
import re
from nltk import NaiveBayesClassifier


def clean_tweet(tweet):
    return ' '.join(re.sub(
        "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


mydata = []
json_data = open('convertcsv.json', 'r')
data = json.load(json_data)
for d in data:
    if d.get('hate_speech') == 0:
        mydata.append(
            {"text": clean_tweet(d.get('tweet')), "label": "pos"})
    else:
        mydata.append(
            {"text": clean_tweet(d.get('tweet')), "label": "neg"})

cl = NaiveBayesClassifier(mydata, format="json")
cl.classify("This is an amazing library!")