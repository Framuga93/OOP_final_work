from Home_Work.OOP_final_work.data.Circle import Circle
from Home_Work.OOP_final_work.data.Rectangle import Rectangle
from Home_Work.OOP_final_work.data.Squared import Squared
from Home_Work.OOP_final_work.data.Triangle import Triangle


class UserController:

    def __init__(self, __rep):
        self.__rep = __rep

    def get_all_figure(self):
        return self.__rep.get_figure_list()

    def create_circle(self, radius):
        if radius <= 0:
            print("Incorrect data")
        else:
            self.__rep.add(Circle(radius))

    def create_triangle(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("All sides must be > 0")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            print("Lengths sum of two sides must be bigger than third side")
        else:
            self.__rep.add(Triangle(side1, side2, side3))

    def create_rect(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            print("All sides must be > 0")
        else:
            self.__rep.add(Rectangle(side1, side2))

    def create_squared(self, side1):
        if side1 <= 0:
            print("Side must be > 0")
        else:
            self.__rep.add(Squared(side1))

    def get_all_perimeters(self):
        return self.__rep.get_all_perimeter()

    def get_all_lengths(self):
        return self.__rep.get_all_length()

    def get_all_areas(self):
        return self.__rep.get_all_areas()
