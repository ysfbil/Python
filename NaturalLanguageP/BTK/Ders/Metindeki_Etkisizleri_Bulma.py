stop_words=['acaba','ve','bir','birçok','ama','için']
message='Acaba metindeki dolgu kelimlerini bulmak ve temizlemek için ne yapılmalı?'
S1=set(stop_words)
S2=set(message.lower().split())
print(S1.intersection(S2))
