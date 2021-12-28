from typing import List
import os


def compute_triangular_fuel_cost(prev_pos: int, next_pos: int) -> int:
    dist = abs(next_pos - prev_pos)

    return dist * (dist+1) // 2


def compute_linear_fuel_cost(prev_pos: int, next_pos: int) -> int:
    return abs(next_pos - prev_pos)


class CrabSwarm:
    position_counts: List[int] = []

    def __init__(self, position_counts: List[int]):
        self.position_counts = position_counts

    @staticmethod
    def make_from_file(filename="input.txt") -> "CrabSwarm":
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, filename), 'r') as f:
            lines = f.readlines()
            positions = [int(s) for s in lines[0].split(",") if s != '']
            max_pos = max(positions)
            position_counts = [0] * (max_pos + 1)

            for p in positions:
                position_counts[p] += 1

            return CrabSwarm(position_counts)

    def compute_fuel_cost_linear(self, next_pos: int) -> int:
        # https://byjus.com/maths/triangular-numbers/

        def get_pos(ct, prev_pos, next_pos):
            return ct * compute_linear_fuel_cost(prev_pos=prev_pos, next_pos=next_pos)

        return sum([get_pos(c, prev_pos, next_pos) for prev_pos, c in enumerate(self.position_counts)])

    def compute_fuel_cost_triangular(self, next_pos: int) -> int:
        def get_pos(ct, prev_pos, next_pos):
            return ct * compute_triangular_fuel_cost(prev_pos=prev_pos, next_pos=next_pos)

        return sum([get_pos(c, prev_pos, next_pos) for prev_pos, c in enumerate(self.position_counts)])

    def get_available_positions(self) -> List[int]:
        return list(range(len(self.position_counts)))

    def find_best_position_linear(self) -> int:
        return min(self.get_available_positions(), key=lambda pos: self.compute_fuel_cost_linear(pos))

    def find_best_position_triangular(self) -> int:
        return min(self.get_available_positions(), key=lambda pos: self.compute_fuel_cost_triangular(pos))


def get_part_one(filename="input.txt") -> int:
    swarm = CrabSwarm.make_from_file(filename)
    return swarm.compute_fuel_cost_linear(swarm.find_best_position_linear())


def get_part_two(filename="input.txt") -> int:
    swarm = CrabSwarm.make_from_file(filename)
    return swarm.compute_fuel_cost_triangular(swarm.find_best_position_triangular())


def main():
    print(f"Part one: {get_part_one()}")
    print(f"Part two: {get_part_two()}")


if __name__ == "__main__":
    main()
