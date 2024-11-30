from Window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, left : bool, right : bool, top: bool, bottom : bool, window : Window):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.point_top_left = Point(0,0)
        self.point_bottom_right = Point(0,0)
        self.center = Point(0,0)
        self._win = window

    def draw(self, point_top_left : Point, point_bottom_right : Point):
        self.point_bottom_right = point_bottom_right
        self.point_top_left = point_top_left

        top_right = Point(point_bottom_right.x,point_top_left.y)
        bottom_left = Point(point_top_left.x,point_bottom_right.y)

        self.center = Point(
            (self.point_top_left.x + self.point_bottom_right.x) / 2,
            (self.point_top_left.y + self.point_bottom_right.y) / 2
        )

        if(self.has_left_wall):
            self._win.draw_line(Line(point_top_left, bottom_left), 'black')
        if(self.has_right_wall):
            self._win.draw_line(Line(point_bottom_right, top_right), 'black')
        if(self.has_top_wall):
            self._win.draw_line(Line(point_top_left, top_right), 'black')
        if(self.has_bottom_wall):
            self._win.draw_line(Line(bottom_left, point_bottom_right), 'black')
    
    def draw_move(self, to_cell, undo=False):
        self._win.draw_line(Line(self.center, to_cell.center), 'gray' if undo else 'red')