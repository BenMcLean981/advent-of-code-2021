from aoc.day_3.day_3 import get_average_ith_place, read_nytes, get_gamma_rate, get_epsilon_rate, get_average_ith_place


def test_read_nytes():
    nytes = read_nytes("test.txt")

    assert len(nytes) > 3
    assert nytes[0] == [0, 0, 1, 0, 0]
    assert nytes[1] == [1, 1, 1, 1, 0]
    assert nytes[2] == [1, 0, 1, 1, 0]


def test_get_gamma_rate():
    nytes = read_nytes("test.txt")

    assert get_gamma_rate(nytes) == [1, 0, 1, 1, 0]


def test_get_epsilon_rate():
    nytes = read_nytes("test.txt")
    assert get_epsilon_rate(nytes) == [0, 1, 0, 0, 1]


def test_get_average_ith_place():
    nytes = read_nytes("test.txt")
    assert get_average_ith_place(nytes, 0) == 7 / 12
    assert get_average_ith_place(nytes, 1) == 5 / 12
    assert get_average_ith_place(nytes, 2) == 8 / 12
    assert get_average_ith_place(nytes, 3) == 7 / 12
    assert get_average_ith_place(nytes, 4) == 5 / 12
