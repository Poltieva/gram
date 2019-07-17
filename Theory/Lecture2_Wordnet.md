
# Linguistic Resources
## How I Learned to Stop Worrying and Love NLTK

# Part II: WordNet

# WordNet
## One of a kind lexical database
## Started in 1985 by Cognitive Science Laboratory of Princeton University
## Became the basis of [FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/), [VerbNet](http://verbs.colorado.edu/~mpalmer/projects/verbnet/downloads.html), [ConceptNet](http://api.conceptnet.io/ld/conceptnet5.6/context.ld.json), [ImageNet](http://www.image-net.org/) and a lot of domain-specific ontologies

# WordNet links

## hypernym: Y is a hypernym of X if every X is a (kind of) Y (`canine` is a hypernym of `dog`)
## hyponym: Y is a hyponym of X if every Y is a (kind of) X (`dog` is a hyponym of `canine`)

## meronym: Y is a meronym of X if Y is a part of X (`window` is a meronym of `building`)
## holonym: Y is a holonym of X if X is a part of Y (`building` is a holonym of `window`)

## and more! (also, those are not only noun-applicable)

# Let's dive in!


```python
import nltk
from nltk.corpus import wordnet as wn
```


```python
# Just in case, don't forget about easily accessible documentation!
help(wn)
```

    Help on LazyCorpusLoader in module nltk.corpus.util object:
    
    wordnet = class LazyCorpusLoader(builtins.object)
     |  To see the API documentation for this lazily loaded corpus, first
     |  run corpus.ensure_loaded(), and then run help(this_corpus).
     |  
     |  LazyCorpusLoader is a proxy object which is used to stand in for a
     |  corpus object before the corpus is loaded.  This allows NLTK to
     |  create an object for each corpus, but defer the costs associated
     |  with loading those corpora until the first time that they're
     |  actually accessed.
     |  
     |  The first time this object is accessed in any way, it will load
     |  the corresponding corpus, and transform itself into that corpus
     |  (by modifying its own ``__class__`` and ``__dict__`` attributes).
     |  
     |  If the corpus can not be found, then accessing this object will
     |  raise an exception, displaying installation instructions for the
     |  NLTK data package.  Once they've properly installed the data
     |  package (or modified ``nltk.data.path`` to point to its location),
     |  they can then use the corpus object without restarting python.
     |  
     |  :param name: The name of the corpus
     |  :type name: str
     |  :param reader_cls: The specific CorpusReader class, e.g. PlaintextCorpusReader, WordListCorpusReader
     |  :type reader: nltk.corpus.reader.api.CorpusReader
     |  :param nltk_data_subdir: The subdirectory where the corpus is stored.
     |  :type nltk_data_subdir: str
     |  :param *args: Any other non-keywords arguments that `reader_cls` might need.
     |  :param *kargs: Any other keywords arguments that `reader_cls` might need.
     |  
     |  Methods defined here:
     |  
     |  __getattr__(self, attr)
     |  
     |  __init__(self, name, reader_cls, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __unicode__ = __str__(self, /)
     |      Return str(self).
     |  
     |  unicode_repr = __repr__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


# Exlploring synsets


```python
wn.synsets("class")
```




    [Synset('class.n.01'),
     Synset('class.n.02'),
     Synset('class.n.03'),
     Synset('course.n.01'),
     Synset('class.n.05'),
     Synset('class.n.06'),
     Synset('class.n.07'),
     Synset('class.n.08'),
     Synset('classify.v.01')]




```python
wn.synsets("bitten")
```




    [Synset('bite.v.01'),
     Synset('bite.v.02'),
     Synset('bite.v.03'),
     Synset('sting.v.02')]



# Synset properties


```python
wn.synset('class.n.01').lemma_names()
```




    ['class', 'category', 'family']




```python
wn.synset('class.n.01').definition()
```




    'a collection of things sharing a common attribute'




```python
wn.synset('class.n.01').hypernyms()
```




    [Synset('collection.n.01')]




```python
lemma_good_1 = wn.synset('good.n.02').lemmas()[0]
print("{} - {}".format(lemma_good_1, lemma_good_1.antonyms()))
```

    Lemma('good.n.02.good') - [Lemma('evil.n.03.evil')]



```python
lemma_good_2 = wn.synset('good.n.02').lemmas()[1]
print("{} - {}".format(lemma_good_2, lemma_good_2.antonyms()))
```

    Lemma('good.n.02.goodness') - [Lemma('evil.n.03.evilness')]


# WordNet tags


```python
wn.synsets('duck', pos='v')
```




    [Synset('duck.v.01'),
     Synset('duck.v.02'),
     Synset('dip.v.10'),
     Synset('hedge.v.01')]




```python
wn.synset('small.a.01').lemma_names()
```




    ['small', 'little']




```python
wn.synset('small.a.01').similar_tos()
```




    [Synset('atomic.s.03'),
     Synset('bantam.s.01'),
     Synset('bitty.s.01'),
     Synset('dinky.s.01'),
     Synset('dwarfish.s.01'),
     Synset('elfin.s.02'),
     Synset('gnomish.s.01'),
     Synset('half-size.s.01'),
     Synset('infinitesimal.s.01'),
     Synset('lesser.s.02'),
     Synset('micro.s.01'),
     Synset('microscopic.s.04'),
     Synset('miniature.s.01'),
     Synset('minuscule.s.03'),
     Synset('olive-sized.s.01'),
     Synset('pocket-size.s.02'),
     Synset('puny.s.02'),
     Synset('slender.s.04'),
     Synset('small-scale.s.01'),
     Synset('smaller.s.01'),
     Synset('smallish.s.01'),
     Synset('subatomic.s.02'),
     Synset('undersize.s.01')]



# Help is on the way!


```python
print(nltk.corpus.reader.wordnet.Synset.__doc__)
```

    Create a Synset from a "<lemma>.<pos>.<number>" string where:
        <lemma> is the word's morphological stem
        <pos> is one of the module attributes ADJ, ADJ_SAT, ADV, NOUN or VERB
        <number> is the sense number, counting from 0.
    
        Synset attributes, accessible via methods with the same name:
    
        - name: The canonical name of this synset, formed using the first lemma
          of this synset. Note that this may be different from the name
          passed to the constructor if that string used a different lemma to
          identify the synset.
        - pos: The synset's part of speech, matching one of the module level
          attributes ADJ, ADJ_SAT, ADV, NOUN or VERB.
        - lemmas: A list of the Lemma objects for this synset.
        - definition: The definition for this synset.
        - examples: A list of example strings for this synset.
        - offset: The offset in the WordNet dict file of this synset.
        - lexname: The name of the lexicographer file containing this synset.
    
        Synset methods:
    
        Synsets have the following methods for retrieving related Synsets.
        They correspond to the names for the pointer symbols defined here:
        https://wordnet.princeton.edu/documentation/wninput5wn
        These methods all return lists of Synsets.
    
        - hypernyms, instance_hypernyms
        - hyponyms, instance_hyponyms
        - member_holonyms, substance_holonyms, part_holonyms
        - member_meronyms, substance_meronyms, part_meronyms
        - attributes
        - entailments
        - causes
        - also_sees
        - verb_groups
        - similar_tos
    
        Additionally, Synsets support the following methods specific to the
        hypernym relation:
    
        - root_hypernyms
        - common_hypernyms
        - lowest_common_hypernyms
    
        Note that Synsets do not support the following relations because
        these are defined by WordNet as lexical relations:
    
        - antonyms
        - derivationally_related_forms
        - pertainyms
        


# DIY Time!
## Let's write a function that will pretty print all info that WordNet has for a word:
## ---- the function accepts a word as an argument
## ---- if a word is not present in WordNet, prints apologies :)
## ---- otherwise prints information on the word in a fancy way
## Hint: use the documentation to find what info is availiable

# Sample output


```python
from solutions.print_info import *
wordnet_info("Carcosa")
```

    The word 'Carcosa' was not found. I'm sorry, I'm so sorry.



```python
wordnet_info("bug")
```

    The word 'bug' has the following meanings:
    
    1. NOUN: general term for any insect or similar creeping or crawling invertebrate
    Hypernyms: insect.
    
    2. NOUN: a fault or defect in a computer program, system, or machine
    It has the following synonyms: glitch.
    Hypernyms: defect.
    
    3. NOUN: a small hidden microphone; for listening secretly
    Hypernyms: microphone.
    
    4. NOUN: insects with sucking mouthparts and forewings thickened and leathery at the base; usually show incomplete metamorphosis
    It has the following synonyms: hemipterous_insect, hemipteran, hemipteron.
    Hypernyms: insect.
    Hyponyms: backswimmer, bedbug, coreid_bug, leaf_bug, lygaeid, true_bug.
    Holonyms: hemiptera.
    
    5. NOUN: a minute life form (especially a disease-causing bacterium); the term is not in technical use
    It has the following synonyms: microbe, germ.
    Hypernyms: microorganism.
    
    6. VERB: annoy persistently
    Typical examples of usage:
    'The children teased the boy because of his stammer'
    It has the following synonyms: tease, badger, pester, beleaguer.
    Hypernyms: torment.
    
    7. VERB: tap a telephone or telegraph wire to get information
    Typical examples of usage:
    'The FBI was tapping the phone line of the suspected spy'
    'Is this hotel room bugged?'
    It has the following synonyms: wiretap, tap, intercept.
    Hypernyms: listen_in.


# Let's explore verb-specific data

### Causes: A causes B if B inevitably happens because of A


```python
wn.synset('transfer.v.05').causes()
```




    [Synset('change_hands.v.01')]



### Entailments: A entails B if A cannot be done without doing B


```python
wn.synset('eat.v.01').entailments()
```




    [Synset('chew.v.01'), Synset('swallow.v.01')]



### Verb groups: verbs similar in meaning that have been manually grouped together.


```python
wn.synset('train.v.01').verb_groups()
```




    [Synset('build_up.v.05'), Synset('prepare.v.05'), Synset('train.v.02')]



# DIY time
## Write a short function that returns lists of all verbs that:
### --- entail anything
### --- cause anything
### --- are members of a verb group
## Hint: use the all_synsets() method.
## Explore the relations :)

# Sample output


```python
from solutions.verb_rel import *
entailments, causes, verb_groups = verbs_with_relations()
print(len(entailments))
print(len(causes))
print(len(verb_groups))
```

    390
    218
    1498



```python
for e in entailments[33:44]:
    print("{} entails {}".format(e.lemma_names()[0],
                                   " ".join([ent.lemma_names()[0] for ent in e.entailments()])))
```

    freeze entails solidify
    fuse entails heat
    macerate entails drench
    putrefy entails smell
    naturalize entails immigrate
    immigrate entails arrive
    settle entails move
    settle entails migrate
    emigrate entails leave
    scale_down entails decrease
    scale_up entails increase


# More useful (and fun!) methods

# Depth


```python
dog = wn.synset('dog.n.01')
dog.max_depth()
```




    13




```python
dog.min_depth()
```




    8



# Paths in hierarchy


```python
dog.hypernym_paths()
```




    [[Synset('entity.n.01'),
      Synset('physical_entity.n.01'),
      Synset('object.n.01'),
      Synset('whole.n.02'),
      Synset('living_thing.n.01'),
      Synset('organism.n.01'),
      Synset('animal.n.01'),
      Synset('chordate.n.01'),
      Synset('vertebrate.n.01'),
      Synset('mammal.n.01'),
      Synset('placental.n.01'),
      Synset('carnivore.n.01'),
      Synset('canine.n.02'),
      Synset('dog.n.01')],
     [Synset('entity.n.01'),
      Synset('physical_entity.n.01'),
      Synset('object.n.01'),
      Synset('whole.n.02'),
      Synset('living_thing.n.01'),
      Synset('organism.n.01'),
      Synset('animal.n.01'),
      Synset('domestic_animal.n.01'),
      Synset('dog.n.01')]]



## common_hypernyms()
### Provides a tool to learn what two synsets have in common


```python
cat = wn.synset('cat.n.01')
dog.common_hypernyms(cat)
```




    [Synset('object.n.01'),
     Synset('vertebrate.n.01'),
     Synset('chordate.n.01'),
     Synset('physical_entity.n.01'),
     Synset('mammal.n.01'),
     Synset('organism.n.01'),
     Synset('placental.n.01'),
     Synset('living_thing.n.01'),
     Synset('animal.n.01'),
     Synset('carnivore.n.01'),
     Synset('whole.n.02'),
     Synset('entity.n.01')]



## lowest_common_hypernyms()


```python
human = wn.synset("human.n.01")
robot = human.lowest_common_hypernyms(wn.synset("robot.n.01"))[0]
alien = human.lowest_common_hypernyms(wn.synset("alien.n.01"))[0]
unicorn = human.lowest_common_hypernyms(wn.synset("unicorn.n.01"))[0]
print("Human and robot are both {0} ({1})".format(robot.definition(), robot.lemma_names()[0]))
print("Human and alien are both {0} ({1})".format(alien.definition(), alien.lemma_names()[0]))
print("Human and unicorn are both {0} ({1})".format(unicorn.definition(), unicorn.lemma_names()[0]))
```

    Human and robot are both an assemblage of parts that is regarded as a single entity (whole)
    Human and alien are both a living thing that has (or can develop) the ability to act or function independently (organism)
    Human and unicorn are both that which is perceived or known or inferred to have its own distinct existence (living or nonliving) (entity)


# DIY Time
### Let's write a function that would list all parts of an entity (meronyms) with their definitions
### Would you include different meronym types or only one?
### Can you make it write out parts of parts of parts too?
### Can you sort the parts from more general ones to the most specific?

# Sample output


```python
from solutions.parts import bits_and_pieces
bits_and_pieces(wn.synset('snake.n.01'))
```

    No parts found



```python
bits_and_pieces(wn.synset('forest.n.01'))
```

    The parts of forest are the following:
     - underbrush (the brush (small trees and bushes and ferns etc.) growing beneath taller trees in a wood or forest)
     - tree (a tall perennial woody plant having a main trunk and branches forming a distinct elevated crown; includes both gymnosperms and angiosperms)
      - crown (the upper branches and leaves of a tree or other plant)
      - stump (the base part of a tree that remains standing after the tree has been felled)
      - burl (a large rounded outgrowth on the trunk or branch of a tree)
       - burl (the wood cut from a tree burl or outgrowth; often used decoratively in veneer)
      - heartwood (the older inactive central wood of a tree or woody plant; usually darker and denser than the surrounding sapwood)
      - sapwood (newly formed outer wood lying between the cambium and the heartwood of a tree or woody plant; usually light colored; active in water conduction)
      - trunk (the main stem of a tree; usually covered with bark; the bole is usually the part that is commercially useful for lumber)
       - bark (tough protective covering of the woody stems and roots of trees and other woody plants)
      - limb (any of the main branches arising from the trunk or a bough of a tree)



```python
bits_and_pieces(wn.synset('brain.n.01'))
```

    The parts of brain are the following:
     - brainstem (the part of the brain continuous with the spinal cord and comprising the medulla oblongata and pons and midbrain and parts of the hypothalamus)
      - medulla oblongata (lower or hindmost part of the brain; continuous with spinal cord; (`bulb' is an old term for medulla oblongata))
       - respiratory center (the center in the medulla oblongata and pons that integrates sensory information about the level of oxygen and carbon dioxide in the blood and determines the signals to be sent to the respiratory muscles)
      - pons (a band of nerve fibers linking the medulla oblongata and the cerebellum with the midbrain)
       - respiratory center (the center in the medulla oblongata and pons that integrates sensory information about the level of oxygen and carbon dioxide in the blood and determines the signals to be sent to the respiratory muscles)
      - reticular formation (a complex neural network in the central core of the brainstem; monitors the state of the body and functions in such processes as arousal and sleep and attention and muscle tone)
       - reticular activating system (the network in the reticular formation that serves an alerting or arousal function)
     - forebrain (the anterior portion of the brain; the part of the brain that develops from the anterior part of the neural tube)
      - diencephalon (the posterior division of the forebrain; connects the cerebral hemispheres with the mesencephalon)
       - infundibulum (any of various funnel-shaped parts of the body (but especially the hypophyseal stalk))
       - hypothalamus (a basal part of the diencephalon governing autonomic nervous system)
       - mamillary body (one of two small round structures on the undersurface of the brain that form the terminals of the anterior arches of the fornix)
       - thalamus (large egg-shaped structures of grey matter that form the dorsal subdivision of the diencephalon)
        - geniculate body (one of four small oval masses that protrude slightly from the underside of the thalamus and function as synaptic centers on the way to the cerebral cortex)
        - subthalamus (the ventral part of the thalamus)
         - subthalamic nucleus (an oval mass of grey matter located in the caudal part of the subthalamus; associated with the striate body)
       - third eye (a sensory structure capable of light reception located on the dorsal side of the diencephalon in various reptiles)
       - basal ganglion (any of several masses of subcortical grey matter at the base of each cerebral hemisphere that seem to be involved in the regulation of voluntary movement)
       - pituitary (the master gland of the endocrine system; located at the base of the brain)
        - hypophyseal stalk (the funnel-shaped stalk connecting the pituitary gland to the hypothalamus)
        - anterior pituitary (the anterior lobe of the pituitary body; primarily glandular in nature)
         - pars distilis (the anterior part of the anterior pituitary)
        - posterior pituitary (the posterior lobe of the pituitary body; primarily glandular in nature)
         - pars intermedia (a thin piece of tissue that has become part of the posterior pituitary)
       - optic nerve (the cranial nerve that serves the retina)
...


# Semantic similarity metrics

## path_similarity()
### Assigns a score (0...1) based on the shortest path between the concepts in the hypernym hierarchy (None is returned in those cases where a path cannot be found).


```python
cheese = wn.synset('cheese.n.01')
milk = wn.synset('milk.n.01')
dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
fly = wn.synset('fly.n.01')
elephant = wn.synset('elephant.n.01')
print(wn.path_similarity(milk, cheese))
print(wn.path_similarity(dog, cat))
print(wn.path_similarity(fly, elephant))
```

    0.3333333333333333
    0.2
    0.08333333333333333


## wup_similarity()
### Wu-Palmer Similarity
### Considers the depth of the two concepts in the taxonomy and the depth of their most specific ancestor node


```python
print(wn.wup_similarity(milk, cheese))
print(wn.wup_similarity(dog, cat))
print(wn.wup_similarity(fly, elephant))
```

    0.875
    0.8571428571428571
    0.56


# Let's try some disambiguation!
### Implement simplified Lesk algorithm:
### • input = a word and a sentence it is in
### • collect all possible synsets for the word
### • define synset's signature as all the words in its definition and examples
### • choose the synset whose signature has most overlapping words with the input sentence


```python
from solutions.lesk import *
simplified_lesk("flies", "An eagle flies high in the sky.")
simplified_lesk("flies", "I hate those bloodsucker flies around.")
simplified_lesk("bank", "The bank will not be accepting cash on Saturdays.")
simplified_lesk("bank", "The river overflowed the bank.")
```

    flies: fly.v.01, v, travel through the air; be airborne
    flies: fly.n.01, n, two-winged insects characterized by active flight
    bank: depository_financial_institution.n.01, n, a financial institution that accepts deposits and channels the money into lending activities
    bank: bank.n.01, n, sloping land (especially the slope beside a body of water)


# Useful links
### [WordNet online](https://wordnet.princeton.edu/)
### [Using WordNet within NLTK](http://www.nltk.org/howto/wordnet.html)


```python

```
