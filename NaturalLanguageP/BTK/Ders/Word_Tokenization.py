import nltk

# nltk.download('punkt')

from nltk import word_tokenize 
sentences = [
"Susmayın !", 
"Saat 16' da Kadıköy'de buluşalım. ",
"Açıklık cahillik göstergesinin en üst sınırıdır. ",
"Fuhşiyat geleceği karartır. ",
"Bozgunculuk, insanlığa ihanettir. ",
"Her sessiz kalınan haram bir gün sizi bulur.", 
"Bunlar Allah'ın kanunlarıdır."]
 
for sentence in sentences:
    print(word_tokenize(sentence))


'''

Çıktı:

['Susmayın', '!']
['Saat', '16', "'", 'da', "Kadıköy'de", 'buluşalım', '.']
['Açıklık', 'cahillik', 'göstergesinin', 'en', 'üst', 'sınırıdır', '.']
['Fuhşiyat', 'geleceği', 'karartır', '.']
['Bozgunculuk', ',', 'insanlığa', 'ihanettir', '.']
['Her', 'sessiz', 'kalınan', 'haram', 'bir', 'gün', 'sizi', 'bulur', '.']
['Bunlar', "Allah'ın", 'kanunlarıdır', '.']

'''