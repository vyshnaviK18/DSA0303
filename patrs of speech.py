import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

txt = "The quick brown fox jumps over the lazy dog. " \
      "Python is a versatile programming language. " \
      "Natural language processing is a fascinating field " \
      "that involves understanding human language."

# sent_tokenize is one of instances of 
# PunktSentenceTokenizer from the nltk.tokenize.punkt module

tokenized = sent_tokenize(txt)
for i in tokenized:
	
	# Word tokenizers is used to find the words 
	# and punctuation in a string
	wordsList = nltk.word_tokenize(i)

	# removing stop words from wordList
	wordsList = [w for w in wordsList if not w in stop_words] 

	# Using a Tagger. Which is part-of-speech 
	# tagger or POS-tagger. 
	tagged = nltk.pos_tag(wordsList)

	print(tagged)
