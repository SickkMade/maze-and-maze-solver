from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.title("Maze!")
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.isWindowRunning = False

    def redraw(self):
        self.window.update_idletasks()
        self.window.update()

    def wait_for_close(self):
        self.isWindowRunning = True
        while(self.isWindowRunning):
            self.redraw()

    def close(self):
        self.isWindowRunning = False

    def draw_line(self, line : Line, line_color):
        line.draw(self.canvas, line_color)
    