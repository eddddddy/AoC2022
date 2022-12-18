import os
import functools


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line]

    packets = []
    for i in range(0, len(lines), 2):
        # really bad!
        packets.append((eval(lines[i]), eval(lines[i + 1])))

    return packets


def order(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    for i in range(max(len(a), len(b))):
        if i >= len(a) and i >= len(b):
            return 0
        elif i >= len(a):
            return -1
        elif i >= len(b):
            return 1

        suborder = order(a[i], b[i])
        if suborder != 0:
            return suborder

    return 0


def part1(packets):
    total = 0
    for i, (a, b) in enumerate(packets):
        if order(a, b) < 0:
            total += i + 1

    return total


def part2(packets):
    packets = [packet for pair in packets for packet in pair] + [[[2]], [[6]]]
    packets = sorted(packets, key=functools.cmp_to_key(order))

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def main():
    packets = read_input()
    print(part1(packets))
    print(part2(packets))


if __name__ == '__main__':
    main()
