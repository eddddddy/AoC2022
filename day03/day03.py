import os
from string import ascii_letters


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def part1(sacks):
    total = 0
    for sack in sacks:
        first = sack[: len(sack) // 2]
        second = sack[len(sack) // 2:]
        both = [item for item in first if item in second][0]
        total += ascii_letters.index(both) + 1

    return total


def part2(sacks):
    total = 0
    for i in range(0, len(sacks) // 3):
        first, second, third = sacks[3 * i: 3 * (i + 1)]
        both = [item for item in first if item in second]
        all = [item for item in both if item in third][0]
        total += ascii_letters.index(all) + 1

    return total


def main():
    sacks = read_input()
    print(part1(sacks))
    print(part2(sacks))


if __name__ == '__main__':
    main()
