from aoc.day_3.day_3 import Nyte, read_nytes


def test_nyte_create():
    q = Nyte([True, True, False, True, False])

    assert repr(q) == "11010"
    assert str(q) == "11010"


def test_read_nytes():
    nytes = read_nytes("test.txt")

    assert len(nytes) == 3
    assert nytes[0].bs == [True, False, True, True, True]
    assert nytes[1].bs == [True, True, False, True, True]
    assert nytes[2].bs == [True, True, True, False, False]
