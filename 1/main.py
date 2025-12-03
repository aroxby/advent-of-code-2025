#!/usr/bin/env python3
import sys


def main():
    size = 100
    pos = 50
    zeros = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        letter, turns = line[0], int(line[1:])

        turns %= size
        if letter == "L":
            turns = -turns
        # else assume R
        pos += turns
        if pos < 0:
            pos += size
        pos %= size

        if pos == 0:
            zeros += 1

    print(zeros)


if __name__ == "__main__":
    main()