'''Tuple Unpacking


Tuples can be used to output multiple values from a function.
You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
The perimeter is the sum of all sides, while the area is the square of the side length.

Sample Input
3

Sample Output
Perimeter: 12
Area: 9
The given code takes a number from user input, passes it to the calc() function, and uses unpacking to get the returned values.
'''


def calc(x):
    # your code goes here
    a = x * 4
    b = x * x
    return a, b


side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))
