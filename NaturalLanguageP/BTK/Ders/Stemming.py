#kelime kökünü bulma

import nltk

from nltk.stem.porter import * 
porter_stemmer=PorterStemmer()
word='civilizations'
print(porter_stemmer.stem(word))

'''
Çıktı:

civil

'''