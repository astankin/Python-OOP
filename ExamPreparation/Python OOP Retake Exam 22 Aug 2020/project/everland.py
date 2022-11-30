from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = 0
        for room in self.rooms:
            consumption += room.expenses + room.room_cost
        return f"Monthly consumptions: {consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                result.append(
                    f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        all_people_in_the_hotel = 0
        for room in self.rooms:
            all_people_in_the_hotel += room.members_count
        result = f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for i in range(len(room.children)):
                    result += f"--- Child {i + 1} monthly cost: {room.children[i].cost * 30:.2f}$\n"
            if hasattr(room, "appliances"):
                result += f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$\n"
        return result.strip()
