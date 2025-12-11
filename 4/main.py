#!/usr/bin/env python3
import sys


def main():
    rolls = 0
    grid = [list(line.strip()) for line in sys.stdin]
    h = len(grid)
    w = len(grid[0])
    prev_rolls = -1
    repeating = True
    while rolls != prev_rolls:
        prev_rolls = rolls
        for y in range(h):
            for x in range(w):
                if grid[y][x] not in "@x":
                    continue
                neigh = neighbors(grid, x, y)
                if neigh < 4:
                    grid[y][x] = "x"
                    rolls += 1

        for line in grid:
            print(''.join(line))

        if not repeating:
            prev_rolls = rolls
        else:
            for y in range(h):
                for x in range(w):
                    if grid[y][x] == "x":
                        grid[y][x] = "."

    print(rolls)


def neighbors(grid, x, y):
    h = len(grid)
    w = len(grid[0])
    count = 0
    for ny in range(max(0, y-1), min(h, y+2)):
        for nx in range(max(0, x-1), min(w, x+2)):
            if nx == x and ny == y:
                continue
            if  grid[ny][nx] in "@x":
                count += 1
    return count


if __name__ == "__main__":
    main()