class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []
        self.driver_cars = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string!")
        self.__name = value


