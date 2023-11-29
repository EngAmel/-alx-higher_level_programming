#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for ch, p in str:
        new += chr(ch)
        if p == n:
            continue
    print("{:s}".format(new), end="")
