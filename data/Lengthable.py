from abc import ABC, abstractmethod


class Lengthable(ABC):
    @abstractmethod
    def length(self):
        pass
