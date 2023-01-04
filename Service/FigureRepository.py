from Home_Work.OOP_final_work.data.Figure import Figure
from Home_Work.OOP_final_work.data.Lengthable import Lengthable
from Home_Work.OOP_final_work.data.Perimeterable import Perimeterable
from Home_Work.OOP_final_work.Service.Repository import Repository


class FigureRepository(Repository):
    def __init__(self):
        self.__figure_list = []

    def add(self, figure):
        self.__figure_list.append(figure)

    def get_all_perimeter(self):
        perimeter = 0.0
        for figure in self.__figure_list:
            if isinstance(figure, Perimeterable):
                perimeter += figure.perimeter()
        return perimeter

    def get_all_length(self):
        length = 0.0
        for figure in self.__figure_list:
            if isinstance(figure, Lengthable):
                length += figure.length()
        return length

    def get_all_areas(self):
        area = 0.0
        for figure in self.__figure_list:
            if isinstance(figure, Figure):
                area += figure.count_area()
        return area

    def get_figure_list(self):
        return self.__figure_list
