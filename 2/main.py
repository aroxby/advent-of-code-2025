#!/usr/bin/env python3
import sys


def main():
    ranges = sys.stdin.read().split(",")
    sum = 0
    multiples = True
    used = set()
    for r in ranges:
        lower, upper = (int(s) for s in r.split("-"))
        seen = set()
        for pid in range(lower, upper + 1):
            if pid in seen:
                continue
            seen.add(pid)
            spid = str(pid)
            seq_lens = range(1, len(spid) // 2 + 1) if multiples else [len(spid) // 2]
            for seq_len in seq_lens:
                if seq_len == 1 and len(spid) % 2 != 0 and not multiples:
                    continue
                if len(spid) % seq_len != 0:
                    continue
                prefix = spid[:seq_len]
                multipler = len(spid) // seq_len
                new_pid = prefix * multipler

                if new_pid == spid and spid not in used:
                    print(seq_len, len(spid), pid)
                    used.add(spid)
                    sum += pid

    print(sum)


if __name__ == "__main__":
    main()