from Home_Work.OOP_final_work.Service.FigureRepository import FigureRepository
from Home_Work.OOP_final_work.controller.UserController import UserController


class Main:
    def main(self):
        rep = FigureRepository()
        uc = UserController(rep)
        uc.create_circle(10.0)
        uc.create_squared(1.0)
        uc.create_triangle(5.0, 2.0, 6.0)
        uc.create_rect(6.0, 4.0)
        print(uc.get_all_perimeters())
        print(uc.get_all_areas())
        print(uc.get_all_lengths())

if __name__ == "__main__":
    a = Main()
    a.main()
