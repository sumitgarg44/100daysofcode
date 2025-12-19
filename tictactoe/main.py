"""Tic-Tac-Toe Game runner"""

import cli
from game import TicTacToe


def main():
    """Main loop of game"""
    game = TicTacToe()

    while True:
        cli.draw_board(game)
        move = cli.get_player_move(game)

        if move.lower() == "q":
            print("\nThanks for playing! Goodbye!")
            break

        if not move.isdigit():
            cli.wait_for_continue("Invalid input. Enter a number between 0-8.")
            continue

        move = int(move)

        if not game.is_valid_move(move):
            cli.wait_for_continue(
                "Invalid move. Cell already occupied or out of range."
            )
            continue

        game.apply_move(move)

        if game.check_winner():
            game.update_score()
            cli.draw_board(game)
            cli.wait_for_continue(f"\nPlayer {game.current_player} wins!")
            if not play_again(game):
                break
            continue

        if game.is_draw():
            cli.draw_board(game)
            cli.wait_for_continue("\nIt's a Draw!")
            if not play_again(game):
                break
            continue

        game.switch_player()


def play_again(game):
    """Prompt user to play again or not"""
    response = input("\nPlay again? (Y/N): ").strip().lower()
    if response.startswith("y"):
        game.reset_board()
        return True
    return False


if __name__ == "__main__":
    main()
