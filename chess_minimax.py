import chess
import numpy as np
from evaluate_board import white_score_eval, black_score_eval


# Note: there was an issue found in the minimax algorithm. When it was corrected, the function became
# much slower. Even with a depth of 3, it lagged a bit so the depth used in the app is 2

# Calculate minimax algorithm for white player
def minimax_white(fen_input, move, alpha, beta, depth = 2):
    board = chess.Board(fen_input)
    if depth == 0 or board.is_game_over():
        return move, white_score_eval(fen_input)
    if board.turn == 1:
        best_move = None
        best_score = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            new_move, new_score = minimax_white(fen_input, move, alpha, beta, depth - 1)
            if new_score > best_score:
                best_score, best_move = new_score, new_move
            board.pop()
            alpha = max(alpha, new_score)
            if beta <= alpha:
                return best_move, best_score
        return best_move, best_score
    else:
        best_move = None
        best_score = float('inf')
        for move in board.legal_moves:
            board.push(move)
            new_move, new_score = minimax_white(fen_input, move, alpha, beta, depth - 1)
            if new_score < best_score:
                    best_score, best_move = new_score, new_move
            board.pop()
            beta = min(beta, new_score)
            if beta <= alpha:
                return best_move, best_score
        return best_move, best_score


# Calculate minimax algorithm for black player
def minimax_black(fen_input, move, alpha, beta, depth = 2):
    board = chess.Board(fen_input)
    if depth == 0 or board.is_game_over():
        return move, black_score_eval(fen_input)
    if board.turn == 0:
        best_move = None
        best_score = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            new_move, new_score = minimax_black(fen_input, move, alpha, beta, depth - 1)
            if new_score > best_score:
                best_score, best_move = new_score, new_move
            board.pop()
            alpha = max(alpha, new_score)
            if beta <= alpha:
                return best_move, best_score
        return best_move, best_score
    else:
        best_move = None
        best_score = float('inf')
        for move in board.legal_moves:
            board.push(move)
            new_move, new_score = minimax_black(fen_input, move, alpha, beta, depth - 1)
            if new_score < best_score:
                    best_score, best_move = new_score, new_move
            board.pop()
            beta = min(beta, new_score)
            if beta <= alpha:
                return best_move, best_score
        return best_move, best_score


# Pull minimax functions for black and white players into one function
def get_minimax_move(fen_input):
    board = chess.Board(fen_input)
    if board.turn:
        best_move, best_score = minimax_white(fen_input, None, -float('inf'), float('inf'))
    else:
        best_move, best_score = minimax_black(fen_input, None, -float('inf'), float('inf'))
    selected_move = board.san(best_move)
    return selected_move
