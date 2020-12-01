from aoc2020.utils import read_input


def make_int(alist):
    r = []
    for a in alist:
        r.append(int(a))
    return r


def stage_one(inp, target=2020):
    for value in inp:
        if (target - value) in inp:
            return (target - value) * value
    return 0


def stage_two(inp):
    for value in inp:
        r = stage_one(inp, (2020 - value))
        if r:
            return r * value


def solve(inp):
    inp = make_int(inp)

    # Stage One
    print(f"Stage 1: {stage_one(inp)}")

    # Stage Two
    print(f"Stage 2: {stage_two(inp)}")
