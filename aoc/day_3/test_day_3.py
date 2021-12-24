from aoc.day_3.day_3 import Nyte


def test_nyte_create():
    q = Nyte([True, True, False, True, False])

    assert repr(q) == "11010"
    assert str(q) == "11010"
