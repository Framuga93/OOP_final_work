import math
from abc import ABC
from Home_Work.OOP_final_work.data.Figure import Figure
from Home_Work.OOP_final_work.data.Lengthable import Lengthable


class Circle(Figure, Lengthable, ABC):

    def __init__(self, radius):
        self.radius = radius

    def circle(self, radius):
        self.radius = radius

    def count_area(self):
        return math.pi * self.radius * self.radius

    def length(self):
        return 2 * math.pi * self.radius
