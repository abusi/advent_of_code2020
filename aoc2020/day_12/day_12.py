def move(cc, order, value):
    if order == "N":
        cc[1] += value
    if order == "S":
        cc[1] -= value
    if order == "E":
        cc[0] += value
    if order == "W":
        cc[0] -= value

    return cc


def stage1(inp):
    direct = ["S", "W", "N", "E"]
    facing = "E"
    current_coord = [0, 0]
    for order in inp:
        value = int(order[1:])
        if order[0] in ["S", "W", "N", "E"]:
            current_coord = move(current_coord, order[0], value)
        if order[0] == "R":
            facing = direct[(direct.index(facing) + int(value / 90)) % 4]
        if order[0] == "L":
            nd = direct.index(facing) - int(value / 90)
            if nd < 0:
                nd = 4 - abs(nd)
            facing = direct[nd]
        if order[0] == "F":
            current_coord = move(current_coord, facing, value)

    return abs(current_coord[0]) + abs(current_coord[1])


def stage2(inp):
    current_w_coord = [10, 1]
    current_s_coord = [0, 0]
    for order in inp:
        value = int(order[1:])
        if order[0] in ["S", "W", "N", "E"]:
            current_w_coord = move(current_w_coord, order[0], value)
        if order[0] == "R":
            for _ in range(0, int(value / 90)):
                cc = current_w_coord[1]
                current_w_coord[1] = -current_w_coord[0]
                current_w_coord[0] = cc
        if order[0] == "L":
            for _ in range(0, int(value / 90)):
                cc = current_w_coord[1]
                current_w_coord[1] = current_w_coord[0]
                current_w_coord[0] = -cc
        if order[0] == "F":
            if current_w_coord[0] > 0:
                current_s_coord = move(current_s_coord, "E", value * current_w_coord[0])
            else:
                current_s_coord = move(
                    current_s_coord, "W", value * abs(current_w_coord[0])
                )

            if current_w_coord[1] > 0:
                current_s_coord = move(current_s_coord, "N", value * current_w_coord[1])
            else:
                current_s_coord = move(
                    current_s_coord, "S", value * abs(current_w_coord[1])
                )

    return abs(current_s_coord[0]) + abs(current_s_coord[1])


def solve(inp):
    s1, s2 = (0, 0)

    s1 = stage1(inp)
    s2 = stage2(inp)

    return s1, s2
