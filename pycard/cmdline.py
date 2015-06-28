import argparse
import fileinput
from itertools import chain
from pathlib import Path

from .pycard import PyCard


__all__ = ["add_args", "process"]


def add_args(parser):
    subparsers = parser.add_subparsers(
        dest="command", metavar="COMMAND", help="Command to execute")
    subparser_show = subparsers.add_parser(
        'show', help="Show the content of files given as arguments.")
    subparser_show.add_argument("filenames", metavar="filename",nargs="+",
                                help="Files containing vcards.")


def process(parser):
    args = parser.parse_args()
    if args.command == "show":
        show(args)


def show(args):
    filenames = fileinput.input(args.filenames)
    for pyCard in PyCard.from_stream(filenames):
        print(pyCard.format())
