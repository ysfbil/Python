import nltk
#nltk.download('averaged_perceptron_tagger')
tokens=nltk.word_tokenize("Can you buy me a red chili pepper from gorecery?")
print("Part of Speech: ", nltk.pos_tag(tokens))


'''
Çıktı:

Part of Speech:  [('Can', 'MD'), ('you', 'PRP'), ('buy', 'VB'), ('me', 'PRP'), ('a', 'DT'), ('red', 'JJ'), ('chili', 'NN'), ('pepper', 'NN'), ('from', 'IN'), ('gorecery', 'NN'), ('?', '.')]

'''