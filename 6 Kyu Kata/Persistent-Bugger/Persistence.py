"""
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit.
"""
def persistence(n):
    count = 0
    if len(str(n)) == 1:
        return count
    result = 1
    n_chars = [char for char in str(n)]
    for x in n_chars:
        result *= int(x)
    return 1 + persistence(result)
