import argparse


def is_valid_float(n):
    n = float(n)
    if n < 0 or n > 2.5:
        raise argparse.ArgumentTypeError("a must be between 0 and 2.5")
    return n


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=is_valid_float, help="constant")
    args = parser.parse_args()
    return args
