import nltk
from nltk.tokenize import word_tokenize
from nltk.parse import ChartParser

# Define a sentence for parsing
sentence = "The fox jumps over dog"

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Define a context-free grammar for parsing
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'The' | 'a'
    N -> 'fox' | 'dog'
    V -> 'jumps' | 'over'
""")

# Create a parser using the defined grammar
parser = ChartParser(grammar)

# Parse the sentence
for tree in parser.parse(words):
    tree.pretty_print()
