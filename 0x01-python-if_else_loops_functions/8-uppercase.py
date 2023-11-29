#!/usr/bin/python3
def uppercase(str):
    if ord(*str) in range(ord('a'), ord('z') + 1):
        ord(*str) = ord(*str) - 32
    print("{:s}.format(*str)")
