from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []  # objects
        self.jockeys = []  # objects
        self.horse_races = []  # objects

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        else:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    def __find_horse(self, horse_type):
        for horse in reversed(self.horses):
            if type(horse).__name__ == horse_type and not horse.is_taken:
                return horse
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def __find_race(self, race_type_):
        for race in self.horse_races:
            if race.race_type == race_type_:
                return race
        else:
            raise Exception(f"Race {race_type_} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return

        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey(jockey_name)
        horse = self.__find_horse(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race(race_type)
        jockey = self.__find_jockey(jockey_name)
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        highest_speed = 0
        jockey_name = ""
        horse_name = ""
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name
        return f"The winner of the {race_type} race, " \
               f"with a speed of {highest_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."





