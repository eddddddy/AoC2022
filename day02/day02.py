import os


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]

    return lines


def winner(a, x):
    a = {'A': 0, 'B': 1, 'C': 2}[a]
    x = {'X': 0, 'Y': 1, 'Z': 2}[x]

    return (a - x + 3) % 3


def part1(rounds):
    score = 0
    for opp, me in rounds:
        win = winner(opp, me)
        s = {'X': 1, 'Y': 2, 'Z': 3}
        if win == 0:
            # tie
            score += 3 + s[me]
        elif win == 1:
            # loss
            score += s[me]
        else:
            score += 6 + s[me]

    return score


def part2(rounds):
    score = 0
    for opp, out in rounds:
        out = {'X': 1, 'Y': 0, 'Z': 2}[out]
        for me in ['X', 'Y', 'Z']:
            if winner(opp, me) == out:
                break

        s = {'X': 1, 'Y': 2, 'Z': 3}
        if out == 0:
            # tie
            score += 3 + s[me]
        elif out == 1:
            # loss
            score += s[me]
        else:
            score += 6 + s[me]

    return score



def main():
    rounds = read_input()
    print(part1(rounds))
    print(part2(rounds))


if __name__ == '__main__':
    main()
