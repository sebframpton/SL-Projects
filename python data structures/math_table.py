# split list into their own elements and rejoin them to display in string format
# and tab new line each math symbol in each column

addition = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(addition)
for i in addition:
    x = i.split()
    print(x)
    listToStr = '\n'.join([str(elem) for elem in addition])
    print(listToStr)

print(i)
# using list comprehension
# listToStr = ''.join([str(elem) for elem in addition])
#b = len(listToStr) / len(addition)
# print(len(listToStr))
# print(listToStr)
# print(b)
