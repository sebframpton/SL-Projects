# Spelling Backwards


# Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

# Sample Input
# HELLO

# Sample Output
# O
# L
# L
# E
# H
# Complete the recursive spell() function to produce the expected result.
def spell(txt):
    # your code goes here
    for a in txt[::-1]:
        print(a)
    return txt


txt = input()
spell(txt)
