#!/usr/bin/python3

import sys
import math


def factorize(number):
    """Find two factors of the number."""
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i, number // i
    return 1, number


def main(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                n = int(line.strip())
                p, q = factorize(n)
                print(f"{n} = {p} * {q}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
