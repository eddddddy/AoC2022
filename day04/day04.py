import os
from string import ascii_letters


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(',') for line in lines]
        lines = [[[int(i) for i in interval.split('-')] for interval in line] for line in lines]

    return lines


def part1(assignments):
    total = 0
    for range1, range2 in assignments:
        low1, high1 = range1
        low2, high2 = range2

        if (low1 <= low2 and high1 >= high2) or (low2 <= low1 and high2 >= high1):
            total += 1

    return total


def part2(assignments):
    total = 0
    for range1, range2 in assignments:
        low1, high1 = range1
        low2, high2 = range2

        if (low2 <= low1 <= high2) or (low2 <= high1 <= high2) or (low1 <= low2 <= high1) or (low1 <= high2 <= high1):
            total += 1

    return total


def main():
    assignments = read_input()
    print(part1(assignments))
    print(part2(assignments))


if __name__ == '__main__':
    main()
