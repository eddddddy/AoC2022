import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        lines = [[line[0], int(line[1])] for line in lines]

    return lines


def sign(x):
    if x > 0:
        return 1

    if x < 0:
        return -1

    return 0


def part1(steps):
    head = (0, 0)
    tail = (0, 0)
    visited = {(0, 0)}

    for dir, num in steps:
        for _ in range(num):
            # update head
            if dir == 'R':
                head = (head[0] + 1, head[1])
            elif dir == 'L':
                head = (head[0] - 1, head[1])
            elif dir == 'U':
                head = (head[0], head[1] + 1)
            else:
                head = (head[0], head[1] - 1)

            # update tail
            x_delta = head[0] - tail[0]
            y_delta = head[1] - tail[1]

            if x_delta not in [-1, 0, 1] or y_delta not in [-1, 0, 1]:
                tail = (tail[0] + sign(x_delta), tail[1] + sign(y_delta))
                visited.add(tail)

    return len(visited)


def part2(steps):
    positions = [(0, 0) for _ in range(10)]
    visited = {(0, 0)}

    for dir, num in steps:
        for _ in range(num):
            # update head
            if dir == 'R':
                positions[0] = (positions[0][0] + 1, positions[0][1])
            elif dir == 'L':
                positions[0] = (positions[0][0] - 1, positions[0][1])
            elif dir == 'U':
                positions[0] = (positions[0][0], positions[0][1] + 1)
            else:
                positions[0] = (positions[0][0], positions[0][1] - 1)

            # update tails
            for i in range(1, 10):
                x_delta = positions[i - 1][0] - positions[i][0]
                y_delta = positions[i - 1][1] - positions[i][1]

                if x_delta not in [-1, 0, 1] or y_delta not in [-1, 0, 1]:
                    positions[i] = (positions[i][0] + sign(x_delta), positions[i][1] + sign(y_delta))

            visited.add(positions[-1])

    return len(visited)


def main():
    steps = read_input()
    print(part1(steps))
    print(part2(steps))


if __name__ == '__main__':
    main()
