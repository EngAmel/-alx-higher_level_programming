#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new = ""
        for i, ch in enumerate(str):
            if i != n:
                new += ch
        return new
    else:
        return str
