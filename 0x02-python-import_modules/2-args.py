#!/usr/bin/python3
import sys


def main():
    arg_len = len(sys.argv) - 1

    if (arg_len == 0):
        print("{} arguments.".format(arg_len))
        return
    elif (arg_len == 1):
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))

    for ind, args in enumerate(sys.argv):
        if (ind == 0):
            continue
        print("{}: {}".format(ind, args))


if __name__ == "__main__":
    main()
