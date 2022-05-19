import enum


class Player(enum.Enum):
    black = 1
    white = -1

    def other(self):
        return Player.black if self == Player.white else Player.white
