from graphics import Cell
import random
import time
class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        to_break = ""
        while(1):
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1,j, 'left'))
                    to_break = 'left'
            if i < self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1,j, 'right'))
                    to_break = 'right'
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i,j-1, 'up'))
                    to_break = 'up'
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i,j+1, 'down'))
                    to_break = 'down'
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = to_visit[random.randrange(0, len(to_visit), 1)]
                # Removing both walls that are in between two cells is not necessary,
                # but i'm doing it just in case something changes
                # where the white isn't drawn over the black lines
                if direction[2] == 'left':
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                elif direction[2] == 'right':
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                elif direction[2] == 'up':
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                elif direction[2] == 'down':
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False

                self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False



    def _create_cells(self):
        self._cells = [[Cell(self._win) for i in range (self._num_rows)] for i in range (0, self._num_cols)]

        for i in range (self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
