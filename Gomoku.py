from BoardGame import GameState as Gs
from Player import Player
import numpy as np


class Gomoku(Gs):
    def is_over(self):
        self.board