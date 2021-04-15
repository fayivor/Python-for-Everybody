"""
Solution - Remove duplicates from a list while preserving the order of items
"""

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]
print(cleanlist)


def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    no_duplicates = []
    for item in items:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return no_duplicates



# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']
