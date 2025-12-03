#!/usr/bin/env python3
import sys


def main():
    size = 100
    pos = 50
    zeros = 0
    clicks = True
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        letter, turns = line[0], int(line[1:])

        if letter == "L":
            turns = -turns
        # else assume R

        while turns < 0:
            turns += 1
            pos -= 1
            pos %= size
            if clicks and pos == 0:
                zeros += 1

        while turns > 0:
            turns -= 1
            pos += 1
            pos %= size
            if clicks and pos == 0:
                zeros += 1

        if not clicks and pos == 0:
            zeros += 1

    print(zeros)


if __name__ == "__main__":
    main()