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


def test_pos_apply_command_down():
    p = Pos(horizontal=5, depth=6, aim=3)
    c = Command(direction="down", dist=1)
    h = p.handle_command(c)
    assert h == p.move_down(1)


def test_pos_apply_command_up():
    p = Pos(horizontal=5, depth=6, aim=3)
    c = Command(direction="up", dist=1)
    h = p.handle_command(c)
    assert h == p.move_up(1)


def test_pos_apply_command_forward():
    p = Pos(horizontal=5, depth=6, aim=3)
    c = Command(direction="forward", dist=1)
    h = p.handle_command(c)
    assert h == p.move_forward(1)


def test_combine_commands():
    c1 = Command(direction="down", dist=2)
    c2 = Command(direction="up", dist=1)
    c3 = Command(direction="forward", dist=3)
    assert combine_commands([c1, c2, c3]) == Pos(horizontal=3, depth=3, aim=1)
