#!/usr/bin/env python3
import sys


def main():
    total = 0
    grid = []
    for line in sys.stdin:
        line = line.strip()
        parts = [part for part in line.split(" ") if part]
        grid.append(parts)

    h = len(grid)
    w = len(grid[0])
    for x in range(w):
        numbers = [int(grid[y][x]) for y in range(h - 1)]
        operation = grid[h - 1][x]
        result = sum(numbers) if operation == "+" else product(numbers)
        operation = " " + operation + " "
        print(operation.join(str(n) for n in numbers), "=", result)
        total += result

    print(total)


def product(iterable):
    p = iterable[0]
    for n in iterable[1:]:
        p *= n
    return p

if __name__ == "__main__":
    main()