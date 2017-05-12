# -- coding: utf-8 --
"""
习题 17: 更多文件操作
"""

from sys import argv
from os.path import exists

def main_func():
    "The main func"
    if len(argv) < 3:
        exit("Error: you must assign from_file and to_file!")

    from_file = argv[1]
    to_file = argv[2]

    print("Copying from %s to %s" % (from_file, to_file))

    # We could do these two on one line too, how?
    input = open(from_file)
    indata = input.read()

    print("The input file is %d bytes long" % len(indata))

    print("Does the output file exist? %r" % exists(to_file))
    print("Ready, hit Return to continue, CTRL-C to abort.")
    raw_input()

    output = open(to_file, 'w')
    output.write(indata)
    print("Alright, all done.")

    output.close()
    input.close()



if __name__ == "__main__":
    main_func()
