#!/usr/bin/python3

for fd in range(0, 9):
    for ld in range(1, 10):
        if (ld > fd):
            print("{}{}".format(fd, ld), end="")
            if (fd != 8 or ld != 9):
                print(", ", end="")
print("")
