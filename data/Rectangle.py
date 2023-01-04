from Home_Work.OOP_final_work.data.Squared import Squared


class Rectangle(Squared):

    def __init__(self, side1, side2):
        super().__init__(side1)
        self.sides = [side1, side2]
    #
    # def perimeter(self):
    #     return super().perimeter() * 2
    #
    # def count_area(self):
    #     return self.sides[0] * self.sides[1]

