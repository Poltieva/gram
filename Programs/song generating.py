import random
import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk import FreqDist

with open("queen.txt", "r", encoding='utf-8') as file:
    text = file.readlines()

all = {}
words = []
for tokens in text:
    token = word_tokenize(tokens)
    if token:
        words.append(token)
    bigr = list(ngrams(token, 2,
                       pad_right=True, right_pad_symbol='</s>',
                       pad_left=True, left_pad_symbol='<s>'))
    for el in bigr:
        if el not in all.keys():
            all[el] = 1
        else:
            all[el] += 1

def most_com_bigr(word):
    top = []
    top2 = []
    for k, v in all.items():
        if k[0] == word:
            top.append((k, v))
            top2.append(k)
    top = sorted(top, key=lambda kv: kv[1], reverse = True)
    return top2
def generate_line(first_word):
    output = []
    def generate(first_word):
        if first_word != "</s>":
            choises = most_com_bigr(first_word)
            choose = random.choice(choises)
            output.append(first_word + " " + choose[1])
            generate(choose[1])
        else: output.append("</s>")
    generate(first_word)
    return " ".join(output[::2])

def generate_song(first_word):
    output = []
    output.append(generate_line(first_word))
    count = 9
    while count:
        output.append(generate_line(random.choice(words[random.choice(range(10))])))
        count -= 1
    return "\n".join(output)

first_word = input("Enter the 1st word to generate a Queen's song:\n")
print(generate_song(first_word))