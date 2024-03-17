#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for ind, col in enumerate(row):
                print("{:d}".format(col), end="")
                if (ind != len(row) - 1):
                    print("", end=" ")
            print("")
