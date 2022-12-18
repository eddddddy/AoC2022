import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]

    return lines


def part1(insts):
    count_cycles = [20, 60, 100, 140, 180, 220]

    x = 1
    total = 0
    i = 0
    cycle = 1
    execute_count = 0

    while i < len(insts):
        inst = insts[i]

        if cycle in count_cycles:
            total += cycle * x

        if inst[0] == 'noop':
            i += 1
        else:
            if execute_count == 0:
                execute_count = 1
            else:
                x += int(inst[1])
                execute_count = 0
                i += 1

        cycle += 1

    return total


def part2(insts):

    x = 1
    i = 0
    cycle = 1
    execute_count = 0
    screen = []
    row = []

    while i < len(insts):
        inst = insts[i]

        if ((cycle - 1) % 40) + 1 in [x, x + 1, x + 2]:
            row.append('#')
        else:
            row.append('.')

        if cycle % 40 == 0:
            screen.append(row)
            row = []

        if inst[0] == 'noop':
            i += 1
        else:
            if execute_count == 0:
                execute_count = 1
            else:
                x += int(inst[1])
                execute_count = 0
                i += 1

        cycle += 1

    return '\n'.join([''.join(row) for row in screen])


def main():
    insts = read_input()
    print(part1(insts))
    print(part2(insts))


if __name__ == '__main__':
    main()
