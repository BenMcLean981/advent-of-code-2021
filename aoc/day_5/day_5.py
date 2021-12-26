from dataclasses import dataclass
import os
from typing import List
import re


@dataclass
class Line:
    x1: int
    y1: int

    x2: int
    y2: int

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_diagonal(self) -> bool:
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        return dx == dy


class Grid:
    grid: List[List[int]]

    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid

    @staticmethod
    def make_size(x: int, y: int) -> "Grid":
        return Grid([[0 for _x in range(x + 1)] for _y in range(y + 1)])

    def add_horizontal(self, line: Line) -> None:
        start = min(line.x1, line.x2)
        end = max(line.x1, line.x2) + 1
        for x in range(start, end):
            self.increment(x=x, y=line.y1)

    def add_vertical(self, line: Line) -> None:
        start = min(line.y1, line.y2)
        end = max(line.y1, line.y2) + 1
        for y in range(start, end):
            self.increment(x=line.x1, y=y)

    def add_diagonal(self, line: Line) -> None:
        start_x = min(line.x1, line.x2)
        end_x = max(line.x1, line.x2) + 1

        m = (line.y2 - line.y1) / (line.x2 - line.x1)
        b = line.y1 - m * line.x1

        for x in range(start_x, end_x):
            y = int(m * (x) + b)
            self.increment(x=x, y=y)

    def add_line(self, line: Line, d: bool = False) -> None:
        if line.is_horizontal():
            self.add_horizontal(line)
        elif line.is_vertical():
            self.add_vertical(line)
        elif line.is_diagonal() and d:
            self.add_diagonal(line)

    def increment(self, x: int, y: int) -> None:
        self.grid[y][x] += 1

    def get_all_cells(self) -> List[int]:
        return [cell for row in self.grid for cell in row]

    def count_ns(self, n: int) -> int:
        return len([cell for cell in self.get_all_cells() if cell >= n])


def read_lines(filename: str) -> List[Line]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        lines = f.readlines()
        arrow_removed = [l.replace('->', ' ').replace("\n", '') for l in lines]
        line_ps = [[int(s) for s in re.split(',| ', l) if s != '']
                   for l in arrow_removed]

        return [Line(x1=i[0], y1=i[1], x2=i[2], y2=i[3]) for i in line_ps]


def get_max_x(lines: List[Line]) -> int:
    xs = [*[line.x1 for line in lines], *[line.x2 for line in lines]]
    return max(xs)


def get_max_y(lines: List[Line]) -> int:
    ys = [*[line.y1 for line in lines], *[line.y2 for line in lines]]
    return max(ys)


def part_one(lines: List[Line]) -> int:
    grid = Grid.make_size(x=get_max_x(lines), y=get_max_y(lines))

    for line in lines:
        grid.add_line(line)

    return grid.count_ns(2)


def part_two(lines: List[Line]) -> int:
    grid = Grid.make_size(x=get_max_x(lines), y=get_max_y(lines))

    for line in lines:
        grid.add_line(line, True)

    return grid.count_ns(2)


if __name__ == "__main__":
    lines = read_lines('input.txt')

    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
