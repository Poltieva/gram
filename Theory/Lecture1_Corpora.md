
<h1> <font size="100">Linguistic Resources</font></h1>

## How I Learned to Stop Worrying and Love NLTK

# Part I: Corpora


## What resources are available?
## Why do we need them?
## How do we use them?


## Dictionaries
## Thesauri
## Ontologies
## Corpora


# Dictionaries
### Many languages, many types (try a [reverse dictionary](https://reversedictionary.org/wordsfor/high-sounding%20but%20with%20little%20meaning), it’s fun).
### Easily available online, some available for download and use.
### Contain info about words’ meanings, grammatical properties and examples.
### Good when you need to prove that you are right (no one dares to argue with Oxford linguists).

# Thesauri
### Contain lemmas and some links between them.
### Usually that boils down to synonyms and antonyms.

# Ontologies
### Usually model some topics
### Hard to come by, even harder to create
### Contain extralinguistic data
### Classes, individuals, links between them...
### ... and logical implications!

# Corpora
### Large digital collections of texts
### Maintained in a unified format
### Created for specific tasks (must be representative)
### Contain info on language usage rather than language rules

# Corpora: different goals, different formats

## Brat stand-alone format (NER-UK)
![brat](images/brat.png)

## XML — FCE (part of Cambridge Learner Corpus, CLC)
![xml-fce](images/xml-fce.png)

## PTB-JSONL — Stanford Natural Language Inference (SNLI) Corpus
![ptb](images/ptb_jsonl.png)

## In short
![one-does-not](images/one-does-not.jpg)

# Let's take a minute to appreciate the work behind the data sets
![data-sets](images/break.jpg)
([image source](https://twitter.com/shivon/status/864889085697024000))

# Brown corpus

### Texts of American English
### ~ 1M words
### Distributed across 15 genres
### Available in nltk
### Later tagged with parts of speech


```python
import nltk
from nltk.corpus import brown
print(brown.readme())
```

    BROWN CORPUS
    
    A Standard Corpus of Present-Day Edited American
    English, for use with Digital Computers.
    
    by W. N. Francis and H. Kucera (1964)
    Department of Linguistics, Brown University
    Providence, Rhode Island, USA
    
    Revised 1971, Revised and Amplified 1979
    
    http://www.hit.uib.no/icame/brown/bcm.html
    
    Distributed with the permission of the copyright holder,
    redistribution permitted.
    


# Some Brown corpus statistics


```python
print("Paragraphs: {}".format(len(brown.paras())))
print("Sentences: {}".format(len(brown.sents())))
print("Words: {}".format(len(brown.words())))
```

    Paragraphs: 15667
    Sentences: 57340
    Words: 1161192


# Raw Brown corpus


```python
print(brown.raw()[:255])
```

    
    
    	The/at Fulton/np-tl County/nn-tl Grand/jj-tl Jury/nn-tl said/vbd Friday/nr an/at investigation/nn of/in Atlanta's/np$ recent/jj primary/nn election/nn produced/vbd ``/`` no/at evidence/nn ''/'' that/cs any/dti irregularities/nns took/vbd place/nn ./.
    
    


# New annotation


```python
brown.tagged_words(tagset='universal')[201:206]
```




    [('the', 'DET'),
     ('Atlanta', 'NOUN'),
     ('and', 'CONJ'),
     ('Fulton', 'NOUN'),
     ('County', 'NOUN')]




```python
brown.tagged_sents(tagset='universal')[0]
```




    [('The', 'DET'),
     ('Fulton', 'NOUN'),
     ('County', 'NOUN'),
     ('Grand', 'ADJ'),
     ('Jury', 'NOUN'),
     ('said', 'VERB'),
     ('Friday', 'NOUN'),
     ('an', 'DET'),
     ('investigation', 'NOUN'),
     ('of', 'ADP'),
     ("Atlanta's", 'NOUN'),
     ('recent', 'ADJ'),
     ('primary', 'NOUN'),
     ('election', 'NOUN'),
     ('produced', 'VERB'),
     ('``', '.'),
     ('no', 'DET'),
     ('evidence', 'NOUN'),
     ("''", '.'),
     ('that', 'ADP'),
     ('any', 'DET'),
     ('irregularities', 'NOUN'),
     ('took', 'VERB'),
     ('place', 'NOUN'),
     ('.', '.')]



# Brown categories


```python
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



# Reading the corpus texts


```python
print(brown.paras(categories='humor')[0])
```

    [['It', 'was', 'among', 'these', 'that', 'Hinkle', 'identified', 'a', 'photograph', 'of', 'Barco', '!', '!'], ['For', 'it', 'seems', 'that', 'Barco', ',', 'fancying', 'himself', 'a', "ladies'", 'man', '(', 'and', 'why', 'not', ',', 'after', 'seven', 'marriages', '?', '?'], [')', ',', 'had', 'listed', 'himself', 'for', 'Mormon', 'Beard', 'roles', 'at', 'the', 'instigation', 'of', 'his', 'fourth', 'murder', 'victim', 'who', 'had', 'said', ':', '``', 'With', 'your', 'beard', ',', 'dear', ',', 'you', 'ought', 'to', 'be', 'in', 'movies', "''", '!', '!']]


# Looping through a paragraph


```python
for sentence in brown.paras(categories='humor')[0]:
    print(" ".join(sentence))
    print("\n")
```

    It was among these that Hinkle identified a photograph of Barco ! !
    
    
    For it seems that Barco , fancying himself a ladies' man ( and why not , after seven marriages ? ?
    
    
    ) , had listed himself for Mormon Beard roles at the instigation of his fourth murder victim who had said : `` With your beard , dear , you ought to be in movies '' ! !
    
    


# Don't forget about the documentation!


```python
help(nltk.corpus.reader)
```

    Help on package nltk.corpus.reader in nltk.corpus:
    
    NAME
        nltk.corpus.reader
    
    DESCRIPTION
        NLTK corpus readers.  The modules in this package provide functions
        that can be used to read corpus fileids in a variety of formats.  These
        functions can be used to read both the corpus fileids that are
        distributed in the NLTK corpus package, and corpus fileids that are part
        of external corpora.
        
        Corpus Reader Functions
        =======================
        Each corpus module defines one or more "corpus reader functions",
        which can be used to read documents from that corpus.  These functions
        take an argument, ``item``, which is used to indicate which document
        should be read from the corpus:
        
        - If ``item`` is one of the unique identifiers listed in the corpus
          module's ``items`` variable, then the corresponding document will
          be loaded from the NLTK corpus package.
        - If ``item`` is a fileid, then that file will be read.
        
        Additionally, corpus reader functions can be given lists of item
        names; in which case, they will return a concatenation of the
        corresponding documents.
        
        Corpus reader functions are named based on the type of information
        they return.  Some common examples, and their return types, are:
        
        - words(): list of str
        - sents(): list of (list of str)
        - paras(): list of (list of (list of str))
        - tagged_words(): list of (str,str) tuple
        - tagged_sents(): list of (list of (str,str))
        - tagged_paras(): list of (list of (list of (str,str)))
        - chunked_sents(): list of (Tree w/ (str,str) leaves)
        - parsed_sents(): list of (Tree with str leaves)
        - parsed_paras(): list of (list of (Tree with str leaves))
        - xml(): A single xml ElementTree
        - raw(): unprocessed corpus contents
        
        For example, to read a list of the words in the Brown Corpus, use
        ``nltk.corpus.brown.words()``:
        
            >>> from nltk.corpus import brown
            >>> print(", ".join(brown.words()))
            The, Fulton, County, Grand, Jury, said, ...
...
   
    


# DIY time: find the most ambiguous word
### Write a functuon that
### --- goes through the tagged words of Brown corpus
### --- and finds the word that has the biggest number of different POS-tags

# Sample output


```python
from solutions.sort_by_tags import *
tagged_words = brown.tagged_words(tagset = 'universal')
words_and_tags = sort_words_by_tag_number(tagged_words)
fifth = words_and_tags[5]
print("{} - {}".format(fifth[0], fifth[1]))
```

    damn - ['VERB', 'ADV', 'ADJ', 'PRT', 'NOUN']


# Penn Treebank
### Published in 1991
### 4.5 million words
### American English
### POS-tagged
### Annotated for syntactic structures
### Wall Street Journal articles + retagged Brown Corpus


```python
from nltk.corpus import treebank
print(treebank.readme())
```

    [ PENN TREEBANK SAMPLE ]
    http://www.cis.upenn.edu/~treebank/home.html
    
    This is a ~5% fragment of Penn Treebank, (C) LDC 1995.  It is made
    available under fair use for the purposes of illustrating NLTK tools
    for tokenizing, tagging, chunking and parsing.  This data is for
    non-commercial use only.
    
    Contents: raw, tagged, parsed and combined data from Wall Street
    Journal for 1650 sentences (99 treebank files wsj_0001 .. wsj_0099).
    For details about each of the four types, please see the other README
    files included in the treebank sample directory.  Examples of the four
    types are shown below:
    
    ----raw----
    Pierre Vinken, 61 years old, will join the board as a nonexecutive
    director Nov. 29.
    ----tagged----
    [ Pierre/NNP Vinken/NNP ]
    ,/, 
    [ 61/CD years/NNS ]
    old/JJ ,/, will/MD join/VB 
    [ the/DT board/NN ]
    as/IN 
    [ a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ]
    ./. 
    ----parsed----
    ( (S (NP-SBJ (NP Pierre Vinken)
                 ,
                 (ADJP (NP 61 years)
    		   old)
                 ,)
         (VP will
             (VP join
                 (NP the board)
                 (PP-CLR as
    		     (NP a nonexecutive director))
    	     (NP-TMP Nov. 29)))
         .))
    ----combined----
    ( (S 
        (NP-SBJ 
          (NP (NNP Pierre) (NNP Vinken) )
          (, ,) 
          (ADJP 
            (NP (CD 61) (NNS years) )
            (JJ old) )
          (, ,) )
        (VP (MD will) 
          (VP (VB join) 
            (NP (DT the) (NN board) )
            (PP-CLR (IN as) 
              (NP (DT a) (JJ nonexecutive) (NN director) ))
            (NP-TMP (NNP Nov.) (CD 29) )))
        (. .) ))
    
    -----------------------------------------------------------------------
    
    [ README file for Merged (a.k.a. Combined) files ]
    
    The files in this hierarchy were automatically created by inserting the
    part of speech tags from a tagged text file (.pos file) into a parsed text
    file (.prd file).  The tags are inserted as nodes immediately dominating
    the terminals.  The -NONE- node means that there is no part of speech for
    that terminal symbol (i.e., it is a "null element"; see manual).
    
    Most of the technical errors in the last release should be fixed, but note
    that the combining program applies a number of patches to make the .prd and
    .pos files match; see the file MERGE.LOG for the verbose information
    provided by the combiner.  The combiner itself is included in this release;
    see the tools/ directory for details.
    
    These files have the extension .mrg, to distinguish them from the .cmb
    files of the previous release.  The indentation of the trees is also
    somewhat different than before, though the use of parentheses is unchanged.
 ...   
    

    


# Penn Treebank tagging


```python
print(treebank.tagged_sents()[301])
```

    [('The', 'DT'), ('latest', 'JJS'), ('two', 'CD'), ('funds', 'NNS'), ('were', 'VBD'), ('assembled', 'VBN'), ('*-42', '-NONE-'), ('jointly', 'RB'), ('by', 'IN'), ('Goldman', 'NNP'), (',', ','), ('Sachs', 'NNP'), ('&', 'CC'), ('Co.', 'NNP'), ('of', 'IN'), ('the', 'DT'), ('U.S.', 'NNP'), ('and', 'CC'), ('Japan', 'NNP'), ("'s", 'POS'), ('Daiwa', 'NNP'), ('Securities', 'NNPS'), ('Co', 'NNP'), ('.', '.')]



```python
print(treebank.parsed_sents()[301])
```

    (S
      (NP-SBJ-42 (DT The) (JJS latest) (CD two) (NNS funds))
      (VP
        (VBD were)
        (VP
          (VBN assembled)
          (NP (-NONE- *-42))
          (ADVP-MNR (RB jointly))
          (PP
            (IN by)
            (NP-LGS
              (NP
                (NP (NNP Goldman) (, ,) (NNP Sachs) (CC &) (NNP Co.))
                (PP (IN of) (NP (DT the) (NNP U.S.))))
              (CC and)
              (NP
                (NP (NNP Japan) (POS 's))
                (NNP Daiwa)
                (NNPS Securities)
                (NNP Co))))))
      (. .))


# Tree structure


```python
def print_child_nodes(spaces,node):
    if type(node) != str:
        for child in node:
            if type(child) != str:
                label = child.label()
                print("{}({}".format(" " * spaces, label))
                print_child_nodes(spaces + 3, child)
            else:
                print("{}'{}')".format(" " * spaces, child))

sample_sentence = treebank.parsed_sents()[301]
print("Root label = {}".format(sample_sentence.label()))
for child in sample_sentence:
    print(child.label())
    print_child_nodes(3, child)
```

    Root label = S
    NP-SBJ-42
       (DT
          'The')
       (JJS
          'latest')
       (CD
          'two')
       (NNS
          'funds')
    VP
       (VBD
          'were')
       (VP
          (VBN
             'assembled')
          (NP
             (-NONE-
                '*-42')
          (ADVP-MNR
             (RB
                'jointly')
          (PP
             (IN
                'by')
             (NP-LGS
                (NP
                   (NP
                      (NNP
                         'Goldman')
                      (,
                         ',')
                      (NNP
                         'Sachs')
                      (CC
                         '&')
                      (NNP
                         'Co.')
                   (PP
                      (IN
                         'of')
                      (NP
                         (DT
                            'the')
                         (NNP
                            'U.S.')
                (CC
                   'and')
                (NP
                   (NP
                      (NNP
                         'Japan')
                      (POS
                         ''s')
                   (NNP
                      'Daiwa')
                   (NNPS
                      'Securities')
                   (NNP
                      'Co')
    .
       '.')


# DIY time: search the treebank
### Write a function `search_by_tag_sequence(tag_seq, tagged_tokens)` that
### --- takes a list of tags and a list of tokens (you can use `tagged_words()`) as arguments
### --- finds the sequences that match the given tags
### --- accepts `*` as `any tag`
### --- can find by first letters of a tag (given `NN*`, can find `NN`,  `NNS`, `NNP` and `NNPS`)
### Try to find all sequences that have `a determiner, some word, an adjective and any noun`

# Sample output


```python
from solutions.search_tags import *
search_by_tag_sequence(['VBN', '*', 'VBN'], treebank.tagged_words())[:10]
```




    [[('achieved', 'VBN'), ('and', 'CC'), ('maintained', 'VBN')],
     [('been', 'VBN'), ('correspondence', 'NN'), ('mailed', 'VBN')],
     [('been', 'VBN'), ('temporarily', 'RB'), ('mollified', 'VBN')],
     [('exhausted', 'VBN'), ('the', 'DT'), ('limited', 'VBN')],
     [('been', 'VBN'), ('well', 'RB'), ('stoked', 'VBN')],
     [('dressed', 'VBN'), (',', ','), ('decorated', 'VBN')],
     [('suspended', 'VBN'), ('or', 'CC'), ('barred', 'VBN')],
     [('barred', 'VBN'), ('nor', 'CC'), ('suspended', 'VBN')],
     [('repaired', 'VBN'), ('or', 'CC'), ('replaced', 'VBN')],
     [('robbed', 'VBN'), ('or', 'CC'), ('murdered', 'VBN')]]



# Other corpora in NLTK

# Reuters
### Corpus for text categorization
### 90 topics (overlapping)
### 10,788 news documents (~ 1.3 million words)
### Divided into train and test sets

# Reuters categories


```python
from nltk.corpus import reuters
print(reuters.categories())
```

    ['acq', 'alum', 'barley', 'bop', 'carcass', 'castor-oil', 'cocoa', 'coconut', 'coconut-oil', 'coffee', 'copper', 'copra-cake', 'corn', 'cotton', 'cotton-oil', 'cpi', 'cpu', 'crude', 'dfl', 'dlr', 'dmk', 'earn', 'fuel', 'gas', 'gnp', 'gold', 'grain', 'groundnut', 'groundnut-oil', 'heat', 'hog', 'housing', 'income', 'instal-debt', 'interest', 'ipi', 'iron-steel', 'jet', 'jobs', 'l-cattle', 'lead', 'lei', 'lin-oil', 'livestock', 'lumber', 'meal-feed', 'money-fx', 'money-supply', 'naphtha', 'nat-gas', 'nickel', 'nkr', 'nzdlr', 'oat', 'oilseed', 'orange', 'palladium', 'palm-oil', 'palmkernel', 'pet-chem', 'platinum', 'potato', 'propane', 'rand', 'rape-oil', 'rapeseed', 'reserves', 'retail', 'rice', 'rubber', 'rye', 'ship', 'silver', 'sorghum', 'soy-meal', 'soy-oil', 'soybean', 'strategic-metal', 'sugar', 'sun-meal', 'sun-oil', 'sunseed', 'tea', 'tin', 'trade', 'veg-oil', 'wheat', 'wpi', 'yen', 'zinc']



```python
print(reuters.sents(categories='orange')[:10])
```

    [['WEATHER', 'HURTS', 'ITALIAN', 'ORANGES', '-', 'USDA', 'REPORT', 'Unfavorable', 'weather', 'conditions', 'during', 'the', 'second', 'week', 'of', 'March', 'caused', 'damage', 'to', 'oranges', 'in', 'the', 'Calabria', 'region', 'in', 'southern', 'Italy', ',', 'the', 'U', '.', 'S', '.', 'Agriculture', 'Department', "'", 's', 'officer', 'in', 'Rome', 'said', 'in', 'a', 'field', 'report', '.'], ['The', 'report', ',', 'dated', 'April', '3', ',', 'said', 'the', 'region', 'accounts', 'for', 'about', '22', ',', '000', 'hectares', 'of', 'the', 'Italian', 'orange', 'crop', 'or', 'about', '26', 'pct', 'of', 'total', 'production', '.'], ['However', ',', 'orange', 'production', 'in', 'the', 'region', 'for', 'marketing', 'year', '1986', '/', '87', 'is', 'forecast', 'at', '565', ',', '000', 'tonnes', 'or', '25', 'pct', 'of', 'the', 'total', 'Italian', 'orange', 'crop', ',', 'it', 'said', '.'], ['The', 'report', 'said', 'trade', 'contacts', 'agree', 'that', 'about', '15', 'pct', 'of', 'the', 'orange', 'output', 'in', 'Calabria', 'was', 'damaged', 'by', 'frost', '.'], ['USDA', '1986', '/', '87', 'U', '.', 'S', '.', 'ORANGE', 'CROP', '190', ',', '050', ',', '000', 'BOXES', ',', 'FLORIDA', 'CROP', '122', ',', '900', ',', '000', 'BOXES'], ['USDA', '1986', '/', '87', 'U', '.', 'S', '.', 'ORANGE', 'CROP', '190', ',', '050', ',', '000', 'BOXES', ',', 'FLORIDA', 'CROP', '122', ',', '900', ',', '000', 'BOXES'], ['USDA', 'ESTIMATES', '1986', '/', '87', 'ORANGE', 'JUICE', 'YIELD', 'AT', '1', '.', '50', 'GALS', 'PER', 'BOX', 'FROM', 'FLORIDA', 'CROP'], ['USDA', 'ESTIMATES', '1986', '/', '87', 'ORANGE', 'JUICE', 'YIELD', 'AT', '1', '.', '50', 'GALS', 'PER', 'BOX', 'FROM', 'FLORIDA', 'CROP'], ['U', '.', 'S', '.', 'CITRUS', 'CROP', 'ESTIMATE', '--', 'USDA', 'The', 'U', '.', 'S', '.', 'Agriculture', 'Department', 'estimated', '1986', '/', '87', 'citrus', 'production', ',', 'as', 'follows', '(', 'in', 'boxes', ')', '--', 'Total', 'U', '.', 'S', '.', 'orange', 'crop', '(', 'excluding', 'Florida', 'Temples', ')', '--', '190', ',', '050', ',', '000', 'boxes', ',', 'vs', '190', ',', '850', ',', '000', 'boxes', 'last', 'month', 'and', '176', ',', '410', ',', '000', 'boxes', 'in', 'the', '1985', '/', '86', 'crop', '.'], ['Florida', 'oranges', '(', 'excluding', 'Temples', ')', '--', '122', ',', '900', ',', '000', 'boxes', ',', 'vs', '124', ',', '000', ',', '000', 'last', 'month', 'and', '119', ',', '000', ',', '000', 'boxes', 'in', '1985', '/', '86', '.']]


# Parsed corpora
### Penn Treebank
### CoNLL 2007 Dependency Treebank
### YCOE — York-Toronto-Helsinki Parsed Corpus of Old English Prose (needs separate installation)

# Text diversity
### Web Text
### NPS Chat
### Inaugural Adress Corpus
### Gutenberg books
### Indian Language Corpus

# Where to get data
### Books, magazines, newspapers
### Web (e.g. CommonCrawl)
### Field trips

## Let's explore!
### Good way to start exploring the data is building concordances.
### Nothing too fancy — that's just a way to look at the contexts in which a word form occurs.

![firth](images/firth.png)


```python
# Here's a small bunch of plaintext corpora
from nltk.book import *
```

    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908



```python
print(nltk.text.Text.__doc__)
```

    
        A wrapper around a sequence of simple (string) tokens, which is
        intended to support initial exploration of texts (via the
        interactive console).  Its methods perform a variety of analyses
        on the text's contexts (e.g., counting, concordancing, collocation
        discovery), and display the results.  If you wish to write a
        program which makes use of these analyses, then you should bypass
        the ``Text`` class, and use the appropriate analysis function or
        class directly instead.
    
        A ``Text`` is typically initialized from a given document or
        corpus.  E.g.:
    
        >>> import nltk.corpus
        >>> from nltk.text import Text
        >>> moby = Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
    
        



```python
print(text1)
text1.concordance("bare")
```

    <Text: Moby Dick by Herman Melville 1851>
    Displaying 10 of 10 matches:
    liar character of the day , does the bare mention of Whitsuntide marshal in th
    tic ghostliness over the soul at the bare mention of that name , while the tho
    s into a cave . " As the Lakeman ' s bare head was just level with the planks 
    ng them to be such , taking them for bare , blackened elevations of the soil ;
    - time the bees rush to the boughs . Bare - headed in the sultry sun , Ahab st
    en these poor sun - burnt mariners , bare - footed , and with their trowsers r
    ticular lights , the case might by a bare possibility in some small degree be 
    m the front of the try - works , the bare masonry of that side is exposed , pe
     places . You ' ll do to give us the bare words and facts , but we come in to 
     Pequod was torn of her canvas , and bare - poled was left to fight a Typhoon 



```python
print(text3)
text3.concordance("bare")
```

    <Text: The Book of Genesis>
    Displaying 25 of 56 matches:
    e his wife ; and she conceived , and bare Cain , and said , I have gotten a ma
     a man from the LORD . And she again bare his brother Abel . And Abel was a ke
    w his wife ; and she conceived , and bare Enoch : and he builded a city , and 
     name of the other Zillah . And Adah bare Jabal : he was the father of such as
    rp and organ . And Zillah , she also bare Tubalcain , an instructor of every a
    d Adam knew his wife again ; and she bare a son , and called his name Se For G
    unto the daughters of men , and they bare children to them , the same became m
    rth ; and the waters increased , and bare up the ark , and it was lift up abov
    Jebusites . Now Sarai Abram ' s wife bare him no children : and she had an han
    between Kadesh and Bered . And Hagar bare Abram a son : and Abram called his s
    alled his son ' s name , which Hagar bare , Ishmael . And Abram was fourscore 
    score and six years old , when Hagar bare Ishmael to Abram . And when Abram wa
    by their father . And the first born bare a son , and called his name Moab : t
    his day . And the younger , she also bare a son , and called his name Benam th
    fe , and his maidservants ; and they bare children . For the LORD had fast clo
    d spoken . For Sarah conceived , and bare Abraham a son in his old age , at th
     that was born unto him , whom Sarah bare to him , Isaac . And Abraham circumc
    cubine , whose name was Reumah , she bare also Tebah , and Gaham , and Thahash
    ethuel the son of Milcah , which she bare unto Nahor . She said moreover unto 
    asses . And Sarah my master ' s wife bare a son to my master when she was o an
    ethuel , Nahor ' s son , whom Milcah bare unto h and I put the earring upon he
    , and her name was Keturah . And she bare him Zimran , and Jokshan , and Medan
     the Egyptian , Sarah ' s handmaid , bare unto Abrah And these are the names o
    ac was threescore years old when she bare them . And the boys grew : and Esau 
    as barren . And Leah conceived , and bare a son , and she called his name Reub



```python
print(text1)
text1.similar("bare")
```

    <Text: Moby Dick by Herman Melville 1851>
    long mast can huge above enormous prodigious spoken passing
    decapitated honey ebon weightiest



```python
print(text3)
text3.similar("bare")
```

    <Text: The Book of Genesis>
    said in and called went became put took gave take spake saw that made
    unto is to for give hath


# How corpora are made
## A quick glance at raw text processing


```python
import os
print(os.getcwd())
```

    /Users/elizaveta.zhbankova/summer-school-tools



```python
yellow_raw_text = open("data/king_in_yellow.txt", "r").read()
print(yellow_raw_text)
```

    Robert W. Chambers
    The Repairer Of Reputations
    "Ne raillons pas les fous; leur folie dure plus longtemps que la notre .... Voila toute la difference."
    I
    Toward the end of the year 1920 the government of the United States had practically completed the programme adopted during the last months of President Winthrop's administration. The country was apparently tranquil. Everybody knows how the Tariff and Labor questions were settled. The war with Germany, incident on that country's seizure of the Samoan Islands, had left no visible scars upon the republic, and the temporary occupation of Norfolk by the invading army had been forgotten in the joy over repeated naval victories and the subsequent ridiculous plight of General Von Gartenlaube's forces in the State of New Jersey. The Cuban and Hawaiian investments had paid one hundred per cent., and the territory of Samoa was well worth its cost as a coaling station. The country was in a superb state of defense. Every coast city had been well supplied with land fortifications; the army, under the parental eye of the general staff, organized according to the Prussian system, had been increased to three hundred thousand men, with a territorial reserve of a million; and six magnificent squadrons of cruisers and battle-ships patrolled the six stations of the navigable seas, leaving a steam reserve amply fitted to control home waters. The gentlemen from the West had at last been constrained to acknowledge that a college for the training of diplomats was a necessary as law schools are for the training of barristers; consequently we were no longer represented abroad by incompetent patriots. The nation was prosperous. Chicago, for a moment paralyzed after a second great fire, had risen from its ruins, white and imperial, and more beautiful than the white city which had been built for its plaything in 1893. Everywhere good architecture was replacing bad, and even in New York a sudden craving for decency had swept away a great portion of the existing horrors. Streets had been widened, properly paved, and lighted, trees had been planted, squares laid out, elevated structures demolished, and underground roads built to replace them. The new government buildings and barracks were fine bits of architecture, and the long system of stone quays which completely surrounded the island had been turned into parks, which proved a godsend to the population. The subsidizing of the state theatre and state opera brought its own reward. The United States National Academy of Design was much like European institutions of the same kind. Nobody envied the Secretary of Fine Arts either his cabinet position or his portfolio. The Secretary of Forestry and Game Preservation had a much easier time, thanks to the new system of National Mounted Police. We had profited well by the latest treaties with France and England; the exclusion of foreign-born Jews as a measure of national self-preservation, the settlement of the new independent negro state of Suanee, the checking of immigration, the new laws concerning naturalization, and the gradual centralization of power in the executive all contributed to national calm and prosperity. When the government solved the Indian problem and squadrons of Indian cavalry scouts in native costume were substituted for the pitiable organizations tacked on to the tail of skeletonized regiments by the former Secretary of War, the nation drew a long sigh of relief. When, after the colossal Congress of Religions, bigotry and intolerance were laid in their graves, and kindness and charity began to draw warring sects together, many thought the millennium had arrived, at least in the new world, which, after all, is a world by itself.
 ...   



```python
print(len(yellow_raw_text))
```

    68053



```python
yellow_paragraphs = yellow_raw_text.splitlines()
print(len(yellow_paragraphs))
print(yellow_paragraphs[143])
```

    271
    He looked at me narrowly, much as Dr. Archer used to, and I knew he thought I was mentally unsound. Perhaps it was fortunate for him that he did not use the word lunatic just then.


# Segmentation
## How to determine where the sentence begins and ends?


```python
def sentence_split(text):
    return text.split(".")
sentence_split("He looked at me narrowly, much as Dr. Archer used to, and I knew he thought I was mentally unsound.")
```




    ['He looked at me narrowly, much as Dr',
     ' Archer used to, and I knew he thought I was mentally unsound',
     '']



### Sentence segmentation is easy they said... just split by period characters they said...

## What about ellipses?
### He looked at me narrowly . . . much as Dr. Archer used to.

### He looked at me narrowly .
### .
### .
### much as Dr.
### Archer used to.

## And many other problems!
### I'm trying to execute scipt.EXE but it doesn't work!!!
### Here's a sentence.And I forgot to add a space And a period too, btw.
### Not to mention websites, you know -- like www.some.awesome.website.com. How do you parse that?

### Thankfully, nltk has a readily available function for that. It's not perfect, so considering your data, you might have to come up with some extensions and further features.


```python
from nltk import sent_tokenize
sent_tokenize("He looked at me narrowly, much as Dr. Archer used to, and I knew he thought I was mentally unsound.")
```




    ['He looked at me narrowly, much as Dr. Archer used to, and I knew he thought I was mentally unsound.']




```python
sent_tokenize(yellow_paragraphs[103])
```




    ['I put on my hat and went out into the park for a little walk before dinner.',
     'As I crossed the central drive-way a group of officers passed, and one of them called out, "Hello, Hildred!"',
     'and came back to shake hands with me.',
     'It was my cousin Louis, who stood smiling and tapping his spurred heels with his riding-whip.']



### You can see that 'sent_tokenize()' has some drawbacks. Well, as any solution does.
### Now, using this imperfect function provided by fellow linguists, split the paragraphs into sentences and put them all in one list.


```python
yellow_sentences = []
for par in yellow_paragraphs:
    for s in sent_tokenize(par):
        yellow_sentences.append(s)
yellow_sentences[4:14]
```




    ["Toward the end of the year 1920 the government of the United States had practically completed the programme adopted during the last months of President Winthrop's administration.",
     'The country was apparently tranquil.',
     'Everybody knows how the Tariff and Labor questions were settled.',
     "The war with Germany, incident on that country's seizure of the Samoan Islands, had left no visible scars upon the republic, and the temporary occupation of Norfolk by the invading army had been forgotten in the joy over repeated naval victories and the subsequent ridiculous plight of General Von Gartenlaube's forces in the State of New Jersey.",
     'The Cuban and Hawaiian investments had paid one hundred per cent., and the territory of Samoa was well worth its cost as a coaling station.',
     'The country was in a superb state of defense.',
     'Every coast city had been well supplied with land fortifications; the army, under the parental eye of the general staff, organized according to the Prussian system, had been increased to three hundred thousand men, with a territorial reserve of a million; and six magnificent squadrons of cruisers and battle-ships patrolled the six stations of the navigable seas, leaving a steam reserve amply fitted to control home waters.',
     'The gentlemen from the West had at last been constrained to acknowledge that a college for the training of diplomats was a necessary as law schools are for the training of barristers; consequently we were no longer represented abroad by incompetent patriots.',
     'The nation was prosperous.',
     'Chicago, for a moment paralyzed after a second great fire, had risen from its ruins, white and imperial, and more beautiful than the white city which had been built for its plaything in 1893.']



## Next step: tokenization
### Remember, we had functions pars(), sents() and words()?

## A token is:

### minimal lexical unit
### either an independent word or a punctuation mark
### that has a distinct meaning

# How would you tokenize these:
## `Let's` vs. `it's` vs. `John's` vs. `Simpsons'`

## What about `don't`, `won't`, `can't` and `cannot`?

![notaword](images/not-a-word.jpg)

## Handling punctuation marks:
### e.g., B.B.C.
### jblack@mail.yahoo.com
### http://www.nltk.org/book/
### ;-),  😍

## And hyphens
### co-education
### Hewlett-Packard
### the hold-him-back-and-drag-him-away maneuver

## And many other things
### жар-птиця, йди-но,
### Lebensversicherungsgesellschaftsangestellter
### San Francisco, au fait, not to mention
### (800) 234-2333, $3M, 6.34

## And that's only a start!
### Some languages don't use spaces at all (e.g. Korean, some versions of Sanskrit)
### Some languages use spaces differently:
### ---- Тымэйӈылевтпыгтыркын — I have a fierce headache. (Chukchi)
### ---- Usaopuspe aeyaykotuymasiramsuypa. — I wonder about various rumors. (Ainu)


## So how is it done?

## Step 1: analyze your data.
### Determine how does word segmentation work in the target language

## Step 2: set your goals.
### What kind of segments work for your purposes?
### ---- O + ' + Niel, O'Niel, O' + Niel?
### What kind of tokens are standart for the tools you are going to use?
### ---- e.g. will the parser you work with tag as POS 's or ' + s

## Step 3: tokenize!
### Write a basic function (usually regexp based)
### Add a ton or two of exceptions :)


```python
from nltk.tokenize import word_tokenize
word_tokenize(yellow_sentences[4])
```




    ['Toward',
     'the',
     'end',
     'of',
     'the',
     'year',
     '1920',
     'the',
     'government',
     'of',
     'the',
     'United',
     'States',
     'had',
     'practically',
     'completed',
     'the',
     'programme',
     'adopted',
     'during',
     'the',
     'last',
     'months',
     'of',
     'President',
     'Winthrop',
     "'s",
     'administration',
     '.']




```python
yellow_tokens = []
for sent in yellow_sentences:
    for token in word_tokenize(sent):
        yellow_tokens.append(token)
```


```python
from nltk.text import Text
yellow_corpus = Text(yellow_tokens)
```


```python
yellow_corpus.concordance("hastur")
```

    Displaying 5 of 5 matches:
    `` when from Carcosa , the Hyades , Hastur , and Aldebaran , '' to `` Castaign
    iped my forehead , but I thought of Hastur and of my own rightful ambition , a
    Carcosa , the lakes which connected Hastur , Aldebaran , and the mystery of th
    , the people should know the son of Hastur , and the whole world bow to the bl
    st I was King , King in my right in Hastur , King because I knew the mystery o


# Normalization
### Because words have lots of forms and you don't want to search your texts with regular expressions.
### At least not in every query, right?


# Stemming: cutting the suffixes off the root
## agonizing -> agon
## different -> differ
## replacement -> replac
## ponies -> poni


```python
from nltk.stem import *
stemmer = porter.PorterStemmer()
words = ['flies', 'fly','flying',
         'died', 'dying', 'dead',
         'computer', 'computational',
         'replaced', 'replacement',
         'does', 'did', 'done',
         'women', 'normal', 'normalized', 'normalization']
```


```python
for word in words:
    print("Word: {0} --> {1}".format(word, stemmer.stem(word)))
```

    Word: flies --> fli
    Word: fly --> fli
    Word: flying --> fli
    Word: died --> die
    Word: dying --> die
    Word: dead --> dead
    Word: computer --> comput
    Word: computational --> comput
    Word: replaced --> replac
    Word: replacement --> replac
    Word: does --> doe
    Word: did --> did
    Word: done --> done
    Word: women --> women
    Word: normal --> normal
    Word: normalized --> normal
    Word: normalization --> normal


# Now, let's build a concordance that can look for stems!
### What we need:
### 1. a new class `IndexedText` that would have a search index with stems as keys.
### 2. a class initializer to build that index from a given text 
### 3. a function `concordance()` for that class that would return right and left context for the occurrences of the stem of a given word.
### That sounds a bit complicated, so let's just peek at the solution right away :)


```python
class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/2)   
        idx = self._index[key]
        if len(idx) > 0:
            for i in self._index[key]:
                lcontext = ' '.join(self._text[i-wc:i])
                rcontext = ' '.join(self._text[i:i+wc])
                ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                print(ldisplay, rdisplay)
        else:
            print("No matches found :(")

    def _stem(self, word):
        return self._stemmer.stem(word).lower()
```

# Concordance with stemmer index


```python
indexed_by_stemmer = IndexedText(nltk.PorterStemmer(), yellow_tokens)
indexed_by_stemmer.concordance("start", width = 30)
```

     me that I had better stop . I started up and flung the book 
    not finish , for Constance had started to her feet with terro
    love him , '' he suggested . I started to reply , but a sudde
    ng a hatchet from the pantry , started to find the infernal b
    pt and notes , took my hat and started for the door . Mr. Wil
    ly ceased to be an effort . He started when , in the closely 



```python
indexed_by_stemmer.concordance("women", width = 30)
```

    No matches found :(


# Lemmatization
## More 'linguistic' way of normalization
## It is the process of transforming the word into its base form:
### believes, believed, believing -> believe
### are, am, is, being, been -> be
### women -> woman



# NLTK has a tool for that too!



```python
wnl = nltk.WordNetLemmatizer()
for word in words:
    print("Word: {0} --> {1}".format(word, wnl.lemmatize(word)))
```

    Word: flies --> fly
    Word: fly --> fly
    Word: flying --> flying
    Word: died --> died
    Word: dying --> dying
    Word: dead --> dead
    Word: computer --> computer
    Word: computational --> computational
    Word: replaced --> replaced
    Word: replacement --> replacement
    Word: does --> doe
    Word: did --> did
    Word: done --> done
    Word: women --> woman
    Word: normal --> normal
    Word: normalized --> normalized
    Word: normalization --> normalization


# DIY time!
## Update the IndexedText class so that it uses WordNet lemmatizer instead of a stemmer.


```python
class IndexedTextL(object):

    def __init__(self, lemmatizer, text):
        self._text = text
        self._lemmatizer = lemmatizer
        self._index = nltk.Index((self._lemma(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._lemma(word)
        wc = int(width/2)   
        idx = self._index[key]
        if len(idx) > 0:
            for i in self._index[key]:
                lcontext = ' '.join(self._text[i-wc:i])
                rcontext = ' '.join(self._text[i:i+wc])
                ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                print(ldisplay, rdisplay)
        else:
            print("No matches found :(")

    def _lemma(self, word):
        return self._lemmatizer.lemmatize(word).lower()
```


```python
indexed_by_lemmatizer = IndexedTextL(nltk.WordNetLemmatizer(), yellow_tokens)
indexed_by_lemmatizer.concordance("feet", width = 30)
```

    r Constance had started to her feet with terror written on he
    ark . Groping about , I set my foot on something soft , which
    e sunshine on the bench at the foot of the equestrian status 
    tance . '' Louis sprang to his feet , and I arose also , and 



```python
indexed_by_stemmer.concordance("feet", width = 30)
```

    r Constance had started to her feet with terror written on he
    tance . '' Louis sprang to his feet , and I arose also , and 



```python
indexed_by_lemmatizer.concordance("start", width = 30)
```

    No matches found :(



```python
indexed_by_stemmer.concordance("start", width = 30)
```

     me that I had better stop . I started up and flung the book 
    not finish , for Constance had started to her feet with terro
    love him , '' he suggested . I started to reply , but a sudde
    ng a hatchet from the pantry , started to find the infernal b
    pt and notes , took my hat and started for the door . Mr. Wil
    ly ceased to be an effort . He started when , in the closely 


### Explore WordNet lemmatizer on different words.
### What could be done better?
### How to handle ambiguous cases?

# DIY time! Make lemmatization better!
### Provide Part-Of-Speech tags to WordNet lemmatizer.
### First, let's get word's POS-tag with nltk.pos_tag


```python
nltk.pos_tag(["tried"])
```




    [('tried', 'VBN')]




```python
nltk.pos_tag(nltk.word_tokenize("Time flies like an arrow."))
```




    [('Time', 'NNP'),
     ('flies', 'NNS'),
     ('like', 'IN'),
     ('an', 'DT'),
     ('arrow', 'NN'),
     ('.', '.')]



### As you see, this function doesn't handle POS ambiguities well.
### All it does, is gives the most frequent POS tag for the form, but for now, it'll do.

## Write a function that converts nltk POS tags to wordnet POS tags:
### VBD, VBZ, VBN... -> wordnet.VERB
### JJ, JJR... -> wordnet.ADJ
### NN, NNS, NNPS, NNPS -> wordnet.NOUN
### RB, RBR... -> wordnet.ADV
### Don't forget to add a default value to handle all determiners, punctuation etc.


```python
from solutions.tag_convert import *
get_wordnet_pos("tried")
```




    'v'



# Now try WordNet lemmatizer with POS tags!


```python
nltk.WordNetLemmatizer().lemmatize("tried", get_wordnet_pos("tried"))
```




    'try'




```python
wnl = nltk.WordNetLemmatizer()
for word in words:
    tag = get_wordnet_pos(word)
    print("Word: {} ({}) --> {}".format(word, tag, wnl.lemmatize(word, tag)))
```

    Word: flies (n) --> fly
    Word: fly (n) --> fly
    Word: flying (v) --> fly
    Word: died (v) --> die
    Word: dying (v) --> die
    Word: dead (a) --> dead
    Word: computer (n) --> computer
    Word: computational (n) --> computational
    Word: replaced (v) --> replace
    Word: replacement (n) --> replacement
    Word: does (v) --> do
    Word: did (v) --> do
    Word: done (v) --> do
    Word: women (n) --> woman
    Word: normal (a) --> normal
    Word: normalized (v) --> normalize
    Word: normalization (n) --> normalization


# DIY: upgrade your IndexedText class to IndexedTextPOS
### Provide better lemmatization giving tags to your lemmatizer


```python
class IndexedTextPOS(object):

    def __init__(self, lemmatizer, text):
        self._text = text
        self._lemmatizer = lemmatizer
        self._index = nltk.Index((self._lemma(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._lemma(word)
        wc = int(width/2)   
        idx = self._index[key]
        if len(idx) > 0:
            for i in self._index[key]:
                lcontext = ' '.join(self._text[i-wc:i])
                rcontext = ' '.join(self._text[i:i+wc])
                ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                print(ldisplay, rdisplay)
        else:
            print("No matches found :(")

    def _lemma(self, word):
        pos_tag = get_wordnet_pos(word)
        return self._lemmatizer.lemmatize(word, pos_tag).lower()
```


```python
yellow_better_idx = IndexedTextPOS(nltk.WordNetLemmatizer(), yellow_tokens)
yellow_better_idx.concordance("tried")
```

    bent over her small , gloved fingers . I tried to excuse myself , alleging an eng
    od before the steel safe in my bedroom , trying on the golden jewelled crown . Th
    ck to your rooms with you . '' `` Do n't try your doctor 's tricks on me , '' I c
     but if you refuse you shall die . '' He tried to calm me , but I was roused at l



```python
yellow_better_idx.concordance("was")
```

    Winthrop 's administration . The country was apparently tranquil . Everybody know
    knows how the Tariff and Labor questions were settled . The war with Germany , in
    tion of Norfolk by the invading army had been forgotten in the joy over repeated 
    d per cent. , and the territory of Samoa was well worth its cost as a coaling sta
     cost as a coaling station . The country was in a superb state of defense . Every
     state of defense . Every coast city had been well supplied with land fortificati
    d according to the Prussian system , had been increased to three hundred thousand
     The gentlemen from the West had at last been constrained to acknowledge that a c
     a college for the training of diplomats was a necessary as law schools are for t
    diplomats was a necessary as law schools are for the training of barristers ; con
    training of barristers ; consequently we were no longer represented abroad by inc
    oad by incompetent patriots . The nation was prosperous . Chicago , for a moment 
     beautiful than the white city which had been built for its plaything in 1893 . E



# Useful links
### [Ukrainian Brown Corpus](https://github.com/brown-uk/corpus)
### [Ukrainian Corpus with UI](http://www.mova.info/corpus.aspx)
### [Russian National Corpus](http://www.ruscorpora.ru/new/search-main.html)
### [iWeb corpus](https://corpus.byu.edu/iweb/help/iweb_overview.pdf)
### [COCA vs. ANC](https://corpus.byu.edu/coca/compare-anc.asp)
### [COCA vs. BNC](https://corpus.byu.edu/coca/compare-bnc.asp)
### [Tokenization](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)
### [Stemming & Lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)
### [NLTK book](www.nltk.org) (1-3 chapters)


```python

```
