#!/usr/bin/python3
for ch in range(0, 100):
    fst = ch // 10
    snd = ch % 10
    if fst != snd and fst < snd:
        if ch != 89:
            print("{:02d}".format(ch), end=", ")
        else:
            print("{:02d}".format(ch))
    else:
        continue
