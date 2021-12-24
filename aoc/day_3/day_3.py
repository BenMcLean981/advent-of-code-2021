from typing import List


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
