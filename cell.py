from graphics import Point, Line

class Cell(object):
    def __init__(self, x1, y1, x2, y2, window):
        """
        x1, y1 - cords of top-left corner
        x2, y2 - cords of bottom-right corner
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
        self._centre = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)

        if self.has_left_wall:
            left_wall_line = Line(top_left, bottom_left)
            self._win.draw_line(left_wall_line)
        if self.has_right_wall:
            right_wall_line = Line(top_right, bottom_right)
            self._win.draw_line(right_wall_line)
        if self.has_top_wall:
            top_wall_line = Line(top_left, top_right)
            self._win.draw_line(top_wall_line)
        if self.has_bottom_wall:
            bottom_wall_line = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall_line)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_colour = "red"
        else:
            fill_colour = "gray"
        
        line_between_cells = Line(self._centre, to_cell._centre)
        self._win.draw_line(line_between_cells, fill_colour)