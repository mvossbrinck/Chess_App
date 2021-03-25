import chess
import numpy as np

FEN = "rnbqkbnr/pppppp1p/8/6p1/3P4/5N2/PPP1PPPP/RNBQKB1R"
board = chess.Board(FEN)

legal_moves = list(board.legal_moves)
rand_move_num = np.random.randint(0,len(legal_moves))
random_move = board.san(legal[rand_move_num])
random_move