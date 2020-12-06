def solve(inp):
    uniq = set()
    al = set()
    s1 = 0
    s2 = 0
    f = 1
    for line in inp:
        if line == "\n":
            s1 += len(uniq)
            s2 += len(al)
            uniq = set()
            al = set()
            f = 1
            continue
        [uniq.add(x) for x in line[:-1]]

        if f:
            al = set(line[:-1])
            f = 0
        else:
            al = al.intersection(set(line[:-1]))

    s1 += len(uniq)
    s2 += len(al)
    print(f"One: {s1}")
    print(f"Two: {s2}")
