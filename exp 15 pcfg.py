from nltk import CFG
from nltk.parse.generate import generate
grammar = CFG.fromstring("""
Story -> Introduction MainQuest End
LocationInfo -> 'He found himself in a small village where he grew up.'
Introduction -> 'Long ago there was a boy who decided to become a knight.'

MainQuest -> LocationInfo 'He had to get a sword first to fight monsters' Navigate

Navigate -> '[He could go west]' GoodEnd | '[He could go east]' BadEnd
GoodEnd -> 'And he lived happily ever after.'
BadEnd -> 'Finally he died painfully.'
End -> 'The End'
""")

#print(grammar.start())
#print(grammar.productions())
for sentence in generate(grammar, n=2):
    print('\n'.join(sentence))
    print('\n')

