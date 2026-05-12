import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = ("Natural language processing is a"
        " fascinating field of study, and it involves "
        "the analysis of textual data.")

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if
word.lower() not in stop_words]

print("After Stopword Removal:")
print(filtered_words)