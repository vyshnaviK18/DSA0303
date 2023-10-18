import nltk
from nltk import CFG, ChartParser

# Define a context-free grammar for subject-verb agreement
grammar = CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> 'the' 'cat'
    NP_PL -> 'the' 'cats'
    VP_SG -> 'chases'
    VP_PL -> 'chase'
""")

# Function to check subject-verb agreement
def check_agreement(sentence):
    tokens = sentence.split()
    parser = ChartParser(grammar)
    for tree in parser.parse(tokens):
        return True  # Parse tree generated, agreement is correct
    return False  # No valid parse tree found, agreement is incorrect

# Input sentences to check for agreement
sentences = [
    "the cat chases",
    "the cats chases",
    "the cats chase",
    "the cat chase"
]

# Check agreement for each sentence
for sentence in sentences:
    if check_agreement(sentence):
        print(f"'{sentence}' has subject-verb agreement.")
    else:
        print(f"'{sentence}' does not have subject-verb agreement.")
