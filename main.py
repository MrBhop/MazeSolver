from graphics import *
from cell import *

def main():
    win = Window(600, 800)
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(100, 100, 200, 200)
    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.has_bottom_wall = False
    cell_2.draw(200, 100, 300, 200)
    cell.draw_move(cell_2, undo=True)
    win.wait_for_close()


if __name__ == "__main__":
    main()