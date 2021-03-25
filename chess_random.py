import chess
import numpy as np

def get_random_move(fen_input):
    board = chess.Board(fen_input)
    legal_moves = list(board.legal_moves)
    rand_move_num = np.random.randint(0,len(legal_moves))
    random_move = board.san(legal_moves[rand_move_num])
    return random_move
