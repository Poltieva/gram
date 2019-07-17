
# Lexical Resources
## How I Learned to Stop Worrying and Love NLTK

# Part IV: Making Predictions

# Frequency and probability
### For NLP, frequency of an item in your corpus is pretty much its probability.
### How likely are you to find the word 'American' in the inaugural corpus?
### What is the probability of 'Klingon' encounter in this corpus?


```python
import nltk
from nltk import FreqDist
from nltk.corpus import inaugural
fd = FreqDist(inaugural.words())
print(fd.freq('the'))
print(fd.freq('we'))
print(fd.freq('American'))
print(fd.freq('unity'))
print(fd.freq('Klingon'))
```

    0.06368408412529591
    0.007829279171098226
    0.0010086801386077469
    0.0001921295502109994
    0.0


# Frequencies vs. probabilities
### What is the probability of Billy being a unicorn if you know that Billy is a rainbow-colored unicorn?


<img src="images/unicorn.jpg" alt="Drawing" style="height: 15em;" align="center"/>

### P(Billy == unicorn) = 1, but the frequency of the event 'Billy being a unicorn'... well... realistically... 0

# Frequencies vs. probabilities
### Beware of fast conclusion!
### If there are no Klingon in your corpus, that doesn't make the probability of encountering a Klingon in text 0.
### Let's say `it's close to zero, given our data`.

### And vice versa, if every sentence in your data ends with a period, that doesn't mean all English sentences end with a period.
### Let's say `the probability of a period at the end of a sentence is close to 1, given our data`.

# Jumping to conclusions: how (not) to
### Remember TF-IDF?
### Consider a linguist who used TF-IDF to build a topic classifier for the news articles.
### It fairly well distinguishes between 'Politics', 'Sports', 'TV', 'Culture' etc.
### Until one day it doesn't.
### Turns out, 'Politics' section is overwhelmed by recipes, Octoberfest news, and other weird stuff.

# Investigation
### The culprit soon was found: the word 'pretzel' had very, very high score in the TF-IDF dictionary.

![pretzel](images/pretzel.jpg)

# Language models

![lm](images/deathstar.jpg)

# Sequences in a language model
### Unigrams
### Bigrams
### Trigrams
### N-grams

# Unigrams


```python
random_text = "I love turtles."
random_words = ["I", "love", "turtles", "more", "than", "you", "ever", "will", "!"]
```


```python
char_unigrams = [c for c in random_text]
word_unigrams = [w for w in random_words]
print(char_unigrams)
print(word_unigrams)
```

    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 't', 'u', 'r', 't', 'l', 'e', 's', '.']
    ['I', 'love', 'turtles', 'more', 'than', 'you', 'ever', 'will', '!']


# Bigrams


```python
from nltk.util import bigrams, trigrams, ngrams
print(list(bigrams(random_text)))
print(list(bigrams(random_words)))
```

    [('I', ' '), (' ', 'l'), ('l', 'o'), ('o', 'v'), ('v', 'e'), ('e', ' '), (' ', 't'), ('t', 'u'), ('u', 'r'), ('r', 't'), ('t', 'l'), ('l', 'e'), ('e', 's'), ('s', '.')]
    [('I', 'love'), ('love', 'turtles'), ('turtles', 'more'), ('more', 'than'), ('than', 'you'), ('you', 'ever'), ('ever', 'will'), ('will', '!')]


# Trigrams and n-grams


```python
print(list(trigrams(random_text)))
print(list(trigrams(random_words)))
```

    [('I', ' ', 'l'), (' ', 'l', 'o'), ('l', 'o', 'v'), ('o', 'v', 'e'), ('v', 'e', ' '), ('e', ' ', 't'), (' ', 't', 'u'), ('t', 'u', 'r'), ('u', 'r', 't'), ('r', 't', 'l'), ('t', 'l', 'e'), ('l', 'e', 's'), ('e', 's', '.')]
    [('I', 'love', 'turtles'), ('love', 'turtles', 'more'), ('turtles', 'more', 'than'), ('more', 'than', 'you'), ('than', 'you', 'ever'), ('you', 'ever', 'will'), ('ever', 'will', '!')]



```python
print(list(ngrams(random_text, 5)))
print(list(ngrams(random_words, 5)))
```

    [('I', ' ', 'l', 'o', 'v'), (' ', 'l', 'o', 'v', 'e'), ('l', 'o', 'v', 'e', ' '), ('o', 'v', 'e', ' ', 't'), ('v', 'e', ' ', 't', 'u'), ('e', ' ', 't', 'u', 'r'), (' ', 't', 'u', 'r', 't'), ('t', 'u', 'r', 't', 'l'), ('u', 'r', 't', 'l', 'e'), ('r', 't', 'l', 'e', 's'), ('t', 'l', 'e', 's', '.')]
    [('I', 'love', 'turtles', 'more', 'than'), ('love', 'turtles', 'more', 'than', 'you'), ('turtles', 'more', 'than', 'you', 'ever'), ('more', 'than', 'you', 'ever', 'will'), ('than', 'you', 'ever', 'will', '!')]


# Google Ngram Viewer

![google ngrams](images/google-ngrams.png)
[Google Ngrams](https://books.google.com/ngrams/graph?content=machine+learning%2Cdeep+learning&year_start=1800&year_end=2008&corpus=17)

# Longer texts


```python
random_sentence = inaugural.sents('2009-Obama.txt')[1]
for trg in ngrams(random_sentence, 3):
    print(trg)
```

    ('I', 'stand', 'here')
    ('stand', 'here', 'today')
    ('here', 'today', 'humbled')
    ('today', 'humbled', 'by')
    ('humbled', 'by', 'the')
    ('by', 'the', 'task')
    ('the', 'task', 'before')
    ('task', 'before', 'us')
    ('before', 'us', ',')
    ('us', ',', 'grateful')
    (',', 'grateful', 'for')
    ('grateful', 'for', 'the')
    ('for', 'the', 'trust')
    ('the', 'trust', 'you')
    ('trust', 'you', 'have')
    ('you', 'have', 'bestowed')
    ('have', 'bestowed', ',')
    ('bestowed', ',', 'mindful')
    (',', 'mindful', 'of')
    ('mindful', 'of', 'the')
    ('of', 'the', 'sacrifices')
    ('the', 'sacrifices', 'borne')
    ('sacrifices', 'borne', 'by')
    ('borne', 'by', 'our')
    ('by', 'our', 'ancestors')
    ('our', 'ancestors', '.')


# Including beginning and end


```python
print(list(bigrams(random_sentence, pad_right=True)))
```

    [('I', 'stand'), ('stand', 'here'), ('here', 'today'), ('today', 'humbled'), ('humbled', 'by'), ('by', 'the'), ('the', 'task'), ('task', 'before'), ('before', 'us'), ('us', ','), (',', 'grateful'), ('grateful', 'for'), ('for', 'the'), ('the', 'trust'), ('trust', 'you'), ('you', 'have'), ('have', 'bestowed'), ('bestowed', ','), (',', 'mindful'), ('mindful', 'of'), ('of', 'the'), ('the', 'sacrifices'), ('sacrifices', 'borne'), ('borne', 'by'), ('by', 'our'), ('our', 'ancestors'), ('ancestors', '.'), ('.', None)]



```python
print(list(trigrams(random_sentence, pad_right=True)))
```

    [('I', 'stand', 'here'), ('stand', 'here', 'today'), ('here', 'today', 'humbled'), ('today', 'humbled', 'by'), ('humbled', 'by', 'the'), ('by', 'the', 'task'), ('the', 'task', 'before'), ('task', 'before', 'us'), ('before', 'us', ','), ('us', ',', 'grateful'), (',', 'grateful', 'for'), ('grateful', 'for', 'the'), ('for', 'the', 'trust'), ('the', 'trust', 'you'), ('trust', 'you', 'have'), ('you', 'have', 'bestowed'), ('have', 'bestowed', ','), ('bestowed', ',', 'mindful'), (',', 'mindful', 'of'), ('mindful', 'of', 'the'), ('of', 'the', 'sacrifices'), ('the', 'sacrifices', 'borne'), ('sacrifices', 'borne', 'by'), ('borne', 'by', 'our'), ('by', 'our', 'ancestors'), ('our', 'ancestors', '.'), ('ancestors', '.', None), ('.', None, None)]



```python
for trg in (ngrams(random_sentence, 4,
                   pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')):
    print(trg)
```

    ('<s>', '<s>', '<s>', 'I')
    ('<s>', '<s>', 'I', 'stand')
    ('<s>', 'I', 'stand', 'here')
    ('I', 'stand', 'here', 'today')
    ('stand', 'here', 'today', 'humbled')
    ('here', 'today', 'humbled', 'by')
    ('today', 'humbled', 'by', 'the')
    ('humbled', 'by', 'the', 'task')
    ('by', 'the', 'task', 'before')
    ('the', 'task', 'before', 'us')
    ('task', 'before', 'us', ',')
    ('before', 'us', ',', 'grateful')
    ('us', ',', 'grateful', 'for')
    (',', 'grateful', 'for', 'the')
    ('grateful', 'for', 'the', 'trust')
    ('for', 'the', 'trust', 'you')
    ('the', 'trust', 'you', 'have')
    ('trust', 'you', 'have', 'bestowed')
    ('you', 'have', 'bestowed', ',')
    ('have', 'bestowed', ',', 'mindful')
    ('bestowed', ',', 'mindful', 'of')
    (',', 'mindful', 'of', 'the')
    ('mindful', 'of', 'the', 'sacrifices')
    ('of', 'the', 'sacrifices', 'borne')
    ('the', 'sacrifices', 'borne', 'by')
    ('sacrifices', 'borne', 'by', 'our')
    ('borne', 'by', 'our', 'ancestors')
    ('by', 'our', 'ancestors', '.')
    ('our', 'ancestors', '.', '</s>')
    ('ancestors', '.', '</s>', '</s>')
    ('.', '</s>', '</s>', '</s>')


# DIY time
### Take 3 texts from the inaugural corpus
### Gather ngrams (from bigrams, trigrams and 5-grams) from these texts
### Print out 5 most frequent ngrams of length 2, 3 and 5 for each of the texts
### Which length of ngrams seems more informative?


```python
from solutions.freq_ngrams import *
texts = ['1797-Adams.txt', '1861-Lincoln.txt', '2001-Bush.txt']
print_most_frequent_grams(texts, 4)
```

    1797-Adams.txt
                                       of the people , ~ 3
                                 the people of America ~ 3
                               the Constitution of the ~ 3
                            Constitution of the United ~ 3
                                  of the United States ~ 3
    1861-Lincoln.txt
                                  of the United States ~ 3
                              the Constitution and the ~ 3
                             The Constitution does not ~ 3
                       Constitution does not expressly ~ 3
                                does not expressly say ~ 3
    2001-Bush.txt
                                      America , at its ~ 4
                                         , at its best ~ 4
                                         at its best , ~ 4
                                        our nation ' s ~ 3
                                         its best , is ~ 3


## Why sequence probabilities matter
### --- speech/handwriting recognition
###  --- spelling correction
###  --- machine translation
###  --- augumentative communication
###  --- text generation
### You name it!


# How does a prediction work?
### Suppose we want to predict the next word
### We can do that with word counts:

![cantblame](images/cantblame.png)

# Let's say the web is our corpus


```python
c_me = 1910000
c_blame = 29000000
p_me = (round ((c_me / c_blame), 3))
print("Probability of 'me' after 'you can't blame' is {}".format(p_me))
```

    Probability of 'me' after 'you can't blame' is 0.066



```python
c_gravity = 49500
c_yourself = 403000
c_aliens = 332
print("Probability of 'yourself' after 'you can't blame' is {}".format((round ((c_yourself / c_blame), 3))))
print("Probability of 'gravity' after 'you can't blame' is {}".format((round ((c_gravity / c_blame), 3))))
print("Probability of 'aliens' after 'you can't blame' is {}".format((round ((c_aliens / c_blame), 5))))
```

    Probability of 'yourself' after 'you can't blame' is 0.014
    Probability of 'gravity' after 'you can't blame' is 0.002
    Probability of 'aliens' after 'you can't blame' is 1e-05


# What about longer sentences?
### Using web search (don't forget quotations), try to determine the probability of eating a whole pack of `biscuits`, `cookies`, `nachos`, or your favorite midnight snack.
### Let the starting phrase be `Yesterday I ate a whole pack of ...`

# Chain rule of probability
## Probability of a word w depends on the joint probability of the words before it:


![chainrule](images/chainrule.png)

# Chain rule of probability: an example

## P(May the Force be with you) =
## &emsp;&emsp;P(May) x 
## &emsp;&emsp;&emsp;P(the|May) x 
## &emsp;&emsp;&emsp;&emsp;P(Force|May the) x 
## &emsp;&emsp;&emsp;&emsp;&emsp;P(be|May the Force) x 
## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(with|May the Force be) x 
## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(you|May the Force be with)

# That doesn't help with zeroes!
### (Un)fortunately, the language is far too creative.
### This formula will yield zero every time when at least one probability in the chain is zero.
### That is, if the data does not contain `I hate licorice`, the probability of `I hate licorice candies` is equal to the probability of `I hate licorice chairs` — both are 0.

# Approximation

![new-hope](images/new-hope.jpg)

# Markov assumption
## The probability of a word depends only on the previous word.

![markov](images/markov.png)

### This enables us to predict the probability of finding 'chairs' or 'candy' solely based on the previous 'licorice', because we assume that lacorice lovers and haters are irrelevant for this issue.

# Markov assumption generalization
## (for calculating probability of a whole sequence of words)

![Markov assumption gen](images/markov-gen.png)

# Chain rule with Markov assumption

### P(May the Force be with you) =
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(May|`<s>`) x 
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(the|May) x 
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(Force|the) x 
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(be|Force) x 
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(with|be) x 
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P(you|with)

### Now the probability of 'you' depends solely on 'with' (P(you|with)) and not on the whole previous sequence — P(you|May the Force be with)

### That's how Markov model works.

# Erm... but how do I calculate this?

![thisisfine](images/thisisfine.jpg)

# Maximum likelihood estimation (MLE)
### An intuitive approach to probabilities estimation:
### Get the count of an ngram and normalize it so it fits between 0 and 1
### Normalize == divide by the sum of counts of all ngrams that have the same beginning

# MLE formula for bigrams

![mle](images/mle.png)

# No need to panic! We can simplify it!
## The sum of all bigram counts that start with a given word Wn−1 must be equal to the unigram count for that word.

![mle-simple](images/mle-simple.png)

# Calculating MLE

![sam](images/sam.png)

![sam-res1](images/sam-res1.png)

![sam-res2](images/sam-res2.png)

# Let's code it!
## First, we build bigrams counts dictionary (don't forget to add `<s>` and `</s>`) 
## And unigrams dictionary (how about  `<s>` and `</s>` here too?)


```python
from nltk.tokenize import word_tokenize
examples = ["I am Sam", "Sam I am", "I do not like green eggs and ham"]
unigrams_list = []
bigrams_list = []
for sentence in examples:
    tokens = word_tokenize(sentence)
    s_grams = bigrams(tokens,
                   pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')
    unigrams_list += tokens + ['<s>', '</s>']
    bigrams_list += s_grams
bigrams_d = FreqDist(bigrams_list)
unigrams_d = FreqDist(unigrams_list)
    
def bigram_prob(bigram, unigrams_d, bigrams_d):
    b = tuple(bigram.split(' '))
    bigram_count = bigrams_d[b]
    first_word_bigrams_count = unigrams_d[bigram.split(' ')[0]]
    prob =  bigram_count/first_word_bigrams_count
    print("P({}|{}) = {}".format(b[1], b[0], round(prob, 2)))
```


```python
bigram_prob("<s> I", unigrams_d, bigrams_d)
bigram_prob("<s> Sam", unigrams_d, bigrams_d)
bigram_prob("I am", unigrams_d, bigrams_d)
bigram_prob("Sam </s>", unigrams_d, bigrams_d)
bigram_prob("am Sam", unigrams_d, bigrams_d)
bigram_prob("I do", unigrams_d, bigrams_d)
```

    P(I|<s>) = 0.67
    P(Sam|<s>) = 0.33
    P(am|I) = 0.67
    P(</s>|Sam) = 0.5
    P(Sam|am) = 0.5
    P(do|I) = 0.33


# Calculating sentence probability
## What we have:
### --- Markov chain rule
### --- Maximum likelihood estimation
### --- Bigrams and unigrams counts
## Problems:
### --- Beware of zeroes!

# Zeroes problem
### We've already included non-existent `<s>` and `</s>` in unigrams
### But what if there's a bigram that's not on the list?
### What if we have `I am` but not `am I` in the corpus?

# Example: Shakespeare corpus
### Number of tokens = 884,647, vocabulary = 29,066
### Shakespeare	produced ~ 300,000 bigram types	out	of 844 million possibilities (pow(vocabulary, 2))
### So 99.96% of the possible bigrams have never appeared in the corpus

# When you try to cover the gaps in your data

![thatstoomuch](images/thatstoomuch.jpg)

# Laplace smoothing (aka Add-one estimation)
### Pretend you have seen any n-gram one more time than you actually did
### Add to the new vocabulary length (number of unique n-1-grams) to the denominator

![laplace](images/laplace.png)


```python
def add_one(gram, grams_dict):
    if gram in grams_dict:
        return grams_dict[gram] + 1
    else:
        return 1

def smooth_prob(gram, unigrams_d, bigrams_d):
    b = tuple(gram.split(' '))
    bigram_count = add_one(b, bigrams_d)
    first_word_bigrams_count  = add_one(b[0], unigrams_d)
    prob = bigram_count/(first_word_bigrams_count + len(unigrams_d))
    print("P({}|{}) = {}".format(b[1], b[0], round(prob, 2)))

print("Before smoothing:")
bigram_prob("<s> I", unigrams_d, bigrams_d)
bigram_prob("<s> If", unigrams_d, bigrams_d)
print("After smoothing:")
smooth_prob("<s> I", unigrams_d, bigrams_d)
smooth_prob("<s> If", unigrams_d, bigrams_d)
```

    Before smoothing:
    P(I|<s>) = 0.67
    P(If|<s>) = 0.0
    After smoothing:
    P(I|<s>) = 0.19
    P(If|<s>) = 0.06


# Smoothing techniques
### Add-one smoothing has its drawbacks — it shares way to much probability mass with the unknown ngrams
### There are many other smoothing algorithms aroud:
### • Additive smoothing
### • Good-Turing estimate
### • Katz smoothing (backoff)
### • Jelinek-Mercer smoothing (interpolation)
### • Kneser-Ney smoothing

# DIY time: calculating sentence probability
### 1. Choose your corpus (or corpora) and collect unigram and bigram counts
### 2. Calculate probability for each bigram in the sentence using Markov assumption
### 3. Don't forget to apply smoothing so that zeroes don't bug you
### 4. Multiply the probabilities, so you can find out:
### --- Who of the United States Presidents is more likely to say "The Vikings are nearing our borders."?
### --- Which sentence is more likely in American English "The pair was dancing" or "The pair were dancing"?
### --- Where in the Brown corpus are you more likely to find a phrase "The spacecraft has reached Alpha Centauri"?


```python
from nltk.corpus import brown
from solutions.sentence_prob import *
uni_counts, bigram_counts = gather_grams(brown.sents())
test_sentences = ["I saw a van", "eyes awe of an"]
for test in test_sentences:
    tokens = word_tokenize(test)
    sent_grams = bigrams(tokens,
                       pad_right=True, right_pad_symbol='</s>',
                       pad_left=True, left_pad_symbol='<s>')
    prob = score_sentence(sent_grams, uni_counts, bigram_counts)
    print("Probability of '{}' = {:.2e}".format(test, prob))
```

    Probability of 'I saw a van' = 1.27e-18
    Probability of 'eyes awe of an' = 2.81e-22



```python
tokens = word_tokenize("The spaceship has reached Alpha Centauri.")
sent_grams = list(bigrams(tokens,
                       pad_right=True, right_pad_symbol='</s>',
                       pad_left=True, left_pad_symbol='<s>'))
texts = ['romance', 'news', 'science_fiction']
for text in texts:
    uni_c, bigram_c = gather_grams(brown.sents(categories=text))
    prob = score_sentence(sent_grams, uni_c, bigram_c)
    print("Probability for {} = {}".format(text, prob))
```

    Probability for romance = 1.33881966768474e-26
    Probability for news = 8.736592675747847e-28
    Probability for science_fiction = 2.7405567629136283e-24


# Song writer!
## Your corpus — lyrics of your favourite artist
## Write a function that generates similar lyrics!

# The idea
### Generate ngrams counts from you data
### Give the `song_generator` a word to start
### Let the song_generator come up with the second word
### ... and with the third, given the second...
### ... and so on!
### That's Markov assumption in action!

# Step-by-step song generation:
### 1. Explore your data (you might want to get rid of all those [Chorus] things)
### 2. Collect ngram counts from tokens of your corpus
### 3. Write a function that finds 10 most common bigrams, given the first word, and chooses one randomly (`random.choice()`) 
### 4. Write a function `generate_line(first_word)` that repeatedly chooses the next word based on the previous one (don't forget to end the loop)
### 5. Write a function `generate_song(first_word)` that invokes `generate_line` 10 times (don't forget to provide a starting word every time) and prints the song (prettily)
### 6. Have fun!


```python
import solutions.songgenerator as gen
```


```python
Blind_Guardian_Gen = SongGenerator("Blind_Guardian", 3)
Blind_Guardian_Gen.generate_song("I")
```

    I can't free my mind
    You've got out well
    Now they're hiding
    And a vision of past dreams comes true
    In asylum's cage
    I will wait for execution
    There must be a sign for the bark
    A crow, a storm
    You coward
    Now let the play begin


# If bigram song generation seemed too easy:
### 1. Try generalizing your song generation to n-grams. Which sequence length works better?
### 2. Solve 'zero problem': what should the generator do if the first word is unknown?
### 3. Try making an acronym generator so that every line of your song starts with a letter from the artist name.
### 4. How about adding rhymes? (Try [pronouncing 0.2.0](https://pypi.org/project/pronouncing/))
### 5. Maybe a chorus then? How would you choose lines for it?


```python
Blind_Guardian_Gen = SongGenerator("Blind_Guardian", 5)
Blind_Guardian_Gen.generate_acronym()
```

    By the spell of gold
    Like whispering echos in the wind
    If there's some way in
    Nothing is real
    Did you hear my crying?
    
    Go out and get it
    Until one day he smiled
    Ashes to ashes and dust will be dust
    Risin' up for Jerusalem
    Dark realms I went through
    Insanity said coldy
    And we praise the handsome knight
    Now break through


# Useful links:
### [Smoothing tutorial](https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf)
### [Mathematical proof of Add-one smoothing](http://people.cs.georgetown.edu/nschneid/cosc572/f16/09_LM_slides.pdf)
### [N-gram Language Model](https://web.stanford.edu/~jurafsky/slp3/3.pdf) (a chapter from Speech and Language Processing by Dan Jurafsky)
### [Types of Language Models](https://nlp.stanford.edu/IR-book/html/htmledition/language-models-1.html) (from Introduction to Information Retrieval by Christopher Manning)
### [Video lectures by Dan Jurafsky](https://www.youtube.com/watch?v=hB2ShMlwTyc) (we've covered lectures 12-16, but there's so many interesting thing ahead!)


```python

```
