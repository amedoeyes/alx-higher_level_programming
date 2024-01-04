#!/usr/bin/python3

import sys
import calculator_1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    ops = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        "*": calculator_1.mul,
        "/": calculator_1.div,
    }

    op = sys.argv[2]

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    res = ops[op](a, b)

    print("{:d} {} {:d} = {:d}".format(a, op, b, res))
