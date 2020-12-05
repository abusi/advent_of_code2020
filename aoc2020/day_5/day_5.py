def solve(inp):
    max = 0
    sids = []
    for line in inp:
        r = [i for i in range(0, 128)]
        c = [i for i in range(0, 8)]
        for i in range(0, 7):

            if line[i] == "F":
                r = r[: int(len(r) / 2)]
            if line[i] == "B":
                r = r[int(len(r) / 2) :]

        for i in range(7, 10):
            if line[i] == "L":
                c = c[: int(len(c) / 2)]
            if line[i] == "R":
                c = c[int(len(c) / 2) :]

        sid = r[0] * 8 + c[0]
        sids.append(sid)
        if sid > max:
            max = sid
    print(f"One: {max}")
    sids = sorted(sids)
    l = 0
    for i in range(1, len(sids)):
        l = sids[i - 1]
        if sids[i] > l + 1:
            print(f"Two: {sids[i] - 1}")
            break
