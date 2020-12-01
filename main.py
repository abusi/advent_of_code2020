import argparse
import importlib

from aoc2020.utils import read_input

if __name__ == "__main__":
    parser = argparse.ArgumentParser("aOc2020")
    parser.add_argument("--day", dest="day", required=True)

    args = parser.parse_args()

    module = importlib.import_module(f"aoc2020.day_{args.day}.day_{args.day}")
    module.solve(read_input(f"inputs/{args.day}.txt"))
