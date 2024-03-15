#!/usr/bin/python3
import sys
import calculator_1


def main():
    argv = sys.argv
    argv_len = len(argv) - 1
    ops = "+-*/"
    funcs = [
            calculator_1.add,
            calculator_1.sub,
            calculator_1.mul,
            calculator_1.div
            ]

    if (argv_len != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if (argv[2] not in ops):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])

    for ind, op in enumerate(ops):
        if (argv[2] == op):
            print(f"{num1} {op} {num2} = {funcs[ind](num1, num2)}")


if __name__ == "__main__":
    main()
