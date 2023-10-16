import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["program", "programs", "programmer", "programming", "programmers"]

stemmed_words = [stemmer.stem(word) for word in words]

for word, stemmed_word in zip(words, stemmed_words):
    print(f"Original Word: {word} \t Stemmed Word: {stemmed_word}")
