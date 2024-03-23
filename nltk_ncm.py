# Tokenization and Filtering Module
import nltk
from nltk.corpus import stopwords

def tokenize_sentence(sentence):
    return nltk.word_tokenize(sentence)

def tokenize_array(sentence_array):
    return [nltk.word_tokenize(sentence) for sentence in sentence_array]

def remove_unimportant_words(sentence):
    stop_words = set(stopwords.words('english'))
    return [word for word in nltk.word_tokenize(sentence) if word.lower() not in stop_words]

def remove_unimportant_words_array(sentence_array):
    return [' '.join(remove_unimportant_words(sentence)) for sentence in sentence_array]

def sentence_tagging(sentence):
    tags = nltk.pos_tag(nltk.word_tokenize(sentence))
    return tags

def sentence_tagging_array(sentence_array):
    return [sentence_tagging(sentence) for sentence in sentence_array]


# Library Download Module
import subprocess

def download_library(library_name):
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"Successfully downloaded {library_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to download {library_name}")

# Example usage to download NLTK library
#
# Example Usage

# Download necessary libraries

# Input sentence
"""
input_sentence = "This is an example sentence for tokenization and filtering."

# Tokenize sentence
tokenized_sentence = tokenize_sentence(input_sentence)
print("Tokenized Sentence:", tokenized_sentence)

# Remove unimportant words
filtered_sentence = remove_unimportant_words(input_sentence)
print("Filtered Sentence:", filtered_sentence)

# Sentence tagging
tagged_sentence = sentence_tagging(input_sentence)
print("Tagged Sentence:", tagged_sentence)

# Now, let's try with an array of sentences
input_array = ["Another example sentence.", "Tokenization is interesting."]

# Tokenize array
tokenized_array = tokenize_array(input_array)
print("\nTokenized Array:", tokenized_array)

# Remove unimportant words from array
filtered_array = remove_unimportant_words_array(input_array)
print("Filtered Array:", filtered_array)

# Sentence tagging in array
tagged_array = sentence_tagging_array(input_array)
print("Tagged Array:", tagged_array)"""
