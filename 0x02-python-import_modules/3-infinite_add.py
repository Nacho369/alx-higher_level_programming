#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    summ = 0

    for ind, num in enumerate(argv):
        if (ind == 0):
            continue

        summ += int(num)

    print("{}".format(summ))


if __name__ == "__main__":
    main()
