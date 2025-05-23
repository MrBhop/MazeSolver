from graphics import *


class Cell:
    def __init__(self, window=None):
        self._win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False
        
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        def get_color(wall_exists):
            if wall_exists:
                return "black"

            return "white"
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, get_color(self.has_left_wall))

        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, get_color(self.has_top_wall))

        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, get_color(self.has_right_wall))

        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, get_color(self.has_bottom_wall))
            
            
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo:
            color = "gray"
        else:
            color = "red"

        self._win.draw_line(Line(self.center(), to_cell.center()), color)

    
    def center(self):
        if self._x1 is None or self._y1 is None or self._x2 is None or self._y2 is None:
            return

        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)