from typing import List
import os


class Nyte:
    bs: List[bool]

    def __init__(self, bs: List[bool]):
        self.bs = bs

    def __repr__(self) -> str:
        s = ""
        for b in self.bs:
            s += "1" if b else "0"
        return s

    def __str__(self) -> str:
        return self.__repr__()


def read_nytes(filename="input.txt") -> List[Nyte]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        str_bits = [line.strip() for line in f.readlines()]
        return [Nyte([b == "1" for b in bits]) for bits in str_bits]
