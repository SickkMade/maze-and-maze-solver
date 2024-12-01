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
        self.visited = False
        self._win = window

    def draw(self, point_top_left : Point = None, point_bottom_right : Point = None):
        self.point_bottom_right = point_bottom_right or self.point_bottom_right
        self.point_top_left = point_top_left or self.point_top_left

        top_right = Point(self.point_bottom_right.x,self.point_top_left.y)
        bottom_left = Point(self.point_top_left.x,self.point_bottom_right.y)

        self.center = Point(
            (self.point_top_left.x + self.point_bottom_right.x) / 2,
            (self.point_top_left.y + self.point_bottom_right.y) / 2
        )

        self._win.draw_line(Line(self.point_top_left, bottom_left), 'black' if self.has_left_wall else 'systemWindowBackgroundColor')
        self._win.draw_line(Line(self.point_bottom_right, top_right), 'black' if self.has_right_wall else 'systemWindowBackgroundColor')
        self._win.draw_line(Line(self.point_top_left, top_right), 'black' if self.has_top_wall else 'systemWindowBackgroundColor')
        self._win.draw_line(Line(bottom_left, self.point_bottom_right), 'black' if self.has_bottom_wall else 'systemWindowBackgroundColor')
    
    def draw_move(self, to_cell, undo=False):
        self._win.draw_line(Line(self.center, to_cell.center), 'gray' if undo else 'red')

    def destroy_wall(self, arr_direction):
        if arr_direction == [-1, 0]:
            self.has_top_wall = False
        elif arr_direction == [1, 0]:
            self.has_bottom_wall = False
        elif arr_direction == [0, -1]:
            self.has_left_wall = False
        elif arr_direction == [0, 1]:
            self.has_right_wall = False
        self.draw()