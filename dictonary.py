import json

data = json.load(open("data.json"))

def translate(word):
    for i,line in enumerate(data[word], start=1):
        print('{}.{}'.format(i, line))
            
