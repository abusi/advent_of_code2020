from copy import copy


def _execute(inp):
    acc = 0
    try:
        index = 0
        already_done = []
        while True:
            if "nop" in inp[index]:
                already_done.append(index)
                index += 1

            elif "acc" in inp[index]:
                already_done.append(index)
                acc += int(inp[index].split()[1].strip())
                index += 1

            elif "jmp" in inp[index]:
                already_done.append(index)
                index += int(inp[index].split()[1].strip())

            if index in already_done:
                return acc, -1
    except:
        return acc, 0


def solve(inp):
    s1, _ = _execute(inp)
    print(f"One: {s1}")
    lim = 0
    r = -1
    s2 = 0
    while r == -1:
        modified = copy(inp)
        for index, line in enumerate(modified):
            if index < lim:
                continue
            if line.startswith("nop"):
                lim = index + 1
                modified[index] = f"jmp {line.split()[1].strip()}"
                s2, r = _execute(modified)
                break
            elif line.startswith("jmp"):
                lim = index + 1
                modified[index] = f"nop {line.split()[1].strip()}"
                s2, r = _execute(modified)
                break

    print(f"Two: {s2}")
