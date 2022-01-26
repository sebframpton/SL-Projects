# Registration System


# You are making a registration form for a website.
# The form has a name field, which should be more than 3 characters long.
# Any name that has less than 4 characters is invalid.
# Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". Output "Account Created" if the name is valid.

# Sample Input
# abc

# Sample Output
# Invalid Name
# Use try/raise/except statements.
try:
    name = input()
    # your code goes here
    x = len(name)
    if x < 4:
        raise
except:
    print("Invalid Name")

else:
    print("Valid Name")
