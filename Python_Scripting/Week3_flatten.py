"""
Solution - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list,
    return the list formed by joining all of these lists
    """
    flattened_list = []
    for sub_list in nested_list:
        flattened_list.extend(sub_list)
    return flattened_list

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]
