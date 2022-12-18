import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        lines = [[int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])] for line in lines]

    return lines


def part1(positions):
    row = 2000000

    not_allowed = set()
    for x_s, y_s, x_b, y_b in positions:
        dist = abs(x_s - x_b) + abs(y_s - y_b)
        min_x_dist = dist - abs(y_s - row)

        if min_x_dist >= 0:
            not_allowed.update(range(x_s - min_x_dist, x_s + min_x_dist + 1))

    for _, _, x_b, y_b in positions:
        if y_b == row and x_b in not_allowed:
            not_allowed.remove(x_b)

    return len(not_allowed)


def part2(positions):
    max_pos = 4000000

    disallowed_bounds = {row: [] for row in range(max_pos + 1)}
    for x_s, y_s, x_b, y_b in positions:
        dist = abs(x_s - x_b) + abs(y_s - y_b)
        for row in range(max_pos + 1):
            min_x_dist = dist - abs(y_s - row)

            if min_x_dist >= 0:
                lower = max(0, x_s - min_x_dist)
                upper = min(max_pos, x_s + min_x_dist)
                disallowed_bounds[row].append([lower, upper])

    for row, bounds in disallowed_bounds.items():
        bounds = sorted(bounds, key=lambda x: x[0])
        prev_upper = -1

        for lower, upper in bounds:
            if lower > prev_upper + 1:
                col = prev_upper + 1
                break

            prev_upper = max(prev_upper, upper)
        else:
            continue

        break

    return col * 4000000 + row


def main():
    positions = read_input()
    print(part1(positions))
    print(part2(positions))


if __name__ == '__main__':
    main()
