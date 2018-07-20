import json

with open('dataset.json') as json_data:
    data = json.load(json_data)
    for d in data:
        print d.get('tweet')
