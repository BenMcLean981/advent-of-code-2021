import os
from typing import List, Union
from enum import Enum


class Step(Enum):
    UP = 1
    DOWN = 2
    NONE = 3
    NA = 4


def read_nums(filename="input.txt") -> List[int]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        return [int(line) for line in f.readlines()]


def find_step(prev: Union[None, int], curr: int) -> Step:
    if prev == None:
        return Step.NA

    elif (curr < prev):
        return Step.DOWN
    elif (curr > prev):
        return Step.UP
    else:
        return Step.NONE


def sliding_window_sum(nums: List[int], size=3) -> List[int]:
    return [sum(nums[i:i+size]) for i in range(len(nums) - size + 1)]


def map_steps(nums: List[int]) -> List[Step]:
    l = [None, *nums]

    return [find_step(p, c) for p, c in zip(l, l[1:])]


def count_step_ups(steps: List[Step]) -> int:
    return sum([1 for step in steps if step == Step.UP])


if __name__ == "__main__":
    depths = read_nums()
    steps = map_steps(depths)
    step_ups = count_step_ups(steps)

    print('Solution to part 1 is: {}'.format(step_ups))
