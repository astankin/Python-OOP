from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        total_guests = 0
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            total_guests += room.guests
            if not room.is_taken:
                free_rooms.append(room.number)
            else:
                taken_rooms.append(room.number)
        return f"Hotel {self.name} has {total_guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"
