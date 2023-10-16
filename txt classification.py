# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample data for text classification
corpus = [
    "This is a positive review.",
    "I enjoyed reading this book.",
    "This is a negative review.",
    "The movie was terrible.",
]

labels = ["positive", "positive", "negative", "negative"]

# Step 1: Feature extraction - Convert text data into numerical vectors using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(corpus)

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Step 3: Build and train a text classification model (e.g., Naive Bayes)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = classifier.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=1)


print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
