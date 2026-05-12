#Python script to demonsrate stemming with visualization
#-------------------
#0.Import the required modules
#-----------------------

import matplotlib.pyplot as plt
import nltk
import re
from collections import Counter
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


#------------------------
#1.Dowload the required data
#---------------------
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")
#---------------------------------------
#2.Sample text
#----------------------------
TEXT = """
The researchers were studying the running patterns of various animals.
They observed that faster runners consistently outperformed slower ones.
The studies showed interesting running behaviours.
"""

# Initialise the stemmer
stemmer = SnowballStemmer("english")


# -------------------------------------------------------------------------
# 3. Text Preparation Function
# -------------------------------------------------------------------------

def preprocess_text(text: str) -> list:
    """
    """

    tokens = word_tokenize(text.lower())

    cleaned_tokens = [
        re.sub(pattern=r'[^a-z]', repl='', string=token)
        for token in tokens
    ]

    return [token for token in cleaned_tokens if token]


# -------------------------------------------------------------------------
# 4. Stemming Function
# -------------------------------------------------------------------------
def apply_stemming(tokens: list) -> list:
    """
    Apply stemming to a list of tokens.

    :param tokens: List of word tokens
    :return: List of stemmed word tokens
    """

    return [stemmer.stem(token) for token in tokens]


# -------------------------------------------------------------------------
# 5. Visualisation Function
# -------------------------------------------------------------------------
def plot_frequencies(original: list, stemmed: list) -> None:
    original_counts = Counter(original)
    stemmed_counts = Counter(stemmed)

    # Select top items for clarity
    top_original = dict(original_counts.most_common(5))
    top_stemmed = dict(stemmed_counts.most_common(5))

    # Plot original word frequencies
    plt.figure(figsize=(12, 8))
    plt.bar(top_original.keys(), top_original.values())
    plt.title('Top Original Words')

    # Plot stemmed word frequencies
    plt.figure()
    plt.bar(top_stemmed.keys(), top_stemmed.values())
    plt.title('Top Stemmed Words')

    plt.show()


# -------------------------------------------------------------------------
# 6. Main Execution Function
# -------------------------------------------------------------------------
def main():
    print(f"\nOriginal Text:\n{TEXT}")

    # Preprocess the text
    tokens = preprocess_text(TEXT)
    print(f"\nTokens:\n{tokens}")

    # Apply stemming
    stemmed_tokens = apply_stemming(tokens)
    print(f"\nStemmed Tokens:\n{stemmed_tokens}")

    # Show/display visual comparison
    plot_frequencies(tokens, stemmed_tokens)

#---------------------------------------------------
#7.Run the script by invoking the main function(main)
#------------------------------------------------------

if __name__ == "__main__":
    main()

