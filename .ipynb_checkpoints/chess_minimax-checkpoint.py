import chess
import numpy as np
from minimax_white import minimax_white
from minimax_black import minimax_black

def get_minimax_move(fen_input):
    board = chess.Board(fen_input)
    if board.turn:
        best_move, best_score = minimax_white(fen_input, None, -float('inf'), float('inf'))
    else:
        best_move, best_score = minimax_black(fen_input, None, -float('inf'), float('inf'))
    selected_move = board.san(best_move)
    return selected_move
