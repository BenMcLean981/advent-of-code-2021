import os
from typing import List
from dataclasses import dataclass


class Pos:
    horizontal: float
    depth: float
    aim: float

    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def __eq__(self, other: "Pos") -> bool:
        return (
            self.horizontal == other.horizontal and
            self.depth == other.depth and
            self.aim == other.aim
        )

    def __repr__(self) -> str:
        return (f"<{self.horizontal}, {self.depth}, {self.aim}>")

    def __str__(self) -> str:
        return (f"<{self.horizontal}, {self.depth}, {self.aim}>")

    def move_down(self, a: float) -> "Pos":
        return Pos(
            horizontal=self.horizontal,
            depth=self.depth,
            aim=self.aim + a
        )

    def move_up(self, a: float) -> "Pos":
        return Pos(
            horizontal=self.horizontal,
            depth=self.depth,
            aim=self.aim - a
        )

    def move_forward(self, d: float) -> "Pos":
        return Pos(
            horizontal=self.horizontal + d,
            depth=self.depth + self.aim * d,
            aim=self.aim
        )

    def handle_command(self, command: "Command") -> "Pos":
        if command.direction == "down":
            return self.move_down(command.dist)
        elif command.direction == "up":
            return self.move_up(command.dist)
        elif command.direction == "forward":
            return self.move_forward(command.dist)
        else:
            raise ValueError(f"Unknown direction: {command.direction}")


@dataclass
class Command:
    direction: str
    dist: float


def read_commands(filename="input.txt") -> List[Command]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        lines = [line.split(" ") for line in f.readlines()]
        return [Command(d, float(dist)) for [d, dist] in lines]


def combine_commands(l: List[Command]) -> Pos:
    p = Pos()
    for c in l:
        p = p.handle_command(c)
    return p


if __name__ == "__main__":
    commands = read_commands()
    pos = combine_commands(commands)

    print(f"Part 1 |x*depth|: {abs(pos.horizontal * pos.depth)}")
