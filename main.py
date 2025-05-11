from graphics import *

def main():
    win = Window(600, 800)
    win.draw_line(Line(Point(0, 0), Point(300, 300)))
    win.wait_for_close()


if __name__ == "__main__":
    main()