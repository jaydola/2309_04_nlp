import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = ("Named Entity Recognition is crucial"
        " innatural language processing tasks, "
        "identifyingentities such as organizations, persons, andlocations.")

words = word_tokenize(text)

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word)for word in words]

print("Lemmatization:")
print(lemmatized_words)


