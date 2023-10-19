import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.metrics import edit_distance

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

text = """
Natural language processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. It involves various techniques for understanding, interpreting, and generating human language. NLP has applications in machine translation, chatbots, and sentiment analysis.
NLP technologies have advanced rapidly in recent years. They have enabled machines to perform tasks like language translation with high accuracy and fluency. Despite these advancements, NLP systems still face challenges related to understanding context and sarcasm.
Word embeddings play a crucial role in NLP. They represent words as vectors in a high-dimensional space, capturing their semantic meaning. Word2Vec and GloVe are popular word embedding models.
"""

sentences = sent_tokenize(text)
words = [word_tokenize(sentence) for sentence in sentences]
def word_similarity(word1, word2):
    synset1 = lesk(word1, word2)
    synset2 = lesk(word2, word1)

    if synset1 and synset2:
        depth1 = synset1.min_depth()
        depth2 = synset2.min_depth()
        return 1 / (depth1 + depth2 + 1)
    else:
        return 1 / (1 + edit_distance(word1, word2))

def calculate_coherence(sentences, words):
    total_similarity = 0
    total_pairs = 0

    for i in range(len(sentences) - 1):
        sentence1 = words[i]
        sentence2 = words[i + 1]

        similarity = 0
        pairs = 0

        for word1 in sentence1:
            for word2 in sentence2:
                similarity += word_similarity(word1, word2)
                pairs += 1

        if pairs > 0:
            total_similarity += similarity / pairs
            total_pairs += 1

    return total_similarity / total_pairs if total_pairs > 0 else 0

coherence = calculate_coherence(sentences, words)
print("Coherence score:", coherence)
