import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]

    return lines


def find_dir(tree, dir):
    cur_dir = tree
    for d in dir:
        cur_dir = cur_dir[d]

    return cur_dir


def parse_tree(terminal):
    tree = {'/': {}}
    cwd = ['/']
    cdir = tree['/']

    listing = False
    for line in terminal[1:]:
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    cwd = ['/']
                    cdir = tree['/']
                elif line[2] == '..':
                    cwd = cwd[:-1]
                    cdir = find_dir(tree, cwd)
                else:
                    cwd.append(line[2])
                    cdir = cdir[line[2]]
        elif line[0] == 'dir':
            cdir[line[1]] = {}
        else:
            cdir[line[1]] = int(line[0])

    return tree


def compute_sizes(tree):
    sizes = {}
    for file, val in tree.items():
        if isinstance(val, int):
            sizes[file] = (val, {})
        else:
            dir_sizes = compute_sizes(val)
            sizes[file] = (sum([v[0] for v in dir_sizes.values()]), dir_sizes)

    return sizes


def part1(tree):

    def sum_sizes(tree):
        total = 0
        for file, (size, subtree) in tree.items():
            if subtree:
                s = sum_sizes(subtree)
                if size <= 100000:
                    s += size
                total += s

        return total

    sizes = compute_sizes(tree)
    return sum_sizes(sizes)


def part2(tree):

    def min_dir(tree):
        min = sizes['/'][0] + 1
        for file, (size, subtree) in tree.items():
            if subtree:
                sub_min = min_dir(subtree)
                if min_size <= sub_min < min:
                    min = sub_min
                elif min_size <= size < min:
                    min = size

        return min

    sizes = compute_sizes(tree)
    min_size = sizes['/'][0] - 40000000
    return min_dir(sizes)


def main():
    terminal = read_input()
    tree = parse_tree(terminal)
    print(part1(tree))
    print(part2(tree))


if __name__ == '__main__':
    main()
