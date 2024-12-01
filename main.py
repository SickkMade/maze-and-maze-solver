from Window import Window
from maze import Maze

win = Window(800, 600)

Maze(200, 100, 15, 15, 25, 25, win)

win.wait_for_close()

