import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    cals = []
    elf_cals = []
    for line in lines:
        if not line:
            cals.append(elf_cals)
            elf_cals = []
        else:
            elf_cals.append(int(line))

    return cals


def part1(cals):
    total_cals = [sum(cal) for cal in cals]
    return max(total_cals)


def part2(cals):
    total_cals = [sum(cal) for cal in cals]
    sorted_cals = sorted(total_cals)
    return sum(sorted_cals[-3:])


def main():
    cals = read_input()
    print(part1(cals))
    print(part2(cals))


if __name__ == '__main__':
    main()
