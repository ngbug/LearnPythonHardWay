# -- coding: utf-8 --
"""
习题 33: While 循环
"""

i = 0
numbers = []
while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("Nubmers now: ", numbers)
    print("At the bottom i is %d" % i)

print "The numbers: "

for num in numbers:
    print(num)
