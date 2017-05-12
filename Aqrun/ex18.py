# -- coding: utf-8 --
"""
习题 18: 命名、变量、代码、函数
"""

def print_two(*args):
    "This one is like your scripts with argv"
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
    "OK, That *args is actually pointless, we can just do this"
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    "This just takes on argument"
    print("arg1: %r" % arg1)

def print_none():
    "This one takes no arguments"
    print("I got nothin'.")

if __name__ == '__main__':
    print_two('Zed', 'Shaw')
    print_two_again("Zed", "Shaw")
    print_one("First!")
    print_none()