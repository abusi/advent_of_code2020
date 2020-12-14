import math


def next_timestamp(ts, bus):
    x = 0
    while x < ts:
        x += bus
    return x


def stage1(inp):
    timestamp = int(inp[0])
    buses = [int(x.strip()) for x in inp[1].split(",") if x.strip() != "x"]

    next_pass = []
    for bus in buses:
        next_pass.append(next_timestamp(timestamp, bus))

    nest_ts = min(next_pass)

    s1 = buses[next_pass.index(nest_ts)] * (nest_ts - timestamp)
    return s1


def is_ok(x, buses):
    for i, b in enumerate(buses):
        if b == "x":
            continue

        if (x + i) % int(b) != 0:
            return False
    return True


def stage2(inp):

    buses = [x.strip() for x in inp[1].split(",")]
    ii = []
    ib = []

    for i, x in enumerate(buses):
        if x == "x":
            continue
        ii.append(i)
        ib.append(int(x))

    r = []
    for i, b in zip(ii, ib):
        r.append(b - i)

    p = 1
    for x in ib:
        p *= x

    mp = [math.floor(p / x) for x in ib]
    im = [pow(m, -1, b) for b, m in zip(ib, mp)]

    # un ptit coups de bezout car vive les nombre premier
    rr = 0
    for a, b, c in zip(r, mp, im):
        rr += a * b * c

    return rr % p


def solve(inp):
    s1, s2 = (0, 0)
    s1 = stage1(inp)
    s2 = stage2(inp)
    return s1, s2
