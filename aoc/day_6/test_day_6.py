import aoc.day_6.day_6 as day_6


def test_population_init():
    population = day_6.Population([0, 1, 1, 2, 1, 0, 0, 0, 0])
    assert population.timers == [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_population_make_from_file():
    population = day_6.Population.make_from_file("test.txt")
    assert population.timers == [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_population_str():
    population = day_6.Population.make_from_file("test.txt")
    assert str(population) == "After 0 days: 0,1,1,2,1,0,0,0,0"


def test_get_part_one():
    pop = day_6.Population.make_from_file("test.txt")
    assert day_6.get_part_one(pop, days=18) == 26


def test_get_part_two():
    pop = day_6.Population.make_from_file("test.txt")
    assert day_6.get_part_two(pop, days=256) == 26984457539
