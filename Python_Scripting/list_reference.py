"""
Given the list in the template, make a new reference  to .
Update the first entry in  to be zero. What happened to the first entry in.
 Explain your answer (in a comment).

Solution - Analyze another example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment

# Answer - list1 and list2 are two references to distinct lists
# Updating an item in one list does not affect the second list


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]
