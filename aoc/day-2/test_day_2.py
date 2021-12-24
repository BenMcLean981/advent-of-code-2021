from aoc.utils.vector import Vector
from day_2 import combine_vectors, to_vector


def test_to_vector_forward():
    v = to_vector("forward", 5)

    assert v.x == 5
    assert v.y == 0
    assert v.z == 0


def test_to_vector_up():
    v = to_vector("up", 5)

    assert v.x == 0
    assert v.y == 0
    assert v.z == 5


def test_to_vector_down():
    v = to_vector("down", 5)

    assert v.x == 0
    assert v.y == 0
    assert v.z == -5


def test_to_vector_none():
    v = to_vector("foo", 5)

    assert v == None


def test_combine_vectors():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(-2, -3, -4)

    v = combine_vectors([v1, v2, v3])

    assert v.x == 3
    assert v.y == 4
    assert v.z == 5
