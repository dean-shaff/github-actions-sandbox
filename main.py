import argparse

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sample Program with command line arguments")
    parser.add_argument("-i", "--ints", type=int, nargs="+", help="Numbers to sum")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    return parser


def main():
    parser = create_parser()
    parsed = parser.parse_args()



if __name__ == "__main__":
    main()
