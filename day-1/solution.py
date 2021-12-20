from typing import List


def read_nums(filename="input.txt") -> List[int]:
    with open(filename, 'r') as f:
        return [int(line) for line in f.readlines()]

def test_read_nums():
    assert read_nums("test.txt") == [173, 175, -10]