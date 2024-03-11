from state import NQueens, CellOptions
import math


class Operator:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def preconditon_fulfilled(self, n_queens):
        # zh type
        return n_queens.table[self.row][self.col] == CellOptions.FREE

    def use(self, n_queens):
        n = n_queens.n

        result = NQueens(n=n)

        for r in range(n):
            for c in range(n):
                result.table[r][c] = n_queens.table[r][c]

        result.table[self.row][self.col] = CellOptions.QUEEN

        # change row and columns of queens to UNDER_ATTACK (ezeket a helyeket uti a kiralyno a soraban vagy oszlopban)
        for c in range(n):
            if result.table[self.row][c] == CellOptions.FREE:
                result.table[self.row][c] = CellOptions.UNDER_ATTACK

        for r in range(n):
            if result.table[r][self.col] == CellOptions.FREE:
                result.table[r][self.col] = CellOptions.UNDER_ATTACK

        # diagonals

        # up and left diagonal
        r = self.row - 1
        c = self.col - 1

        while r >= 0 and c >= 0:
            if result.table[r][c] == CellOptions.FREE:
                result.table[r][c] = CellOptions.UNDER_ATTACK

            r -= 1
            c -= 1

        # up and right diagonal
        r = self.row - 1
        c = self.col + 1

        while r >= 0 and c < n:
            if result.table[r][c] == CellOptions.FREE:
                result.table[r][c] = CellOptions.UNDER_ATTACK

            r -= 1
            c += 1

        # down and left diagonal
        r = self.row + 1
        c = self.col - 1

        while r < n and c >= 0:
            if result.table[r][c] == CellOptions.FREE:
                result.table[r][c] = CellOptions.UNDER_ATTACK

            r += 1
            c -= 1

        # down and right diagonal
        r = self.row + 1
        c = self.col + 1

        while r < n and c < n:
            if result.table[r][c] == CellOptions.FREE:
                result.table[r][c] = CellOptions.UNDER_ATTACK

            r += 1
            c += 1

        return result

    # nem zh type to string
    def __str__(self):
        return f"Operator [Row={self.row}, Col={self.col}]"


if __name__ == "__main__":
    print("")

    n_queens = NQueens(n=8)

    print("State", n_queens)

    o = Operator(row=4, col=4)

    print("Operator", o)

    print("Pre-condition", o.preconditon_fulfilled(n_queens))

    n_queens = o.use(n_queens)

    print("State after:", n_queens)