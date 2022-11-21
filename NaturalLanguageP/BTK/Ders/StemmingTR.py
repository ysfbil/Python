#pip install snowballstemmer
from snowballstemmer import TurkishStemmer

stemmer=TurkishStemmer()
word='çiçeklikler'
print(stemmer.stemWord(word))

word='ekmeklerdendir'
print(stemmer.stemWord(word))

'''
Çıktı:

çiçeklik
ekmek

'''
