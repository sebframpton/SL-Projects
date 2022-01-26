

# Print odd numbers modulus
print("odd numbers")
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)

print("---")
# Print even numbers modulus
print("even numbers")
for numbers in range(1, 10):
    if(numbers % 2 != 1):
        print(numbers)


num = int(input("Prompt: What number are you thinking?: "))

print("Input: ", num)
if (num % 2) == 0:
    print("Output: that's an even number")
else:
    print("Output: that's a odd number")
