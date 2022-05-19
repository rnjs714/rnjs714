from BoardGame import GameState as Gs
import enum
import numpy as np


class Player(enum.Enum):
    black = 1
    white = -1

    def other(self):
        return Player.black if self == Player.white else Player.white


class TicTacToe(Gs):
    def is_over(self):
        line_sum_array = np.concatenate((self.board.sum(axis=0), self.board.sum(axis=1)), axis=0)
        temp_sum1 = 0
        temp_sum2 = 0
        for line_sum in range(self.board_size):
            temp_sum1 += self.board[line_sum, line_sum]
            temp_sum2 += self.board[line_sum, self.board_size - 1 - line_sum]
        line_sum_array = np.append(line_sum_array, temp_sum1)
        line_sum_array = np.append(line_sum_array, temp_sum2)
        for line_sum in line_sum_array:
            if line_sum * line_sum == self.board_size * self.board_size:
                if line_sum > 0:
                    self.winner = Player.black
                else:
                    self.winner = Player.white
                return True
        if np.prod(self.board, axis=None) != 0:
            return True
        return False


class Gomoku(Gs):
    def is_over(self):

