import nltk

text = "John is a software engineer. He works for a tech company. The company is located in New York. It is known for its innovative products."

sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

pos_tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

resolved_text = []
pronoun_buffer = {}

for sentence, pos_tags in zip(sentences, pos_tagged_sentences):
    resolved_sentence = []

    for word, pos in pos_tags:
        if word.lower() in ("he", "she", "it"):
            antecedent = pronoun_buffer.get(pos.lower())
            if antecedent:
                resolved_sentence.append(antecedent)
            else:
                resolved_sentence.append(word)
        else:
            resolved_sentence.append(word)
            if pos.lower() in ("he", "she", "it"):
                pronoun_buffer[pos.lower()] = word

    resolved_text.append(" ".join(resolved_sentence))

resolved_text = " ".join(resolved_text)

print("Original Text:")
print(text)
print("\nResolved Text:")
print(resolved_text)
