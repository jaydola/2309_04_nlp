import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
# Sample text
text = ("Named Entity Recognition is crucial"
        " in natural language processing tasks, "
        "identifying entities such as organizations, persons, and locations.")

words = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
# Lemmatize the words
lemmatized_words = [
    lemmatizer.lemmatize(word) for word in words
]

print("Lemmatization:")
print(lemmatized_words)