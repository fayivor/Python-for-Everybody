def count_letters(word_list):
    """ See question description """

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
    for word in word_list:
        for letter in word:
            letter_count[letter] +=1
    v=list(letter_count.values())
    k=list(letter_count.keys())
    return k[v.index(max(v))]
    #return letter_count

print(count_letters(["hello", "world"]))
monty_quote = "listen strange women lying in ponds distributing swords is no basis \
for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
#print(monty_words)
print(count_letters(monty_words))

    # enter code here
