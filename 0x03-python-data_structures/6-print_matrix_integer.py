#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    # [print(elem) for row in matrix for elem in row]

    for row in matrix:
        for col in row:
            print("{}".format(col), end=" ")
        print("")
