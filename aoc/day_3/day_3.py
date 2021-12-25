from typing import List
import os
from decimal import Decimal
import math


def col_round(x):  # round to nearest, tie breaker rounds up
    frac = x - math.floor(x)
    if frac < 0.5:
        return math.floor(x)
    return math.ceil(x)


def read_nytes(filename="input.txt") -> List[bool]:
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, filename), 'r') as f:
        str_bits = [line.strip() for line in f.readlines()]
        return [[b == "1" for b in bits] for bits in str_bits]


def get_average_ith_place(nytes: List[List[bool]], i: int) -> float:
    return sum([nyte[i] for nyte in nytes]) / len(nytes)


def get_gamma_rate(nytes: List[List[bool]]) -> List[bool]:
    size = len(nytes[0])

    common = [get_most_common_ith(nytes, i) for i in range(size)]

    return common


def get_epsilon_rate(nytes: List[List[bool]]) -> List[bool]:
    gamma_rate = get_gamma_rate(nytes)
    return [not g for g in gamma_rate]


def all_same(nytes: List[List[bool]]) -> bool:
    first = nytes[0]
    return all([nyte == first for nyte in nytes])


def get_most_common_ith(nytes: List[List[bool]], place) -> bool:
    return col_round(get_average_ith_place(nytes, place)) == 1


def place_equal(nyte: List[bool], bit: bool, place: int) -> bool:
    return nyte[place] == bit


def get_oxygen_generator_rating(nytes: List[List[bool]], place=0) -> int:
    if len(nytes) == 1 or all_same(nytes):
        return nytes[0]
    else:
        c = get_most_common_ith(nytes, place)
        m = [n for n in nytes if place_equal(nyte=n, bit=c, place=place)]
        return get_oxygen_generator_rating(m, place + 1)


def get_c02_scrubber_rating(nytes: List[List[bool]], place=0) -> int:
    if len(nytes) == 1 or all_same(nytes):
        return nytes[0]
    else:
        most_common = get_most_common_ith(nytes, place)
        matching = [n for n in nytes if not place_equal(n, most_common, place)]
        return get_c02_scrubber_rating(matching, place + 1)


def to_decimal(nytes: List[bool]) -> int:
    return sum([2**i * n for i, n in enumerate(nytes[::-1])])


def get_part_one(nytes: List[List[bool]]) -> int:
    gamma = to_decimal(get_gamma_rate(nytes))
    epsilon = to_decimal(get_epsilon_rate(nytes))
    return gamma * epsilon


def get_part_two(nytes: List[List[bool]]) -> int:
    oxygen = to_decimal(get_oxygen_generator_rating(nytes))
    c02 = to_decimal(get_c02_scrubber_rating(nytes))
    return oxygen * c02


if __name__ == "__main__":
    nytes = read_nytes()

    print(f"Part 1 gamma * epsilon: {get_part_one(nytes)}")
    print(f"Part 2 02 * C02: {get_part_two(nytes)}")
