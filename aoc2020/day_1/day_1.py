from aoc2020.utils import make_int


def stage_one(inp, target=2020, uabs=False):
    abss = abs
    if not uabs:
        abss = lambda x: x
    for value in inp:
        if abss(target - value) in inp:
            return (target - value) * value
    return 0


def stage_two(inp):
    for value in inp:
        r = stage_one(inp, (2020 - value))
        if r:
            return r * value


def solve(inp):
    inp = make_int(inp)
    return stage_one(inp), stage_two(inp)
