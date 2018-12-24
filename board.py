import numpy as np
from timeit import default_timer as timer


class Board:
    def __init__(self, size = 10):
        self.board = np.zeros(shape=(size, size), dtype='float32')
        self.size = size
        self.board[1, 1] = 1
        self.board[1, 2] = 1
        self.board[1, 3] = 1

    def set_board(self, board):
        self.board = board

    def clear_board(self):
        self.board = np.zeros(shape=(self.size, self.size))

    def get_cell(self, x, y):
        if self.size > x >= 0 and self.size > y >= 0:
            return self.board[x, y]
        else:
            return 0

    def set_cell(self, x, y, value):
        if self.size > x >= 0 and self.size > y >= 0:
            self.board[x, y] = value

    def count_neighbors(self, x, y):
        count = 0
        for x_delta in [-1, 0, 1]:
            for y_delta in [-1, 0, 1]:
                if x_delta == 0 and y_delta == 0:
                    continue
                count += self.get_cell(x + x_delta, y + y_delta)
        return count

    def generate_neighbor_board(self):
        def conv2d(a, f):
            s = f.shape + tuple(np.subtract(a.shape, f.shape) + 1)
            strd = np.lib.stride_tricks.as_strided
            subM = strd(a, shape=s, strides=a.strides * 2)
            return np.einsum('ij,ijkl->kl', f, subM)
        board_padded = np.pad(self.board, 1, "constant")
        return np.array(conv2d(board_padded, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])), dtype='float32').flatten()

    def rand_pop(self):
        self.board = np.where(np.random.rand(self.size, self.size) > 0.8, 1, 0)
