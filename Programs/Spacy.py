#Working with spaCy
import spacy
nlp = spacy.load("en_core_web_md")
# nlp() creates a Doc object
text = nlp("Jack Sparrow was a legendary pirate of the Seven Seas, " +
           "and the irreverent trickster of the Caribbean. Jack's " +
           "first love was the sea. His second love was his beloved " +
           "ship, the Black Pearl.")
# text.sents -> sentences
for sentence in text.sents:
    print(sentence)

# text.ents -> entities; each entity has a .label_
for entity in text.ents:
    print("{:<20}{:10}{:5}{:5}".format(entity.text, entity.label_,
                                          entity.start, entity.end))
 # Let's work with the second sentence onwards
second_sentence = list(text.sents)[1]
# Doc is a sequence of Token objects
for token in second_sentence:
    print("{:<5}{:12}{:12}".format(token.i, token.text, token.lemma_))

for token in second_sentence:
    print("{:<5}{:<7}{:12}{:12}{:10}{:5}{:5}".format(
        token.i, token.idx, token.text, token.lemma_, token.shape_,
        token.is_punct, token.whitespace_ == " "))

# each Token contains information about its POS tag
for token in second_sentence:
    print("{:<5}{:12}{:12}{:7}{:7}".format(
        token.i, token.text, token.lemma_, token.tag_, token.pos_))

 # each Token contains information about its Entity
for token in second_sentence:
    print("{:<5}{:12}{:10}".format(
        token.i, token.text, token.ent_type_)) # also: token.ent_iob_

# each Token contains information about its dependency and its parent
for token in second_sentence:
    print("{:<5}{:12}{:12}{:10}".format(
        token.i, token.text, token.dep_, token.head.text))

 # each Token contains information about its children
for token in second_sentence:
    children = list(token.children)
    if len(children) > 0:
        print("Children of \"{}\": {}"
              .format(token.text,
                      [child.text for child in children]))

from spacy import displacy
sentence = nlp("Jack Sparrow was a legendary pirate of the Seven Seas.")
# visualization of dependencies
displacy.render(sentence, style='dep',
                options={"collapse_punct": False, "distance": 110},
                jupyter=True)
# visualization of entities
displacy.render(sentence, style='ent',
                options={"collapse_punct": False, "distance": 110},
                jupyter=True)