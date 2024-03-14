#!/usr/bin/python3

for i in range(0, 10):
    for r in range(0, 10):
        if r > i and (i + r) != 17:
            print("{}{}".format(i, r), end=", ")

        elif r > i and (i + r) == 17:
            print("{}{}".format(i, r))
