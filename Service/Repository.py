from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, figure):
        pass
