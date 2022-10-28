from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary
        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        animals_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            animals_dict[animal.__class__.__name__].append(animal)
        for animal, value in animals_dict.items():
            result += f"----- {len(value)} {animal}s:\n"
            for elem in value:
                result += repr(elem) + "\n"
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}
        for worker in self.workers:
            workers_dict[worker.__class__.__name__].append(worker)
        for worker, value in workers_dict.items():
            result += f"----- {len(value)} {worker}s:\n"
            for elem in value:
                result += repr(elem) + "\n"
        return result.strip()








