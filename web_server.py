from flask import Flask, render_template, request, jsonify
from ncm import make_array, file_to_array, remove_word, check_match_value, get_match_value_index, read_value_by_index, convert_to_sentence, array_to_file, word_is_exist_with, check_word_exist, open_file_and_read_value, array_to_words
from nltk_ncm import remove_unimportant_words_array, sentence_tagging_array

app = Flask(__name__)

def remove_word_from_array(arr, word_to_remove):
    return [word for word in arr if word != word_to_remove]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_input = data['input']
    user_input=user_input.lower()
    file=file_to_array("remove.txt")
    chat = user_input.split()
    chat=remove_word(chat,file)
    chat = remove_unimportant_words_array(chat)

    header_file = file_to_array("header.txt")
    match = check_match_value(chat, header_file)
    match_index = get_match_value_index(header_file, chat)
    match_next_value = read_value_by_index(header_file, match_index + 1)
    file_name = convert_to_sentence(match_next_value)
    new_chat = remove_word_from_array(chat, match_next_value)

    for words in match_next_value:
        if ".txt" in words:
            file = file_to_array(words)
            match_value_1 = check_match_value(new_chat, file)
            match_value_index_1 = get_match_value_index(file, new_chat)
            match_value_next_word_1 = read_value_by_index(file, match_value_index_1 + 1)
            sentence = convert_to_sentence(match_value_next_word_1)
            return jsonify({'output': sentence})
        else:
            file = file_to_array(words)
            match_value_1 = check_match_value(new_chat, file)   
            match_value_index_1 = get_match_value_index(file, new_chat)
            match_value_next_word = read_value_by_index(file, match_value_index_1 + 1)
            sentence = convert_to_sentence(match_value_next_word)
            return jsonify({'output': sentence})

    # Move the return statement outside of the loop
    return jsonify({'output': 'I do not under stand this or i am not training on this type'})

if __name__ == '__main__':
    app.run(debug=True)
