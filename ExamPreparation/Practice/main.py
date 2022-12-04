from project.space_station import SpaceStation

app = SpaceStation()
print(app.add_astronaut("Biologist", "John"))
print(app.add_astronaut("Biologist", "Lili"))
print(app.add_astronaut("Geodesist", "Jake"))
print(app.add_astronaut("Geodesist", "Nasko"))
print(app.add_astronaut("Meteorologist", "Marti"))
print(app.add_astronaut("Meteorologist", "Kris"))
print(app.add_astronaut("Meteorologist", "Mimi"))

print(app.add_planet("Planet", ""))
print(app.send_on_mission("Planet"))
print(app.report())

