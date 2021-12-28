from typing import List
import os


class Population:
    # represent a population as a list of timers to next birth

    timers: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    day: int = 0

    def __init__(self, timers: List[int]) -> None:
        self.timers = timers

    @staticmethod
    def make_from_file(filename="input.txt") -> "Population":
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, filename), 'r') as f:
            lines = f.readlines()
            timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

            timer_ls = [int(s) for s in lines[0].split(",") if s != '']
            for t in timer_ls:
                timers[t] += 1

            return Population(timers)

    def __str__(self) -> str:
        ages_str = ",".join([str(t) for t in self.timers])
        return f"After {self.day} days: {ages_str}"

    def __repr__(self) -> str:
        return str(self)

    def run_day(self) -> None:
        new_timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Handle birthing logic
        new_timers[8] = self.timers[0]
        new_timers[7] = self.timers[8]
        new_timers[6] = self.timers[7] + self.timers[0]

        # decrement the rest
        for n in range(6, 0, -1):  # does not include 0
            new_timers[n-1] = self.timers[n]

        self.timers = new_timers

    def simulate(self, days: int) -> None:
        for _ in range(days):
            self.run_day()

    def get_num_fish(self) -> int:
        return sum(self.timers)


def get_part_one(pop: Population, days=80) -> int:
    pop.simulate(days)
    return pop.get_num_fish()


def get_part_two(pop: Population, days=256) -> int:
    pop.simulate(days)
    return pop.get_num_fish()


if __name__ == "__main__":
    pop = Population.make_from_file()
    print(f"Part 1: {get_part_one(pop)}")
    pop = Population.make_from_file()
    print(f"Part 2: {get_part_two(pop)}")
