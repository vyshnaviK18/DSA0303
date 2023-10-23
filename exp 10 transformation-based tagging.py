def transformation_based_tagging(text):
    words = text.split()
    tagged_words = [(word, 'NNP' if word[0].isupper() else 'NN') for word in words]
    return tagged_words

# Main
text = "Alice lives in Wonderland. She loves it there."
tagged_words = transformation_based_tagging(text)
print(tagged_words)
