# Python script to demonstarate tokenization
import nltk
from nltk.tokenize import word_tokenize
# Example
text = "Natural language processing is a fascinating field of study."
# Tokenize into words
words = word_tokenize(text)
# Output: Tokenization into Words and Sentences
print("Tokenization into Words:")
print(words)