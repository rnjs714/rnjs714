from Minimax import MinimaxAgent
from DpAI import DpAgent
import Game as Gs

mm_agent = MinimaxAgent
dp_agent = DpAgent
state = Gs.GameState(3, Gs.Player.black)

while state.is_over() is False:
    if state.next_player == Gs.Player.black:
        move = mm_agent.select_move(state)
    else:
        string = input("입력: ")
        x = int(string[0]) - 1
        y = ord(string[1]) - 65
        move = (x, y)
    state = state.apply_move(move)
    state.show_board()

print(state.winner)
