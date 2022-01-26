# Phone Number Validator


# You are given a number input, and need to check if it is a valid phone number.
# A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
# Output "Valid" if the number is valid and "Invalid", if it is not.

# Sample Input
# 81239870

# Sample Output
# Valid
# You can use a regular expression to check if the input matches the given pattern.
import re
# your code goes here

x = input()
pattern = r"^(1|8|9)"
if re.match(pattern, x) and len(x) == 8:
    print("Valid")
else:
    print("Invalid")
