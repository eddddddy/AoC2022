import os
import copy


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line]

    monkeys = []
    for i in range(len(lines) // 6):
        items = lines[6 * i + 1].split()[2:]
        items = [int(item.replace(',', '')) for item in items]

        # really bad!
        operation = ''.join(lines[6 * i + 2].split()[3:])
        operation = eval(f'lambda old: {operation}')

        div = int(lines[6 * i + 3].split()[-1])
        true = int(lines[6 * i + 4].split()[-1])
        false = int(lines[6 * i + 5].split()[-1])

        monkeys.append([items, operation, div, true, false])

    return monkeys


def part1(monkeys):
    monkeys = copy.deepcopy(monkeys)
    counts = [0] * len(monkeys)

    for _ in range(20):
        for i, (items, operation, div, true, false) in enumerate(monkeys):
            for item in items:
                item = operation(item)
                item = item // 3
                if item % div == 0:
                    monkeys[true][0].append(item)
                else:
                    monkeys[false][0].append(item)

            counts[i] += len(items)
            monkeys[i][0] = []

    first = max(counts)
    counts.remove(first)
    second = max(counts)
    return first * second


def part2(monkeys):
    monkeys = copy.deepcopy(monkeys)
    counts = [0] * len(monkeys)

    divs = [monkey[2] for monkey in monkeys]
    for monkey in monkeys:
        monkey[0] = [[item % div for div in divs] for item in monkey[0]]

    for _ in range(10000):
        for i, (items, operation, div, true, false) in enumerate(monkeys):
            for item in items:
                item = [operation(it) % div for it, div in zip(item, divs)]
                if item[i] == 0:
                    monkeys[true][0].append(item)
                else:
                    monkeys[false][0].append(item)

            counts[i] += len(items)
            monkeys[i][0] = []

    first = max(counts)
    counts.remove(first)
    second = max(counts)
    return first * second


def main():
    monkeys = read_input()
    print(part1(monkeys))
    print(part2(monkeys))


if __name__ == '__main__':
    main()
