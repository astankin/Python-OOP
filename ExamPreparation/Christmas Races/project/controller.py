from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from collections import Counter


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def find_car(self, car_type):
        for car in reversed(self.cars):
            if type(car).__name__ == car_type and not car.is_taken:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
        else:
            car = MuscleCar(model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_driver(driver_name)
        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        car = self.find_car(car_type)
        if car and driver:
            if driver.car:
                old_car = driver.car
                old_car.is_taken = False
                driver.car = car
                car.is_taken = True
                return f"Driver {driver.name} changed his car from {old_car.model} to {driver.car.model}."
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_race(race_name)
        driver = self.find_driver(driver_name)
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if race and driver:
            if driver in race.drivers:
                return f"Driver {driver_name} is already added in {race_name} race."
            race.drivers.append(driver)
            race.driver_cars[driver] = driver.car.speed_limit
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.find_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        k = Counter(race.driver_cars)
        high = k.most_common(3)
        result = []
        for elem in high:
            fastest_driver, speed_limit = elem
            fastest_driver.number_of_wins += 1
            result.append(f"Driver {fastest_driver.name} wins the {race_name} race with a speed of {speed_limit}.")
        return '\n'.join(result)






