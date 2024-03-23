import pandas as pd

def read_csv(file_path):
    """
    Reads a CSV file using pandas and returns a DataFrame.
    """
    return pd.read_csv(file_path)

def check_in_csv(csv_file, array):
    """
    Reads a CSV file and checks if any word in the given array is present in the CSV.
    Prints all matching values in plain text.
    """
    df = read_csv(csv_file)
    matching_values = []

    for word in array:
        matches = df[df.apply(lambda row: word in row.values, axis=1)]
        if not matches.empty:
            matching_values.extend(matches.values)

    if matching_values:
        print("")
        for values in matching_values:
            print(values)
    else:
        print("No matching values found.")


def get_all_match_value(csv_file, array):
    """
    Reads a CSV file and retrieves all matching values for each word in the given array.
    Returns a single array containing all matching values.
    """
    df = read_csv(csv_file)
    matching_values = []

    for word in array:
        matches = df[df.apply(lambda row: word in row.values, axis=1)]
        if not matches.empty:
            matching_values.extend(matches.values.flatten())

    return matching_values

# Example usage:
    """
csv_file_path = "my.csv"
array_to_check = ["hi", "hello"]
check_in_csv("my.csv",array_to_check)
"""