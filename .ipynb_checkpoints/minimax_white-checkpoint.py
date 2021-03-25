import chess
import numpy as np
from evaluate_white import evaluate_white

def minimax_white(fen_input, move, alpha, beta, depth = 3):
    board = chess.Board(fen_input)
    if depth == 0 or board.is_game_over():
        return move, evaluate_white(fen_input)
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
