import nltk
from nltk.corpus import brown
# # print(brown.readme())
# # print("Paragraphs: {}".format(len(brown.paras())))
# # print("Sent: {}".format(len(brown.sents())))
# # print("Words: {}".format(len(brown.words())))
# # print(brown.raw()[:255])
# # print(brown.tagged_words(tagset='universal')[201:206])
# # print(brown.categories())
# # for sent in brown.paras(categories='humor')[0]:
# #     print(" ".join(sent))
# #     print("\n")
# #####################3 Concondance
# # from nltk.book import *
# # print(text1.concordance(","))
# # print(text1.similar("bare"))
# import os
# from nltk import sent_tokenize
# print(os.getcwd())
# raw = open("C:/Users/user/Desktop/Grammarly/summer-school-2019/classes/3_python/data/jekyll_hyde.txt").read()
# paragr = raw.splitlines()
# sentences = []
# for par in paragr:
#     for s in sent_tokenize(par):
#         sentences.append(s)
# from nltk.tokenize import word_tokenize
# tokens = []
# for sent in sentences:
#     for token in word_tokenize(sent):
#         tokens.append(token)
# from nltk.text import Text
# corpus = Text(tokens)
# # corpus.concordance("has")
# ##Stemming
# from nltk.stem import *
# stemmer = porter.PorterStemmer()
# words = ['flies', 'fly','flying',
#          'died', 'dying', 'dead',
#          'computer', 'computational',
#          'replaced', 'replacement',
#          'does', 'did', 'done',
#          'women', 'normal', 'normalized', 'normalization']
#
# for word in words:
#     print("Word: {0} --> {1}".format(word, stemmer.stem(word)))
#
# class IndexedText(object):
#
#     def __init__(self, stemmer, text):
#         self._text = text
#         self._stemmer = stemmer
#         self._index = nltk.Index((self._stem(word), i)
#                                  for (i, word) in enumerate(text))
#
#     def concordance(self, word, width=40):
#         key = self._stem(word)
#         wc = int(width/2)
#         idx = self._index[key]
#         if len(idx) > 0:
#             for i in self._index[key]:
#                 lcontext = ' '.join(self._text[i-wc:i])
#                 rcontext = ' '.join(self._text[i:i+wc])
#                 ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
#                 rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
#                 print(ldisplay, rdisplay)
#         else:
#             print("No matches found :(")
#
#     def _stem(self, word):
#         return self._stemmer.stem(word).lower()
# indexed_by_stemmer = IndexedText(nltk.PorterStemmer(), tokens)
# indexed_by_stemmer.concordance("start", width = 30)
# ##Lematization
# wnl = nltk.WordNetLemmatizer()
# for word in words:
#     print("Word: {0} --> {1}".format(word, wnl.lemmatize(word)))
# nltk.pos_tag(nltk.word_tokenize("Time flies like an arrow."))
def convert_pos_tag(treebank_tag):
    if treebank_tag.startswith(("V", "MD")):
        return 'v'
    elif treebank_tag.startswith("N"):
        return 'n'
    elif treebank_tag.startswith("J"):
        return 'a'
    else:
        return 'r'

def get_wordnet_pos(word):
    return convert_pos_tag(nltk.pos_tag([word])[0][1])
# print(nltk.WordNetLemmatizer().lemmatize("tried", get_wordnet_pos("tried")))
#
# class IndexedTextPOS(object):
#
#     def __init__(self, lemmatizer, text):
#         self._text = text
#         self._lemmatizer = lemmatizer
#         self._index = nltk.Index((self._lemma(word), i)
#                                  for (i, word) in enumerate(text))
#
#     def concordance(self, word, width=40):
#         key = self._lemma(word)
#         wc = int(width/2)
#         idx = self._index[key]
#         if len(idx) > 0:
#             for i in self._index[key]:
#                 lcontext = ' '.join(self._text[i-wc:i])
#                 rcontext = ' '.join(self._text[i:i+wc])
#                 ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
#                 rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
#                 print(ldisplay, rdisplay)
#         else:
#             print("No matches found :(")
#
#     def _lemma(self, word):
#         pos_tag = get_wordnet_pos(word)
#         return self._lemmatizer.lemmatize(word, pos_tag).lower()
# yellow_better_idx = IndexedTextPOS(nltk.WordNetLemmatizer(), tokens)
# yellow_better_idx.concordance("tried")
#
# #word net
from nltk.corpus import wordnet as wn
# help(wn)
#synset
# print(wn.synsets("do"))
# # synonims
# print(wn.synset('bash.n.02').lemma_names())
# print(wn.synset('hedge.v.01').definition())
# print(wn.synset('bash.n.02').hypernyms())
# print(wn.synsets('duck', pos='v'))
# # adj
# print(wn.synset('small.a.01').lemma_names())
# # adj satellites
# print(wn.synset('joyful.a.01').similar_tos())
# # verbs
# print(wn.synset('transfer.v.05').causes())
# print(wn.synset('wake.v.02').entailments())
# print(wn.synset('train.v.01').verb_groups())
# print(nltk.corpus.reader.wordnet.Synset.__doc__)
# import time
# def defin(word):
#     synsets = wn.synsets(word)
#     if not synsets:
#         print("Apologies")
#     else:
#         pos = []
#         for synset in synsets:
#             if synset.pos() not in pos:
#                 pos.append(synset.pos())
#         print("this word can be")
#         for el in pos:
#             if el == "n":
#                 print("A noun")
#             elif el == "v":
#                 print("A verb")
#             elif el == "a" or el == "s":
#                 print("An adjective")
#             else: print("An adverb")
#         print("This word has:\n")
#         for synset in synsets:
#             print("Synonim:", synset.name(), ", which means", synset.definition(), ".")
#             print("     Examples:")
#             for el in synset.examples(): print("        ", el, end=" ")
#             print("\n     Its synonims are:", synset.lemma_names())
#             print("     Its hyponims are:", synset.hyponyms())

# Frequences
from nltk import FreqDist
brown_freqd = FreqDist(brown.words())
# print(brown_freqd.most_common(10))
# print(brown_freqd["swiftly"])
# print(brown_freqd["shifty"])
# print(brown_freqd["shwifty"])
# for word in brown_freqd.most_common(10):
#     print("{} ~ {}".format(word[0], round(brown_freqd.freq(word[0]), 3)))
# print(brown_freqd.freq("kitten"))
# Hapaxes - 1 time in dict
# print(sorted(brown_freqd.hapaxes(), key = lambda w: len(w), reverse = True)[:20])
# Zipf's law
# brown_freqd.plot(10)
from nltk import ConditionalFreqDist
# print(brown.categories())
# cats = ['mystery', 'adventure']
# cfd = nltk.ConditionalFreqDist(
#     (genre, word.lower())
#     for genre in cats
#     for word in brown.words(categories=genre))
# for cond in cfd.conditions():
#     print(cond)
#     print(cfd[cond].most_common(20))
#     print()
#     print("question mark in {} - {} - {}".format(cond,
#                                                  cfd[cond]["?"],
#                                                  round(cfd[cond].freq("?"), 4)))
# cfd.tabulate(samples = ["ran", "fired", "thought", "guessed", "asked"])
# # NLTK word list
from nltk.corpus import names, stopwords, words
# print(names.words("male.txt")[:10])
# print(names.words("female.txt")[:10])
# print(words.fileids())
# print(sorted(stopwords.words('english')))
from nltk.corpus import inaugural
# print(inaugural.fileids())
# , '1793-Washington.txt'

from nltk import WordNetLemmatizer

def lemmatize_tokens(tokens):
    lemmatized = []
    if type(tokens) == str:
        tokens = word_tokenize(tokens)
    for word in tokens:
        treebank_tag = nltk.pos_tag([word])[0][1]
        wn_tag = convert_pos_tag(treebank_tag)
        # we'll lemmatize only adjectives, nouns, adverbs and verbs to save time
        if treebank_tag[0] in ['J', 'N', 'R', 'V']:
            word = WordNetLemmatizer().lemmatize(word, wn_tag)
        lemmatized.append(word)
    return lemmatized
# speech_tokens = inaugural.words('1789-Washington.txt')
# lemmatized_t = lemmatize_tokens(speech_tokens)
# print("Raw tokens:")
# print(speech_tokens[:30])
# print("Lemmatized:")
# print(lemmatized_t[:30])
import re
def get_keywords(tokens):
    refined_tokens = []
    exceptions = stopwords.words('english')
    for token in tokens:
        lowercased_token = token.lower()
        if lowercased_token not in exceptions and re.match(r"^[a-z]+(?:['-]?[a-z]+)*$", lowercased_token):
            refined_tokens.append(lowercased_token)
    lemmatized_tokens = lemmatize_tokens(refined_tokens)
    fd = FreqDist(lemmatized_tokens)
    return [tpl[0] for tpl in fd.most_common(20)]
#
# print(get_keywords(inaugural.words('1789-Washington.txt')))
# print(get_keywords(inaugural.words('1793-Washington.txt')))
# Metrics - TF-IDF - importance of word to a text in collection of texts
# words = get_keywords(inaugural.words('1793-Washington.txt'))
# for word in words:
#     freq_in_text = FreqDist(inaugural.words('1793-Washington.txt'))
#     tf = freq_in_text[word] / freq_in_text.N()
#     doc = 0
#     for el in inaugural.fileids():
#         freq_word = FreqDist(lemmatize_tokens(inaugural.words(el)))
#         if freq_word[word] != 0:
#             doc += 1
#
#     from math import log
#     idf = log(len(inaugural.fileids()) / doc)
#     print(word, tf * idf)
# import math
# corpus = inaugural.fileids()
# lemmatized_data = {}
# for doc in corpus:
#     lemmatized_data[doc] = lemmatize_tokens(inaugural.words(doc))
#
# def calculate_tfs(target_texts, lemmatized_data):
#     tfs = {}
#     for t in target_texts:
#         tfs[t] = {}
#         for lemma in lemmatized_data[t]:
#             if lemma not in tfs[t]:
#                 tfs[t][lemma] = 1
#             else:
#                 tfs[t][lemma] += 1
#         for lemma in tfs[t]:
#             tfs[t][lemma] = tfs[t][lemma] / len(lemmatized_data[t])
#     return tfs
#
# def calculate_idfs(target_texts, lemmatized_data):
#     idfs = {}
#     for text in lemmatized_data:
#         lemmas = set(lemmatized_data[text])
#         for lemma in lemmas:
#             if lemma not in idfs:
#                 idfs[lemma] = 1
#             else:
#                 idfs[lemma] += 1
#     for lemma in idfs:
#         idfs[lemma] = round(math.log(len(lemmatized_data) / idfs[lemma]), 3)
#     return idfs
#
# def calculate_tfidfs(texts, lemmatized_data, tfs, idfs):
#     tfidfs = {}
#     for text in texts:
#         tfidfs[text] = {}
#         for lemma in lemmatized_data[text]:
#             tfidfs[text][lemma] = round(tfs[text][lemma] * idfs[lemma], 3)
#     return tfidfs
#
# target_speeches = ['1789-Washington.txt', '1861-Lincoln.txt', '2001-Bush.txt']
# tfs = calculate_tfs(target_speeches, lemmatized_data)
# idfs = calculate_idfs(target_speeches, lemmatized_data)
#
# tfidfs = calculate_tfidfs(target_speeches, lemmatized_data, tfs, idfs)
# for speech in tfidfs:
#     speech_parts = speech.split('-')
#     print("Most important words for the {0}'s {1} speech:".format(speech_parts[1][:-4], speech_parts[0]))
#     print([w[0] for w in sorted(tfidfs[speech].items(), key=lambda x: x[1], reverse=True)[:15]])
#     print()
# Probabilities
from nltk.util import bigrams, trigrams, ngrams
# random_text = "I love turtles."
# random_words = ["I", "love", "turtles", "more", "than", "you", "ever", "will", "!"]
#
# print(list(bigrams(random_text)))
# print(list(bigrams(random_words)))
#
# print(list(ngrams(random_text, 5)))
# print(list(ngrams(random_words, 5)))
# Google n-gram viewer
# random_sentence = inaugural.sents('2009-Obama.txt')[1]
# for trg in ngrams(random_sentence, 3):
#     print(trg)
# print(list(bigrams(random_sentence, pad_right=True)))
# for trg in (ngrams(random_sentence, 4,
#                    pad_right=True, right_pad_symbol='</s>',
#                    pad_left=True, left_pad_symbol='<s>')):
#     print(trg)
target_speeches = ['1789-Washington.txt', '1861-Lincoln.txt', '2001-Bush.txt']
ngr = {}
# tokens
for text in target_speeches:
    data = inaugural.words(text)
    for trg in (ngrams(data, 2)):
        if trg not in ngr:
            ngr[trg] = 1
        else: ngr[trg] += 1
ngr = sorted(ngr.items(), key=lambda kv: kv[1], reverse= True)
# sentences
bigr_of_text = []
for text in target_speeches:
    data = inaugural.sents(text)
    bigr_of_text += (ngrams(data, 2))

print(bigr_of_text)
# a = FreqDist(bigr_of_text)
# print(a.most_common(5))