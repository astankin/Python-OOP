from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut("Biologist", "Pesho"))
print(space_station.add_astronaut("Meteorologist", "Pesho2"))
print(space_station.add_astronaut("Geodesist", "Pesho3"))

print(space_station.add_planet("Mars"))
print(space_station.send_on_mission("Mars"))
print(space_station.report())
