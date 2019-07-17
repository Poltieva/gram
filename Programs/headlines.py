# Making an API standard headline
import re
import spacy
nlp = spacy.load("en_core_web_md", disable=['textcat', 'ner'])

# Baseline == only the 1st rule
def funct(headline):
    start = 0
    end = len(headline) -1
    for token in headline:
        if token.text[0].isalpha():
            start = token.i
            break
    for token in reversed(headline):
        if token.text[0].isalpha():
            end = token.i
            break
    return (start, end)
def format_headline(headline):
    formatted_headline = ""
    start, end = funct(headline)
    for token in headline:
        word = token.text
        if re.findall(r"[A-z][A-Z]", word):
            formatted_headline += word
        elif word in ("n't", "'s"):
            formatted_headline += word.lower()
        elif start != 0 and token.i == start:
            formatted_headline += word.title()
        elif len(word) > 3 or token.pos_ in ("ADJ", "ADV", "NOUN", "NUM", "PRON", "PROPN", "SCONJ", "VERB") or \
                token.i == 0 or token.i == len(headline) - 1:
            formatted_headline += word.title()
        elif token.pos_ in ("ADP", "AUX", "CCONJ", "DET", "INT", "PART"):
            formatted_headline += word.lower()
        else:
            formatted_headline += word
        formatted_headline += token.whitespace_
    return formatted_headline
headline1 = nlp('"McFly" sdjshd.')
print(format_headline(headline1))
# Implement metrics
import json

with open("C:/Users/user/Desktop/test-set.json", "r", encoding="utf-8") as f:
    test_data = json.load(f)

print(test_data[0])

def accuracy(test_data):
    tp = 0
    for sample in test_data:
        formatted_headline = format_headline(nlp(sample[0]))
        if formatted_headline == sample[1]:
            tp += 1
    return tp / len(test_data)
print(accuracy(test_data))

with open("C:/Users/user/Desktop/Grammarly/summer-school-2019/classes/6_full_cycle/task-headlines/dev-set.txt") as file:
    text = file.readlines()
for line in text[:20]:
    print(format_headline(nlp(line)))