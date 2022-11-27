from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    decrease_coefficient = 10

    def __init__(self, name: str):
        super().__init__(name, 50)
