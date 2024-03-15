#!/usr/bin/python3

def no_c(my_string):

    new_string = [x for x in my_string]
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            new_string[i] = ''

    return ''.join(new_string)
