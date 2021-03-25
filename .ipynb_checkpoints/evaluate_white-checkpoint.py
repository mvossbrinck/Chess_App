import chess
import numpy as np
from whiteScore import whiteScore
from blackScore import blackScore

def evaluate_white(fen_input):
    return whiteScore(fen_input) - blackScore(fen_input)
