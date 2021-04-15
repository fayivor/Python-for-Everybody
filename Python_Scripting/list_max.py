"""
Write a Python function  that takes a non-empty list of numbers  and returns
maximum (largest) number in the list. Since there is a built-in function
in Python that performs this computation in a single step, instead implement
this function using a loop that iterates over the input list

Solution - Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    maximum = numbers[0]
    for number in numbers[1 :]:
        if number > maximum:
            maximum = number
    return maximum

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))


# Output
#4
#4
#7
#5
