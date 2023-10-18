import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# Define a context-free grammar for simple English sentences
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'ball'
    V -> 'chased' | 'ate'
""")

# Input sentence to parse
sentence = "the cat chased the dog"

# Tokenize the sentence
tokens = sentence.split()

# Create a parser with the defined grammar
parser = EarleyChartParser(grammar)

# Generate and print the parse tree
for tree in parser.parse(tokens):
    tree.pretty_print()
