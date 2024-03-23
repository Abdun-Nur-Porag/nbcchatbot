def detect_match(word, sentence):
    return word in sentence.lower()

# Read data from file
with open('ai_data.txt', 'r') as file:
    lines = file.readlines()

# Extract word array and sentence
word_to_find = input("Enter the word to find: ").lower()
sentence = lines[1].strip()

# Perform matching
if detect_match(word_to_find, sentence):
    print(sentence)
else:
    print("Word not found in the sentence.")
