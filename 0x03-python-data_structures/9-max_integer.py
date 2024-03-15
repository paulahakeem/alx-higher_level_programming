#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    else:
        for element in my_list:
            if not isinstance(element, int):
                return
        my_list.sort()
        return (my_list[len(my_list) - 1])
