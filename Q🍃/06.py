import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 📊 Sample dataset (you can replace with real dataset later)
data = {
    'email': [
        'Win money now',
        'Hello how are you',
        'Claim your prize',
        'Meeting at 10am',
        'Earn dollars fast',
        'Lets have lunch',
        'Free gift waiting',
        'Project deadline tomorrow'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# ✂ Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['email'], df['label'], test_size=0.25, random_state=42
)

# 🔤 Convert text → numbers
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 🤖 Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 📈 Prediction
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))

# 🔍 Test your own email
def check_email(text):
    vec = vectorizer.transform([text])
    result = model.predict(vec)[0]
    return "Spam" if result == 1 else "Not Spam"

# 🎯 Try it
while True:
    msg = input("\nEnter email text (or 'exit'): ")
    if msg.lower() == 'exit':
        break
    print("Prediction:", check_email(msg))