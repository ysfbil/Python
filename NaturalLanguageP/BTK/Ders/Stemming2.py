import nltk
from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer(language='english')
word='civilizations'
print(stemmer.stem(word))
