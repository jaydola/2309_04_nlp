from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

text = "Natural language processing is a fascinating field of studies."

words = nltk.word_tokenize(text)

lemmatizer = WordNetLemmatizer()

normalized_words = [lemmatizer.lemmatize(word,
wordnet.VERB) for word in words]
print("Text Normalization:")
print(normalized_words)