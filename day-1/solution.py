import os
from typing import List, Union
from enum import Enum


DEFAULT_FILENAME = "input.txt"


class Step(Enum):
    UP = 1
    DOWN = 2
    NONE = 3
    NA = 4


def read_nums(filename=DEFAULT_FILENAME) -> List[int]:
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


def get_step_ups(window_size=1, filename=DEFAULT_FILENAME) -> int:
    depths = read_nums(filename)
    windowed = sliding_window_sum(depths, window_size)
    steps = map_steps(windowed)
    return count_step_ups(steps)


if __name__ == "__main__":
    print('Solution to part 1 is: {}'.format(get_step_ups()))
    print('Solution to part 2 is: {}'.format(get_step_ups(3)))
