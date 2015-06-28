import argparse

from .cmdline import add_args, process


def main():
    parser = argparse.ArgumentParser()
    add_args(parser)
    process(parser)


if __name__ == "__main__":
    main()
