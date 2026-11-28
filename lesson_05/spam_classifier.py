# our sample emails
emails = [
    # Spam emails
    "Win a free iPhone now",
    "Claim your cash prize",
    "Congratulations you won a lottery",
    "Get a free gift card today",
    "You have won a cash reward",
    "Click here to claim your prize",
    "Earn money quickly from home",
    "Exclusive offer buy now",
    "You are selected for a free vacation",
    "Claim your lottery winnings today",

    # Not Spam emails
    "Meeting scheduled for tomorrow",
    "Please review the project report",
    "Let's discuss the assignment",
    "Can we schedule a team meeting",
    "Please send me the project details",
    "The report is ready for review",
    "Your appointment is confirmed",
    "Let's discuss the work tomorrow",
    "Please check the attached document",
    "The team meeting starts at ten"
]

# labels for the sample emails
labels = [
    "Spam", "Spam", "Spam", "Spam", "Spam",
    "Spam", "Spam", "Spam", "Spam", "Spam",

    "Not Spam", "Not Spam", "Not Spam", "Not Spam",
    "Not Spam", "Not Spam", "Not Spam", "Not Spam",
    "Not Spam", "Not Spam"
]

# print("Emails:", emails)
# print("Labels:", labels)

# from sklearn.feature_extraction.text import CountVectorizer

# # Create a vectorizer
# vectorizer = CountVectorizer()

# Convert emails into numerical data
# X = vectorizer.fit_transform(emails)

# print("Unique words:")
# print(vectorizer.get_feature_names_out())

# print("X:")
# print(X)

# print("\nNumerical representation:")
# print(X.toarray())

from sklearn.model_selection import train_test_split

emails_train, emails_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.33,
    random_state=42
)

print("Training emails:", len(emails_train))
print("Testing emails:", len(emails_test))

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(emails_train)
X_test = vectorizer.transform(emails_test)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

print(vectorizer.get_feature_names_out())
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(X_train, y_train)

print("Model training completed!")

predictions = model.predict(X_test)

print("Predicted labels:", predictions)
print("Actual labels:", y_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")

new_emails = [
    "Congratulations claim your free cash prize"
]

new_emails_vectorized = vectorizer.transform(new_emails)

prediction = model.predict(new_emails_vectorized)

print("New Email:", new_emails[0])
print("Prediction:", prediction[0])

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_test,
    predictions,
    labels=["Spam", "Not Spam"]
)

print("Confusion Matrix:")
print(cm)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))