# python 3.10.4 64bit
import spacy
from spacy import displacy
from collections import Counter
nlp=spacy.load('en_core_web_sm')
sentence=nlp('Michael Jordan is a professor at Berkeley')
print([(X.text,X.label_) for X in sentence.ents])

'''
Çıktı:

[('Michael Jordan', 'PERSON'), ('Berkeley', 'ORG')]

'''
