from graphics import *
from cell import *
from maze import *
import sys

def main():
    sys.recursionlimit(10000)
    win = Window(600, 800)
    maze = Maze(100, 100, 10, 10, 50, 50, win, 0)
    print("solving maze ...")
    if maze.solve():
        print("maze solved!")
    else:
        print("maze could not be solved!")
    win.wait_for_close()


if __name__ == "__main__":
    main()