class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_next_id():
        return Equipment.id + 1

    def __repr__(self):
        return f"Equipment <{Equipment.id}> {self.name}"

    
