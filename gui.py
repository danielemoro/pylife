import sys, pygame
import time
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CELL_ON = BLACK
CELL_OFF = WHITE


class GUI():
    def __init__(self):
        pygame.init()

        self.size = width, height = 1000, 1000
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(WHITE)
        self.zoom_size = 10
        self.zoom_pos = (0, 0)

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Consolas', 10)

    def update_canvas(self, board):
        x = 0
        y = 0
        board_size = min(board.size, self.zoom_size)
        w = self.size[0] / board_size
        h = self.size[1] / board_size
        self.screen.fill(WHITE)

        start_x = self.zoom_pos[0]
        start_y = self.zoom_pos[1]

        for x_b in range(start_x, board_size+start_x):
            for y_b in range(start_y, board_size+start_y):
                self.draw_cell(board.get_cell(x_b, y_b), y, x, w, h)
                x = (x+w) % self.size[0]
            y += h

        pygame.display.update()

    def draw_cell(self, cell_value, x, y, w, h, text=None):
        if cell_value == 0:
            color = CELL_OFF
        else:
            color = CELL_ON
        self.screen.fill(color, pygame.Rect(x, y, w, h))

        if text is not None:
            textsurface = self.myfont.render(text, False, RED)
            self.screen.blit(textsurface, (x+w/2, y+h/2))

    def draw_one_cell(self, board, cell_value, x_board, y_board, text=None):
        w = self.size[0] / board.shape[1]
        h = self.size[1] / board.shape[0]
        x = x_board * w
        y = y_board * h
        self.draw_cell(cell_value, x, y, w, h, text=text)
        pygame.display.update()

    def get_mouse_cell_pos(self, mouse_x, mouse_y, board):
        w = self.size[0] / self.zoom_size
        h = self.size[1] / self.zoom_size
        size = min(board.size, self.zoom_size)
        start_x = self.zoom_pos[1]
        start_y = self.zoom_pos[0]
        x = 0
        y = 0
        for x_board in range(start_x, size+start_x):
            for y_board in range(start_y, size+start_y):
                if x < mouse_x < (x+w) and y < mouse_y < (y+h):
                    return y_board, x_board
                x = (x + w) % self.size[0]
            y += h
        return -1, -1

    def move_camera(self, delta, board_size):
        new_zoom_pos = (self.zoom_pos[0] + delta[0], self.zoom_pos[1] - delta[1])
        if board_size > new_zoom_pos[0] >= 0 and board_size > new_zoom_pos[1] >= 0:
            self.zoom_pos = new_zoom_pos

    def zoom_camera(self, delta, board_size):
        new_zoom = self.zoom_size + delta
        if board_size > new_zoom > 0:
            self.zoom_size = new_zoom


    def handle_events(self, events, board):
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
            # if event.type == pygame.KEYDOWN:

        if sum(pygame.key.get_pressed()) == 1:
            name = pygame.key.name(pygame.key.get_pressed().index(1))
            if name == "left":
                self.move_camera((-1, 0), board.size)
            if name == "right":
                self.move_camera((1, 0), board.size)
            if name == "up":
                self.move_camera((0, 1), board.size)
            if name == "down":
                self.move_camera((0, -1), board.size)
            if name == "=":
                self.zoom_camera(-2, board.size)
            if name == "-":
                self.zoom_camera(2, board.size)
            return False

        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_rel() != (0, 0):
            m_pos = pygame.mouse.get_pos()
            pos = self.get_mouse_cell_pos(m_pos[0], m_pos[1], board)
            print("clicked", pos)
            board.set_cell(pos[0], pos[1], 1)
            return False
        else:
            return True






