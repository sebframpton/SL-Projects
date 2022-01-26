# Longest Word


# Given a text as input, find and output the longest word.

# Sample Input
# this is an awesome text

# Sample Output
# awesome
# Recall the split(' ') method, which returns a list of words of the string.
txt = input()
a = txt.split()
longest_string = max(a, key=len)
print(longest_string)


# your code goes here
