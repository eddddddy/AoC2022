import os
import functools


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        lines = [line[0::2] for line in lines]
        lines = [[tuple(int(a) for a in point.split(',')) for point in line] for line in lines]

    return lines


def make_grid(paths):
    flat_paths = functools.reduce(lambda x, y: x + y, paths)

    min_x = min(point[0] for point in flat_paths)
    max_x = max(point[0] for point in flat_paths)
    min_y = 0
    max_y = max(point[1] for point in flat_paths)

    height = max_y - min_y + 1
    width = max_x - min_x + 1

    grid = [['.'] * width for _ in range(height)]

    for path in paths:
        for i in range(len(path) - 1):
            start, end = path[i:i + 2]
            if start[0] == end[0]:
                if start[1] <= end[1]:
                    for j in range(start[1], end[1] + 1):
                        grid[j - min_y][start[0] - min_x] = '#'
                else:
                    for j in range(end[1], start[1] + 1):
                        grid[j - min_y][start[0] - min_x] = '#'
            else:
                if start[0] <= end[0]:
                    for j in range(start[0], end[0] + 1):
                        grid[start[1] - min_y][j - min_x] = '#'
                else:
                    for j in range(end[0], start[0] + 1):
                        grid[start[1] - min_y][j - min_x] = '#'

    return grid, min_x


def part1(grid, min_x):
    grid = [row[:] for row in grid]
    source = (500 - min_x, 0)

    count = 0
    while True:
        pos = source
        while True:
            if pos[1] + 1 >= len(grid):
                return count

            if grid[pos[1] + 1][pos[0]] == '.':
                pos = (pos[0], pos[1] + 1)
                continue

            if pos[0] - 1 < 0:
                return count

            if grid[pos[1] + 1][pos[0] - 1] == '.':
                pos = (pos[0] - 1, pos[1] + 1)
                continue

            if pos[0] + 1 >= len(grid[0]):
                return count

            if grid[pos[1] + 1][pos[0] + 1] == '.':
                pos = (pos[0] + 1, pos[1] + 1)
                continue

            break

        grid[pos[1]][pos[0]] = 'o'
        count += 1


def part2(grid, min_x):
    grid = [row[:] for row in grid]
    padding = len(grid) + 4

    for i, row in enumerate(grid):
        grid[i] = ['.'] * padding + row + ['.'] * padding

    grid.append(['.'] * len(grid[0]))
    grid.append(['#'] * len(grid[0]))
    min_x = min_x - padding

    source = (500 - min_x, 0)

    count = 0
    while True:
        pos = source
        while True:

            if grid[pos[1] + 1][pos[0]] == '.':
                pos = (pos[0], pos[1] + 1)
                continue

            if grid[pos[1] + 1][pos[0] - 1] == '.':
                pos = (pos[0] - 1, pos[1] + 1)
                continue

            if grid[pos[1] + 1][pos[0] + 1] == '.':
                pos = (pos[0] + 1, pos[1] + 1)
                continue

            break

        grid[pos[1]][pos[0]] = 'o'
        count += 1

        if pos == source:
            return count


def main():
    paths = read_input()
    grid, min_x = make_grid(paths)
    print(part1(grid, min_x))
    print(part2(grid, min_x))


if __name__ == '__main__':
    main()
