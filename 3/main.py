#!/usr/bin/env python3
import sys


def main():
    jolts = 0
    for line in sys.stdin:
        bank = line.strip()
        if not line:
            continue

        tens = max(bank[:len(bank) - 1])
        bank = bank.split(tens, 1)[1]
        ones = max(bank)
        print("+", tens+ones)
        jolts += int(tens+ones)

    print(jolts)


if __name__ == "__main__":
    main()