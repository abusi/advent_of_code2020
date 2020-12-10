from aoc2020.utils import make_int


def stage1(ordered):

    d1 = 0
    d3 = 1  # cause +3 at the end always
    for i, v in enumerate(ordered):
        prev = ordered[i - 1] if i > 0 else 0
        if v - prev == 1:
            d1 += 1
        if v - prev == 3:
            d3 += 1
    return d1 * d3


def solve(inp):
    inp = make_int(inp)
    s1, s2 = (0, 0)

    ordered = sorted(inp)
    s1 = stage1(ordered)

    return s1, s2
