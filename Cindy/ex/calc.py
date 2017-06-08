def sum (num1, num2):
    return num1 + num2

def minus (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

def calc (handle, num1, num2):
    if handle == '+':
        return sum (num1 , num2)
    elif handle == '-':
         return minus (num1 , num2)
    elif handle == '*':
        return multiply (num1 , num2)
    else:
         return divide(num1 , num2)

if __name__ == '__main__':
    result = calc ('*', 8,2)
    result2 = calc ('+', 8,2)
    result3 = calc('-', 8, 2)
    result4 = calc('/', 8, 2)

    print('%d,%d,%d,%d ' % (result,result2,result3,result4))

