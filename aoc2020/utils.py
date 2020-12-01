from logging import getLogger

LOGGER = getLogger(__file__)


def read_input(path):
    with open(path) as afile:
        return afile.readlines()
