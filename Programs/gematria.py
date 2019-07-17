# Returns a file with words with the same gematria, works from console
import re
import sys
from nltk import sent_tokenize, word_tokenize
letter_values_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}

letter_values_2 = {"a":6, "b":12, "c":18, "d":24, "e":30, "f":36, "g":42,
"h":48, "i":54, "j":60, "k":66, "l":72, "m":78, "n":84, "o":90, "p":96,
"q":102, "r":108, "s":114, "t":120, "u":126, "v":132, "w":138, "x":144,
"y":150, "z":156}

words_with_same_gematria = {}
def count_gematria(word, option):
    count = 0
    global letter_values_1, letter_values_2
    for l in word:
        l = l.lower()
        if l in letter_values_1.keys():
            if option == "1":
                count += letter_values_1[l]
            elif option == "2":
                count += letter_values_2[l]
    return count
def decode(text, option, output_file):
    global words_with_same_gematria
    if option not in ("1", "2"):
        print("Second agument must be '1' or '2'")
    else:
        with open(text, "r", encoding="utf-8") as f:
            text = f.read()
        words = re.split(r'[ \n]', text)
        for el in words:
            el = el.lower()
            if re.search(r'[^a-z]', el) is None:
                gematria = count_gematria(el, option)
                if gematria not in words_with_same_gematria.keys():
                    words_with_same_gematria[gematria] = [el]
                else:
                    if el not in words_with_same_gematria[gematria]:
                        words_with_same_gematria[gematria].append(el)
        with open(output_file, "w", encoding='utf-8') as f:
            for key in set(words_with_same_gematria.keys()):
                f.write("{}: {}\n".format(key, " ".join(words_with_same_gematria[key])))


if __name__ == '__main__':
    decode(sys.argv[1], sys.argv[2], sys.argv[3])
