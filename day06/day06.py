import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()

    return lines[0].strip()


def part1(data):
    for i in range(4, len(data) + 1):
        if len(set(data[i - 4: i])) == 4:
            return i


def part2(data):
    for i in range(14, len(data) + 1):
        if len(set(data[i - 14: i])) == 14:
            return i


def main():
    data = read_input()
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()
