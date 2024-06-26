#!/usr/bin/python3
"""
Defines a Log Parsin function
"""
import sys


def print_status():
    """
        Printing the status of the request
    """
    counter = 0
    size = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for x in sys.stdin:
        line = x.split()
        try:
            size += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except KeyboardInterrupt:
            continue
        if counter == 9:
            print("File size: {:d}".format(size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{:d}: {:d}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {:d}".format(size))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{:d}: {:d}".format(key, val))


if __name__ == "__main__":
    print_status()
