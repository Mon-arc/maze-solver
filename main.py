from graphics import Window, Line, Cell
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(0, 0, 12, 10, 50, 50, win)

    win.wait_for_close()

main()
