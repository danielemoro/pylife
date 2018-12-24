from board import Board
from gui import GUI
import time
import sys, pygame
import copy
import numpy as np
from timeit import default_timer as timer
from numba import vectorize

def gol(board):
    size = board.size

    @vectorize(['float32(float32, float32)'], target='cuda')
    def worker(val, nbrs):
        if val == 0:
            if nbrs > 1:
                return np.float32(1.0)
            else:
                return np.float32(0.0)
        else:
            return np.float32(0.0)


        # if val == 1:  # alive
        #     if nbrs < 2 or nbrs > 3:  # kill lonely or overcrowded cells
        #         return np.float32(0.0)
        #     else:
        #         return np.float32(1.0)
        # else:
        #     if nbrs == 3:  # create new cells
        #         return np.float32(1.0)
        #     else:
        #         return val

    neighbors = board.generate_neighbor_board()
    result = worker(np.array(board.board.flatten(), dtype='float32'),
                    neighbors
                    ).reshape((size, size))
    board.set_board(result)


board = Board(size = 1000)
# board.rand_pop()
gui = GUI()
tick = 0

while True:
    start = time.time()
    tick += 1
    if gui.handle_events(pygame.event.get(), board):
        pass
        gol(board)
    gui.update_canvas(board)
    print("Tick {} took {} ms".format(tick, (time.time() - start)*1000))



