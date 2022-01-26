'''Boolean Logic


The comfortable relative humidity for humans is between 40% and 60%.
The given program takes the percent of humidity as input.

Task
Complete the code to output "norm" if the taken percent of humidity is in the range of 40 and 60 inclusive.
Don't output anything otherwise.

Sample Input
45

Sample Output
norm
Use the and operator to chain the conditions in the if statement.
'''
humidity = int(input())
# your code goes here
if humidity < 60 and humidity > 40:
    print("norm")
else:
    print("not norm")
