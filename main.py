from graphics import Window, Line, Cell
from maze import Maze

def main():
    win = Window(1280, 720)

    maze = Maze(0.025 * 720, 0.025 * 1280, 15, 15, 35, 35, win, seed=0)
    #maze.solve()

    win.wait_for_close()

main()
