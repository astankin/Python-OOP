from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    decrease_coefficient = 5

    def __init__(self, name: str):
        super().__init__(name, 70)





