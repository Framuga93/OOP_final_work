from abc import ABC

from Home_Work.OOP_final_work.data.Polygon import Polygon


class Squared(Polygon, ABC):
    def __init__(self, side1):
        super().__init__()
        self.sides = [side1, side1]

    def perimeter(self):
        return super().perimeter() * 2

    def count_area(self):
        return self.sides[0] * self.sides[1]