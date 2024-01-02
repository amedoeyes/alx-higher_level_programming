#!/usr/bin/python3


def fizzbuzz():
    res = ""
    map = {
        3: "Fizz",
        5: "Buzz",
    }

    for i in range(1, 101):
        out = ""

        for k, v in map.items():
            if i % k == 0:
                out += v

        res += out if out else str(i)
        res += " "

    print(res, end="")
