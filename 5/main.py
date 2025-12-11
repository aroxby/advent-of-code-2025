#!/usr/bin/env python3
import sys


def main():
    fresh = 0

    fresh_ranges = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            lower_s, upper_s = line.split("-")
            fresh_ranges.append(range(int(lower_s), int(upper_s) + 1))
        else:
            break

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        iid = int(line)
        for frange in fresh_ranges:
            # print(iid, frange, iid in frange)
            if iid in frange:
                fresh += 1
                break

    print(fresh)


if __name__ == "__main__":
    main()