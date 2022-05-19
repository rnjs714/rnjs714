from abc import *
import numpy as np
import copy


class GameState:
    def __init__(self, board_size, next_player):
        self.winner = None
        self.next_player = next_player
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)

    @abstractmethod
    def is_over(self):
        pass

    def legal_moves(self):
        moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i, j] == 0:
                    moves.append((i, j))
        return moves

    def apply_move(self, move):
        vrt_state = copy.deepcopy(self)
        row = move[0]
        col = move[1]
        vrt_state.board[row, col] = vrt_state.next_player.value
        vrt_state.next_player = vrt_state.next_player.other()
        return vrt_state

    def show_board(self):
        result = np.zeros(self.board.shape, dtype=str)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 1:
                    result[i, j] = '◯'
                elif self.board[i, j] == -1:
                    result[i, j] = '●'
                else:
                    result[i, j] = ' '
        print('__| ', end='')
        for i in range(self.board.shape[0]):
            print(chr(65 + i) + ' | ', end='')
        print()
        for i in range(self.board.shape[0]):
            print((i + 1), end=' ')
            for j in range(self.board.shape[1]):
                print('|{' + result[i, j] + '}', end='')
            print('|')
