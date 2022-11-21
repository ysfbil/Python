import nltk

# nltk.download('punkt')

from nltk import sent_tokenize 
text = """
Susmayın ! 
Saat 16' da Kadıköy'de buluşalım. 
Açıklık cahillik göstergesinin en üst sınırıdır. 
Fuhşiyat geleceği karartır. 
Bozgunculuk, insanlığa ihanettir. 
Her sessiz kalınan haram bir gün sizi bulur. 
Bunlar Allah'ın kanunlarıdır. """ 
sentences = sent_tokenize(text) 
 
for sentence in sentences:
    print(sentence,"\n")
