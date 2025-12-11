#!/usr/bin/env python3
import sys


def main():
    ranges = sys.stdin.read().split(",")
    sum = 0
    multiples = False
    for r in ranges:
        lower, upper = (int(s) for s in r.split("-"))
        for pid in range(lower, upper + 1):
            spid = str(pid)
            if len(spid) % 2 != 0:
                continue
            mids = range(len(spid) // 2 + 1) if multiples else [len(spid) // 2]
            for mid in mids:
                left, right = spid[:mid], spid[mid:]
                if left + right == right + left:
                    print(pid)
                    sum += pid

    print(sum)


if __name__ == "__main__":
    main()