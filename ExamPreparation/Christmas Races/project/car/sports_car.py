from project.car.car import Car


class SportsCar(Car):
    min_speed = 400
    max_speed = 600

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False



