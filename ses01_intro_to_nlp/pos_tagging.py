import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# Sample text
text = ("POS tagging allows us to discern the"
        " roles of individual words within sentences,"
        " distinguishing between nouns, verbs, adjectives, and more.")

words = word_tokenize(text)

pos_tags = pos_tag(words)
print("POS Tagging:")
print(pos_tags)