import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
# Sample text
text = ("Natural language processingexplores "
        "applications such as sentimentanalysis"
        " and named entity recognition.")
words = word_tokenize(text)

pos_tags = pos_tag(words)
# Perform Named Entity Recognition
ner_result = ne_chunk(pos_tags)

print("Named Entity Recognition:")
print(ner_result)