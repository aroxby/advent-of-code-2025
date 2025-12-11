#!/usr/bin/env python3
import sys


def main():
    jolts = 0
    digits = 12
    for line in sys.stdin:
        bank = line.strip()
        if not bank:
            continue

        bank_jolts_s = ""
        bank_digits = digits
        while(bank_digits > 0):
            bank_digits -= 1
            tens = max(bank[:len(bank) - bank_digits])
            bank = bank.split(tens, 1)[1]
            bank_jolts_s += tens
        print(line.strip(), bank_jolts_s)
        jolts += int(bank_jolts_s)

    print(jolts)


if __name__ == "__main__":
    main()