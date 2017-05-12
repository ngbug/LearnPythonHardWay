# -- coding: utf-8 -- 
"""
习题 13: 参数、解包、变量
"""

from sys import argv

script, first, second, third = argv

print("The script is called: %s" % script)
print("Your first variable is: %s" % first)
print("Your second variable is: %s" % second)
print("Your third variable is: %s" % third)
