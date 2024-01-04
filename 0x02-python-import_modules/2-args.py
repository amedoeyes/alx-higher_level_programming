#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argc = len(argv)

    print(
        "{:d} argument{}{}".format(
            argc - 1,
            "s" if argc == 1 or argc > 2 else "",
            "." if argc == 1 else ":",
        )
    )

    if argc > 1:
        print(
            "\n".join(
                [
                    "{:d}: {}".format(i, arg)
                    for i, arg in enumerate(argv[1:], 1)
                ]
            )
        )
