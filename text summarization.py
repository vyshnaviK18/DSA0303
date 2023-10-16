import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

# Sample text
text = """
Text summarization is the process of reducing a large piece of text to a shorter, coherent version while retaining the most important information.
There are two main approaches to text summarization: extractive and abstractive summarization.
Extractive summarization involves selecting sentences or phrases from the original text and extracting them to form a summary.
In this example, we'll implement extractive summarization using Python and the nltk library.
"""

# Sentence Tokenization
sentences = nltk.sent_tokenize(text)

# Preprocess the text: remove stopwords and punctuation
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Create sentence vectors using TF-IDF
def sentence_to_vector(sentence, word_embeddings):
    words = nltk.word_tokenize(sentence)
    words = [word for word in words if word in word_embeddings]
    if not words:
        return np.zeros(300)
    word_vectors = [word_embeddings[word] for word in words]
    return np.mean(word_vectors, axis=0)

word_embeddings = {}
f = open("glove.txt", encoding="utf-8")
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype="float32")
    word_embeddings[word] = coefs
f.close()

sentence_vectors = [sentence_to_vector(preprocess_text(sentence), word_embeddings) for sentence in sentences]

# Calculate sentence similarity using cosine similarity
def sentence_similarity(s1, s2):
    return 1 - cosine_distance(s1, s2)

# Create a similarity matrix
similarity_matrix = np.zeros((len(sentences), len(sentences)))

for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:
            similarity_matrix[i][j] = sentence_similarity(sentence_vectors[i], sentence_vectors[j])

# Apply PageRank to rank sentences
from networkx import pagerank

nx_graph = nx.from_numpy_array(similarity_matrix)
scores = pagerank(nx_graph)

# Sort sentences by their scores
ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

# Select the top N sentences as the summary
summary_length = 2
summary_sentences = [sentence for score, sentence in ranked_sentences[:summary_length]]

# Print the summary
print("\n".join(summary_sentences))

