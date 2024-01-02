#!/usr/bin/python3
print(
    "{}".format(
        "".join(chr(c) if c % 2 == 0 else chr(c - 32) for c in range(97, 123))[
            ::-1
        ]
    ),
    end="",
)
