import nltk

nltk.download('wordnet')

from nltk.corpus import wordnet

def explore_word_meanings(word):
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for '{word}'.")
        return

    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {', '.join(synset.examples())}")
        print(f"Hypernyms (parent terms): {', '.join([h.name() for h in synset.hypernyms()])}")
        print(f"Hyponyms (child terms): {', '.join([h.name() for h in synset.hyponyms()])}")
        print()


word_to_explore = "car"

explore_word_meanings(word_to_explore)
