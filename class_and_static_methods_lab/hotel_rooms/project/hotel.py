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
        room = [r for r in self.rooms if room_number == r.number][0]
        guests = room.take_room(people)
        if not guests:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if room_number == r.number][0]
        people = room.guests
        room.free_room()
        self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"
