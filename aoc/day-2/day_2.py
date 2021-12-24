from aoc.utils.vector import Vector
import os
from typing import List


def to_vector(direction: str, dist: float) -> Vector:
    if direction == "forward":
        return Vector(dist, 0, 0)
    elif direction == "down":
        return Vector(0, 0, -dist)
    elif direction == "up":
        return Vector(0, 0, dist)


def read_commands(filename="input.txt") -> List[Vector]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        lines = [line.split(" ") for line in f.readlines()]
        return [to_vector(d, float(dist)) for [d, dist] in lines]
