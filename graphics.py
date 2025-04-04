from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while(self.is_running):
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.is_running = False

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2.5)

class Cell:

    def __init__(
        self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_bottom_wall:
            line = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_right_wall:
            line = Line(Point(x2, y2), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y2), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        if not undo:
            line = Line(self.center_point(), to_cell.center_point())
            self._win.draw_line(line, fill_color="red")
        else:
            line = Line(self.center_point(), to_cell.center_point())
            self._win.draw_line(line, fill_color="gray")

    def center_point(self) -> Point:
        if self._x1 and self._x2 and self._y1 and self._y2:
            return Point((self._x1 + self._x2) / 2,
                         (self._y1 + self._y2) / 2)
        return Point(None, None)
