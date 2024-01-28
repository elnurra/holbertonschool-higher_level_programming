#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    count -= 1
    arg1 = "argument:"
    arg2 = "arguments:"
    if count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} {}".format(count, arg1 if count == 1 else arg2))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
