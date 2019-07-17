# Different tasks
# 1
def british_colours(word):
    word = word.replace("color", "colour")
    return word

# 2
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
# 3
def exclamate(sentence):
    sentence[-1] = "!"
    sentence[0], sentence[1] = sentence[1].title(), sentence[0].lower()
    return sentence
# 4
def is_valid(password):
    digit = 0
    capital = 0
    for el in password:
        if el.isupper():
            capital += 1
        elif el.isdigit():
            digit += 1
    if password.isalnum() and len(password) >= 8 and capital == 2 and digit == 2:
        return True
    else:
        return False
# 5
def the_longest_common_prefix(word_1, word_2):
    answ = ""
    for el, elem in zip(word_1, word_2):
        if el == elem:
            answ += el
        else:
            break
    return answ
# 6
def ari(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    text = text.split("\n")
    words_in_sent = []
    len_of_word = []
    for sentence in text:
        sentence = sentence.replace(" ,", "").replace(" .", "").replace(" :", "").replace("– ", "").replace(" ;", "")
        words_in_sent.append(len(sentence.split()))
        for word in sentence.split():
            len_of_word.append(len(word))
    μs = sum(words_in_sent) / len(text)
    μw = sum(len_of_word) / len(len_of_word)
    return round(4.71 * μw + 0.5 * μs - 21.43, 2)

def lexical_diversity(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    unique = set()
    total = []
    text = text.split("\n")
    for sentence in text:
        sentence = sentence.replace(" ,", "").replace(" .", "").replace(" :", "").replace("– ", "").replace(" ;", "")
        for word in sentence.split():
            unique.add(word)
            total.append(word)
    return round(len(unique) / len(total), 2)

#2-2
import re
def number_of_articles(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    text = text.replace(" ,", "").replace(" .", "").replace(" :", "").replace("– ", "").replace(" ?", "").replace(" !", "")
    article = re.findall(r"(?i)\b(the|a|an)\b", text, flags=re.MULTILINE)
    text = text.split("\n")
    return len(article) / len(text)
#2-4
def real_zen(input_file):
    with open(input_file, 'r', encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"^//.*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"(.*?\n)(.*)(?:Author:)(.*)", r"\1by\3\2", text, flags=re.DOTALL)
    text = text[:-1]
    text = text.split("\n")
    for num, line in enumerate(text):
        num -= 1
        if num > 0:
            print(str(num) + ". " + line)
        else:
            print(line)
#2-5
def tokenize(sentence):
    sentence = re.sub(r"(!|\?|\.$|\'$|\"$|\.\.\.|,|\)|;|:)", r" \1", sentence)
    sentence = re.sub(r"((?<=\w)\. \'?\"?$)", r" \1", sentence)
    sentence = re.sub(r"(,|\.\.\.)(\'|\")", r"\1 \2", sentence)
    sentence = re.sub(r"(^\"|\')", r"\1 ", sentence)
    sentence = re.sub(r"(\w+)\' ", r"\1 ", sentence)
    sentence = re.sub(r"(\w+)n t ", r"\1 n't ", sentence)
    return sentence
