#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    args = sys.argv[1:]
    ln = len(args)
    i = 1
    if ln == 0:
        print("{} arguments.".format(ln))
    else:
        if ln == 1:
            print("{} argument:".format(ln))
        else:
            print("{} arguments:".format(ln))
        if args:
            for elm in args:
                print("{}: {}".format(i, elm))
                i += 1
