import pytest

from game import TicTacToe


@pytest.fixture
def game():
    return TicTacToe()


def test_valid_move(game):
    assert game.is_valid_move(0) is True


def test_invalid_move_out_of_range(game):
    assert game.is_valid_move(10) is False
    assert game.is_valid_move(-1) is False


def test_invalid_move_not_integer(game):
    assert game.is_valid_move("1") is False
    assert game.is_valid_move(None) is False


def test_invalid_move_occupied_cell(game):
    game.board[0] = "X"
    assert game.is_valid_move(0) is False


def test_apply_move_success(game):
    result = game.apply_move(1)
    assert result is True
    assert game.board[1] == "X"


def test_apply_move_failure(game):
    game.board[2] = "X"
    result = game.apply_move(2)
    assert result is False


def test_switch_player(game):
    assert game.current_player == "X"
    game.switch_player()
    assert game.current_player == "O"
    game.switch_player()
    assert game.current_player == "X"


def test_winner_row(game):
    game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert game.check_winner() is True


def test_winner_column(game):
    game.board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
    game.current_player = "O"
    assert game.check_winner() is True


def test_winner_diagonal(game):
    game.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
    assert game.check_winner() is True


def test_no_winner(game):
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "O"]
    assert game.check_winner() is False


def test_draw(game):
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert game.is_draw() is True


def test_not_draw(game):
    game.board[0] = "X"
    assert game.is_draw() is False


def test_update_score_player1(game):
    game.current_player = "X"
    game.update_score()
    assert game.pl1_score == 1
    assert game.pl2_score == 0


def test_update_score_player2(game):
    game.current_player = "O"
    game.update_score()
    assert game.pl2_score == 1
    assert game.pl1_score == 0


def test_reset_board(game):
    game.board = ["X"] * 9
    game.current_player = "O"
    game.reset_board()

    assert game.board == [" "] * 9
    assert game.current_player == "X"
