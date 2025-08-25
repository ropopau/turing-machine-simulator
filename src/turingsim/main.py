import argparse

from .tui import TUI


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dir",
        nargs='+',
        required=True,
        help="Specify one or more directory where the turing machines files could be found"
    )
    args = parser.parse_args()
    tui: TUI = TUI(args.dir)
    tui.show_home()
            