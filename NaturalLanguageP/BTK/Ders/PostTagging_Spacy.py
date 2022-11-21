#python 3.10.4 64bit 
import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp("I want an early upgrade")
for token in doc:
    print(token.text,token.pos_)
    
'''

Çıktı:

I PRON
want VERB
an DET
early ADJ
upgrade NOUN

'''
