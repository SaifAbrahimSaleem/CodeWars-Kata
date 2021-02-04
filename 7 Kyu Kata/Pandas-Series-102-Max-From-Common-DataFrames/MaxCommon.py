"""
Input parameters:
    - Two pandas.DataFrame objects

Task:
    - Your function must return a new pandas.DataFrame with the same data and columns from the first parameter. For common columns in both inputs you must return the greater value of each cell for that column.
    - You must not modify the original inputs.
    - Input DataFrame will never be empty. The number rows of both inputs will be the same.
"""

import pandas as pd

def max_common(df_a, df_b):
    return pd.concat([df_a, df_b]).filter(items=df_a.columns).groupby(level=0).max().astype('float64')
