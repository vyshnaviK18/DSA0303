import random
from collections import defaultdict

def generate_bigrams(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return bigrams

def generate_bigram_model(bigrams):
    model = defaultdict(list)
    for w1, w2 in bigrams:
        model[w1].append(w2)
    return model

def generate_text(model, start_word, num_words):
    current_word = start_word
    sentence = [current_word]
    for _ in range(num_words):
        if current_word not in model:
            break
        possible_words = model[current_word]
        next_word = random.choice(possible_words)
        sentence.append(next_word)
        current_word = next_word
    return ' '.join(sentence)

#main
text = "This is a car.this car has four wheels.it is red in color"
bigrams = generate_bigrams(text)
model = generate_bigram_model(bigrams)
print(generate_text(model, "This", 10))
