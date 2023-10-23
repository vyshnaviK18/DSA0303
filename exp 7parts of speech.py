import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


txt = "The quick brown fox jumps over the lazy dog. " \
      "Python is a versatile programming language. " \
      "Natural language processing is a fascinating field " \
      "that involves understanding human language."


tokenized = sent_tokenize(txt)
for i in tokenized:
	
	wordsList = nltk.word_tokenize(i)
	# POS-tagger. 
	tagged = nltk.pos_tag(wordsList)

	print(tagged)
