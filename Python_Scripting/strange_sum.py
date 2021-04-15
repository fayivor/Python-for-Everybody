"""
Takes a list and returns the sum of integers not divisible by 3
"""

def strange_sum(numbers):
    sum = 0
    for number in numbers:
        if number%3 != 0:
            sum += number
    return sum


print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
