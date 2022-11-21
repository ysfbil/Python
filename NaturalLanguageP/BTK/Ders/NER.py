#name entitiy recognition NER: kelime sınıflarının çıkarılması
import nltk
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk import ne_chunk
sentence="Legendary scientist Alber Einstein is born in Ulm, Germany."
tokens=nltk.word_tokenize(sentence)
tagged_tokens=nltk.pos_tag(tokens)
entities=nltk.chunk.ne_chunk(tagged_tokens)
print(entities)

''' Çıktı:
(S
  Legendary/JJ
  scientist/NN
  (PERSON Alber/NNP Einstein/NNP)
  is/VBZ
  born/VBN
  in/IN
  (GPE Ulm/NNP)
  ,/,
  (GPE Germany/NNP)
  ./.)
 '''
