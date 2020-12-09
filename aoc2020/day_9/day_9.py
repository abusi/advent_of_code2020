from aoc2020.day_1.day_1 import make_int
from aoc2020.day_1.day_1 import stage_one


def find_sumable_contigues(inp, s1):
    s = 0
    while s < len(inp):
        ss = 0
        for i, n in enumerate(inp[s:]):
            ss += n
            if ss == s1:
                return inp[s : s + i + 1]
            if ss > s1:
                break
        s += 1
    return None


def solve(inp):
    inp = make_int(inp)
    ps = 25
    preamble = inp[:ps]
    data = inp[ps:]

    s1 = 0

    for i, n in enumerate(data):
        if not stage_one(preamble, n):
            s1 = n
            break
        preamble = inp[i + 1 :][:ps]

    print(f"One: {s1}")

    sumable = find_sumable_contigues(inp, s1)

    print(f"Two: {min(sumable) + max(sumable)}")
