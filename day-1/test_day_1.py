from day_1 import Step, read_nums, find_step, map_steps, count_step_ups, sliding_window_sum


def test_read_nums():
    assert read_nums("test.txt") == [173, 175, -10]


def test_find_step():
    assert find_step(None, 5) == Step.NA
    assert find_step(0, 10) == Step.UP
    assert find_step(0, -10) == Step.DOWN
    assert find_step(10, 10) == Step.NONE


def test_map_steps():
    assert map_steps([173, 175, -10, -10]) == [Step.NA,
                                               Step.UP, Step.DOWN, Step.NONE]


def test_count_step_ups():
    assert count_step_ups(
        [Step.UP, Step.DOWN, Step.UP, Step.NONE, Step.NA]) == 2


def test_sliding_window_sum():
    assert sliding_window_sum([3, 4, 5, 6]) == [12, 15]
