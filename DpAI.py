import random


class DpAgent:
    @classmethod
    def find_winning_move(cls, game_state, next_player):
        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)
            if next_state.is_over() is True and next_state.winner == next_player:
                return candidate_move
        return None

    @classmethod
    def eliminate_losing_moves(cls, game_state, next_player):
        opponent = next_player.other()
        possible_moves = []
        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)
            opponent_winning_move = cls.find_winning_move(next_state, opponent)
            if opponent_winning_move is None:
                possible_moves.append(candidate_move)
        return possible_moves

    @classmethod
    def find_two_step_win(cls, game_state, next_player):
        opponent = next_player.other()
        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)
            good_responses = cls.eliminate_losing_moves(next_state, opponent)
            if not good_responses:
                return candidate_move
        return None

    @classmethod
    def select_move(cls, game_state):
        next_player = game_state.next_player
        win = cls.find_winning_move(game_state, next_player)
        defend = cls.eliminate_losing_moves(game_state, next_player)
        two_step_win = cls.find_two_step_win(game_state, next_player)
        if win is not None:
            print('win')
            return win
        elif len(defend) == 0:
            print('random')
            possible_moves = game_state.legal_moves()
            return random.choice(possible_moves)
        elif two_step_win is not None and two_step_win in defend:
            print('tsw')
            return two_step_win
        else:
            print('elm')
            print(defend)
            return random.choice(defend)
