#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    sum = 0
    if args:
        for elm in args:
            sum = sum + int(elm)
    print(sum)
