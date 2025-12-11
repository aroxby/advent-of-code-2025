#!/usr/bin/env python3
import sys


def main():
    fresh = 0
    totalling = True

    fresh_ranges = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            lower_s, upper_s = line.split("-")
            fresh_ranges.append(range(int(lower_s), int(upper_s) + 1))
        else:
            break

    if totalling:
        old_len = -1
        while len(fresh_ranges) != old_len:
            print(len(fresh_ranges))
            old_len = len(fresh_ranges)
            fresh_ranges = reduce(fresh_ranges)

        for frange in fresh_ranges:
            fresh += len(frange)
    else:
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


def reduce(fresh_ranges):
    new_ranges = []
    for frange in fresh_ranges:
        any_overlap = False
        for idx, nrange in enumerate(new_ranges):
            overlap = bool(range(max(frange[0], nrange[0]), min(frange[-1], nrange[-1]) + 1))
            if overlap:
                new_ranges[idx] = range(min(frange.start, nrange.start), max(frange.stop, nrange.stop))
            any_overlap = any_overlap or overlap
        if not any_overlap:
            new_ranges.append(frange)
    return new_ranges


if __name__ == "__main__":
    main()