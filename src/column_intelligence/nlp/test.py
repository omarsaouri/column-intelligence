import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("kafia laamri est un femme")

for ent in doc.ents:
    print(ent.text, ent.label_)


# ent.label is important
#
