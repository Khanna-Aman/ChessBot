from Chessnut import Game
import random

class ChessBot:
    def __init__(self):
        self.move_count = 0  # Track the number of moves made

    def evaluate_position(self, game):
        """Evaluates the board position by summing piece values."""
        piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0}
        fen = game.get_fen().split(' ')[0]  # Get the board state in FEN notation
        value = sum(piece_values.get(p.upper(), 0) * (1 if p.isupper() else -1) for p in fen)
        return value

    def find_best_move(self, game):
        """Finds the best move based on evaluation."""
        moves = list(game.get_moves())  # Get all legal moves
        if not moves:
            return None  # Return None if no legal moves are available

        # Check if any move results in checkmate
        for move in moves:
            game_copy = Game(game.get_fen())
            game_copy.apply_move(move)
            if game_copy.status == "checkmate":
                return move  # Return the move if it results in checkmate

        # Otherwise, choose the move with the best material gain
        best_move = max(moves, key=lambda move: self.evaluate_move(game, move))
        return best_move

    def evaluate_move(self, game, move):
        """Evaluates the material gain of a move."""
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        return self.evaluate_position(game_copy)

    def chess_bot(self, obs):
        """Main function to select the best move based on the current game state."""
        game = Game(obs['board'])  # Initialize the game with the provided board state
        self.move_count += 1
        return self.find_best_move(game)  # Return the best move

# Agent wrapper for Kaggle compatibility
def agent_wrapper(observation, configuration):
    if not hasattr(agent_wrapper, 'bot'):
        agent_wrapper.bot = ChessBot()
    return agent_wrapper.bot.chess_bot(observation)
