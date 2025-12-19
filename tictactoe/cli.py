"""Tic-Tac-Toe text based UI"""

from helpers.clear_screen import clear_screen


def draw_board(game):
    """Draw Tic-Tac-Toe board"""
    clear_screen()
    print(f"Player1 Score: {game.pl1_score}\tPlayer2 Score: {game.pl2_score}\n")
    board = game.board
    print(f"\t {board[0]} | {board[1]} | {board[2]} ")
    print("\t-----------")
    print(f"\t {board[3]} | {board[4]} | {board[5]} ")
    print("\t-----------")
    print(f"\t {board[6]} | {board[7]} | {board[8]} ")


def wait_for_continue(msg=""):
    """Print message and ask user input to continue"""
    msg += "\nPress Enter to continue..."
    print(f"\n{msg}")
    input()


def get_player_move(game):
    """Ask move of the player"""
    move = input(
        f"\nPlayer {game.current_player}, Choose a position (0-8) or 'q' to quit: "
    )
    return move.strip()
