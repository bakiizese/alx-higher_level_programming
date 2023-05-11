#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    ln = len(sys.argv)
    if ln != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
       sys.exit(1)
    a = int(sys.argv[1])
    p = sys.argv[2]
    b = int(sys.argv[3])
    if p == '*':
        print("{} {} {} = {}".format(a, p, b, mul(a, b)))
    elif p == '/':
        print("{} {} {} = {}".format(a, p, b, div(a, b)))
    elif p == '-':
        print("{} {} {} = {}".format(a, p, b, sub(a, b)))
    elif p == '+':
        print("{} {} {} = {}".format(a, p, b, add(a, b)))
    else:
        print("Unknown operator. Availbale operators: +, -, * and /")
        sys.exit(1)
