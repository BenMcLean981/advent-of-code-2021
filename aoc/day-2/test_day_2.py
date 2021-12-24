from day_2 import to_vector


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
