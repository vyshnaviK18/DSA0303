def transformation_based_tagging(text):
    words = text.split()
    tagged_words = []
    
    for i in range(len(words)):
        word = words[i]

        if word[0].isupper() and i != 0:
            tagged_word = (word, 'NNP')
        else:
            tagged_word = (word, 'NN')
        
        tagged_words.append(tagged_word)
    
    return tagged_words

#main
text = "Alice lives in Wonderland. She loves it there."
tagged_words = transformation_based_tagging(text)
print(tagged_words)
