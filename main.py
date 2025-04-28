from graphics import Window, Point, Line

win = Window(800, 600)

point_a = Point(1,1)
point_b = Point(800,600)
line_a_b = Line(point_a, point_b)

point_c = Point(800,0)
point_d = Point(0,600)
line_c_d = Line(point_c, point_d)

win.draw_line(line_a_b, "red")
win.draw_line(line_c_d, "blue")

win.wait_for_close()