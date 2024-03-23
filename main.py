from ncm import make_array, file_to_array, remove_word, check_match_value, get_match_value_index, read_value_by_index, convert_to_sentence, array_to_file, word_is_exist_with, check_word_exist, open_file_and_read_value, array_to_words

from nltk_ncm import remove_unimportant_words_array, sentence_tagging_array
from ncm_csv import read_csv,check_in_csv,get_all_match_value
def remove_word_from_array(arr, word_to_remove):
    """
    Removes a specific word from the array.

    Parameters:
    - arr (list): The input array.
    - word_to_remove (str): The word to be removed from the array.

    Returns:
    - list: The modified array after removing the specified word.
    """
    return [word for word in arr if word != word_to_remove]

# Starting
chat = input(">Chat=>")
chat=chat.lower()
chat = chat.split()
chat = remove_unimportant_words_array(chat)
#print(chat)

# get chat and make it an array
header_file = file_to_array("header.txt")
#header_file=remove_unimportant_words_array(header_file)
match = check_match_value(chat, header_file)
#print(match)
match_index = get_match_value_index(header_file, chat)
match_next_value = read_value_by_index(header_file, match_index + 1)
#print(match_next_value)
file_name = convert_to_sentence(match_next_value)
#print(file_name)

new_chat = remove_word_from_array(chat, match_next_value)

# check word existence in header
# layer 1
for words in match_next_value:
    if ".txt" in words:
        print(f".txt exists in {words}")
        # open file due to containing .txt
        #print(new_chat)
        file = file_to_array(words)
        match_value_1 = check_match_value(new_chat, file)
        match_value_index_1 = get_match_value_index(file, new_chat)
        #print(match_value_index_1)
        match_value_next_word_1 = read_value_by_index(file, match_value_index_1 + 1)
        #print(match_value_next_word_1)
        sentence = convert_to_sentence(match_value_next_word_1)
        print(sentence)
        #print(new_chat)
        #check exist of word   
        
    else:
        #print("not exist .txt")
        # read value due to no .txt
        file = file_to_array(words)
        match_value_1 = check_match_value(new_chat, file)   
        #print(match_value_1)
        match_value_index_1 = get_match_value_index(file, new_chat)
        match_value_next_word = read_value_by_index(file, match_value_index_1 + 1)
        #print(match_value_next_word)
        sentence=convert_to_sentence(match_value_next_word)
        print(sentence)
