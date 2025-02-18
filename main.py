from Chessnut import Game
import random

class ChessBot:
    def __init__(self):
        self.move_count = 0

    def evaluate_position(self, game):
        """Simple evaluation: prioritize checkmate, material gains, and king activity."""
        piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0}
        fen = game.get_fen().split(' ')[0]
        value = sum(piece_values.get(p.upper(), 0) * (1 if p.isupper() else -1) for p in fen)
        return value

    def find_best_move(self, game):
        """Selects the best move using simple evaluation."""
        moves = list(game.get_moves())
        if not moves:
            return None  # No legal moves

        # Prioritize checkmate
        for move in moves:
            game_copy = Game(game.get_fen())
            game_copy.apply_move(move)
            if game_copy.status == "checkmate":
                return move

        # Pick the move with the best material gain
        best_move = max(moves, key=lambda move: self.evaluate_move(game, move))
        return best_move

    def evaluate_move(self, game, move):
        """Evaluates a move based on material gain."""
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        return self.evaluate_position(game_copy)

    def chess_bot(self, obs):
        """Main move selection function."""
        game = Game(obs['board'])
        self.move_count += 1
        return self.find_best_move(game)

# Agent wrapper for Kaggle compatibility
def agent_wrapper(observation, configuration):
    if not hasattr(agent_wrapper, 'bot'):
        agent_wrapper.bot = ChessBot()
    return agent_wrapper.bot.chess_bot(observation)
