import nltk

text = "Early parsing in Python NLP code is essential for linguistic analysis."

# Tokenization
tokens = nltk.word_tokenize(text)

# Part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)

# Parsing for syntax (using a simple parser)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(pos_tags)

# Display the parse tree
tree.pretty_print()
