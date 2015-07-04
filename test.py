__author__ = 'jersonmezquita'

def multi(user_input):
    user_input = user_input*10
    return user_input

def multi_newline(user_input):
    user_input = (user_input + "\n") * 10
    return user_input


x = raw_input("type your name: ")
y = raw_input("which function u want to ex: multi or multi_newline: ")

if y == "multi":
    print multi(x)

elif y == "multi_newline":
    print multi_newline(x)

