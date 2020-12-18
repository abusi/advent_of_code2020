def execu(r, td, x):
    if td == "+":
        r += x
        return r
    if td == "*":
        r *= x
        return r


def solve_m1(expr: list):
    if len(expr) == 1:
        return expr[0]
    r = 0
    td = None
    fn = False
    p = []
    while expr:
        e = expr.pop(0)
        if e not in ["+", "*"]:
            p.append(e)
            if not expr:
                r = execu(r, td, int("".join(p)))
                return str(r)
        else:
            if not fn:
                fn = True
                r = int("".join(p))
                p = []
                td = e
            else:
                if not td:
                    td = e
                r = execu(r, td, int("".join(p)))
                p = []
                td = e

    return str(r)


def solve_m2(expr: list):
    new_math = []
    sub_math = []
    gotp = False
    while expr:
        x = expr.pop(0)
        if x == "*":
            if gotp:
                new_math.append(solve_m1(sub_math))
                gotp = False
            else:
                new_math.extend(sub_math)
            new_math.append("*")
            sub_math = []
        else:
            sub_math.append(x)
            if x == "+":
                gotp = True
        if not expr:
            if gotp:
                new_math.append(solve_m1(sub_math))
            else:
                new_math.extend(sub_math)

    return str(solve_m1(new_math))


def bad_math1(expr, solver):
    nb_p = 0
    p_s = -1
    r = 0
    new_math = []
    for i, v in enumerate(expr):
        if v == "(":
            nb_p += 1
            if p_s == -1:
                p_s = i
        if v == ")":
            nb_p -= 1
        if nb_p == 0 and p_s > -1:
            new_math.append(bad_math1(expr[p_s + 1 : i], solver))
            p_s = -1
        elif nb_p == 0:
            new_math.append(v)

    return solver(new_math)


def solve(inp):
    s1, s2 = (0, 0)

    for i in inp:
        s1 += int(bad_math1(i.strip().replace(" ", ""), solver=solve_m1))

    for i in inp:
        s2 += int(bad_math1(i.strip().replace(" ", ""), solver=solve_m2))

    return s1, s2
