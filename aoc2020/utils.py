def read_input(path):
    with open(path) as afile:
        return afile.readlines()


def make_int(alist):
    r = []
    for a in alist:
        r.append(int(a))
    return r
