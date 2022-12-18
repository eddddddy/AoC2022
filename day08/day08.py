import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [[int(c) for c in line] for line in lines]

    return lines


def part1(grid):
    height, width = len(grid), len(grid[0])
    visible = [[False for _ in range(width)] for _ in range(height)]

    # from top
    for col in range(width):
        max_height = -1
        for row in range(height):
            if grid[row][col] > max_height:
                visible[row][col] = True
                max_height = grid[row][col]

    # from bottom
    for col in range(width):
        max_height = -1
        for row in range(height - 1, -1, -1):
            if grid[row][col] > max_height:
                visible[row][col] = True
                max_height = grid[row][col]

    # from left
    for row in range(height):
        max_height = -1
        for col in range(width):
            if grid[row][col] > max_height:
                visible[row][col] = True
                max_height = grid[row][col]

    # from right
    for row in range(height):
        max_height = -1
        for col in range(width - 1, -1, -1):
            if grid[row][col] > max_height:
                visible[row][col] = True
                max_height = grid[row][col]

    return sum([sum(row) for row in visible])


def part2(grid):

    def score(row, col):
        tree_height = grid[row][col]

        top_view = 0
        for r in range(row + 1, height):
            top_view += 1
            if grid[r][col] >= tree_height:
                break

        bottom_view = 0
        for r in range(row - 1, -1, -1):
            bottom_view += 1
            if grid[r][col] >= tree_height:
                break

        left_view = 0
        for c in range(col + 1, width):
            left_view += 1
            if grid[row][c] >= tree_height:
                break

        right_view = 0
        for c in range(col - 1, -1, -1):
            right_view += 1
            if grid[row][c] >= tree_height:
                break

        return top_view * bottom_view * left_view * right_view

    height, width = len(grid), len(grid[0])

    max_score = -1
    for row in range(height):
        for col in range(width):
            s = score(row, col)
            if s > max_score:
                max_score = s

    return max_score


def main():
    grid = read_input()
    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()
