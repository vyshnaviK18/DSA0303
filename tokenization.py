# import the existing word and sentence tokenizing 
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 

text =  "The quick brown fox jumps over the lazy dog. " \
      "Python is a versatile programming language. " \
      "Natural language processing is a fascinating field " \
      "that involves understanding human language."

print(sent_tokenize(text)) 
print(word_tokenize(text))
