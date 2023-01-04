from abc import ABC
from Home_Work.OOP_final_work.data.Figure import Figure
from Home_Work.OOP_final_work.data.Perimeterable import Perimeterable


class Polygon(Figure, Perimeterable, ABC):

    def __init__(self):
        self.sides = []

    def polygon(self, sides):
        self.sides = sides

    def perimeter(self):
        perimeter = 0.0
        for side in self.sides:
            perimeter += side
        return perimeter


