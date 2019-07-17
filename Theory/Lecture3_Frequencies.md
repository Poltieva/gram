
# Linguistic Resources
## How I Learned to Stop Worrying and Love NLTK

# Part 3: Frequencies

# A quick warm-up first
## Let's load a brand new corpus from XML files
## We are going to word with news from British National Corpus (BNC)

# Step-by-step guide

## Explore the data before trying to do anything with it.


```python
bnc_sample = open("data/bnc_baby/news/A1E.xml").read()
print(bnc_sample[2651:5000])
```

    
    <wtext type="NEWS"><div level="1" n="891002 edition -- Business and City Page 23"><head type="MAIN">
    <s n="1"><w c5="AJS" hw="late" pos="ADJ">Latest </w><w c5="AJ0" hw="corporate" pos="ADJ">corporate </w><w c5="NN1" hw="unbundler" pos="SUBST">unbundler </w><w c5="VVZ" hw="reveal" pos="VERB">reveals </w><w c5="AJ0" hw="laid-back" pos="ADJ">laid-back </w><w c5="NN1" hw="approach" pos="SUBST">approach</w><c c5="PUN">: </c><w c5="NP0" hw="roland" pos="SUBST">Roland </w><w c5="NP0" hw="franklin" pos="SUBST">Franklin</w><c c5="PUN">, </c><w c5="PNQ" hw="who" pos="PRON">who </w><w c5="VBZ" hw="be" pos="VERB">is </w><w c5="VVG" hw="lead" pos="VERB">leading </w><w c5="AT0" hw="a" pos="ART">a </w><w c5="NN0" hw="697m" pos="SUBST">697m </w><w c5="NN1" hw="pound" pos="SUBST">pound </w><w c5="NN1" hw="break-up" pos="SUBST">break-up </w><w c5="NN1-VVB" hw="bid" pos="SUBST">bid </w><w c5="PRP" hw="for" pos="PREP">for </w><w c5="NP0" hw="drg" pos="SUBST">DRG</w><c c5="PUN">, </c><w c5="NN2-VVZ" hw="talk" pos="SUBST">talks </w><w c5="PRP" hw="to" pos="PREP">to </w><w c5="NP0" hw="frank" pos="SUBST">Frank </w><w c5="NP0" hw="kane" pos="SUBST">Kane</w></s></head><head type="BYLINE">
    <s n="2"><w c5="PRP" hw="by" pos="PREP">By </w><w c5="NP0" hw="frank" pos="SUBST">FRANK </w><w c5="NP0-NN1" hw="kane" pos="SUBST">KANE</w></s></head><p>
    <s n="3"><w c5="PNP" hw="it" pos="PRON">IT </w><w c5="VVZ" hw="seem" pos="VERB">SEEMS </w><w c5="CJT" hw="that" pos="CONJ">that </w><w c5="NP0" hw="roland" pos="SUBST">Roland </w><w c5="NP0" hw="franklin" pos="SUBST">Franklin</w><c c5="PUN">, </c><w c5="AT0" hw="the" pos="ART">the </w><w c5="AJS" hw="late" pos="ADJ">latest </w><w c5="NN1" hw="unbundler" pos="SUBST">unbundler </w><w c5="TO0" hw="to" pos="PREP">to </w><w c5="VVI" hw="appear" pos="VERB">appear </w><w c5="PRP" hw="in" pos="PREP">in </w><w c5="AT0" hw="the" pos="ART">the </w><w c5="NP0" hw="uk" pos="SUBST">UK</w><c c5="PUN">, </c><w c5="VHZ" hw="have" pos="VERB">has </w><w c5="VVN" hw="make" pos="VERB">made </w><w c5="AT0" hw="a" pos="ART">a </w><w c5="AJ0" hw="fatal" pos="ADJ">fatal </w><w c5="NN1" hw="error" pos="SUBST">error </w><w c5="PRP" hw="in" pos="PREP">in </w><w c5="AT0" hw="the" pos="ART">the </w><w c5="NN1" hw="preparation" pos="SUBST">preparation </w><w c5="PRF" hw="of" pos="PREP">of </w><w c5="DPS" hw="he" pos="PRON">his 


### Create file:
### --- `bnc_sentences_tagged.txt` to store sentences with tags
### Import lxml
### Go through elements of the tree
### Find sentences
### --- Concatenate a string of word/tag pairs of the sentence and write this to `bnc_sentences_tagged.txt`



```python
import solutions.parse_bnc as parse
parse.parse_files("data/bnc_baby/news/")
```


```python
open('data/bnc_sentences_tagged.txt', 'r').read().split('\n')[40:50]
```




    ["I||PNP 'm||VBB not||XX0 daft||AJ0",
     'My||DPS brain||NN1 is||VBZ perfectly||AV0 unimpaired||AJ0 writes||VVZ Elaine||NP0 at||PRP the||AT0 end||NN1 of||PRF her||DPS list||NN1',
     'The||AT0 nurses||NN2 are||VBB nice||AJ0-AV0 well-intentioned||AJ0 young||AJ0 girls||NN2 who||PNQ do||VDB their||DPS best||AJS',
     'But||CJC because||CJS they||PNP have||VHB to||TO0 leave||VVI by||PRP 10pm||AV0 all||DT0 they||PNP have||VHB time||NN1 for||PRP are||VBB the||AT0 basic||AJ0 tasks||NN2 cooking||VVG-NN1 dinner||NN1 feeding||VVG Elaine||NP0 taking||VVG off||AVP-PRP her||DPS make-up||NN1 and||CJC getting||VVG her||DPS ready||AJ0 for||PRP bed||NN1',
     'Many||DT0 of||PRF them||PNP are||VBB not||XX0 used||VVN to||PRP disabled||AJ0 people||NN0 and||CJC being||VBG temporary||AJ0 they||PNP rarely||AV0 get||VVB to||TO0 know||VVI her||PNP anyway||AV0',
     "Elaine||NP0 ca||VM0 n't||XX0 talk||VVI and||CJC that||DT0-CJT can||VM0 be||VBI very||AV0 disconcerting||AJ0 for||PRP the||AT0 nurses||NN2 says||VVZ Sylvia||NP0-NN1",
     'Elaine||NP0 interrupts||VVZ',
     'She||PNP does||VDZ not||XX0 need||VVI nurses||NN2 in||PRP uniform||NN1-AJ0 she||PNP almost||AV0 shouts||VVZ just||AV0 because||CJS she||PNP is||VBZ disabled||AJ0-VVN it||PNP does||VDZ not||XX0 mean||VVI she||PNP is||VBZ medically||AV0 ill||AJ0',
     'There||EX0 is||VBZ no||AT0 conversation||NN1 with||PRP the||AT0 nurses||NN2 she||PNP says||VVZ',
     'My||DPS day||NN1 ends||VVZ-NN2 at||PRP five||CRD']



# Open your data
## 1. Create `bnc_tokens` which stores the list of all BNC words
## 2. Create `bnc_tagged` which stores the list of pairs [word, tag]


```python
import nltk
from nltk import Text
from nltk.tokenize import word_tokenize
bnc_tokens = []
bnc_tagged = []
for sent in open('data/bnc_sentences_tagged.txt', 'r').readlines():
    for token in word_tokenize(sent):
        splt = token.split('||')
        if len(splt) > 1:
            bnc_tagged.append([splt[0], splt[1]])
            bnc_tokens.append(splt[0])
bnc = Text(bnc_tokens)
```


```python
print(bnc_tokens[201:211])
print(bnc_tagged[201:211])
```

    ['In', 'the', 'mornings', 'Elaine', 'can', 'not', 'get', 'up', 'before', '9am']
    [['In', 'PRP'], ['the', 'AT0'], ['mornings', 'NN2'], ['Elaine', 'NP0'], ['can', 'VM0'], ['not', 'XX0'], ['get', 'VVI'], ['up', 'AVP'], ['before', 'PRP'], ['9am', 'AV0']]


# Look into your newly acquired data.
## Compare Brown news data and your BNC news. Which queens are mentioned there?
### (You'll need to initialize an nltk `Text()` from the list of bnc_tokens first.)


```python
from nltk.corpus import brown
from nltk.text import Text  

brown_news = Text(brown.words(categories="news"))
brown_news.concordance("queen")
```

    Displaying 5 of 5 matches:
    n fraternity . Their Majesties , The Queen of Carnival and The Queen of Comus ,
    ties , The Queen of Carnival and The Queen of Comus , have jointly issued invit
    ers' dances '' . The mother of young queen , Mrs. G. Henry Pierson Jr. chose a 
    hose daughter was also a maid to the queen , wore an ashes of roses slipper sat
     Feringa Jr. , last year's Achaeans' queen , chose an eggshell white filmy lace



```python
bnc.concordance("queen")
```

    Displaying 25 of 109 matches:
    -high figurines of King Birendra and Queen Aishwarya The King is said to be a r
    r Cecil who had been considering the Queen Elizabeth II Stakes at Ascot believe
    it TEARS FOR CAROLINE CHARLES FAWCUS QUEEN OF SHANNON had tears and not champag
    dent last week Caroline looked after Queen Of Shannon riding her at home She lo
    he funeral is in Derbyshire he added Queen Of Shannon 's jockey Michael Tebbutt
     going stays soft she 'll go for the Queen Elizabeth at Ascot otherwise we 'll 
    rop up in this week 's top event the Queen Elizabeth 11 Stakes at Ascot on Satu
    day It was like this when he won the Queen Elizabeth last year so I wo n't mind
    to miss the meeting 's highlight the Queen Elizabeth II Stakes while Second Set
     seven years with promising newcomer Queen 's View GLOUCESTER trainer Nigel Twi
    re and is poised to prove it against Queen 's Park Rangers tomorrow Manchester 
    the rain she needs has fallen on the Queen 's racetrack in the past week to mak
     judged guilty of violating a beauty queen whom he was convicted of luring to h
    hamp yesterday all set to be crowned Queen next year IT 'S A FACT WYC-WHACK RUN
    s By JOE LOVEJOY Tottenham Hotspur 3 Queen 's Park Rangers 2 THE GROUND is begi
    y outlined the contents of its first Queen 's Speech including a commitment to 
    a will be delivered in future BOSTON Queen 's support THE parents of a boy who 
    n sent a message of support from the Queen Leslie and Linda Skelhorne of Runcor
    f traffic were blocked on the nearby Queen Elizabeth Bridge LONDON New Euro-bis
    oyal travelled in an aircraft of The Queen 's Flight Major Nicholas Barne was i
    ness travelled in an aircraft of The Queen 's Flight ROYAL ENGAGEMENTS The Prin
    harter 1940 338 people died when the Queen Mary liner collided with the British
    ut as exclusive a tag for a house as Queen Elizabeth slept here Hunt and his ev
     Rushdie had grievously insulted the Queen Margaret Thatcher and all white wome
    Picon thereby ruining both drinks as Queen Victoria reputedly did with claret a


# How about searching some phrases in the tagged data?
### Try calling your `search_by_tag_sequence()` function on BNC tagged tokens list.


```python
import solutions.search_tags as search_tags
res = search_tags.search_by_tag_sequence(['DT', '*', 'JJ', 'NN*'], bnc_tagged)
res[:10]
```




    []



![6-vs-9-perspective](images/6-vs-9-perspective.jpg)

# Explore the tagset of BNC
## You can print it out with examples, for instance


```python
tags = {}
for token in bnc_tagged:
    if token[1] not in tags:
        tags[token[1]] = token[0]
for tag in sorted(tags.items())[:10]:
    print("{:>{tagl}} -- {ex}".format(tag[0], tagl = 7, ex = tag[1]))
```

        AJ0 -- Lively
    AJ0-AV0 -- alone
    AJ0-NN1 -- right
    AJ0-VVD -- shrivelled
    AJ0-VVG -- exhausting
    AJ0-VVN -- disabled
        AJC -- worse
        AJS -- best
        AT0 -- the
        AV0 -- severely


## How is it different from the tagsets your function was used to?
## Come up with a sequence of tags for the new data, that would work identically to
## `['DT', '*', 'JJ', 'NN*']` for Brown universal tagset
## Hint: if in trouble, look up for the [BNC tagset](http://www.natcorp.ox.ac.uk/docs/c5spec.html) online

# Sample output


```python
from solutions.search_tags import *
res = search_by_tag_sequence(['VVN', '*', 'VVN'], bnc_tagged)
res[:10]
```




    [[['thought', 'VVN'], ['about', 'PRP'], ['regarded', 'VVN']],
     [['seen', 'VVN'], ['and', 'CJC'], ['heard', 'VVN']],
     [['swollen', 'VVN'], ['almost', 'AV0'], ['shut', 'VVN']],
     [['instituted', 'VVN'], ['FLASHMAN', 'NP0'], ['Warned', 'VVN']],
     [['helped', 'VVN'], ['and', 'CJC'], ['encouraged', 'VVN']],
     [['encouraged', 'VVN'], ['not', 'XX0'], ['discouraged', 'VVN']],
     [['relaxed', 'VVN'], ['and', 'CJC'], ['taken', 'VVN']],
     [['allowed', 'VVN'], ['out', 'AVP'], ['allowed', 'VVN']],
     [['lost', 'VVN'], ['or', 'CJC'], ['drawn', 'VVN']],
     [['got', 'VVN'], ['you', 'PNP'], ['taped', 'VVN']]]



# Why do word counts matter anyway?
### Language is creative and infinitely diverse, hence anything can be found in corpora.
### --- errors in corpora that were assumed to be mistake-free
### --- entities (be that words or syntactic structures) too rare to be assumed part of the language
### Number of word occurencies can give an insight both on the text and on the word

# Take a moment to determine the minimal frequency of a word to be added to a dictionary, for instance

![shwifty](images/get-shwifty.jpg)


```python
from nltk import FreqDist
brown_freqd = FreqDist(brown.words())
brown_freqd.most_common(10)
```




    [('the', 62713),
     (',', 58334),
     ('.', 49346),
     ('of', 36080),
     ('and', 27915),
     ('to', 25732),
     ('a', 21881),
     ('in', 19536),
     ('that', 10237),
     ('is', 10011)]




```python
print(brown_freqd["swiftly"])
print(brown_freqd["shifty"])
print(brown_freqd["shwifty"])
```

    14
    1
    0


# Getting the frequencies out of FreqDist


```python
for word in brown_freqd.most_common(10):
    print("{} ~ {}".format(word[0], round(brown_freqd.freq(word[0]), 3)))
```

    the ~ 0.054
    , ~ 0.05
    . ~ 0.042
    of ~ 0.031
    and ~ 0.024
    to ~ 0.022
    a ~ 0.019
    in ~ 0.017
    that ~ 0.009
    is ~ 0.009


# Hapaxes


```python
sorted(brown_freqd.hapaxes(), key = lambda w: len(w), reverse = True)[:20]
```




    ['nnuolapertar-it-vuh-karti-birifw-',
     "let's-make-your-house-our-club",
     'tris(hydroxymethyl)-aminometha',
     'thiocyanate-perchlorate-fluoro',
     'desegregation-from-court-order',
     'yielding-Mediterranian-woman-',
     'Braddock-against-the-Indians',
     'vertical-takeoff-and-landing',
     'L-5-vinyl-2-thio-oxazolidone',
     'Rundfunk-Sinfonie-Orchester',
     'mailed-fist-in-velvet-glove',
     'social-political-economical',
     'pressure-volume-temperature',
     'solar-corpuscular-radiation',
     'delicate-beyond-description',
     'composer-pianist-conductor',
     'psychological-intellectual',
     'all-something-or-the-other',
     'Scotch-Irish-Scandinavian',
     'Tshombe-Gizenga-Goa-Ghana']



# Zipf's law


```python
brown_freqd.plot(50)
```


![png](output_33_0.png)





    <matplotlib.axes._subplots.AxesSubplot at 0x13897def0>



# Conditional Frequency Distribution
### A tool to study frequency differences between the different kinds of texts
### Given a corpus divided into several categories, by genre, topic, author, etc., we can assume that each genre is a "condition".

# Frequency vs. Conditional frequency
### For a frequency distribution we were inputting a list of words:
### `>>> ["I", "want", "a", "cookie"]`
### For a conditional frequency distribution we will be inputting a list of tuples:
### `>>> [("I", "romance"), ("want", "romance"), ("a", "romance"), ("cookies", "romance"), ("She", "news"), ("was", "news"), ("seen", "news"), ("just", "news"), ("yesterday", "news")]`


```python
from nltk import ConditionalFreqDist
brown.categories()
```




    ['adventure',
     'belles_lettres',
     'editorial',
     'fiction',
     'government',
     'hobbies',
     'humor',
     'learned',
     'lore',
     'mystery',
     'news',
     'religion',
     'reviews',
     'romance',
     'science_fiction']



# Collecting conditional frequency distributions


```python
cats = ['mystery', 'adventure']
cfd = nltk.ConditionalFreqDist(
    (genre, word.lower())
    for genre in cats
    for word in brown.words(categories=genre))
print(cfd)
```

    <ConditionalFreqDist with 2 conditions>



```python
for cond in cfd.conditions():
    print(cond)
    print(cfd[cond].most_common(20))
    print()
```

    mystery
    [('.', 3326), ('the', 2817), (',', 2805), ('to', 1294), ('and', 1282), ('a', 1196), ('he', 1076), ('of', 913), ('was', 828), ('``', 740), ("''", 738), ('in', 695), ('?', 664), ('it', 653), ('i', 583), ('his', 565), ('that', 526), ('had', 520), ('on', 441), ('you', 416)]
    
    adventure
    [('.', 4057), ('the', 3780), (',', 3488), ('and', 1706), ('a', 1432), ('of', 1327), ('to', 1322), ('he', 1283), ('``', 998), ("''", 995), ('was', 919), ('in', 892), ('his', 846), ('i', 652), ('it', 637), ('had', 592), ('that', 533), ('?', 518), ('on', 469), ('her', 468)]
    


# Getting more info from conditional frequencies distribution


```python
for cond in cfd.conditions():
    print("question mark in {} - {} - {}".format(cond,
                                                 cfd[cond]["?"],
                                                 round(cfd[cond].freq("?"), 4)))
```

    question mark in mystery - 664 - 0.0116
    question mark in adventure - 518 - 0.0075



```python
cfd.tabulate(samples = ["ran", "fired", "thought", "guessed", "asked"])
```

                  ran   fired thought guessed   asked 
    adventure      33       6      62       1      34 
      mystery       7       3      54       2      45 


# NLTK word lists

# Names


```python
from nltk.corpus import names, stopwords, words
```


```python
print(names.words("male.txt")[:10])
print(names.words("female.txt")[:10])
```

    ['Aamir', 'Aaron', 'Abbey', 'Abbie', 'Abbot', 'Abbott', 'Abby', 'Abdel', 'Abdul', 'Abdulkarim']
    ['Abagael', 'Abagail', 'Abbe', 'Abbey', 'Abbi', 'Abbie', 'Abby', 'Abigael', 'Abigail', 'Abigale']


# English words vocabulary


```python
print(words.fileids())
```

    ['en', 'en-basic']



```python
print(len(words.words("en")))
print(len(words.words("en-basic")))
```

    235886
    850



```python
print(words.words("en")[:20])
print(words.words("en-basic")[:20])
```

    ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani', 'aardvark', 'aardwolf', 'Aaron', 'Aaronic', 'Aaronical', 'Aaronite', 'Aaronitic', 'Aaru', 'Ab', 'aba', 'Ababdeh', 'Ababua', 'abac']
    ['I', 'a', 'able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount']


# Stop words


```python
print(stopwords.fileids())
```

    ['arabic', 'azerbaijani', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'greek', 'hungarian', 'indonesian', 'italian', 'kazakh', 'nepali', 'norwegian', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish']



```python
print(sorted(stopwords.words('english')))
```

    ['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']


### Is this list enough? Do you see any flaws right away?

# It's cloudy!
## Let's collect word clouds for documents:
### 1. we need to lemmatize the words
### 2. we need to get most common lemmas from frequency distribution

### 0. Choose your document!
### --- import `inaugural` from nltk.corpus
### --- print out available texts with `inaugural.fileids()`
### --- choose two speeches!

# Step 1: lemmatization


```python
from solutions.tag_convert import *
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
```


```python
from nltk.corpus import inaugural
speech_tokens = inaugural.words('2001-Bush.txt')
lemmatized_t = lemmatize_tokens(speech_tokens)
print("Raw tokens:")
print(speech_tokens[:10])
print("Lemmatized:")
print(lemmatized_t[:10])
```

    Raw tokens:
    ['President', 'Clinton', ',', 'distinguished', 'guests', 'and', 'my', 'fellow', 'citizens', ',']
    Lemmatized:
    ['President', 'Clinton', ',', 'distinguish', 'guest', 'and', 'my', 'fellow', 'citizen', ',']


# Step 2: find most frequent words
### given a list of tokens, lemmatize it
### create a frequency distribution on lemmatized tokens
### choose most frequent 20 lemmas and print them out


```python
def get_keywords(tokens):
    lemmatized_tokens = lemmatize_tokens(tokens)
    fd = FreqDist(lemmatized_tokens)
    return [tpl[0] for tpl in fd.most_common(20)]
```


```python
from nltk.corpus import inaugural
print(get_keywords(inaugural.words('2001-Bush.txt')))
print(get_keywords(inaugural.words('2005-Bush.txt')))
```

    [',', '.', 'and', 'be', 'of', 'the', 'our', 'a', 'to', 'we', 'in', 'not', 'will', 'And', 'that', 'We', 'nation', 'it', 'for', 'I']
    [',', 'the', 'of', 'and', '.', 'be', 'our', 'in', 'to', 'have', 'that', 'we', 'a', 'freedom', 'will', 'by', 'America', '¡', 'for', 'on']


# Add a preprocessing step:
### let your `get_keywords` function go through tokens and remove from the list:
### 1. stop words
### 2. punctuation marks (and other non-alpha charaters of your choice)


```python
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
```


```python
print(get_keywords(inaugural.words('2001-Bush.txt')))
print(get_keywords(inaugural.words('2005-Bush.txt')))
```

    ['nation', 'america', 'us', 'citizen', 'story', 'country', 'american', 'time', 'call', 'life', 'must', 'every', 'common', 'new', 'many', 'freedom', 'ideal', 'promise', 'work', 'know']
    ['freedom', 'america', 'liberty', 'nation', 'every', 'american', 'one', 'country', 'time', 'see', 'come', 'world', 'citizen', 'day', 'history', 'hope', 'people', 'free', 'know', 'justice']


# More fun with frequencies: TF-IDF

## Term Frequency — Inverse Document Frequency, is a text mining technique that gives a numeric statistic as to how important a word is to a document in a collection or corpus.
## The idea is to find the most common words in a document that are also not so frequent in other documents, thus finding the words that characterize this document better.

# Term Frequency

![tf](images/tf.png)

# Let's count the importance of the word "linguistics" in a document "D"

### The TF (term frequency) is a frequency of a term in a given document.

### For example, a document "D" is of length 100 words. This document contains the term "linguistics" 12 times, so the TF for the word "linguistics" in a document "D" is

### `TF(linguistics, D) = 12/100 = 0.12`


## You might have noticed that we've already been counting TFs


```python
freq_dict = FreqDist(inaugural.words('2001-Bush.txt'))
```


```python
print("Count of the word 'nation': {0}".format(freq_dict["nation"]))
print("Term Frequency of the word 'nation': {0}".format(freq_dict.freq("nation")))
print("Number of words in the original document: {0}".format(freq_dict.N()))
print("Length of our lexicon: {0}".format(len(freq_dict)))

```

    Count of the word 'nation': 11
    Term Frequency of the word 'nation': 0.006027397260273973
    Number of words in the original document: 1825
    Length of our lexicon: 622


# Inverse Document Frequency

![idf](images/idf.png)

### The IDF of a word is the measure of how significant that term is in the whole corpus.

### For example, your corpus contains 1M documents. And the word "linguistics" occurs only in 300K documents (including our document "D"). Then the IDF (i.e. `log(N/DF(t))`) is given by the total number of documents 1,000,000 divided by the number of documents containing the term "linguistics" (300,000). 

### `IDF(linguistics) = log(1,000,000/300,000) = 1.2`

### Let's compare IDF for "morphological" in the same corpus, where it can be found in 10 articles:

###  `IDF(morphological) = log(1,000,000/10) = 11.5`


![drums](images/drums.gif)

## TF-IDF is calculated by multiplying TF and IDF. Ta-da!



```python
linguistics = 12 # occurences of 'linguistics' in document D
d_length = 100
linguistics_tf = 12 / 100
print("TF for 'linguistics' in D: {}".format(linguistics_tf))
```

    TF for 'linguistics' in D: 0.12



```python
import math
number_of_docs_in_corp = 1000000
docs_containing_linguistics = 300000
linguistics_idf = math.log(number_of_docs_in_corp / docs_containing_linguistics)
print("IDF for 'linguistics' in corpora: {}".format(linguistics_idf))
```

    IDF for 'linguistics' in corpora: 1.2039728043259361



```python
linguistics_tfidf = round(linguistics_tf * linguistics_idf, 3)
print("TD-IDF for 'linguistics' in corpora: {}".format(linguistics_tfidf))
```

    TD-IDF for 'linguistics' in corpora: 0.144


## What does your intuition say about this metric?
## How is it better than just frequencies?
## How can we use it?

# You don't need stopwords lists now!
### 'the' or ',' will have super high TF (remember every `most_common()` output on any raw text?)
### But these tokens are going to be found in almost every document there is in any corpora.
### This will make their IDF score close to zero, and their TF-IDF too.


# Uses of TF-IDF
## Information retrieval (e.g. Okapi BM25)
## Topic modeling
## Text categorization

# Let's make word clouds with TD-IDF!

# 1. We lemmatize the whole corpus in advance
### You can choose several texts to compare instead of going through all text


```python
corpus = inaugural.fileids()
lemmatized_data = {}
for doc in corpus:
    lemmatized_data[doc] = lemmatize_tokens(inaugural.words(doc))
```


```python
lemmatized_data['2009-Obama.txt'][:10]
```




    ['My', 'fellow', 'citizen', ':', 'I', 'stand', 'here', 'today', 'humble', 'by']



# Count TFs
### Choose several speeches
### Write a function that returns a dictionary with TF data for your target speeches
### &emsp;&emsp;tfs = {"speech_1": {"lemma_1": 0.12, "lemma_2": 0.7, ...},
### &emsp;&emsp;&emsp;&emsp;&emsp;"speech_2": {"lemma_3": 0.8, "lemma_4": 0.02, ...},
### &emsp;&emsp;&emsp;&emsp;&emsp;     ...}

# So far, TFs look a bit underwhelming:


```python
from solutions.tfidf import *
target_speeches = ['1789-Washington.txt', '1861-Lincoln.txt', '2001-Bush.txt']
tfs = calculate_tfs(target_speeches, lemmatized_data)
```


```python
print(sorted(tfs['2001-Bush.txt'].items(), key=lambda x: x[1], reverse=True)[:15])
```

    [(',', 0.06027397260273973), ('.', 0.0526027397260274), ('and', 0.03506849315068493), ('be', 0.03397260273972603), ('of', 0.03178082191780822), ('the', 0.0263013698630137), ('our', 0.025205479452054796), ('a', 0.024657534246575342), ('to', 0.024657534246575342), ('we', 0.01808219178082192), ('in', 0.01589041095890411), ('not', 0.014794520547945205), ('will', 0.012602739726027398), ('And', 0.009863013698630137), ('that', 0.009863013698630137)]



```python
print(sorted(tfs['1789-Washington.txt'].items(), key=lambda x: x[1], reverse=True)[:15])
```

    [('the', 0.07477243172951886), ('of', 0.046163849154746424), (',', 0.045513654096228866), ('and', 0.031209362808842653), ('be', 0.031209362808842653), ('to', 0.0305591677503251), ('which', 0.02340702210663199), ('in', 0.018205461638491547), ('I', 0.01495448634590377), ('.', 0.014304291287386216), ('my', 0.014304291287386216), ('by', 0.01235370611183355), ('have', 0.011703511053315995), ('that', 0.011703511053315995), ('with', 0.011053315994798439)]


# Time to calculate the IDFs!
### Write a function that creates a dictionary that stores the number of documents in which lemmas occur:
### idfs = {"lemma_1": 1, "lemma_2": 3, "lemma_3": 2, "lemma_4": 2, ...}

# Stopwords are obsolete now


```python
idfs = calculate_idfs(target_speeches, lemmatized_data)
print(sorted(idfs.items(), key=lambda x: x[1])[:15])
```

    [('have', 0.0), ('it', 0.0), ('be', 0.0), ('for', 0.0), ('.', 0.0), ('all', 0.0), ('by', 0.0), ('of', 0.0), ('this', 0.0), ('and', 0.0), ('in', 0.0), ('the', 0.0), ('to', 0.0), (',', 0.0), ('as', 0.018)]



```python
print(sorted(idfs.items(), key=lambda x: x[1], reverse=True)[:15])
```

    [('notification', 4.025), ('indissoluble', 4.025), ('auspiciously', 4.025), ('aver', 4.025), ('pious', 4.025), ('despondence', 4.025), ('fifth', 4.025), ('interruption', 4.025), ('homage', 4.025), ('indispensably', 4.025), ('disinclination', 4.025), ('palliate', 4.025), ('predilection', 4.025), ('Parent', 4.025), ('mislead', 4.025)]


# Now we finally can calculate TF-IDF
### Calculate TF-IDF for your texts
### For each text in your sample print out 15 most important words

# Sample output


```python
tfidfs = calculate_tfidfs(target_speeches, lemmatized_data, tfs, idfs)
for speech in tfidfs:
    speech_parts = speech.split('-')
    print("Most important words for the {0}'s {1} speech:".format(speech_parts[1][:-4], speech_parts[0]))
    print([w[0] for w in sorted(tfidfs[speech].items(), key=lambda x: x[1], reverse=True)[:15]])
    print()
```

    Most important words for the Washington's 1789 speech:
    ['your', 'immutable', 'impression', 'providential', 'House', 'Representatives', 'notification', '14th', 'retreat', 'fond', 'predilection', 'asylum', 'decline', 'interruption', 'awaken']
    
    Most important words for the Lincoln's 1861 speech:
    ['case', 'fugitive', 'clause', 'Union', 'minority', 'secede', 'Constitution', 'lawfully', 'provision', 'slave', '?', 'expressly', 'fly', 'dissatisfied', 'you']
    
    Most important words for the Bush's 2001 speech:
    ['story', 'affirm', 'And', 'commitment', 'civility', 'Clinton', 'America', 'ideal', 'everyone', 'compassion', 'spar', 'ride', 'whirlwind', 'directs', 'promise']
    


# Is that all, though?
## You guess right, it's not!

![whatif](images/whatif.jpg)

# DIY time!
# Writing a text summarization algorithm.

### Assume that your whole corpus is a just one speech.
### Then your documents are sentences.
### How would you define the most important sentences in the speech?

### Write a function `summarize_speech()` that
### --- takes speech name as input (e.g. `'2001-Bush.txt'`)
### --- calculates TF-IDF for the speech (document — sentence, corpus — whole speech)
### --- sorts the sentences by their importance
### --- prints out 10 most important sentences sorted by their position in original text


```python
from solutions.summarize import *
summarize_speech('1993-Clinton.txt')
```

    0.203   12   Communications and commerce are global .
    0.392   13   Investment is mobile .
    0.225   26   Let us embrace it .
    0.099   30   To renew America we must be bold .
    0.178   33   It will not be easy .
    0.091   37   Our founders saw themselves in the light of posterity .
    0.155   38   We can do no less .
     0.18   63   Their cause is America ' s cause .
    0.101   72   There is so much to be done .
    0.124   80   Thank you , and God bless you all .


# Further options
### Apply a sentence or word position weighting (e.g., assuming that the most important things are said first)
### Taking only nouns and verbs into account (or adjectives too?)
### Adjust your function to work with new speeches not present in the corpus (you can find `2013-Obama.txt` and `2017-Trump.txt` in the data).
### Adding lemmatization for other languages (your function should work with Ukrainian as is, but poorly — you can try `pymorphy`)


```python
summarize_speech('2017-Trump.txt')
```


```python
summarize_speech('2013-Obama.txt')
```


```python

```
