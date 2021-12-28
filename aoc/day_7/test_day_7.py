import aoc.day_7.day_7 as day_7


def test_crab_swarm_make_from_file():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")
    assert swarm.position_counts == [
        1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1
    ]


def test_crab_swarm_get_available_positions():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")

    assert swarm.get_available_positions() == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    ]


def test_linear_fuel_cost():
    assert day_7.compute_linear_fuel_cost(16, 2) == 14
    assert day_7.compute_linear_fuel_cost(1, 2) == 1
    assert day_7.compute_linear_fuel_cost(2, 2) == 0
    assert day_7.compute_linear_fuel_cost(0, 2) == 2
    assert day_7.compute_linear_fuel_cost(4, 2) == 2
    assert day_7.compute_linear_fuel_cost(2, 2) == 0
    assert day_7.compute_linear_fuel_cost(7, 2) == 5
    assert day_7.compute_linear_fuel_cost(1, 2) == 1
    assert day_7.compute_linear_fuel_cost(2, 2) == 0
    assert day_7.compute_linear_fuel_cost(14, 2) == 12


def test_crab_swarm_compute_fuel_cost_linear():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")

    assert swarm.compute_fuel_cost_linear(1) == 41
    assert swarm.compute_fuel_cost_linear(2) == 37
    assert swarm.compute_fuel_cost_linear(3) == 39
    assert swarm.compute_fuel_cost_linear(10) == 71


def test_crab_swarm_find_best_position_linear():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")

    assert swarm.find_best_position_linear() == 2


def test_triangular_fuel_cost():
    assert day_7.compute_triangular_fuel_cost(16, 5) == 66
    assert day_7.compute_triangular_fuel_cost(1, 5) == 10
    assert day_7.compute_triangular_fuel_cost(2, 5) == 6
    assert day_7.compute_triangular_fuel_cost(0, 5) == 15
    assert day_7.compute_triangular_fuel_cost(4, 5) == 1
    assert day_7.compute_triangular_fuel_cost(2, 5) == 6
    assert day_7.compute_triangular_fuel_cost(7, 5) == 3
    assert day_7.compute_triangular_fuel_cost(1, 5) == 10
    assert day_7.compute_triangular_fuel_cost(2, 5) == 6
    assert day_7.compute_triangular_fuel_cost(14, 5) == 45


def test_crab_swarm_compute_fuel_cost_triangular():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")

    assert swarm.compute_fuel_cost_triangular(5) == 168
    assert swarm.compute_fuel_cost_triangular(2) == 206


def test_crab_swarm_find_best_position_triangular():
    swarm = day_7.CrabSwarm.make_from_file("test.txt")

    assert swarm.find_best_position_triangular() == 5


def test_get_part_one():
    assert day_7.get_part_one("test.txt") == 37


def test_get_part_two():
    assert day_7.get_part_two("test.txt") == 168
