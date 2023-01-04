import math
from Home_Work.OOP_final_work.data.Polygon import Polygon


class Triangle(Polygon):

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.sides = [side1, side2, side3]

    def count_area(self):
        return math.sqrt(super().perimeter() / 2 * (super().perimeter() / 2 - self.sides[0]) *
                         (super().perimeter() / 2 - self.sides[1]) * (super().perimeter() / 2 - self.sides[2]))