from typing import DefaultDict


def stage1(spoken):
    for i in range(len(spoken) + 1, 2020 + 1):
        if spoken[-1] not in spoken[:-1]:
            spoken.append(0)
        else:
            lspoken = len(spoken[:-1]) - 1 - spoken[:-1][::-1].index(spoken[-1]) + 1
            spoken.append(i - 1 - lspoken)

    return spoken[-1]


def when_was_i_seen_before(indexes, x):
    try:
        return indexes[x][-2]
    except:
        return indexes[x][0]


def add_to_indexes(index, x, i):
    index[x].append(i)


def stage2(spoken):
    index = DefaultDict(lambda: [])
    for i, x in enumerate(spoken):
        index[x] = [i]

    for i in range(len(spoken), 30000000):
        if (lspoken := when_was_i_seen_before(index, spoken[-1])) == i - 1:
            spoken.append(0)
            index[0].append(i)
        else:
            spoken.append(i - 1 - lspoken)
            add_to_indexes(index, i - 1 - lspoken, i)

    return spoken[-1]


def solve(inp):
    spoken1 = [int(x.strip()) for x in inp[0].split(",")]
    spoken2 = list(spoken1)
    s1, s2 = (stage1(spoken1), stage2(spoken2))

    return s1, s2
