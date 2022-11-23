from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.increase_speed = 3



