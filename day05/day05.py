import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]

    split = lines.index('')

    num_stacks = int(lines[split - 1].strip()[-1])
    stacks = []
    number_line = lines[split - 1]
    for i in range(1, num_stacks + 1):
        stack_index = number_line.index(str(i))
        stack = []
        for line in lines[:split - 1]:
            if line[stack_index] != ' ':
                stack.append(line[stack_index])
        stacks.append(stack)

    steps = lines[split + 1:]
    steps = [step.split() for step in steps]
    steps = [[int(step[1]), int(step[3]), int(step[5])] for step in steps]

    return stacks, steps


def part1(stacks, steps):
    stacks = [stack[:] for stack in stacks]

    for step in steps:
        num, start, end = step
        for _ in range(num):
            crate, stacks[start - 1] = stacks[start - 1][0], stacks[start - 1][1:]
            stacks[end - 1] = [crate] + stacks[end - 1]

    return ''.join([stack[0] for stack in stacks])


def part2(stacks, steps):
    stacks = [stack[:] for stack in stacks]

    for step in steps:
        num, start, end = step
        crates, stacks[start - 1] = stacks[start - 1][:num], stacks[start - 1][num:]
        stacks[end - 1] = crates + stacks[end - 1]

    return ''.join([stack[0] for stack in stacks])


def main():
    stacks, steps = read_input()
    print(part1(stacks, steps))
    print(part2(stacks, steps))


if __name__ == '__main__':
    main()
