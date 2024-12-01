from cell import Cell
from point import Point
from line import Line
import random
from time import time, sleep

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.create_cells()
        if(seed != None):
            random.seed(seed)

        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()
    
    def create_cells(self):
        for j in range(self.num_rows):
            output = []
            for i in range(self.num_cols):
                cell = Cell(True, True, True, True, self.win)
                cell.draw(Point(self.x1+i*self.cell_size_x, self.y1+j*self.cell_size_y), Point(self.x1 + self.cell_size_x * (i+1), self.y1 + self.cell_size_y * (j+1)))
                output.append(cell)
            self._cells.append(output)
        self._break_enterance_and_exit()
        
    def _animate(self):
        self.win.redraw()
        sleep(0.025)

    def solve(self):
        self._solve_r()
    
    def _solve_r(self, j=0, i=0):
        self._animate()
        self._cells[j][i].visited = True
        if(j==self.num_cols-1 and i == self.num_rows-1):
            return True
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while True:
            possible_dirs = []
            for arr in dirs:
                nj = j + arr[0]
                ni = i + arr[1]
                if (0 <= nj < self.num_rows and 0 <= ni < self.num_cols and self._cells[j][i].check_wall(arr) and not self._cells[nj][ni].visited):
                    possible_dirs.append(arr)
            if possible_dirs:
                new_cell = random.choice(possible_dirs)
                nj = j + new_cell[0]
                ni = i + new_cell[1]
                self._cells[j][i].draw_move(self._cells[nj][ni])
                if (self._solve_r(nj, ni)): return True
                else:
                    self._cells[j][i].draw_move(self._cells[nj][ni], undo=True)
            else:
                return False
        
        

    def _break_enterance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False

        self._cells[0][0].draw()
        self._cells[-1][-1].draw()

    def _break_walls_r(self, j, i):
        self._animate()
        self._cells[j][i].visited = True
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while True:
            possible_dirs = []
            for arr in dirs:
                nj = j + arr[0]
                ni = i + arr[1]
                if (0 <= nj < self.num_rows and 0 <= ni < self.num_cols and not self._cells[nj][ni].visited):
                    possible_dirs.append(arr)
            if possible_dirs:
                new_cell = random.choice(possible_dirs)
                nj = j + new_cell[0]
                ni = i + new_cell[1]
                opposite_direction = [-new_cell[0], -new_cell[1]]
                self._cells[j][i].destroy_wall(new_cell)
                self._cells[nj][ni].destroy_wall(opposite_direction)
                self._break_walls_r(nj, ni)
            else:
                return
            
    def _reset_cells_visited(self):
        for j in range(self.num_rows):
            for i in range(self.num_cols):
                self._cells[j][i].visited = False