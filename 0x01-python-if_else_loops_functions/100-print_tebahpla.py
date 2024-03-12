#!/usr/bin/python3

for ch in range(ord('z'), ord('a') - 1, -1):
    if ch % 2 == 1:
        ch = ch - 32
    print("{}".format(chr(ch)), end="")
