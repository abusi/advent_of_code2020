def _get_neightbor(x, y, z):
    coord = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if k == 0 and j == 0 and i == 0:
                    continue
                coord.append((x + i, y + j, z + k))
    return coord


def _nb_neightbor_active(nzz, x, y, z):
    nb = 0
    for x, y, z in _get_neightbor(x, y, z):
        if z < 0 or z >= len(nzz):
            continue
        if x < 0 or x >= len(nzz[0][0]):
            continue
        if y < 0 or y >= len(nzz[0]):
            continue
        if nzz[z][y][x] == "#":
            nb += 1
    return nb


def solve(inp):
    mx = len(inp[0].strip())
    my = len(inp)

    s1, s2 = (0, 0)

    zz = [
        [["."] * mx] * my,
        [list(x.strip()) for x in inp if x != "\n"],
        [["."] * mx] * my,
    ]
    nzz = [[["."] * mx] * my] * (len(zz))
    for i in range(0, 6):
        for z in range(0, len(zz)):
            for x in range(0, mx):
                for y in range(0, my):
                    nna = _nb_neightbor_active(zz, x, y, z)
                    if zz[z][y][x] == "#" and not nna in [2, 3]:
                        nzz[z][y][x] = "."
                    if zz[z][y][x] == "." and nna == 3:
                        nzz[z][y][x] = "#"
        zz = nzz
        print("cycle", i)
        for i, z in enumerate(zz):
            print("z=", i)
            for y in z:
                print(y)
            print("")

        zz = [[["."] * mx] * my] + zz
        zz.append([["."] * mx] * my)
        nzz = [[["."] * mx] * my] * (len(zz))

    return s1, s2
