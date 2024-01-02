#!/usr/bin/python3
print(
    "\n".join(
        "{:d} = 0x{:x}".format(number, number) for number in range(0, 99)
    )
)
