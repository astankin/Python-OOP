from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__adding_to_list(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__adding_to_list(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__adding_to_list(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__adding_to_list(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__adding_to_list(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_object(subscription_id, self.subscriptions)
        customer = self.__find_object(subscription.customer_id, self.customers)
        trainer = self.__find_object(subscription.trainer_id, self.trainers)
        plan = self.__find_object(subscription.trainer_id, self.plans)
        equipment = self.__find_object(plan.equipment_id, self.equipment)
        return repr(subscription) + "\n" + repr(customer) + "\n" + repr(trainer) + "\n" + repr(equipment) + "\n" + repr(plan)

    def __find_object(self, object_id, collection):
        for object in collection:
            if object.id == object_id:
                return object

    def __adding_to_list(self, object, object_list):
        for elem in object_list:
            if elem.id == object.id:
                return
        object_list.append(object)
