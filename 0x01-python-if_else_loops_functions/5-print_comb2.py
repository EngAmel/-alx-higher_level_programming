#!/usr/bin/python3
for ch in range(0, 100):
    if ch != 99:
        print("{:02d}".format(ch), end=", ")
    else:
        print("{:02d}".format(ch))
