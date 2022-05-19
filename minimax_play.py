from Minimax import MinimaxAgent
from DpAI import DpAgent
import Game as ttt

mm_agent = MinimaxAgent
dp_agent = DpAgent
state = ttt.GameState(3, ttt.Player.black)

while state.is_over() is False:
    if state.next_player == ttt.Player.white:
        move = mm_agent.select_move(state)
    else:
        move = dp_agent.select_move(state)
    state = state.apply_move(move)
    state.show_board()

print(state.winner)
