from abc import ABC, abstractmethod


class Perimeterable(ABC):
    @abstractmethod
    def perimeter(self):
        pass