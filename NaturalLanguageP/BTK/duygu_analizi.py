import pandas as pd
data = pd.read_csv("cleaned.csv",sep=",",names=["review","label"])

#veriyi train test kümelerine ayırıyoruz

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(data["review"].values.astype('U'),
                                               data["label"].values.astype('U'),
                                               test_size=0.1,random_state=42)
print(X_train.shape)
print(X_test.shape)

#train kümesindeki cümlelerin sayma vektörlerini (kelime sayısı) çıkarıyoruz
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
print(X_train_counts.shape)

#train kümesindeki cümlelerin TF*IDF vektörlerini sayfa vektörlerinden oluşturuyoruz
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

#çok modlu naive bayes sınıflandırıcı eğitiyoruz
from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(X_train_tfidf,y_train)
X_test_counts=count_vect.transform(X_test)
X_test_tfidf=tfidf_transformer.transform(X_test_counts)

#sınıflandırıcı ile test seti üzerinde tahminleme yapıyoruz
y_pred=clf.predict(X_test_tfidf)
for review,sentiment in zip(X_test[:5],y_pred[:]):
    print("%r => %s" % (review,sentiment))

#performans sonuçları
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
