import itertools


def apply_masks1(value, mask):
    binary = list("{0:b}".format(value).zfill(36))
    for i, v in enumerate(mask):
        if v != "X":
            binary[i] = v

    return int("".join(binary), 2)


def calc_key(x):
    return x.split("[")[1][:-1]


def stage1(inp):
    memory = {}
    mask = str(["X"] * 36)
    for l in inp:
        l = l.strip()
        if l.startswith("mask"):
            mask = l.split()[2]
        else:
            memory[calc_key(l.split()[0])] = apply_masks1(int(l.split()[2]), mask)

    return sum(memory.values())


def stage2(inp):
    memory = {}
    mask = str(["X"] * 36)
    for l in inp:
        l = l.strip()
        if l.startswith("mask"):
            mask = l.split()[2]
        else:
            binary_addr = list("{0:b}".format(int(calc_key(l.split()[0]))).zfill(36))
            for i, m in enumerate(mask):
                if m == "1":
                    binary_addr[i] = "1"

            ix = [i for i, x in enumerate(mask) if x == "X"]
            possibilities = [["0", "1"]] * len(ix)
            for posi in itertools.product(*possibilities):
                for index, p in zip(ix, posi):
                    binary_addr[index] = p
                memory["".join(binary_addr)] = int(l.split()[2])

    return sum(memory.values())


def solve(inp):

    return stage1(inp), stage2(inp)
