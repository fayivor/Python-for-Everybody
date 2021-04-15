"""
Counts the vowels in the word
"""

def count_vowels(word):
    """
     Takes a string and checks to see if it's a vowel then counts it
    """
    count = 0
    for letter in word:
        if letter in  "aeiou":
            count +=1
        else:
            continue
    return count

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
