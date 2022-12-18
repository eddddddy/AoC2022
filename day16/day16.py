import os
import queue


def read_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]

    valves = {}
    for line in lines:
        valve = line[1]
        rate = int(line[4][5:-1])
        adjs = [adj[:2] for adj in line[9:]]
        valves[valve] = (rate, adjs)

    return valves


def all_pairs_shortest_paths(valves):
    shortest_paths = {}

    for valve in valves:
        dists = {valve: 0}
        to_visit = queue.Queue()
        to_visit.put(valve)

        while not to_visit.empty():
            curr = to_visit.get()
            adjs = valves[curr][1]

            for adj in adjs:
                if adj not in dists:
                    dists[adj] = dists[curr] + 1
                    to_visit.put(adj)

        shortest_paths[valve] = dists

    return shortest_paths


def remove_zero_rates(valves, shortest_paths):
    for valve, (rate, adjs) in valves.items():
        if rate == 0 and valve != 'AA':
            for other in valves:
                if other in shortest_paths:
                    del shortest_paths[other][valve]

            del shortest_paths[valve]


def score(curr, time_left, opened, valves, shortest_paths):
    best_score = 0
    for target, dist in shortest_paths[curr].items():
        if target in opened or dist + 1 >= time_left:
            continue

        target_score = score(target, time_left - dist - 1, opened | {target}, valves, shortest_paths)
        target_score += valves[target][0] * (time_left - dist - 1)

        if target_score > best_score:
            best_score = target_score

    return best_score


def score_p2(curr1, curr2, time_left1, time_left2, opened, valves, shortest_paths):

    # if time_left1 == 0 and time_left2 == 0:
    #     return 0
    #
    # if time_left1 >= time_left2:
    #     best_score = 0
    #     best_target = curr1
    #
    #     for target, dist in shortest_paths[curr1].items():
    #         if target in opened or dist + 1 >= time_left1:
    #             continue
    #
    #         target_score = score_p2(target, curr2, time_left1 - dist - 1, time_left2, opened | {target}, valves, shortest_paths)
    #         target_score += valves[target][0] * (time_left1 - dist - 1)
    #
    #         if target_score > best_score:
    #             best_target = target
    #             best_score = target_score
    #
    #     if best_score == 0:
    #         return score_p2(curr1, curr2, 0, time_left2, opened, valves, shortest_paths)
    #
    #     return best_score
    #
    # else:
    #     best_score = 0
    #     best_target = curr2
    #
    #     for target, dist in shortest_paths[curr1].items():
    #         if target in opened or dist + 1 >= time_left2:
    #             continue
    #
    #         target_score = score_p2(curr1, target, time_left1, time_left2 - dist - 1, opened | {target}, valves, shortest_paths)
    #         target_score += valves[target][0] * (time_left2 - dist - 1)
    #
    #         if target_score > best_score:
    #             best_target = target
    #             best_score = target_score
    #
    #     if best_score == 0:
    #         return score_p2(curr1, curr2, time_left1, 0, opened, valves, shortest_paths)
    #
    #     return best_score

    best_score = 0

    for target1, dist1 in shortest_paths[curr1].items():
        for target2, dist2 in shortest_paths[curr2].items():

            if target1 == target2:
                continue

            continue1 = target1 in opened or dist1 + 1 >= time_left1
            continue2 = target2 in opened or dist2 + 1 >= time_left2

            if continue1 and continue2:
                continue

            elif continue1:
                target_score = score(target2, time_left2 - dist2 - 1, opened | {target2}, valves, shortest_paths)
                target_score += valves[target2][0] * (time_left2 - dist2 - 1)

            elif continue2:
                target_score = score(target1, time_left1 - dist1 - 1, opened | {target1}, valves, shortest_paths)
                target_score += valves[target1][0] * (time_left1 - dist1 - 1)

            else:
                target_score = score_p2(target1, target2, time_left1 - dist1 - 1, time_left2 - dist2 - 1, opened | {target1, target2}, valves, shortest_paths)
                target_score += valves[target1][0] * (time_left1 - dist1 - 1) + valves[target2][0] * (time_left2 - dist2 - 1)

            if target_score > best_score:
                best_score = target_score

    return best_score


def part1(valves):
    shortest_paths = all_pairs_shortest_paths(valves)
    remove_zero_rates(valves, shortest_paths)

    return score('AA', 30, set(), valves, shortest_paths)


def part2(valves):
    shortest_paths = all_pairs_shortest_paths(valves)
    remove_zero_rates(valves, shortest_paths)

    return score_p2('AA', 'AA', 26, 26, set(), valves, shortest_paths)


def main():
    valves = read_input()
    print(part1(valves))
    print(part2(valves))


if __name__ == '__main__':
    main()
