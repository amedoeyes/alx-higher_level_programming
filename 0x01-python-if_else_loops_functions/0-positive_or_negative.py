#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(
    "{:d} is {}".format(
        number,
        "positive" if number > 0 else "zero" if number == 0 else "negative",
    )
)
