import sys

import lina


def main():
    major = sys.version_info[0]
    minor = sys.version_info[1]

    if major != 3 or minor < 6:
        print(f'Service requires Python 3.6+\nYou are using Python {major}.{minor}, which is not supported.')
        sys.exit(1)

    lina.main()


if __name__ == '__main__':
    main()
