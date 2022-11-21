'''
#kelime yapım eksiz halini bulma

#aşağıdaki kurulumları python 3.10.4 64bit üzerinde yapınız
#3.8 32bit hata veriyor

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
'''
import spacy
nlp=spacy.load('en_core_web_sm')
word=nlp('civilizations')

for token in word:
    print(token.lemma_)


'''
Çıktı:

civilization

'''