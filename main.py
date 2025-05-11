from graphics import *
from cell import *

def main():
    win = Window(600, 800)
    cell = Cell(win)
    cell.draw(100, 100, 200, 200)
    cell_2 = Cell(win)
    cell_2.has_bottom_wall = False
    cell_2.draw(200, 200, 300, 300)
    win.wait_for_close()


if __name__ == "__main__":
    main()