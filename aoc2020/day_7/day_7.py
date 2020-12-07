import re

_LEAF_BAG = re.compile(r"^(.*) bags contain no other bags\.$")
_OTHER_BAG = re.compile(r"^(.*) bags contain .*$")
_CONTAINED_BAG = re.compile(r"^.* ([0-9]) (.*) bag[s]?.*$")


def contains_x(bags, x):
    for b in bags:
        if b[1] == x:
            return True
    return False


def does_it_contains(bags, bag_to_test, search):

    if contains_x(bag_to_test, search):
        return 1
    for x in bag_to_test:
        if does_it_contains(bags, bags[x[1]], search):
            return 1
    return 0


def number_of_bags_need(bags, bbn):
    if bags[bbn]:
        t = 0
        for bag in bags[bbn]:
            t += (bag[0] * number_of_bags_need(bags, bag[1])) + bag[0]
        return t
    return 0


def solve(inp):
    bags = {}
    for line in inp:
        if bob := _LEAF_BAG.match(line):
            bags[bob.groups()[0].strip()] = []
        else:
            elems = line.split(",")
            container = _OTHER_BAG.match(line).groups()[0].strip()
            cont = []
            for el in elems:
                mm = _CONTAINED_BAG.match(el)
                cont.append((int(mm.groups()[0].strip()), mm.groups()[1].strip()))
            bags[container] = cont

    c = 0
    for _, cont in bags.items():
        c += does_it_contains(bags, cont, "shiny gold")

    print(f"One: {c}")

    c = 0
    for x in bags["shiny gold"]:
        c += x[0] * number_of_bags_need(bags, x[1]) + x[0]
    print(f"Two: {c}")
