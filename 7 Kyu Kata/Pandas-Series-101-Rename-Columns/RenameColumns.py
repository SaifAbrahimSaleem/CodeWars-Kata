"""
Input parameters:
    - pandas.DataFrame object
    - sequence
Task:
    Your function must return a new pandas.DataFrame object with same data than the original input but now
    its column names are the elements of the sequence. You must not modify the original input.

    The number of columns of the input will always be equal to the size of the sequence.
"""
import pandas as pd
def rename_columns(df, names):
    # Convert the current names into list form
    current_names = list(df.columns)
    # Convert the new names from tuple to list form
    names = list(names)
    # Create a dictionary to map old names to new names
    rename_dict = {}
    # iterate through the current names and map each value of
    # the new names to the the old names, making them keys of
    # the rename dictionary
    for index, val in enumerate(current_names):
        rename_dict[val] = names[index]
    # rename the dataframe
    return df.rename(columns=rename_dict)
