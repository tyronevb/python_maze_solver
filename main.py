from graphics import Window, Point, Line
from cell import Cell

win = Window(800, 600)
cell_1 = Cell(10, 10, 30, 30, win)
cell_1.draw()

cell_2 = Cell(80, 10, 90, 400, win)
cell_2.has_bottom_wall = False
cell_2.draw()
win.wait_for_close()