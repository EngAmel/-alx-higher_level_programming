#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new = ""
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            continue
        else:
            new += ch
        i += 1
    return new
