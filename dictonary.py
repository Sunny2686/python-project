import json

data = json.loads(open("data.json"))

def translate(word):
    return data[word]

word = input('Enter word ')
translate(word)