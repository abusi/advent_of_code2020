def stage_one(inp, sx=1, sy=3):
    nb_tree = 0
    y = 0
    line_size = len(inp[0])
    size_mountain = len(inp)
    for x in range(0, size_mountain, sx):
        if inp[x][y] == "#":
            nb_tree = nb_tree + 1
        y = (y + sy) % (line_size - 1)

    return nb_tree


def solve(inp):

    r1_3 = stage_one(inp)

    r1_1 = stage_one(inp, 1, 1)
    r1_5 = stage_one(inp, 1, 5)
    r1_7 = stage_one(inp, 1, 7)
    r2_1 = stage_one(inp, 2, 1)

    r = r1_3 * r1_1 * r1_5 * r1_7 * r2_1

    return r1_3, r
