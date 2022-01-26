'''List Comprehensions


Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.

Sample Input
awesome

Sample Output
['w', 's', 'm']

Use a list comprehension to create the required list of letters and output it.
'''

word = input()
newlist = []

for x in word:
    if x not in ("a", "e", "i", "o", "u"):
        newlist.append(x)

print(newlist)
