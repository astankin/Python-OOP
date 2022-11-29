from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}"


