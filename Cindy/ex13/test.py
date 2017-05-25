from sys import argv
print(argv)
script, file = argv
txt = open(file)

print ( txt.read())
txt.close()