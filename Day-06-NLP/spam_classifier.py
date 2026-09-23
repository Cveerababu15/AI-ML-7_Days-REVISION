import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the data
df = pd.read_csv("./Data/spam_data.csv")

print("Data Loaded:")
print(df)

# Understand the data
print("\nFirst 5 rows:")
print(df.head())

print("\nData Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# Clean the text
def clean_text(text):
    text = text.lower()
    text = text.replace("!", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    return text


df["Text"] = df["Text"].apply(clean_text)

print("\nCleaned Text:")
print(df["Text"])


# Features and Target
X = df["Text"]
Y = df["Label"]


# TF-IDF
vectorizer = TfidfVectorizer()

X_tfidf = vectorizer.fit_transform(X)

print("\nTF-IDF Shape:")
print(X_tfidf.shape)


# Train/Test Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X_tfidf,
    Y,
    test_size=0.2,
    random_state=42
)


# Naive Bayes
model = MultinomialNB()

model.fit(X_train, Y_train)


# Prediction
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)


# Evaluation
accuracy = accuracy_score(Y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(Y_test, predictions))


# New Text Prediction
new_messages = [
    "Congratulations you won free money",
    "Please send me the meeting details"
]

new_messages_cleaned = [clean_text(message) for message in new_messages]

new_messages_tfidf = vectorizer.transform(new_messages_cleaned)

new_predictions = model.predict(new_messages_tfidf)

print("\nNew Message Predictions:")

for message, prediction in zip(new_messages, new_predictions):
    print(message, "->", prediction)