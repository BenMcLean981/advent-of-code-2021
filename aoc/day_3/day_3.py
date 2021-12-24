from typing import List
import os


def read_nytes(filename="input.txt") -> List[bool]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        str_bits = [line.strip() for line in f.readlines()]
        return [[b == "1" for b in bits] for bits in str_bits]


def get_average_ith_place(nytes: List[List[bool]], i: int) -> float:
    return sum([nyte[i] for nyte in nytes]) / len(nytes)


def get_gamma_rate(nytes: List[List[bool]]) -> List[bool]:
    size = len(nytes[0])

    common = [round(get_average_ith_place(nytes, i)) == 1 for i in range(size)]

    return common


def get_epsilon_rate(nytes: List[List[bool]]) -> List[bool]:
    gamma_rate = get_gamma_rate(nytes)
    return [not g for g in gamma_rate]
