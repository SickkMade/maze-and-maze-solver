from Window import Window
from cell import Cell
from point import Point

win = Window(800, 600)
cell = Cell(True, True, True, True, win)
cell_start = Cell(True, True, True, True, win)
cell_start.draw(Point(10, 10), Point(20, 20))

for i in range(10, 100, 10):
    for j in range(10, 100, 10):
        cell.draw(Point(i,j), Point(i+10,j+10))

cell.draw_move(cell_start, undo=False)

win.wait_for_close()

