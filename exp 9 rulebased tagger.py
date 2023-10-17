import nltk
from nltk.corpus import wordnet
nltk.download("averaged_perceptron_tagger")

word_classes=['noun','verb','adjective','adverb','open','closed']

pos_tag={'n':'NN','v':'VB','a':'JJ','r':'RB','u':'UH'}

def tag_coord(word):
    synsets=wordnet.synsets(word)
    if synsets:
        pos_tag=pos_tag[synsets[0].pos()[0]]
        return word,pos_tag
    else:
        return word,None
    

def tag_sen(sen):
    token=nltk.word_tokenize(sen)
    tagged_words=[tag_word(token) for token in token]

    return tagged_words


def print_taggedsen(tagged_sen):
    for coord,pos_tag in tagged_sen:
        if pos_tag:
            print(f'{word}/{pos_tag}')
        else:
            print(f'{word}/<not found>')



sen='the quick brown fox jumps over the lazy dog'

tagged_sen=nltk.pos_tag(nltk.word_tokenize(sen))

for word,tag in tagged_sen:
    print(f'{word}/{tag}')