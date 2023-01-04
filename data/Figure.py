from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def count_area(self):
        pass
