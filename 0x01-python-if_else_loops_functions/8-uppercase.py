#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) in range(ord('a'), ord('z') + 1):
            ord(s) = ord(s) - 32
        print("{:c}.format(ord(s))", end="")
