import aoc.day_4.day_4 as day_4


def test_bingo_board_cell():
    assert day_4.BingoBoardCell(1).value == 1
    assert day_4.BingoBoardCell(1).is_marked == False


def test_bingo_board_init():
    bingo_board = day_4.BingoBoard([[day_4.BingoBoardCell(1)]])
    assert bingo_board.grid[0][0].value == 1


def test_bingo_board_make_from_int_list():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1]])
    assert bingo_board.grid[0][0].value == 1


def test_bingo_board_get_rows():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    assert bingo_board.get_rows() == [
        [day_4.BingoBoardCell(1), day_4.BingoBoardCell(2)],
        [day_4.BingoBoardCell(3), day_4.BingoBoardCell(4)]
    ]


def test_bingo_board_get_cols():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    assert bingo_board.get_cols() == [
        [day_4.BingoBoardCell(1), day_4.BingoBoardCell(3)],
        [day_4.BingoBoardCell(2), day_4.BingoBoardCell(4)]
    ]


def test_bingo_board_get_diagonals():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    assert bingo_board.get_diagonals() == [
        [day_4.BingoBoardCell(1), day_4.BingoBoardCell(4)],
        [day_4.BingoBoardCell(2), day_4.BingoBoardCell(3)]
    ]


def test_bingo_board_get_lines():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    assert bingo_board.get_all_lines() == bingo_board.get_rows() + \
        bingo_board.get_cols() + bingo_board.get_diagonals()


def test_bingo_board_has_won():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    assert bingo_board.has_won() == False
    bingo_board.grid[0][0].is_marked = True
    assert bingo_board.has_won() == False
    bingo_board.grid[0][1].is_marked = True
    assert bingo_board.has_won() == True


def test_bingo_board_mark_number():
    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    bingo_board.mark_number(1)
    assert bingo_board.grid[0][0].is_marked == True
    assert bingo_board.grid[0][1].is_marked == False
    assert bingo_board.grid[1][0].is_marked == False
    assert bingo_board.grid[1][1].is_marked == False

    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    bingo_board.mark_number(4)
    assert bingo_board.grid[0][0].is_marked == False
    assert bingo_board.grid[0][1].is_marked == False
    assert bingo_board.grid[1][0].is_marked == False
    assert bingo_board.grid[1][1].is_marked == True

    bingo_board = day_4.BingoBoard.make_from_int_list([[1, 2], [3, 4]])
    bingo_board.mark_number(5)
    assert bingo_board.grid[0][0].is_marked == False
    assert bingo_board.grid[0][1].is_marked == False
    assert bingo_board.grid[1][0].is_marked == False
    assert bingo_board.grid[1][1].is_marked == False


def test_game_make_from_file():
    game = day_4.Game.make_from_file('test.txt')

    assert game.call_order == [
        7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21,
        24, 10, 16, 13, 6, 15, 25, 12, 22, 18,
        20, 8, 19, 3, 26, 1
    ]

    assert len(game.boards) == 3

    first_board_cells = [cell.value for cell in game.boards[0].get_all_cells()]
    assert first_board_cells == [
        22, 13, 17, 11, 0, 8, 2, 23, 4,
        24, 21, 9, 14, 16, 7, 6, 10, 3,
        18, 5, 1, 12, 20, 15, 19
    ]
