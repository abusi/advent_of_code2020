import re

_R = re.compile(r"^([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)$")


def _parse_in(line):
    r = _R.search(line)
    grp = r.groups()
    return int(grp[0]), int(grp[1]), grp[2], grp[3]


def transform_input_list(inp):
    r = []
    for line in inp:
        r.append(_parse_in(line))
    return r


def stage_1(inp):
    nb_ok_pass = 0
    for min, max, let, pss in inp:
        nb_oc = len(re.findall(let, pss))
        if not (nb_oc < min or nb_oc > max):
            nb_ok_pass = nb_ok_pass + 1

    return nb_ok_pass


def stage_2(inp):
    nb_ok_pass = 0
    for p1, p2, let, pss in inp:
        if (pss[p1 - 1] == let and pss[p2 - 1] != let) or (
            pss[p1 - 1] != let and pss[p2 - 1] == let
        ):
            nb_ok_pass = nb_ok_pass + 1

    return nb_ok_pass


def solve(inp):
    inp = transform_input_list(inp)

    print(f"One: {stage_1(inp)}")
    print(f"Two: {stage_2(inp)}")
