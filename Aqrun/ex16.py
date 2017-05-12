# -- coding: utf-8 --
"""
习题 16: 读写文件
"""

from sys import argv

def main_func():
    "Main Func"
    if len(argv) < 2:
        exit("Error: File name arg is required!")
    filename = argv[1]

    print("We're going to erase %r." % filename)
    print("If you don't want that, hit CTRL-C (^c).")
    print("If you want that, hit RETURN.")

    raw_input("?")

    print("Opening the file...")
    target = open(filename, 'w')

    print "Truncating the file. Goodbye!"
    target.truncate()

    print("Now I'm going to ask you for three lines.")

    line1 = raw_input("line 1: ")
    line2 = raw_input("line 2: ")
    line3 = raw_input("line 3: ")

    print("I'm going to write these to the file.")

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print("And finally, we close it.")
    target.close()

if __name__ == '__main__':
    main_func()
