import string
message="Dil işlemede kullanılan kütüphaneleri: nltk, spacy, scikit-learn vb."
temizlenmis=message.translate(str.maketrans('','',string.punctuation))
print(message)
print(temizlenmis)
