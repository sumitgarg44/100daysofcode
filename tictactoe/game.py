"""Tic-Tac-Toe Game Logic"""


class TicTacToe:
    """Core Tic-Tac-Toe game logic, independent of UI"""

    def __init__(self, player_symbols=("X", "O")):
        self.player1 = player_symbols[0]
        self.player2 = player_symbols[1]
        self.current_player = self.player1
        self.board = [" "] * 9
        self.pl1_score = 0
        self.pl2_score = 0
        self.winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

    def reset_board(self):
        """Reset board"""
        self.board = [" "] * 9
        self.current_player = self.player1

    def switch_player(self):
        """Switch the player turn"""
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def is_valid_move(self, move):
        """Validates player move"""
        if not isinstance(move, int):
            return False
        if move < 0 or move > 8:
            return False
        if self.board[move] != " ":
            return False

        return True

    def apply_move(self, move):
        """Apply move if valid"""
        if self.is_valid_move(move):
            self.board[move] = self.current_player
            return True
        return False

    def check_winner(self):
        """Checks for winner"""
        for combo in self.winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def is_draw(self):
        """Checks for draw"""
        return " " not in self.board

    def update_score(self):
        """Update players score"""
        if self.current_player == self.player1:
            self.pl1_score += 1
        else:
            self.pl2_score += 1
