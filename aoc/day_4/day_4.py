from dataclasses import dataclass
import os
from typing import List


@dataclass
class BingoBoardCell:
    value: int
    is_marked: bool = False

    def mark_number(self, n: int) -> "BingoBoardCell":
        return BingoBoardCell(value=self.value, is_marked=(self.value == n or self.is_marked))

    def __str__(self) -> str:
        if self.is_marked:
            return "*"
        else:
            return str(self.value)

    def __repr__(self) -> str:
        return str(self)


class BingoBoard:
    grid: List[List[BingoBoardCell]]

    def __init__(self, grid: List[List[BingoBoardCell]]):
        self.grid = grid

    @staticmethod
    def make_from_int_list(int_list: List[int]):
        grid = [[BingoBoardCell(i) for i in row] for row in int_list]
        return BingoBoard(grid)

    def get_rows(self) -> List[List[BingoBoardCell]]:
        return self.grid

    def get_cols(self) -> List[List[BingoBoardCell]]:
        return [list(row) for row in zip(*self.grid)]

    def get_diagonals(self) -> List[List[BingoBoardCell]]:
        return [
            [self.grid[i][i] for i in range(len(self.grid))],
            [self.grid[i][-i - 1] for i in range(len(self.grid))]
        ]

    def get_all_lines(self) -> List[List[BingoBoardCell]]:
        return self.get_rows() + self.get_cols()  # diagonals do not count?

    def has_won(self) -> bool:
        lines = self.get_all_lines()
        return any(all(cell.is_marked for cell in line) for line in lines)

    def mark_number(self, n: int) -> None:
        self.grid = [[cell.mark_number(n) for cell in row]
                     for row in self.grid]

    def get_all_cells(self) -> List[BingoBoardCell]:
        return [cell for row in self.grid for cell in row]

    def compute_score(self, last_call: int) -> int:
        unmarked_numbers = [
            cell for cell in self.get_all_cells() if not cell.is_marked]
        return sum(cell.value for cell in unmarked_numbers) * last_call


class Game:
    boards: List[BingoBoard]
    call_order: List[int]
    next_call_idx = 0

    def __init__(self, boards: List[BingoBoard], call_order: List[int]):
        self.boards = boards
        self.call_order = call_order

    @staticmethod
    def make_from_file(filename: str = "input.txt") -> "Game":
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, filename), 'r') as f:
            lines = f.readlines()
            first_line = lines[0].split(",")
            call_order = [int(s) for s in first_line]

            boards = []
            for i in range(1, len(lines), 6):
                rows = []
                for j in range(5):
                    row_s = lines[i+j+1].strip().split(" ")
                    row_n = [s for s in row_s if s != ""]
                    rows.append([int(s) for s in row_n])
                boards.append(BingoBoard.make_from_int_list(rows))

            return Game(boards, call_order)

    def find_first_win(self) -> BingoBoard:
        for n in self.call_order:
            self.next_call_idx += 1
            for board in self.boards:
                board.mark_number(n)
                if board.has_won():
                    return board
        return None


def main(filename="input.txt") -> int:
    game = Game.make_from_file(filename)
    board = game.find_first_win()
    return board.compute_score(game.call_order[game.next_call_idx-1])


if __name__ == "__main__":
    print(main())
