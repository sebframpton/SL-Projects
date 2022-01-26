# Dictionaries


# You are working at a car dealership and store the car data in a dictionary:
'''car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
}'''


# Your program needs to take the key as input and output the corresponding value.

# Sample Input
# year

# Sample Output
# 2018
# The data is already defined in the code.

car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

txt = input()

print(car[txt])

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
