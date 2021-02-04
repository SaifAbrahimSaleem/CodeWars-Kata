"""
    Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.
"""
from collections import Counter
def find_it(sequence):
    occurrences = Counter()
    for index, number in enumerate(sequence):
        occurrences[str(number)] += 1
    for key in occurrences:
        if occurrences[key] % 2 != 0:
            return int(key)
    return None
