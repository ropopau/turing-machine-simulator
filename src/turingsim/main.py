import argparse

from .interface.Tui import Tui


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dir",
        nargs='+',
        required=True,
        help="Specify one or more directory where the turing machines files could be found"
    )
    args = parser.parse_args()
    tui: Tui = Tui (args.dir)
    tui.show_home()
            