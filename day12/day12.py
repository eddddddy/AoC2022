import os
import copy
import queue


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]

    return lines


def make_graph(grid):
    height, width = len(grid), len(grid[0])
    graph_fwd, graph_bwd = {}, {}
    for row in range(height):
        for col in range(width):
            elev = grid[row][col]
            adjs_fwd, adjs_bwd = [], []

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= row + dr < height and 0 <= col + dc < width:
                    adj_elev = grid[row + dr][col + dc]

                    if ord(adj_elev) - ord(elev) <= 1:
                        adjs_fwd.append((row + dr, col + dc))

                    if ord(adj_elev) - ord(elev) >= -1:
                        adjs_bwd.append((row + dr, col + dc))

            graph_fwd[(row, col)] = adjs_fwd
            graph_bwd[(row, col)] = adjs_bwd

    return graph_fwd, graph_bwd


def part1(grid):
    grid = [row[:] for row in grid]

    start, end = None, None
    height, width = len(grid), len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 'S':
                start = (row, col)
                grid[row][col] = 'a'
            elif grid[row][col] == 'E':
                end = (row, col)
                grid[row][col] = 'z'

    graph, _ = make_graph(grid)

    dists = {start: 0}
    to_visit = queue.Queue()
    to_visit.put(start)

    while not to_visit.empty():
        node = to_visit.get()
        adjs = graph[node]
        for adj in adjs:
            if adj not in dists:
                dists[adj] = dists[node] + 1
                to_visit.put(adj)

                if adj == end:
                    return dists[adj]


def part2(grid):
    grid = [row[:] for row in grid]

    starts, end = [], None
    height, width = len(grid), len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col] in ['S', 'a']:
                starts.append((row, col))
                grid[row][col] = 'a'
            elif grid[row][col] == 'E':
                end = (row, col)
                grid[row][col] = 'z'

    _, graph = make_graph(grid)

    dists = {end: 0}
    to_visit = queue.Queue()
    to_visit.put(end)

    while not to_visit.empty():
        node = to_visit.get()
        adjs = graph[node]
        for adj in adjs:
            if adj not in dists:
                dists[adj] = dists[node] + 1
                to_visit.put(adj)

    min_dist = height * width
    for start in starts:
        if start in dists and dists[start] < min_dist:
            min_dist = dists[start]

    return min_dist


def main():
    grid = read_input()
    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()
