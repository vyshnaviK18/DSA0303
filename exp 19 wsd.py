import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

nltk.download("wordnet")

sentence = "I saw a bat in the cave."
tokens = nltk.word_tokenize(sentence)

word_to_disambiguate = "bat"
sense = lesk(tokens, word_to_disambiguate)

if sense:
    sense_definition = sense.definition()
else:
    sense_definition = "No sense found."

print(f"Word to disambiguate: {word_to_disambiguate}")
print(f"Chosen sense: {sense}")
print(f"Sense definition: {sense_definition}")
