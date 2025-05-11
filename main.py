from graphics import *
from cell import *
from maze import *

def main():
    win = Window(600, 800)
    maze = Maze(100, 100, 10, 10, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()