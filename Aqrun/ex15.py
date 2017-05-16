# -- coding:utf-8 --
"""
习题 15: 读取文件
"""

from sys import argv

def main_func():
    data = (0, 0)
    if len(argv) < 2:
        exit('ERROR: arg filename is required!')
    else:
        data = argv
    script, filename = data

    txt = open(filename)
    print("Here's your file %r:" % filename)
    print(txt.read())
    txt.close()

    print("Type the filename again:")
    file_again = input(">")
    txt_again = open(file_again)
    print(txt_again.read())
    txt_again.close()

if __name__=="__main__":
    main_func()

