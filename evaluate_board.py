import chess
import numpy as np


# Function to get score for just white pieces
def white_pieces_score(fen_input):

    # Standard valuations for pieces other than king according to Wikipedia
    piece_values = {
        chess.PAWN: 100,
        chess.ROOK: 500,
        chess.KNIGHT: 300,
        chess.BISHOP: 300,
        chess.QUEEN: 900,
        chess.KING: 50000
        }

    board = chess.Board(fen_input)
    white_score = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            white_score += piece_values[piece.piece_type]

    return white_score


# Function to get score for just black pieces
def black_pieces_score(fen_input):

    # Standard valuations for pieces other than king according to Wikipedia
    piece_values = {
        chess.PAWN: 100,
        chess.ROOK: 500,
        chess.KNIGHT: 300,
        chess.BISHOP: 300,
        chess.QUEEN: 900,
        chess.KING: 50000
        }

    board = chess.Board(fen_input)
    black_score = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.BLACK:
            black_score += piece_values[piece.piece_type]

    return black_score


# Function to evaluate the board for white player
def white_score_eval(fen_input):
    return white_pieces_score(fen_input) - black_pieces_score(fen_input)


# Function to evaluate the board for black player
def black_score_eval(fen_input):
    return black_pieces_score(fen_input) - white_pieces_score(fen_input)
