import nltk
from nltk.tokenize import word_tokenize

text = "Natural language processing is a fascinating field of study."
# Tokenize into words
words = word_tokenize(text)

print("Word Tokenization:")
print(words)