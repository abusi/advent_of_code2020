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


def stage2(ordered):
    myplug = max(ordered) + 1
    ways = [0] * myplug
    ways[0] = 1
    for i in range(1, myplug):
        for x in range(1, 4):
            if (i - x) in ordered:
                ways[i] += ways[i - x]
    return ways[-1]


def solve(inp):
    inp = make_int(inp)
    s1, s2 = (0, 0)

    ordered = sorted(inp)
    s1 = stage1(ordered)

    inp.append(0)
    inp.append(max(inp) + 3)
    s2 = stage2(sorted(inp))

    return s1, s2
