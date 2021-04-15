"""
The nested loop below is same as the list comprehension in line 10

"""

for row in range(5):
    for col in range(3):
        print(col + 3 * row)
print("")
nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]

print(nested_list)
