from cell import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, winow=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = winow
        self._create_cells()
        
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                 self._draw_cell(i, j)

        self._break_entrance_and_exit()
                 
    
    def _break_entrance_and_exit(self):
        col, row = 0, 0
        self._cells[col][row].has_top_wall = False
        self._draw_cell(col, row)
        
        col, row = len(self._cells) - 1, len(self._cells[0]) - 1
        self._cells[col][row].has_bottom_wall = False
        self._draw_cell(col, row)
        
        
    
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