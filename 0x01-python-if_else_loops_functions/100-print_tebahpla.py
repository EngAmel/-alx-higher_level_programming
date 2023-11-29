#!/usr/bin/python3
new = ""
for s in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - s) % 2 == 0:
        new += chr(s)
    else:
        new += chr(s - 32)
print("{:s}".format(new), end="")
