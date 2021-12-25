import aoc.day_3.day_3 as day_3


def test_place_equal():
    assert day_3.place_equal(nyte=[1, 0, 1], bit=0, place=0) == False
    assert day_3.place_equal(nyte=[1, 0, 1], bit=1, place=0) == True
    assert day_3.place_equal(nyte=[1, 0, 1], bit=0, place=1) == True
    assert day_3.place_equal(nyte=[1, 0, 1], bit=1, place=1) == False
    assert day_3.place_equal(nyte=[1, 0, 1], bit=0, place=2) == False
    assert day_3.place_equal(nyte=[1, 0, 1], bit=1, place=2) == True


def test_col_round():
    assert day_3.col_round(0) == 0
    assert day_3.col_round(0.2) == 0
    assert day_3.col_round(0.5) == 1
    assert day_3.col_round(1.1) == 1
    assert day_3.col_round(1.5) == 2
    assert day_3.col_round(-0) == 0
    assert day_3.col_round(-0.2) == 0
    assert day_3.col_round(-0.5) == 0
    assert day_3.col_round(-1.1) == -1
    assert day_3.col_round(-1.5) == -1


def test_read_nytes():
    nytes = day_3.read_nytes("test.txt")

    assert len(nytes) > 3
    assert nytes[0] == [0, 0, 1, 0, 0]
    assert nytes[1] == [1, 1, 1, 1, 0]
    assert nytes[2] == [1, 0, 1, 1, 0]


def test_get_gamma_rate():
    nytes = day_3.read_nytes("test.txt")

    assert day_3.get_gamma_rate(nytes) == [1, 0, 1, 1, 0]


def test_get_epsilon_rate():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_epsilon_rate(nytes) == [0, 1, 0, 0, 1]


def test_get_average_ith_place():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_average_ith_place(nytes, 0) == 7 / 12
    assert day_3.get_average_ith_place(nytes, 1) == 5 / 12
    assert day_3.get_average_ith_place(nytes, 2) == 8 / 12
    assert day_3.get_average_ith_place(nytes, 3) == 7 / 12
    assert day_3.get_average_ith_place(nytes, 4) == 5 / 12


def test_to_decimal():
    nytes = [1, 1, 0, 1, 0]
    assert day_3.to_decimal(nytes) == 26


def test_all_same():
    assert day_3.all_same([[1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]) == False
    assert day_3.all_same([[1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]) == True


def test_get_most_common_ith():
    nytes = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]
    assert day_3.get_most_common_ith(nytes, 0) == 1
    assert day_3.get_most_common_ith(nytes, 1) == 0
    assert day_3.get_most_common_ith(nytes, 2) == 1
    assert day_3.get_most_common_ith([[0], [1]], 0) == 1


def test_get_oxygen_generator_rating():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_oxygen_generator_rating(nytes) == [1, 0, 1, 1, 1]


def test_get_c02_scrubber_rating():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_c02_scrubber_rating(nytes) == [0, 1, 0, 1, 0]


def test_get_part_one():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_part_one(nytes) == 198


def test_get_part_two():
    nytes = day_3.read_nytes("test.txt")
    assert day_3.get_part_two(nytes) == 230
