# -- coding: utf-8 --
"""
习题 14: 提示和传递
"""

from sys import argv

def main_func():
    "The main Function"
    data = (0, 0)
    if len(argv) < 2:
        exit('ERROR: arg user_name is needed!')
    else:
        data = argv
    script, user_name = data
    prompt = '>'

    print("Hi %s, I'm the %s script." % (user_name, script))
    print("I'd like to ask you a few questions.")
    print("Do you like me %s?" % user_name)
    likes = input(prompt)

    print("Where do you live %s?" % user_name)
    lives = input(prompt)

    print("What kind of computer do you have?")
    computer = input(prompt)

    print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
    """ % (likes, lives, computer))

if __name__ == '__main__':
    main_func()

