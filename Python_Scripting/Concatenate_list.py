"""
Write a Python function  that takes a list of non-negative integers
and returns a single intege formed by concatenating the digits of the integer
in the list.
Solution - Take a list of integers and concatenate their digits
"""

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    digits = ""
    for number in int_list:
        digits += str(number)
    return int(digits)

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000
