import aoc.day_5.day_5 as day_5


def test_read_lines():
    lines = day_5.read_lines('test.txt')

    assert lines == [
        day_5.Line(0, 9, 5, 9),
        day_5.Line(8, 0, 0, 8),
        day_5.Line(9, 4, 3, 4),
        day_5.Line(2, 2, 2, 1),
        day_5.Line(7, 0, 7, 4),
        day_5.Line(6, 4, 2, 0),
        day_5.Line(0, 9, 2, 9),
        day_5.Line(3, 4, 1, 4),
        day_5.Line(0, 0, 8, 8),
        day_5.Line(5, 5, 8, 2),
    ]


def test_line_is_horizontal():
    horiz = day_5.Line(0, 0, 5, 0)
    assert horiz.is_horizontal() == True

    vert = day_5.Line(0, 0, 0, 5)
    assert vert.is_horizontal() == False

    diag = day_5.Line(0, 0, 5, 5)
    assert diag.is_horizontal() == False

    none = day_5.Line(0, 0, 4, 5)
    assert none.is_horizontal() == False


def test_line_is_vertical():
    horiz = day_5.Line(0, 0, 5, 0)
    assert horiz.is_vertical() == False

    vert = day_5.Line(0, 0, 0, 5)
    assert vert.is_vertical() == True

    diag = day_5.Line(0, 0, 5, 5)
    assert diag.is_vertical() == False

    none = day_5.Line(0, 0, 4, 5)
    assert none.is_vertical() == False


def test_line_is_diagonal():
    horiz = day_5.Line(0, 0, 5, 0)
    assert horiz.is_diagonal() == False

    vert = day_5.Line(0, 0, 0, 5)
    assert vert.is_diagonal() == False

    diag = day_5.Line(0, 0, 5, 5)
    assert diag.is_diagonal() == True

    none = day_5.Line(0, 0, 4, 5)
    assert none.is_diagonal() == False


def test_make_grid():
    grid = day_5.Grid.make_size(2, 1)
    assert grid.grid == [
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_grid_increment():
    grid = day_5.Grid.make_size(2, 1)
    grid.increment(x=2, y=1)
    assert grid.grid == [
        [0, 0, 0],
        [0, 0, 1]
    ]


def test_grid_add_horizontal():
    grid = day_5.Grid.make_size(3, 2)
    grid.add_horizontal(day_5.Line(x1=1, y1=2, x2=2, y2=2))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    grid.add_horizontal(day_5.Line(x1=2, y1=2, x2=1, y2=2))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 2, 0],
    ]


def test_grid_add_vertical():
    grid = day_5.Grid.make_size(3, 2)
    grid.add_vertical(day_5.Line(x1=2, y1=1, x2=2, y2=2))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
    ]
    grid.add_vertical(day_5.Line(x1=2, y1=2, x2=2, y2=1))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 2, 0],
    ]


def test_grid_add_diagonal():
    grid = day_5.Grid.make_size(3, 2)
    grid.add_diagonal(day_5.Line(x1=1, y1=1, x2=2, y2=2))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]
    grid.add_diagonal(day_5.Line(x1=2, y1=2, x2=1, y2=1))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 2, 0],
    ]
    grid.add_diagonal(day_5.Line(x1=2, y1=1, x2=1, y2=2))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 1, 2, 0],
    ]
    grid.add_diagonal(day_5.Line(x1=1, y1=2, x2=2, y2=1))
    assert grid.grid == [
        [0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 2, 2, 0],
    ]


def test_get_max_x():
    lines = day_5.read_lines('test.txt')
    assert day_5.get_max_x(lines) == 9


def test_get_max_y():
    lines = day_5.read_lines('test.txt')
    assert day_5.get_max_y(lines) == 9


def test_part_one():
    lines = day_5.read_lines('test.txt')
    assert day_5.part_one(lines) == 5


def test_part_two():
    lines = day_5.read_lines('test.txt')
    assert day_5.part_two(lines) == 12
