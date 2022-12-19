import os
import queue


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = list(lines[0].strip())

    return lines


def is_collision(rock, tower):
    if any(point[0] >= 7 for point in rock):
        return True

    if any(point[0] < 0 for point in rock):
        return True

    if any(point in tower for point in rock):
        return True

    return False


def part1(jets):
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]

    tower = {(i, 0) for i in range(7)}
    height = 0

    # jet index
    j = 0

    for i in range(2022):
        rock_pos = rocks[i % 5]
        rock_pos = [(x + 2, y + height + 4) for (x, y) in rock_pos]

        while True:
            if jets[j] == '<':
                new_rock_pos = [(point[0] - 1, point[1]) for point in rock_pos]
            else:
                new_rock_pos = [(point[0] + 1, point[1]) for point in rock_pos]

            j = (j + 1) % len(jets)

            if not is_collision(new_rock_pos, tower):
                rock_pos = new_rock_pos

            new_rock_pos = [(point[0], point[1] - 1) for point in rock_pos]

            if is_collision(new_rock_pos, tower):
                tower.update(rock_pos)
                height = max(height, max([point[1] for point in rock_pos]))
                break

            rock_pos = new_rock_pos

    return height


def part2(jets):
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]

    tower = {(i, 0) for i in range(7)}
    height = 0

    # jet index
    j = 0

    # input-specific
    init_rock, init_height = 1728, 2711
    period, gain = 1735, 2720

    q = (1000000000000 - init_rock) // period
    r = (1000000000000 - init_rock) % period

    num_rocks = init_rock + r

    for i in range(num_rocks):
        rock_pos = rocks[i % 5]
        rock_pos = [(x + 2, y + height + 4) for (x, y) in rock_pos]

        while True:

            if jets[j] == '<':
                new_rock_pos = [(point[0] - 1, point[1]) for point in rock_pos]
            else:
                new_rock_pos = [(point[0] + 1, point[1]) for point in rock_pos]

            j = (j + 1) % len(jets)

            if not is_collision(new_rock_pos, tower):
                rock_pos = new_rock_pos

            new_rock_pos = [(point[0], point[1] - 1) for point in rock_pos]

            if is_collision(new_rock_pos, tower):
                tower.update(rock_pos)
                height = max(height, max([point[1] for point in rock_pos]))
                break

            rock_pos = new_rock_pos

    return height + q * gain


def main():
    jets = read_input()
    print(part1(jets))
    print(part2(jets))


if __name__ == '__main__':
    main()
