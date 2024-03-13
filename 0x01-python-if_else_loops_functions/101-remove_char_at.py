#!/usr/bin/python3

def remove_char_at(str, n):

    str_cp = ""

    for ind, ch in enumerate(str):
        if (ind != n):
            str_cp += ch
        else:
            continue

    return (str_cp)
