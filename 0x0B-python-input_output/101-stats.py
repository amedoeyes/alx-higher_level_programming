#!/usr/bin/python3

"""stats"""

import sys


def print_stats(stats, file_size):
    """print_stats"""
    print(f"File size: {file_size}")
    for key, value in sorted(stats.items()):
        if value == 0:
            continue
        print(f"{key}: {value}")


if __name__ == "__main__":
    current_line = 0
    file_size = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {}

    try:
        for line in sys.stdin:
            if current_line == 10:
                print_stats(stats, file_size)
                current_line = 1
            else:
                current_line += 1

            line = line.split(" ")

            try:
                file_size += int(line[-1])
            except (ValueError, IndexError):
                pass

            try:
                status_code = line[-2]
                if status_code in valid_codes:
                    stats[status_code] = stats.get(status_code, 0) + 1
            except IndexError:
                pass

        print_stats(stats, file_size)

    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
