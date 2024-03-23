import numpy as np
import re

def make_array(user_input):
    try:
        elements_list = user_input.split()
        numpy_array = np.array(elements_list)
        return numpy_array
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def file_to_array(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().split()
        return np.array(content)
    except FileNotFoundError as fe:
        print(f"Error: {fe}")
        return np.array([])

def remove_word(main_array, remove_array):
    try:
        return np.setdiff1d(main_array, remove_array)
    except Exception as e:
        print(f"Error during removal: {e}")
        return main_array

def check_match_value(array1, array2):
    try:
        return np.isin(array1, array2)
    except Exception as e:
        print(f"Error during matching check: {e}")
        return np.array([])

def get_match_value_index(main_array, check_array):
    try:
        return np.where(np.isin(main_array, check_array))[0]
    except Exception as e:
        print(f"Error during getting matching values: {e}")
        return np.array([])

def read_value_by_index(main_array, indices):
    try:
        return main_array[indices]
    except IndexError as ie:
        print(f"Error: {ie}")
        return np.array([])
    except Exception as e:
        print(f"Error during reading values by index: {e}")
        return np.array([])

def elementwise_power(array, exponent):
    try:
        return np.power(array, exponent)
    except Exception as e:
        print(f"Error during element-wise power operation: {e}")
        return np.array([])

def mean_of_array(array):
    try:
        return np.mean(array)
    except Exception as e:
        print(f"Error calculating mean: {e}")
        return None

def concatenate_arrays(array1, array2):
    try:
        return np.concatenate((array1, array2))
    except Exception as e:
        print(f"Error during concatenation: {e}")
        return np.array([])

def sort_array(array):
    try:
        return np.sort(array)
    except Exception as e:
        print(f"Error during sorting: {e}")
        return np.array([])

def unique_elements(array):
    try:
        return np.unique(array)
    except Exception as e:
        print(f"Error finding unique elements: {e}")
        return np.array([])

def median_of_array(array):
    try:
        return np.median(array)
    except Exception as e:
        print(f"Error calculating median: {e}")
        return None

def reshape_array(array, shape):
    try:
        return np.reshape(array, shape)
    except Exception as e:
        print(f"Error during array reshaping: {e}")
        return np.array([])

def max_value_index(array):
    try:
        return np.argmax(array)
    except Exception as e:
        print(f"Error finding index of maximum value: {e}")
        return None

def min_value_index(array):
    try:
        return np.argmin(array)
    except Exception as e:
        print(f"Error finding index of minimum value: {e}")
        return None

def elementwise_multiply(array1, array2):
    try:
        return np.multiply(array1, array2)
    except Exception as e:
        print(f"Error during elementwise multiplication: {e}")
        return np.array([])
def convert_to_sentence(array):
    try:
        sentence = '\n'.join(array)
        return sentence
    except Exception as e:
        print(f"Error during sentence conversion: {e}")
        return ''
def array_to_file(file_names_array):
    try:
        combined_content = []
        for file_name in file_names_array:
            with open(file_name, 'r') as file:
                content = file.read().split()
            combined_content.extend(content)
        return np.array(combined_content)
    except FileNotFoundError as fe:
        print(f"Error: {fe}")
        return np.array([])
       
def word_is_exist_with(array, word):
    match_found = False
    for value in array:
        if re.search(re.escape(word), str(value)):
            try:
                with open(f"{value}", "r") as file:
                    content = file.read()
                    # Split the file content or perform other actions as needed
                    print(f"File content for {value}: {content}")
                match_found = True
            except FileNotFoundError:
                print(f"File {value} not found.")
        else:
            print(f"False")
    
    print(f"True" if match_found else "False")
        
        
def check_word_exist(input_array, array_file):
    # Load arrays using numpy
    input_words = np.array(input_array)
    array_file_words = np.loadtxt(array_file, dtype=str)

    # Check if every word in the input array exists in the array file
    result = all(np.isin(input_words, array_file_words))

    if result:
        return "All words exist."
    else:
        return "Sorry, not all words exist."    
import numpy as np

def open_file_and_read_value(numpy_array):
    for index, word in enumerate(np.nditer(numpy_array)):
        word_str = str(word)
        filename = f"{word_str}.txt"

        try:
            with open(filename, "r") as file:
                content = file.read()
                print(f"File content for {filename}: {content}")
        except FileNotFoundError:
            if '.txt' not in word_str:
                print(f"Word at index {index} does not contain '.txt'")
                try:
                    new_word = numpy_array[index + 1]
                    print(f"New word at index {index + 1}: {new_word}")
                except IndexError:
                    print("No new word found at the next index.")
def array_to_words(arr):
    return ' '.join(map(str, arr))

# Example usage:
"""numpy_array = np.array(['apple', 'banana', 'orange.txt'])
open_file_and_read_value(numpy_array)"""
        
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
        