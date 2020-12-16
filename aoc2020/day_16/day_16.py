def _get_limits(line):
    limits = []
    line = line.split(":")[1]
    r = line.split("or")
    limits.append(
        {"min": int(r[0].split("-")[0].strip()), "max": int(r[0].split("-")[1].strip())}
    )
    limits.append(
        {"min": int(r[1].split("-")[0].strip()), "max": int(r[1].split("-")[1].strip())}
    )
    return limits


def parse_rule(inp):
    rules = {}
    for line in inp:
        if line == "\n":
            break
        rules[line.split(":")[0]] = {"limits": _get_limits(line), "col": []}

    return rules


def parse_my_ticket(inp):
    n = 0
    for line in inp:
        if n == 1:
            return [int(x.strip()) for x in line.split(",")]
        if "your ticket:" in line:
            n = 1


def parse_other_ticket(inp):
    n = 0
    ret = []
    for line in inp:
        if line == "\n":
            continue
        if n == 1:
            ret.append([int(x.strip()) for x in line.split(",")])
        if "nearby tickets:" in line:
            n = 1

    return ret


def _match_rules(rule, x):
    return (x >= rule["limits"][0]["min"] and x <= rule["limits"][0]["max"]) or (
        x >= rule["limits"][1]["min"] and x <= rule["limits"][1]["max"]
    )


def _validate_rules(rule, xs):
    for x in xs:
        if not _match_rules(rule, x):
            return False
    return True


def solve(inp):
    s1, s2 = (0, 0)
    rules = parse_rule(inp)
    my_ticket = parse_my_ticket(inp)
    other_ticket = parse_other_ticket(inp)

    # S1
    valid_ticket = []
    for ticket in other_ticket:
        tv = True
        for x in ticket:
            m = False
            for rule in rules.values():
                if _match_rules(rule, x):
                    m = True
            if not m:
                s1 += x
                tv = False
        if tv:
            valid_ticket.append(ticket)

    # S2

    for rule in rules:
        for c in range(0, len(valid_ticket[0])):
            col = []
            for y in range(0, len(valid_ticket)):
                col.append(valid_ticket[y][c])

            if _validate_rules(rules[rule], col):
                rules[rule]["col"].append(c)

    ct = True
    associated_column = []
    while ct:
        ct = False

        for _, r in rules.items():
            if len(r["col"]) == 1:
                associated_column.append(r["col"][0])
            else:
                ct = True
                nc = []
                for c in r["col"]:
                    if c not in associated_column:
                        nc.append(c)
                r["col"] = nc

    s2 = 1
    for k, v in rules.items():
        if k.startswith("departure"):
            s2 *= my_ticket[v["col"][0]]

    return s1, s2
