from aoc.day_2.day_2 import Pos, Command, combine_commands


def test_pos():
    p = Pos(horizontal=0, depth=0, aim=0)
    assert repr(p) == "<0, 0, 0>"
    assert str(p) == "<0, 0, 0>"


def test_pos_move_down():
    p = Pos(horizontal=5, depth=6, aim=0)
    p = p.move_down(1)
    assert p == Pos(horizontal=5, depth=6, aim=1)


def test_pos_move_up():
    p = Pos(horizontal=5, depth=6, aim=0)
    p = p.move_up(1)
    assert p == Pos(horizontal=5, depth=6, aim=-1)
