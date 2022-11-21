# https://github.com/fthbrmnby/turkish-text-data
# python 3.8 32bit olmalı
# pip install pandas
# pip install nltk
# nltk.download('stopwords')

import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords

data = pd.read_csv('reviews.csv',delimiter='\t')
data = data.sample(frac=1).reset_index(drop=True)
print(data.head())
print (data['label'].value_counts())

noktalama = string.punctuation
etkisiz= stopwords.words("turkish")
etkisiz.extend(["bir","kadar","sonra"])

# etkisizleri çıkartıyoruz         
data["review"]=data["review"].replace(dict.fromkeys(etkisiz, ''))

# noktalamaları çıkarıyoruz
data["review"]=data["review"].str.translate(str.maketrans('','',noktalama))

#sayıları çıkarıyoruz
data.review = data.review.str.replace('\d+', '',regex=True)

print(data.head())

data.to_csv(r'cleaned.csv',index=False)

print("tamamlandı")
