import argparse
import importlib
from datetime import datetime as dt

from aoc2020.utils import read_input


def _run_day(x):
    return importlib.import_module(f"aoc2020.day_{x}.day_{x}").solve(
        read_input(f"inputs/{x}.txt")
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser("aOc2020")
    parser.add_argument("--day", dest="day", required=True)

    args = parser.parse_args()

    if args.day != "all":
        print(_run_day(args.day))
    else:
        for i in range(1, dt.today().day + 1):
            print(f"day {i}")
            print(_run_day(i))
            print("")
