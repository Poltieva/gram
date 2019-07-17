# Colocations of verbs with adverb ending with "ly"
import time
print("Start loading modules")
start1 = time.time()
import re
from nltk import FreqDist
import spacy
nlp = spacy.load("en_core_web_md", disable=['textcat', 'ner'])
from nltk.corpus import wordnet as wn
end1 = time.time()
print("Modules loaded in {} seconds".format(end1-start1))
start2 = time.time()
print("Collecting synonyms")
words = ("say", "tell", "speak", "claim", "communicate")
verbs = set()
for word in words:
    sets = wn.synsets(word, pos = "v")
    for set in sets:
        for el in set.lemma_names():
            if "_" not in el:
                verbs.add(el)
# with open("say_synset.txt", "w", encoding='utf-8') as file:
#     for verb in verbs:
#         file.write(verb)
#         file.write("\n")
end2 = time.time()
print("Synonyms collected in {} seconds".format(end2 - start2))
start3 = time.time()
print("Collecting colocations")
with open("C:/Users/user/Desktop/blog2008.txt", 'r', encoding='utf-8') as file:
    text = file.readlines()

for line in text:
    if re.search(r".*\w+ly\b", line):
        parse = nlp(line)
        for token in parse:
            if token.lemma_ in verbs and token.pos_ == "VERB":
                children = list(token.children)
                for child in children:
                    if child.pos_ == "ADV" and child.text[-2:] == "ly":
                        result.append((token.lemma_, child.lemma_))
                    adv_children = list(child.children)
                    for adv_child in adv_children:
                        if adv_child.pos_ == "ADV" and adv_child.dep_ == 'conj' and adv_child.text[-2:] == "ly":
                             result.append((token.lemma_, adv_child.lemma_))
end4 = time.time()
print("Colocations collected in {} seconds".format(end4 - start4))
output = {}
for tup in result:
    if tup[0] not in output.keys():
        output[tup[0]] = [tup[1]]
    else:
        output[tup[0]] += [tup[1]]

for verb, adverbs in output.items():
    print("{}: {}".format(verb, FreqDist(adverbs).most_common(10)))


