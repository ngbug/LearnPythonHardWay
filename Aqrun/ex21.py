# -- coding: utf-8 --
"""
习题 21: 函数可以返回东西
"""

def add(a, b):
    "add func"
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    "subtract func"
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    "multiply func"
    print("MULTIPLYING %d * %d" % (a, b))
    return a*b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (
    age, height, weight, iq
))

# A puzzle for the extra credit, type it in anyway.
print("Here is puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))



print("That becomes: %s Can you do it by hand?" % what)

# 加分练习部分
data_divide = divide(iq, 2)
data_multiply = multiply(weight, data_divide)
data_subtract = subtract(height, data_multiply)
data = add(age, data_subtract)
print("Result is: %s again" % data)