from abc import ABC, abstractmethod


class Horse(ABC):
    max_speed = None

    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False
        self.increase_speed = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.increase_speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.increase_speed


