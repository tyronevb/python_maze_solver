from cell import Cell
from time import sleep
import random

class Maze(object):
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None,
    ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    
    def _create_cells(self):
        
        self._cells = [] # hold list of cells

        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                row.append(Cell(x1, y1, x2, y2, self.win))
            self._cells.append(row)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.1)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
            self._cells[i][j].visited = True
            while True:
                to_visit = []
                
                if i > 0 and not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
                #print(f"i: {i}, i+1:{i+1}, num_cols:{self.num_cols}")
                if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
                if j > 0 and not self._cells[i][j-1].visited:
                    to_visit.append((i,j-1))
                if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))

                if len(to_visit) == 0:
                    self._draw_cell(i, j)
                    return
                
                rand_idx = random.randrange(len(to_visit))
                next_cell = to_visit[rand_idx]

                if next_cell[0] == i - 1: # left
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall= False
                if next_cell[0] == i + 1: # right
                    self._cells[i][j].has_right_wall = False
                    self._cells[i-1][j].has_left_wall= False
                if next_cell[1] == j - 1: # above
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall= False
                if next_cell[1] == j + 1: # below
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall= False

                self._break_walls_r(next_cell[0], next_cell[1])