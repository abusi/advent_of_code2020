from copy import deepcopy


def _get_new(inp):
    return deepcopy(inp)


def _find_seat(j, i, mat, offset):
    k = j + offset[0]
    l = i + offset[1]
    while True:
        if k >= len(mat) or k < 0:
            return (-1, -1)
        if l >= len(mat[0]) or l < 0:
            return (-1, -1)
        if mat[k][l] != ".":
            return (k, l)
        k += offset[0]
        l += offset[1]


def _get_coord(j, i, mat=None):
    if not mat:
        return [
            (j + 1, i),
            (j + 1, i + 1),
            (j, i + 1),
            (j - 1, i + 1),
            (j - 1, i),
            (j - 1, i - 1),
            (j, i - 1),
            (j + 1, i - 1),
        ]

    offsets = [
        (+1, 0),
        (+1, +1),
        (0, +1),
        (-1, +1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (+1, -1),
    ]
    return [_find_seat(j, i, mat, off) for off in offsets]


def adjfree(j, i, mat, f=False):
    if not f:
        t = _get_coord(j, i)
    else:
        t = _get_coord(j, i, mat)

    for j, i in t:
        if j >= len(mat) or j < 0:
            continue
        if i >= len(mat[0]) or i < 0:
            continue
        if mat[j][i] == "#":
            return False

    return True


def adjocc(j, i, mat, m, f=False):
    if not f:
        t = _get_coord(j, i)
    else:
        t = _get_coord(j, i, mat)
    occ = 0
    for j, i in t:
        if j >= len(mat) or j < 0:
            continue
        if i >= len(mat[0]) or i < 0:
            continue

        if mat[j][i] == "#":
            occ += 1

    if occ >= m:
        return True

    return False


def make_list_of_list(inp):
    r = [0] * len(inp)
    for i, x in enumerate(inp):
        r[i] = list(x.strip())
    return r


def stage(inp, s, ov):
    change = True
    n = _get_new(inp)
    mat = inp
    while change:
        change = False
        for j, y in enumerate(mat):
            for i, x in enumerate(y):
                if x == "L" and adjfree(j, i, mat, ov):
                    n[j][i] = "#"
                    change = True
                if x == "#" and adjocc(j, i, mat, s, ov):
                    n[j][i] = "L"
                    change = True

        mat = n
        n = _get_new(mat)

    r = 0
    for i in mat:
        for j in i:
            if j == "#":
                r += 1
    return r


def solve(inp):
    inp = make_list_of_list(inp)
    s1, s2 = (0, 0)

    s1 = stage(inp, 4, False)
    s2 = stage(inp, 5, True)
    return s1, s2
