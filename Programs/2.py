import nltk
from nltk.corpus import treebank, brown


def search_by_tag_sequence(tag_seq, tagged_tokens):
    output_list = list()
    list_of_one_match = list()
    i = 0
    for pair in tagged_tokens:
        if i == len(tag_seq):
            output_list.append(list_of_one_match)
            list_of_one_match = []
            i = 0
        elif pair[1] == tag_seq[i]:
            list_of_one_match.append(pair)
            i += 1
        else:
            list_of_one_match = []
            i = 0
    print(output_list[:10])

dict = dict()
list_of_tuples = brown.tagged_words(tagset='universal')
for el in list_of_tuples:
    if el[0] not in dict.keys():
        dict[el[0]] = [el[1]]
    else:
        if el[1] not in dict[el[0]]:
            dict[el[0]].append(el[1])
sorted_x = sorted(dict.items(), key=lambda kv: len(kv[1]), reverse = True)
for i in range(10):
    print(sorted_x[i])


search_by_tag_sequence(["NNP", "NNP", "NNP"], treebank.tagged_words())