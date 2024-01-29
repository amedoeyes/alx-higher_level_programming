#!/usr/bin/python3

"""Python script that solves the N queens problem"""

import sys


def is_safe(board, row, col):
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def _solve_n_queens(board, row, N):
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            _solve_n_queens(board, row + 1, N)


def solve_n_queens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    _solve_n_queens(board, 0, N)


def print_solution(board):
    N = len(board)
    sol = []
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                sol.append([row, col])
    print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
