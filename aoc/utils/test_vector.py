from .vector import Vector


def test_vector_init():
    base = Vector()

    assert base.x == 0
    assert base.y == 0
    assert base.z == 0

    non_base = Vector(1, 2, 3)

    assert non_base.x == 1
    assert non_base.y == 2
    assert non_base.z == 3


def test_vector_add():
    v1 = Vector(1, 2, 3)
    v2 = Vector(3, 4, -5)

    v = v1 + v2
    assert v.x == 4
    assert v.y == 6
    assert v.z == -2
