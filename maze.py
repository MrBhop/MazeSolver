from cell import *
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, winow=None, seed=None):
        print("starting maze generation ...")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = winow
        
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self.break_walls(0, 0)
        print("maze generated!")
        
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                 self._draw_cell(i, j)
                 
    
    def _break_entrance_and_exit(self):
        col, row = 0, 0
        self._cells[col][row].has_top_wall = False
        self._draw_cell(col, row)
        
        col, row = len(self._cells) - 1, len(self._cells[0]) - 1
        self._cells[col][row].has_bottom_wall = False
        self._draw_cell(col, row)
        

    def break_walls(self, i, j):
        cells = self._cells
        current = self._cells[i][j]
        current.visited = True
           
        to_visit = []

        # check left
        if i > 0 and not cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
                
        # check right
        if i < len(cells) - 1 and not cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

        # check top
        if j > 0 and not cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
        
        # check bottom
        if j < len(cells[i]) - 1 and not cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            

        while len(to_visit) > 0:
            target = to_visit.pop(random.randint(0, len(to_visit) - 1))
            
            if cells[target[0]][target[1]].visited:
                continue
            
            self.break_walls_between_cells((i, j), target)
            self.break_walls(target[0], target[1])
            
            
    def break_walls_between_cells(self, cell1_tuple, cell2_tuple):
        i1, j1 = cell1_tuple
        cell1 = self._cells[i1][j1]
        i2, j2 = cell2_tuple
        cell2 = self._cells[i2][j2]

        if i1 - 1 == i2:
            cell1.has_left_wall = False
            cell2.has_right_wall = False
        if i1 + 1 == i2:
            cell1.has_right_wall = False
            cell2.has_left_wall = False
        if j1 - 1 == j2:
            cell1.has_top_wall = False
            cell2.has_bottom_wall = False
        if j1 + 1 == j2:
            cell1.has_bottom_wall = False
            cell2.has_top_wall = False
            
        self._draw_cell(i1, j1)
        self._draw_cell(i2, j2)
    
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)