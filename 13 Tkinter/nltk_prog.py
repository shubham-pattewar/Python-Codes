# NLTK: Natural Language ToolKit

from nltk.tokenize import word_tokenize, sent_tokenize

# Word Tokenization
text = "Hello world! How are you today? I'm learning NLTK."
words = word_tokenize(text)
print(words)

# Sentence Tokenization
sentences = sent_tokenize(text)
print(sentences)