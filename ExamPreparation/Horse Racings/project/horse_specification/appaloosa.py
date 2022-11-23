from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.increase_speed = 2

