from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell_1 = Cell(10, 10, 30, 30, win)
    cell_1.draw()

    cell_2 = Cell(80, 10, 90, 400, win)
    cell_2.has_bottom_wall = False
    cell_2.draw()

    cell_3 = Cell(250, 250, 300, 300, win)
    cell_3.has_top_wall = False
    cell_3.has_left_wall = False
    cell_3.draw()

    cell_a = Cell(500, 100, 520, 120, win)
    cell_a.draw()
    cell_b = Cell(550, 150, 570, 170, win)
    cell_b.draw()

    cell_a.draw_move(cell_b)

    cell_a = Cell(500, 400, 520, 420, win)
    cell_a.draw()
    cell_b = Cell(550, 450, 570, 470, win)
    cell_b.draw()

    cell_a.draw_move(cell_b, True)

    win.wait_for_close()

main()