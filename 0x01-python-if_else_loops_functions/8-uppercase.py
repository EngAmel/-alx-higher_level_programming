#!/usr/bin/python3
def uppercase(str):
    new = ""
    for s in str:
        if ord(s) in range(ord('a'), ord('z') + 1):
            new += chr(ord(s) - 32)
        else:
            new += s
    print("{:s}".format(new), end="")
